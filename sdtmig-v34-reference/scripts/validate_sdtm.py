#!/usr/bin/env python3
"""Cross-domain coherence checks for an SDTM dataset (CSV or parquet folder).

Rules are catalogued in references/coherence-rules.md (rule IDs match).
Exit code 1 if any ERROR-level rule fails.

Usage:
    python validate_sdtm.py ./sdtm                # folder with dm.csv, ae.csv, ...
    python validate_sdtm.py ./sdtm --json report.json
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
REF = HERE.parent / "references"

CT_CHECKS = {  # (domain, variable) -> codelist name in codelists-common.csv
    ("DM", "SEX"): "SEX", ("DM", "RACE"): "RACE", ("DM", "ETHNIC"): "ETHNIC",
    ("AE", "AESEV"): "AESEV", ("AE", "AESER"): "NY", ("AE", "AEOUT"): "AEOUT", ("AE", "AEACN"): "ACN",
    ("AE", "AESDTH"): "NY", ("AE", "AESHOSP"): "NY", ("DM", "DTHFL"): "NY",
    **{(d, "EPOCH"): "EPOCH" for d in ("AE", "DS", "EX", "SE", "VS", "LB", "EG", "RS", "IE", "TA")},
}


def load(folder: Path) -> dict[str, pd.DataFrame]:
    out = {}
    for f in sorted(folder.iterdir()):
        if f.suffix == ".parquet":
            out[f.stem.upper()] = pd.read_parquet(f)
        elif f.suffix == ".csv" and f.stem.upper() not in out:
            out[f.stem.upper()] = pd.read_csv(f, dtype=str, keep_default_na=False).replace("", None)
    return out


def mapd(keys: pd.Series, by: pd.Series) -> pd.Series:
    """Map keys to dates; safe when `by` is empty."""
    return pd.to_datetime(keys.map(by.to_dict()), errors="coerce")


def d10(s: pd.Series) -> pd.Series:
    return pd.to_datetime(s.astype("string").str[:10], errors="coerce")


class Report:
    def __init__(self):
        self.results = []

    def check(self, rid, level, desc, bad: pd.DataFrame | int | bool, sample_cols=None):
        n = int(bad) if isinstance(bad, (int, bool)) else len(bad)
        sample = []
        if isinstance(bad, pd.DataFrame) and n:
            cols = [c for c in (sample_cols or bad.columns[:6]) if c in bad.columns]
            sample = bad[cols].head(3).astype(str).to_dict("records")
        self.results.append({"rule": rid, "level": level, "desc": desc, "violations": n, "sample": sample})

    def print(self):
        w = max(len(r["desc"]) for r in self.results)
        for r in self.results:
            status = "PASS" if r["violations"] == 0 else r["level"]
            print(f"{status:5s} {r['rule']:6s} {r['desc']:<{w}}  {r['violations'] or ''}")
            for s in r["sample"]:
                print("            e.g.", s)
        errs = sum(1 for r in self.results if r["violations"] and r["level"] == "ERROR")
        warns = sum(1 for r in self.results if r["violations"] and r["level"] == "WARN")
        print(f"\n{len(self.results)} rules, {errs} errors, {warns} warnings")
        return errs


def validate(ds: dict[str, pd.DataFrame]) -> Report:
    R = Report()
    dm = ds["DM"].copy()
    for c in ["RFSTDTC", "RFENDTC", "RFXSTDTC", "RFXENDTC", "RFICDTC", "RFPENDTC", "DTHDTC"]:
        dm["_" + c] = d10(dm[c]) if c in dm else pd.NaT
    subj = set(dm["USUBJID"])

    # ---- C01-C03 structure / metadata --------------------------------------
    req = {}
    with open(REF / "variables.csv", newline="") as f:
        for r in csv.DictReader(f):
            req.setdefault(r["Dataset Name"], []).append((r["Variable Name"], r["Core"]))
    miss, nulls, exp_missing = [], [], []
    for dom, df in ds.items():
        for v, core in req.get(dom, []):
            if core == "Req" and v not in df:
                miss.append({"domain": dom, "var": v})
            elif core == "Req" and df[v].isna().any():
                nulls.append({"domain": dom, "var": v, "n": int(df[v].isna().sum())})
            elif core == "Exp" and v not in df:
                exp_missing.append({"domain": dom, "var": v})
    R.check("C01", "ERROR", "Required (Core=Req) variables present", pd.DataFrame(miss))
    R.check("C02", "ERROR", "Required variables never null", pd.DataFrame(nulls))
    R.check("C03", "WARN", "Expected (Core=Exp) variables present as columns", pd.DataFrame(exp_missing))
    for dom, df in ds.items():
        seq = f"{dom}SEQ"
        if seq in df and "USUBJID" in df:
            R.check("C04", "ERROR", f"{seq} unique within USUBJID", df[df.duplicated(["USUBJID", seq])],
                    ["USUBJID", seq])
    R.check("C05", "ERROR", "DM has one record per subject", dm[dm.duplicated("USUBJID")], ["USUBJID"])

    # ---- C10-C14 referential integrity -------------------------------------
    orphans = []
    for dom, df in ds.items():
        if "USUBJID" in df and dom != "DM":
            o = df[~df["USUBJID"].isin(subj)]
            orphans += [{"domain": dom, "USUBJID": u} for u in o["USUBJID"].unique()[:3]]
    R.check("C10", "ERROR", "Every USUBJID exists in DM", pd.DataFrame(orphans))
    if "TA" in ds:
        arms = set(ds["TA"]["ARMCD"])
        R.check("C11", "ERROR", "DM ARMCD/ACTARMCD exist in TA",
                dm[(dm["ARMCD"].notna() & ~dm["ARMCD"].isin(arms)) |
                   (dm["ACTARMCD"].notna() & ~dm["ACTARMCD"].isin(arms))], ["USUBJID", "ARMCD"])
    R.check("C12", "ERROR", "ARMNRS populated exactly when ACTARMCD is null",
            dm[dm["ACTARMCD"].isna() != dm["ARMNRS"].notna()], ["USUBJID", "ACTARMCD", "ARMNRS"])
    if "SV" in ds and "TV" in ds:
        tv = set(ds["TV"]["VISITNUM"].astype(float))
        sv = ds["SV"]
        sched = sv[sv["VISIT"].fillna("").str.startswith("UNSCHEDULED") == False]  # noqa: E712
        R.check("C13", "ERROR", "Scheduled SV VISITNUMs exist in TV",
                sched[~sched["VISITNUM"].astype(float).isin(tv)], ["USUBJID", "VISITNUM", "VISIT"])
        keys = set(zip(sv["USUBJID"], sv["VISITNUM"].astype(float)))
        bad = []
        for dom in ("VS", "LB", "EG", "RS", "IE"):
            if dom in ds and "VISITNUM" in ds[dom]:
                df = ds[dom]
                m = [(u, float(v)) not in keys for u, v in zip(df["USUBJID"], df["VISITNUM"])]
                bad += [{"domain": dom, "USUBJID": u, "VISITNUM": v} for u, v in
                        df.loc[m, ["USUBJID", "VISITNUM"]].drop_duplicates().head(3).values]
        R.check("C14", "ERROR", "Findings USUBJID+VISITNUM exist in SV", pd.DataFrame(bad))

    # ---- C20-C27 timeline ----------------------------------------------------
    date_cols = {"AE": ["AESTDTC", "AEENDTC"], "EX": ["EXSTDTC", "EXENDTC"], "DS": ["DSSTDTC"],
                 "SV": ["SVSTDTC"], "VS": ["VSDTC"], "LB": ["LBDTC"], "EG": ["EGDTC"], "RS": ["RSDTC"],
                 "SE": ["SESTDTC", "SEENDTC"], "IE": ["IEDTC"], "CM": ["CMENDTC"]}
    out_of_window, after_death = [], []
    ref = dm.set_index("USUBJID")
    for dom, cols in date_cols.items():
        if dom not in ds:
            continue
        df = ds[dom]
        for c in cols:
            if c not in df:
                continue
            d = d10(df[c])
            lo = df["USUBJID"].map(ref["_RFICDTC"])
            hi = df["USUBJID"].map(ref["_RFPENDTC"])
            m = d.notna() & ((d < lo) | (d > hi))
            if m.any():
                u, v = df.loc[m, ["USUBJID", c]].iloc[0]
                out_of_window.append({"domain": dom, "var": c, "n": int(m.sum()), "e.g.": f"{u} {v}"})
            dth = df["USUBJID"].map(ref["_DTHDTC"])
            m2 = d.notna() & dth.notna() & (d > dth)
            if m2.any():
                after_death.append({"domain": dom, "var": c, "n": int(m2.sum())})
    R.check("C20", "ERROR", "All dates between RFICDTC and RFPENDTC", pd.DataFrame(out_of_window))
    R.check("C21", "ERROR", "No records dated after death", pd.DataFrame(after_death))
    R.check("C22", "ERROR", "RFICDTC <= RFSTDTC <= RFXENDTC <= RFPENDTC",
            dm[(dm["_RFSTDTC"] < dm["_RFICDTC"]) | (dm["_RFXENDTC"] < dm["_RFSTDTC"]) |
               (dm["_RFXENDTC"] > dm["_RFPENDTC"])], ["USUBJID", "RFICDTC", "RFSTDTC", "RFXENDTC", "RFPENDTC"])
    if "EX" in ds:
        ex = ds["EX"].assign(_s=d10(ds["EX"]["EXSTDTC"]), _e=d10(ds["EX"]["EXENDTC"]))
        g = ex.groupby("USUBJID").agg(first=("_s", "min"), last=("_e", "max"))
        j = dm.set_index("USUBJID").join(g, how="left")
        R.check("C23", "ERROR", "RFXSTDTC = first EXSTDTC and RFXENDTC = last EXENDTC",
                j[(j["first"].notna() & ((j["first"] != j["_RFXSTDTC"]) | (j["last"] != j["_RFXENDTC"])))
                  | (j["first"].isna() & j["_RFXSTDTC"].notna())].reset_index(),
                ["USUBJID", "RFXSTDTC", "first", "RFXENDTC", "last"])
        R.check("C24", "ERROR", "Subjects without treatment (ARMNRS set) have no EX",
                ex[ex["USUBJID"].isin(dm.loc[dm["ARMNRS"].notna(), "USUBJID"])], ["USUBJID", "EXTRT"])
        R.check("C25", "ERROR", "EXENDTC >= EXSTDTC", ex[ex["_e"] < ex["_s"]], ["USUBJID", "EXSTDTC", "EXENDTC"])
    if "SE" in ds:
        se = ds["SE"].assign(_s=d10(ds["SE"]["SESTDTC"]), _e=d10(ds["SE"]["SEENDTC"])).sort_values(["USUBJID", "_s"])
        nxt = se.groupby("USUBJID")["_s"].shift(-1)
        R.check("C26", "ERROR", "SE elements contiguous (SEENDTC = next SESTDTC)",
                se[nxt.notna() & (se["_e"] != nxt)], ["USUBJID", "ETCD", "SESTDTC", "SEENDTC"])
        first = se.groupby("USUBJID")["_s"].min()
        R.check("C27", "ERROR", "First element starts at RFICDTC",
                dm[mapd(dm["USUBJID"], first) != dm["_RFICDTC"]], ["USUBJID", "RFICDTC"])
        if "TE" in ds:
            R.check("C28", "ERROR", "SE ETCD exists in TE", se[~se["ETCD"].isin(ds["TE"]["ETCD"])], ["USUBJID", "ETCD"])
        # EPOCH consistency for event/finding dates
        bad = []
        lookup = {u: list(zip(g["_s"], g["_e"], g["EPOCH"])) for u, g in se.groupby("USUBJID")}
        for dom, c in [("AE", "AESTDTC"), ("LB", "LBDTC"), ("VS", "VSDTC"), ("EX", "EXSTDTC"), ("DS", "DSSTDTC")]:
            if dom not in ds or "EPOCH" not in ds[dom]:
                continue
            df = ds[dom]
            dd = d10(df[c])
            for u, d, ep in zip(df["USUBJID"], dd, df["EPOCH"]):
                els = lookup.get(u, [])
                exp = None
                for i, (s, e, epo) in enumerate(els):
                    if s <= d < e or (i == len(els) - 1 and s <= d <= e):
                        exp = epo
                        break
                if (exp or None) != (ep if isinstance(ep, str) else None):
                    bad.append({"domain": dom, "USUBJID": u, "date": str(d)[:10], "EPOCH": ep, "expected": exp})
        R.check("C29", "ERROR", "EPOCH matches the SE element on that date", pd.DataFrame(bad))

    # ---- C30-C33 study day ---------------------------------------------------
    bad = []
    for dom, df in ds.items():
        for c in [c for c in df.columns if c.endswith("DTC") and dom != "DM"]:
            dy = c[:-3] + "DY"
            if dy not in df:
                continue
            d = d10(df[c])
            rf = df["USUBJID"].map(ref["_RFSTDTC"])
            delta = (d - rf).dt.days
            exp = delta.where(delta < 0, delta + 1)
            got = pd.to_numeric(df[dy], errors="coerce")
            m = exp.notna() & (got != exp)
            if m.any():
                bad.append({"domain": dom, "var": dy, "n": int(m.sum())})
            if (got == 0).any():
                bad.append({"domain": dom, "var": dy, "issue": "day 0"})
    R.check("C30", "ERROR", "--DY derived from RFSTDTC (no day 0)", pd.DataFrame(bad))

    # ---- C40-C46 death, disposition, AE/EX coherence ------------------------
    ds_ = ds.get("DS")
    if ds_ is not None:
        eos = ds_[ds_["DSSCAT"].fillna("") == "STUDY PARTICIPATION"]
        R.check("C40", "ERROR", "At most one end-of-study DS record per subject",
                eos[eos.duplicated("USUBJID")], ["USUBJID", "DSDECOD"])
        death_ds = set(ds_.loc[ds_["DSDECOD"] == "DEATH", "USUBJID"])
        dthfl = set(dm.loc[dm["DTHFL"] == "Y", "USUBJID"])
        R.check("C41", "ERROR", "DTHFL=Y <=> DS DEATH record <=> DTHDTC",
                dm[(dm["USUBJID"].isin(dthfl) != dm["USUBJID"].isin(death_ds)) |
                   (dm["DTHFL"].eq("Y") != dm["DTHDTC"].notna())], ["USUBJID", "DTHFL", "DTHDTC"])
        sf = set(dm.loc[dm["ARMNRS"] == "SCREEN FAILURE", "USUBJID"])
        sf_ds = set(ds_.loc[ds_["DSDECOD"] == "SCREEN FAILURE", "USUBJID"])
        R.check("C42", "ERROR", "Screen failures have DS SCREEN FAILURE and no ARMCD",
                dm[(dm["USUBJID"].isin(sf) != dm["USUBJID"].isin(sf_ds)) |
                   (dm["USUBJID"].isin(sf) & dm["ARMCD"].notna())], ["USUBJID", "ARMNRS"])
        if "IE" in ds:
            R.check("C43", "WARN", "Screen failures have at least one IE record",
                    dm[dm["USUBJID"].isin(sf) & ~dm["USUBJID"].isin(ds["IE"]["USUBJID"])], ["USUBJID"])
        if "TS" in ds:
            cut = ds["TS"].loc[ds["TS"]["TSPARMCD"] == "DCUTDTC", "TSVAL"]
            if len(cut):
                cut = pd.Timestamp(cut.iloc[0])
                no_eos = dm[(dm["_RFPENDTC"] < cut - pd.Timedelta(days=1)) & ~dm["USUBJID"].isin(eos["USUBJID"])]
                R.check("C44", "ERROR", "Subjects whose participation ended before cutoff have an EOS record",
                        no_eos, ["USUBJID", "RFPENDTC"])
                R.check("C45", "ERROR", "No dates after data cutoff (DCUTDTC)",
                        dm[(dm["_RFPENDTC"] > cut)], ["USUBJID", "RFPENDTC"])
    if "AE" in ds:
        ae = ds["AE"]
        fatal = ae[ae["AEOUT"] == "FATAL"]
        R.check("C46", "ERROR", "AEOUT=FATAL => AESDTH=Y, DTHFL=Y and AEENDTC = DTHDTC",
                fatal[(fatal["AESDTH"] != "Y") | ~fatal["USUBJID"].isin(dm.loc[dm["DTHFL"] == "Y", "USUBJID"]) |
                      (d10(fatal["AEENDTC"]) != fatal["USUBJID"].map(ref["_DTHDTC"]))],
                ["USUBJID", "AEDECOD", "AEENDTC"])
        R.check("C47", "ERROR", "AEENDTC >= AESTDTC", ae[d10(ae["AEENDTC"]) < d10(ae["AESTDTC"])],
                ["USUBJID", "AESTDTC", "AEENDTC"])
        R.check("C48", "ERROR", "Ongoing AEs (no AEENDTC) are not RECOVERED",
                ae[ae["AEENDTC"].isna() & ae["AEOUT"].isin(["RECOVERED/RESOLVED", "RECOVERED/RESOLVED WITH SEQUELAE"])],
                ["USUBJID", "AEDECOD", "AEOUT"])
        if "EX" in ds:
            wd = ae[ae["AEACN"] == "DRUG WITHDRAWN"].assign(_d=lambda x: d10(x["AESTDTC"]))
            first_wd = wd.groupby("USUBJID")["_d"].min()
            exs = ex.assign(_w=mapd(ex["USUBJID"], first_wd))
            R.check("C49", "ERROR", "No dosing after an AE with AEACN=DRUG WITHDRAWN",
                    exs[exs["_w"].notna() & (exs["_e"] > exs["_w"])], ["USUBJID", "EXTRT", "EXENDTC"])
            if ds_ is not None:  # treatment ends at the EOT decision (may follow the last dose during an interruption)
                eot_d = ds_[ds_["DSSCAT"].fillna("") == "STUDY TREATMENT"].assign(_d=lambda x: d10(x["DSSTDTC"]))
                eot_d = eot_d.groupby("USUBJID")["_d"].min()
                post = ae[(d10(ae["AESTDTC"]) > mapd(ae["USUBJID"], eot_d)) &
                          ae["AEACN"].isin(["DOSE REDUCED", "DRUG INTERRUPTED", "DRUG WITHDRAWN", "DOSE INCREASED"])]
                R.check("C50", "ERROR", "AEs starting after end of treatment have no dose action",
                        post, ["USUBJID", "AEDECOD", "AEACN"])

    if "AE" in ds and ds_ is not None:
        eot = ds_[(ds_["DSSCAT"].fillna("") == "STUDY TREATMENT")].assign(_d=lambda x: d10(x["DSSTDTC"]))
        ae_wd = ds["AE"][ds["AE"]["AEACN"] == "DRUG WITHDRAWN"].assign(_d=lambda x: d10(x["AESTDTC"]))
        first_wd = ae_wd.groupby("USUBJID")["_d"].min()
        e_ae = eot[eot["DSDECOD"] == "ADVERSE EVENT"]
        R.check("C51", "ERROR", "EOT reason ADVERSE EVENT <=> an AE with AEACN=DRUG WITHDRAWN on the EOT date",
                pd.concat([e_ae[mapd(e_ae["USUBJID"], first_wd) != e_ae["_d"]],
                           eot[(eot["DSDECOD"] != "ADVERSE EVENT") & eot["USUBJID"].isin(first_wd.index) &
                               (mapd(eot["USUBJID"], first_wd) <= eot["_d"])]]), ["USUBJID", "DSDECOD", "DSSTDTC"])
        R.check("C52", "ERROR", "End-of-treatment DS date >= RFXENDTC",
                eot[eot["_d"] < eot["USUBJID"].map(ref["_RFXENDTC"])], ["USUBJID", "DSDECOD", "DSSTDTC"])

    # ---- C60-C62 findings ----------------------------------------------------
    if "LB" in ds:
        lb = ds["LB"].copy()
        v, lo, hi = (pd.to_numeric(lb[c], errors="coerce") for c in ("LBSTRESN", "LBSTNRLO", "LBSTNRHI"))
        exp = pd.Series("NORMAL", index=lb.index).mask(v < lo, "LOW").mask(v > hi, "HIGH")
        R.check("C60", "ERROR", "LBNRIND consistent with LBSTRESN and reference range",
                lb[v.notna() & (lb["LBNRIND"] != exp)], ["USUBJID", "LBTESTCD", "LBSTRESN", "LBNRIND"])
    for dom in ("LB", "VS", "EG"):
        if dom in ds and f"{dom}LOBXFL" in ds[dom]:
            df = ds[dom]
            fl = df[df[f"{dom}LOBXFL"] == "Y"]
            R.check("C61", "ERROR", f"{dom}LOBXFL at most once per subject/test",
                    fl[fl.duplicated(["USUBJID", f"{dom}TESTCD"])], ["USUBJID", f"{dom}TESTCD"])
            late = fl[d10(fl[f"{dom}DTC"]) > fl["USUBJID"].map(ref["_RFXSTDTC"])]
            R.check("C62", "ERROR", f"{dom}LOBXFL record is on/before first dose", late, ["USUBJID", f"{dom}DTC"])
    if "AE" in ds and "LB" in ds:
        links = [("neutropenia", "NEUT", "LOW"), ("anaemia", "HGB", "LOW"), ("thrombocytopenia", "PLAT", "LOW"),
                 ("alanine aminotransferase increased", "ALT", "HIGH"), ("hypoalbuminaemia", "ALB", "LOW"),
                 ("hypokalaemia", "K", "LOW"), ("hyponatraemia", "SODIUM", "LOW")]
        lb = ds["LB"].assign(_d=d10(ds["LB"]["LBDTC"]))
        miss = []
        for frag, cd, ind in links:
            a = ds["AE"][ds["AE"]["AEDECOD"].str.lower().str.contains(frag, na=False)]
            for r in a.itertuples():
                s, e = pd.Timestamp(r.AESTDTC[:10]), (pd.Timestamp(r.AEENDTC[:10]) if isinstance(r.AEENDTC, str)
                                                      else pd.Timestamp.max)
                hit = lb[(lb["USUBJID"] == r.USUBJID) & (lb["LBTESTCD"] == cd) & (lb["LBNRIND"] == ind) &
                         (lb["_d"] >= s) & (lb["_d"] <= e)]
                if hit.empty:
                    miss.append({"USUBJID": r.USUBJID, "AEDECOD": r.AEDECOD, "LBTESTCD": cd})
        R.check("C63", "WARN", "Lab-defined AEs have a matching abnormal lab during the AE", pd.DataFrame(miss))
    if "RS" in ds and "DS" in ds:
        pd_subj = set(ds["DS"].loc[(ds["DS"]["DSDECOD"] == "PROGRESSIVE DISEASE"), "USUBJID"])
        rs_pd = set(ds["RS"].loc[ds["RS"]["RSSTRESC"] == "PD", "USUBJID"])
        R.check("C64", "ERROR", "Treatment stopped for PD <=> an RS PD assessment exists",
                pd.DataFrame([{"USUBJID": u} for u in sorted(pd_subj ^ rs_pd)]))

    # ---- C70-C71 controlled terminology & demographics ---------------------
    ct = {}
    with open(REF / "codelists-common.csv", newline="") as f:
        for r in csv.DictReader(f):
            ct.setdefault(r["Codelist_Name"], set()).add(r["Submission_Value"])
    bad = []
    for (dom, var), cl in CT_CHECKS.items():
        if dom in ds and var in ds[dom] and cl in ct:
            vals = set(ds[dom][var].dropna().unique()) - ct[cl]
            if vals:
                bad.append({"domain": dom, "var": var, "invalid": sorted(vals)[:5]})
    R.check("C70", "ERROR", "Values in common CDISC CT codelists", pd.DataFrame(bad))
    if "TS" in ds:
        ts = ds["TS"].set_index("TSPARMCD")["TSVAL"]
        lo = int(str(ts.get("AGEMIN", "P0Y"))[1:-1] or 0)
        hi = int(str(ts.get("AGEMAX", "P200Y"))[1:-1] or 200)
        length = str(ts.get("LENGTH") or "")
        if length.startswith("P") and length.endswith("D"):
            lim = pd.Timedelta(days=int(length[1:-1]) + 14)  # visit-window slack
            R.check("C72", "ERROR", "Participation (RFICDTC..RFPENDTC) within TS LENGTH",
                    dm[(dm["_RFPENDTC"] - dm["_RFICDTC"]) > lim], ["USUBJID", "RFICDTC", "RFPENDTC"])
        age = pd.to_numeric(dm["AGE"], errors="coerce")
        R.check("C71", "ERROR", "DM AGE within TS AGEMIN/AGEMAX", dm[(age < lo) | (age > hi)], ["USUBJID", "AGE"])
    return R


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", type=Path)
    ap.add_argument("--json", type=Path)
    a = ap.parse_args(argv)
    R = validate(load(a.folder))
    errs = R.print()
    if a.json:
        a.json.write_text(json.dumps(R.results, indent=2, default=str))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
