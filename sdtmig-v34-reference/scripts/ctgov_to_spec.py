#!/usr/bin/env python3
"""Fetch a ClinicalTrials.gov study (API v2) and draft a synthetic-study spec.

The spec is the single source of truth for generate_sdtm.py. Every value the
registry cannot provide is filled with a documented default and listed under
`review:` so the user (or the agent) can confirm it before generation.

Usage:
    python ctgov_to_spec.py NCT04487080 --out-dir ./study
    python ctgov_to_spec.py --from-file ./study/NCT04487080.json --out-dir ./study

Outputs <out-dir>/<NCT>.json (raw record) and <out-dir>/<NCT>_spec.yaml.
Only depends on the standard library + PyYAML (falls back to JSON output).
"""
from __future__ import annotations

import argparse
import difflib
import json
import math
import re
import sys
import urllib.request
from collections import Counter
from datetime import date
from functools import reduce
from pathlib import Path

API = "https://clinicaltrials.gov/api/v2/studies/{nct}"

# ---------------------------------------------------------------- mappings --

PHASE_MAP = {  # CT.gov phase -> TSVAL for TPHASE (CDISC CT C66737)
    "EARLY_PHASE1": "PHASE 0 TRIAL", "PHASE1": "PHASE I TRIAL", "PHASE2": "PHASE II TRIAL",
    "PHASE3": "PHASE III TRIAL", "PHASE4": "PHASE IV TRIAL",
    ("PHASE1", "PHASE2"): "PHASE I/II TRIAL", ("PHASE2", "PHASE3"): "PHASE II/III TRIAL",
}
MASKING_MAP = {"NONE": "OPEN LABEL", "SINGLE": "SINGLE BLIND", "DOUBLE": "DOUBLE BLIND",
               "TRIPLE": "DOUBLE BLIND", "QUADRUPLE": "DOUBLE BLIND"}
MODEL_MAP = {"PARALLEL": "PARALLEL", "CROSSOVER": "CROSS-OVER", "FACTORIAL": "FACTORIAL",
             "SINGLE_GROUP": "SINGLE GROUP", "SEQUENTIAL": "SEQUENTIAL"}
RACE_MAP = {
    "american indian or alaska native": "AMERICAN INDIAN OR ALASKA NATIVE",
    "asian": "ASIAN", "black or african american": "BLACK OR AFRICAN AMERICAN",
    "native hawaiian or other pacific islander": "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER",
    "white": "WHITE", "more than one race": "MULTIPLE", "unknown or not reported": "NOT REPORTED",
}
ETHNIC_MAP = {"hispanic or latino": "HISPANIC OR LATINO",
              "not hispanic or latino": "NOT HISPANIC OR LATINO",
              "unknown or not reported": "NOT REPORTED"}
DISC_MAP = {  # CT.gov drop/withdraw type -> CDISC NCOMPLT (C66727)
    "withdrawal by subject": "WITHDRAWAL BY SUBJECT", "lost to follow-up": "LOST TO FOLLOW-UP",
    "adverse event": "ADVERSE EVENT", "death": "DEATH", "physician decision": "PHYSICIAN DECISION",
    "protocol violation": "PROTOCOL DEVIATION", "protocol deviation": "PROTOCOL DEVIATION",
    "lack of efficacy": "LACK OF EFFICACY", "progressive disease": "PROGRESSIVE DISEASE",
    "disease progression": "PROGRESSIVE DISEASE", "study terminated by sponsor": "STUDY TERMINATED BY SPONSOR",
    "pregnancy": "PREGNANCY", "non-compliance": "NON-COMPLIANCE WITH STUDY DRUG",
}
COUNTRY_ISO3 = {
    "argentina": "ARG", "australia": "AUS", "austria": "AUT", "belgium": "BEL", "brazil": "BRA",
    "bulgaria": "BGR", "canada": "CAN", "chile": "CHL", "china": "CHN", "colombia": "COL",
    "croatia": "HRV", "czechia": "CZE", "czech republic": "CZE", "denmark": "DNK", "egypt": "EGY",
    "estonia": "EST", "finland": "FIN", "france": "FRA", "germany": "DEU", "greece": "GRC",
    "hong kong": "HKG", "hungary": "HUN", "india": "IND", "indonesia": "IDN", "ireland": "IRL",
    "israel": "ISR", "italy": "ITA", "japan": "JPN", "korea, republic of": "KOR",
    "south korea": "KOR", "republic of korea": "KOR", "latvia": "LVA", "lithuania": "LTU",
    "malaysia": "MYS", "mexico": "MEX", "netherlands": "NLD", "new zealand": "NZL", "norway": "NOR",
    "peru": "PER", "philippines": "PHL", "poland": "POL", "portugal": "PRT", "romania": "ROU",
    "russian federation": "RUS", "russia": "RUS", "saudi arabia": "SAU", "serbia": "SRB",
    "singapore": "SGP", "slovakia": "SVK", "south africa": "ZAF", "spain": "ESP", "sweden": "SWE",
    "switzerland": "CHE", "taiwan": "TWN", "thailand": "THA", "turkey": "TUR", "türkiye": "TUR",
    "turkiye": "TUR", "ukraine": "UKR", "united kingdom": "GBR", "united states": "USA",
    "vietnam": "VNM", "viet nam": "VNM",
}
ONCOLOGY_HINTS = re.compile(r"cancer|carcinoma|tumou?r|lymphoma|leukemia|leukaemia|myeloma|"
                            r"melanoma|sarcoma|neoplasm|nsclc|glioma|blastoma", re.I)
ROUTE_HINTS = [(r"intravenous|\bIV\b|infusion", "INTRAVENOUS", "INJECTION"),
               (r"subcutaneous|\bSC\b", "SUBCUTANEOUS", "INJECTION"),
               (r"orally|oral|tablet|capsule", "ORAL", "TABLET")]
FREQ_HINTS = [(r"once daily|daily|\bQD\b", "QD", 1), (r"twice daily|\bBID\b", "BID", 1),
              (r"once weekly|every week|weekly|\bQW\b", "QW", 7),
              (r"every 2 weeks|\bQ2W\b", "Q2W", 14), (r"every 3 weeks|\bQ3W\b", "Q3W", 21),
              (r"every 4 weeks|\bQ4W\b|monthly", "Q4W", 28)]


# ----------------------------------------------------------------- helpers --

def fetch(nct: str) -> dict:
    req = urllib.request.Request(API.format(nct=nct), headers={"User-Agent": "sdtm-skill/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def _age_years(txt: str | None) -> int | None:
    if not txt:
        return None
    m = re.match(r"(\d+)\s*(Year|Month|Week|Day)", txt)
    if not m:
        return None
    n, unit = int(m.group(1)), m.group(2)
    return {"Year": n, "Month": n // 12, "Week": n // 52, "Day": n // 365}[unit]


def _best_match(title: str, candidates: list[str]) -> int:
    """Index of the candidate most similar to title (registry groups vs arm labels)."""
    norm = lambda s: re.sub(r"^(experimental|active comparator|placebo comparator|"
                            r"no intervention|sham comparator|other):\s*", "", s.lower())
    nt = norm(title)
    # "Placebo to Drug X" belongs to the arm labelled "Placebo": prefer labels the title starts with
    prefix = [i for i, c in enumerate(candidates) if norm(c) and nt.startswith(norm(c))]
    if prefix:
        return max(prefix, key=lambda i: len(norm(candidates[i])))
    scores = [difflib.SequenceMatcher(None, nt, norm(c)).ratio() for c in candidates]
    return max(range(len(scores)), key=scores.__getitem__)


def _small_int_ratio(counts: list[int]) -> list[int]:
    lo = min(counts)
    raw = [c / lo for c in counts]
    ints = [max(1, round(r)) for r in raw]
    g = reduce(math.gcd, ints)
    return [i // g for i in ints]


def _criteria(text: str) -> list[dict]:
    out, cat = [], None
    for line in (text or "").splitlines():
        s = line.strip()
        if re.match(r"inclusion criteria", s, re.I):
            cat = "INCLUSION"
            continue
        if re.match(r"exclusion criteria", s, re.I):
            cat = "EXCLUSION"
            continue
        if cat and re.match(r"^[*\-•]|^\d+[.)]", s):
            t = re.sub(r"^([*\-•]|\d+[.)])\s*", "", s).replace("\\", "")
            if t:
                out.append({"cat": cat, "text": t})
    n = Counter()
    for c in out:
        n[c["cat"]] += 1
        c["code"] = ("INCL" if c["cat"] == "INCLUSION" else "EXCL") + f"{n[c['cat']]:02d}"
        c["text"] = c["text"][:200]  # IETEST max length 200
    return out


def _intervention_regimen(desc: str) -> dict:
    route, form, freq, every = "ORAL", "TABLET", "QD", 1
    for pat, r, f in ROUTE_HINTS:
        if re.search(pat, desc or "", re.I):
            route, form = r, f
            break
    for pat, f, d in FREQ_HINTS:
        if re.search(pat, desc or "", re.I):
            freq, every = f, d
            break
    m = re.search(r"(\d+(?:\.\d+)?)\s*(mg|milligrams?|mg/kg|µg|mcg)\b", desc or "", re.I)
    dose, unit = (float(m.group(1)), "mg/kg" if "kg" in m.group(2).lower() else "mg") if m else (None, "mg")
    return {"dose": dose, "unit": unit, "route": route, "dosfrm": form, "frequency": freq,
            "every_days": every}


def _week_days(outcomes: list[dict]) -> list[int]:
    weeks = set()
    for o in outcomes:
        for w in re.findall(r"[Ww]eek\s*(\d+)", o.get("timeFrame", "")):
            weeks.add(int(w))
    return sorted(w * 7 + 1 for w in weeks if 0 < w <= 260)


# ------------------------------------------------------------------- draft --

def draft_spec(rec: dict) -> dict:
    p = rec["protocolSection"]
    res = rec.get("resultsSection", {})
    review: list[str] = []
    ident, status, design = p["identificationModule"], p["statusModule"], p["designModule"]
    nct = ident["nctId"]
    conds = p.get("conditionsModule", {}).get("conditions", [])
    oncology = bool(ONCOLOGY_HINTS.search(" ".join(conds + [ident.get("officialTitle", "")])))
    di = design.get("designInfo", {})

    start = status.get("startDateStruct", {}).get("date") or "2022-01-01"
    if len(start) == 7:
        start += "-01"
    cutoff = (status.get("primaryCompletionDateStruct", {}).get("date")
              or status.get("completionDateStruct", {}).get("date") or str(date.today()))
    if len(cutoff) == 7:
        cutoff += "-28"
    span = (date.fromisoformat(cutoff) - date.fromisoformat(start)).days
    review.append("study.data_cutoff defaults to the primary completion date")

    # --- arms -------------------------------------------------------------
    ai = p.get("armsInterventionsModule", {})
    interventions = {f"{i['type'].title()}: {i['name']}": i for i in ai.get("interventions", [])}
    arm_groups = ai.get("armGroups", [])
    labels = [a["label"] for a in arm_groups]
    flow = res.get("participantFlowModule", {})
    started = None
    if flow and arm_groups:
        groups = flow.get("groups", [])
        ms = {m["type"]: m for m in flow["periods"][0]["milestones"]}
        if "STARTED" in ms and groups:
            started = [0] * len(arm_groups)
            for a in ms["STARTED"]["achievements"]:
                g = next(g for g in groups if g["id"] == a["groupId"])
                if "total" in g["title"].lower():
                    continue
                started[_best_match(g["title"], labels)] += int(a["numSubjects"])
    if flow and len(flow.get("periods", [])) > 1:
        review.append("design has %d periods (%s): the generator models ONE treatment element per arm; "
                      "crossover / re-randomization after period 1 is not represented"
                      % (len(flow["periods"]), "; ".join(pp["title"] for pp in flow["periods"])))
    ratio = _small_int_ratio(started) if started and min(started) > 0 else [1] * len(arm_groups)
    if not started:
        review.append("arms[].ratio defaults to 1:1 (no participant flow posted)")

    arms = []
    group_desc = {g["title"]: g.get("description", "") for g in
                  res.get("adverseEventsModule", {}).get("eventGroups", []) + flow.get("groups", [])}
    for k, a in enumerate(arm_groups):
        armcd = chr(ord("A") + k)
        desc = a.get("description", "")
        gd = [v for t, v in group_desc.items() if labels and _best_match(t, labels) == k]
        desc_all = " ".join([desc] + gd)
        ivs = []
        for name in a.get("interventionNames", []):
            iv = interventions.get(name, {"name": name.split(": ", 1)[-1], "description": ""})
            text = iv.get("description", "") + " " + desc_all
            # regimen hints closest to this drug name
            m = re.search(re.escape(iv["name"]) + r"[^.;]{0,250}", desc_all, re.I)
            reg = _intervention_regimen((m.group(0) if m else "") + " " + iv.get("description", ""))
            if reg["dose"] is None:
                reg["dose"] = 1
                reg["unit"] = "TABLET" if reg["route"] == "ORAL" else "mg"
                review.append(f"arms[{armcd}].interventions[{iv['name']}].dose not found in registry text")
            ivs.append({"name": iv["name"].upper(), **reg})
        arms.append({"armcd": armcd, "arm": a["label"][:200], "type": a.get("type", ""),
                     "ratio": ratio[k] if k < len(ratio) else 1, "interventions": ivs})
    review.append("arms[].interventions dose/route/frequency are parsed from free text; check them")

    # --- population ---------------------------------------------------------
    el = p.get("eligibilityModule", {})
    pop = {"age_min": _age_years(el.get("minimumAge")) or 18,
           "age_max": _age_years(el.get("maximumAge")) or 90,
           "age_mean": None, "age_sd": 10.0,
           "sex": {"F": 0.5, "M": 0.5} if el.get("sex", "ALL") == "ALL"
           else ({"F": 1.0} if el["sex"] == "FEMALE" else {"M": 1.0}),
           "race": {"WHITE": 0.7, "BLACK OR AFRICAN AMERICAN": 0.12, "ASIAN": 0.12,
                    "OTHER": 0.03, "NOT REPORTED": 0.03},
           "ethnicity": {"NOT HISPANIC OR LATINO": 0.85, "HISPANIC OR LATINO": 0.12,
                         "NOT REPORTED": 0.03}}
    base = res.get("baselineCharacteristicsModule", {})
    countries: dict[str, int] = {}
    total_col = None
    for i, g in enumerate(base.get("groups", [])):
        if g["title"].lower().startswith("total"):
            total_col = i
    for m in base.get("measures", []):
        t = m["title"].lower()
        def cats(cls):
            for c in cls["categories"]:
                ms = c["measurements"]
                v = ms[total_col if total_col is not None and total_col < len(ms) else -1].get("value")
                yield c.get("title", ""), v
        if t.startswith("age") and m.get("paramType") == "MEAN":
            pop["age_mean"] = float(m["classes"][0]["categories"][0]["measurements"][-1]["value"])
        elif t.startswith("sex"):
            d = {("F" if k.lower().startswith("f") else "M"): float(v) for k, v in cats(m["classes"][0])}
            pop["sex"] = {k: round(v / sum(d.values()), 3) for k, v in d.items()}
        elif t.startswith("race"):
            d = Counter()
            for k, v in cats(m["classes"][0]):
                d[RACE_MAP.get(k.lower(), "OTHER")] += float(v or 0)
            pop["race"] = {k: round(v / sum(d.values()), 3) for k, v in d.items() if v}
        elif t.startswith("ethnicity"):
            d = Counter()
            for k, v in cats(m["classes"][0]):
                d[ETHNIC_MAP.get(k.lower(), "NOT REPORTED")] += float(v or 0)
            pop["ethnicity"] = {k: round(v / sum(d.values()), 3) for k, v in d.items() if v}
        elif t.startswith("region of enrollment"):
            for cls in m["classes"]:
                v = cls["categories"][0]["measurements"]
                v = v[total_col if total_col is not None and total_col < len(v) else -1].get("value")
                countries[cls.get("title", "")] = int(float(v or 0))
    if pop["age_mean"] is None:
        pop["age_mean"] = round((pop["age_min"] + min(pop["age_max"], 80)) / 2, 1)
        review.append("population.age_mean is a midpoint default (no baseline results)")

    # --- sites --------------------------------------------------------------
    locs = p.get("contactsLocationsModule", {}).get("locations", [])
    site_counts = Counter(l.get("country", "").lower() for l in locs)
    weights = countries or dict(site_counts) or {"United States": 1}
    sites, unknown = [], []
    for country, w in sorted(weights.items(), key=lambda kv: -kv[1]):
        iso = COUNTRY_ISO3.get(country.lower())
        if not iso:
            unknown.append(country)
            continue
        sites.append({"country": iso, "weight": w, "n_sites": max(1, site_counts.get(country.lower(), 1))})
    if unknown:
        review.append(f"sites: no ISO 3166 alpha-3 mapping for {unknown}; add them manually")

    # --- disposition ----------------------------------------------------------
    disp = {"screen_failure_rate": 0.25, "study_withdrawal": {}, "death": {},
            "ongoing_at_cutoff": None,
            "treatment_discontinuation": {a["armcd"]: (
                {"PROGRESSIVE DISEASE": 0.45, "PHYSICIAN DECISION": 0.05, "WITHDRAWAL BY SUBJECT": 0.03}
                if oncology else {"LACK OF EFFICACY": 0.05, "WITHDRAWAL BY SUBJECT": 0.04,
                                  "PHYSICIAN DECISION": 0.02}) for a in arms}}
    review.append("disposition.screen_failure_rate default 0.25 (not in registry)")
    review.append("disposition.treatment_discontinuation is a therapeutic-area default (registry only "
                  "reports study withdrawal); AE-driven withdrawals come from adverse_events")
    if flow and started:
        groups = flow.get("groups", [])
        per = flow["periods"][0]
        ongoing = Counter()
        for w in per.get("dropWithdraws", []):
            reason = w["type"].strip().lower()
            for r in w["reasons"]:
                g = next(g for g in groups if g["id"] == r["groupId"])
                k = _best_match(g["title"], labels)
                armcd = arms[k]["armcd"]
                frac = int(r["numSubjects"]) / max(1, started[k])
                if reason == "ongoing":
                    ongoing[armcd] = round(frac, 3)
                elif reason == "death":
                    disp["death"][armcd] = round(frac, 3)
                else:
                    code = DISC_MAP.get(reason, "OTHER")
                    disp["study_withdrawal"].setdefault(armcd, {})
                    disp["study_withdrawal"][armcd][code] = round(
                        disp["study_withdrawal"][armcd].get(code, 0) + frac, 3)
        if ongoing:
            disp["ongoing_at_cutoff"] = dict(ongoing)
    aem = res.get("adverseEventsModule", {})
    for g in aem.get("eventGroups", []):
        if g.get("deathsNumAtRisk"):
            k = _best_match(g["title"], labels)
            disp["death"].setdefault(arms[k]["armcd"], round(g["deathsNumAffected"] / g["deathsNumAtRisk"], 3))
    if not disp["death"]:
        disp["death"] = {a["armcd"]: 0.02 for a in arms}
        review.append("disposition.death default 2% (no results posted)")

    # --- adverse events -----------------------------------------------------
    ae_terms: dict[str, dict] = {}
    if aem:
        gid2arm = {g["id"]: arms[_best_match(g["title"], labels)]["armcd"] for g in aem["eventGroups"]}
        for kind in ("otherEvents", "seriousEvents"):
            for e in aem.get(kind, []):
                t = ae_terms.setdefault(e["term"], {"term": e["term"], "bodsys": e.get("organSystem", ""),
                                                    "incidence": {}, "serious_incidence": {}})
                for s in e.get("stats", []):
                    if not s.get("numAtRisk"):
                        continue
                    inc = s["numAffected"] / s["numAtRisk"]
                    key = "incidence" if kind == "otherEvents" else "serious_incidence"
                    arm = gid2arm[s["groupId"]]
                    t[key][arm] = round(max(inc, t[key].get(arm, 0)), 4)
        for t in ae_terms.values():
            for arm, si in t["serious_incidence"].items():
                t["incidence"][arm] = round(max(t["incidence"].get(arm, 0), si), 4)
        ranked = sorted(ae_terms.values(), key=lambda t: -max(t["incidence"].values() or [0]))
        keep = [t for t in ranked if max(t["incidence"].values() or [0]) >= 0.005][:80]
        src = (aem.get("otherEvents") or aem.get("seriousEvents") or [{}])[0].get("sourceVocabulary", "")
    else:
        keep, src = [], ""
        review.append("adverse_events: no posted results; add expected AEs (term, bodsys, incidence per arm)")

    # --- schedule of activities ---------------------------------------------
    outcomes = p.get("outcomesModule", {})
    weeks = _week_days(outcomes.get("primaryOutcomes", []) + outcomes.get("secondaryOutcomes", []))
    if oncology:
        visits = {
            "screening": {"visit": "SCREENING", "day": -14, "window": 14, "assess": ["VS", "LB", "EG"]},
            "repeating": {"pattern": "CYCLE {n} DAY 1", "start_day": 1, "interval_days": 28,
                          "max_repeats": max(6, math.ceil(span / 28)), "window": 3,
                          "assess": ["VS", "LB"], "assess_every": {"EG": 3}},
            "response": {"assess": "RS", "first_day": 57, "interval_days": 56, "window": 7},
            "end_of_treatment": {"visit": "END OF TREATMENT", "offset_days": 7, "assess": ["VS", "LB", "EG"]},
            "follow_up": [{"visit": "SAFETY FOLLOW-UP", "offset_days": 30, "assess": ["VS", "LB"]}],
        }
        planned_treatment_days = None
    else:
        end = max(weeks or [169])
        grid = [15, 29, 57, 85] + list(range(141, end + 1, 56))  # wk 2, 4, 8, 12, then every 8 weeks
        days = sorted(set([d for d in grid if d <= end] + weeks))
        visits = {
            "screening": {"visit": "SCREENING", "day": -21, "window": 21, "assess": ["VS", "LB", "EG"]},
            "scheduled": [{"visit": "DAY 1", "day": 1, "window": 0, "assess": ["VS", "LB", "EG"]}] +
                         [{"visit": f"WEEK {(d - 1) // 7}", "day": d, "window": 3 if d < 60 else 7,
                           "assess": ["VS", "LB"]} for d in days],
            "end_of_treatment": {"visit": "END OF TREATMENT", "offset_days": 7, "assess": ["VS", "LB", "EG"]},
            "follow_up": [{"visit": "SAFETY FOLLOW-UP", "offset_days": 30, "assess": ["VS", "LB"]}],
        }
        planned_treatment_days = max(days)
    review.append("visits: CT.gov has no schedule of activities; visits are a template "
                  "(oncology: 28-day cycles; otherwise outcome time frames). Replace with the protocol SoA if available")

    ti = _criteria(el.get("eligibilityCriteria", ""))
    enrol = design.get("enrollmentInfo", {}).get("count") or sum(started or []) or 300

    return {
        "spec_version": 1,
        "study": {
            "studyid": f"SYN-{nct}",  # fictional study identifier, never the real one
            "source_nct": nct,
            "title": ident.get("officialTitle") or ident.get("briefTitle"),
            "acronym": ident.get("acronym"),
            "sponsor": p.get("sponsorCollaboratorsModule", {}).get("leadSponsor", {}).get("name"),
            "phase": PHASE_MAP.get(tuple(design.get("phases", [])) if len(design.get("phases", [])) > 1
                                   else (design.get("phases") or ["NA"])[0], "NOT APPLICABLE"),
            "study_type": design.get("studyType", "INTERVENTIONAL"),
            "randomized": di.get("allocation") == "RANDOMIZED",
            "blinding": MASKING_MAP.get(di.get("maskingInfo", {}).get("masking", "NONE"), "OPEN LABEL"),
            "intervention_model": MODEL_MAP.get(di.get("interventionModel", ""), "PARALLEL"),
            "primary_purpose": di.get("primaryPurpose", "TREATMENT"),
            "conditions": conds,
            "therapeutic_area": "ONCOLOGY" if oncology else "OTHER",
            "study_start": start,
            "data_cutoff": cutoff,
            "enrollment_period_days": max(90, min(730, int(span * 0.6))),
            "planned_treatment_days": planned_treatment_days,
            "follow_up_days": 30,
        },
        "generation": {"seed": 20261117, "n_randomized": int(enrol),
                       "domains": ["TS", "TA", "TE", "TV", "TI", "DM", "IE", "DS", "SE", "SV", "EX",
                                   "AE", "MH", "CM", "VS", "LB", "EG"] + (["RS"] if oncology else [])},
        "population": pop,
        "sites": sites,
        "arms": arms,
        "disposition": disp,
        "adverse_events": {"source_vocabulary": src, "terms": [
            {"term": t["term"], "bodsys": t["bodsys"], "incidence": t["incidence"],
             "serious_fraction": {a: round(min(1.0, t["serious_incidence"].get(a, 0) / v), 3)
                                  for a, v in t["incidence"].items() if v}} for t in keep]},
        "medical_history": [{"term": c, "prob": 1.0, "indication": True} for c in conds[:1]],
        "eligibility": ti,
        "visits": visits,
        "review": review,
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("nct", nargs="?")
    ap.add_argument("--from-file", type=Path)
    ap.add_argument("--out-dir", type=Path, default=Path("."))
    a = ap.parse_args(argv)
    if not (a.nct or a.from_file):
        ap.error("give an NCT ID or --from-file")
    rec = json.loads(a.from_file.read_text()) if a.from_file else fetch(a.nct)
    nct = rec["protocolSection"]["identificationModule"]["nctId"]
    a.out_dir.mkdir(parents=True, exist_ok=True)
    if not a.from_file:
        (a.out_dir / f"{nct}.json").write_text(json.dumps(rec, indent=1))
    spec = draft_spec(rec)
    try:
        import yaml
        out = a.out_dir / f"{nct}_spec.yaml"
        out.write_text(yaml.safe_dump(spec, sort_keys=False, allow_unicode=True, width=120))
    except ImportError:
        out = a.out_dir / f"{nct}_spec.json"
        out.write_text(json.dumps(spec, indent=2))
    print(f"wrote {out}")
    print("REVIEW BEFORE GENERATING:")
    for r in spec["review"]:
        print(" -", r)


if __name__ == "__main__":
    sys.exit(main())
