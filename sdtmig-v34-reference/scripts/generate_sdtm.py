#!/usr/bin/env python3
"""Generate a coherent, fictional SDTMIG v3.4 dataset from a study spec.

Coherence comes from the generation order. Each subject gets ONE timeline
(consent -> randomisation -> first dose -> treatment end -> follow-up ->
end of participation / death / data cutoff). Every domain is derived from that
timeline, never sampled independently:

    trial design (TS TA TE TV TI)
      -> subject spine (DM, DS, SE, SV, IE)
        -> interventions (EX, CM, MH)
          -> events (AE; AE withdrawals and deaths feed back into the spine)
            -> findings (VS, LB, EG, RS), with lab values shifted during linked AEs
              -> derived (--SEQ, --DY, EPOCH, VISITNUM, --LOBXFL)

Usage:
    python generate_sdtm.py spec.yaml --out ./sdtm                  # CSV (+ parquet if pyarrow)
    python generate_sdtm.py spec.yaml --out ./sdtm --n 200          # override subject count
    python generate_sdtm.py spec.yaml --uc main.sdtm_synthetic      # also write UC tables (on Databricks)

Deterministic for a given spec + seed. Requires pandas and numpy (PyYAML for YAML specs).
All data is fictional. STUDYID is prefixed "SYN-" and TS TITLE is marked [SYNTHETIC].
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
VARIABLES_CSV = HERE.parent / "references" / "variables.csv"

# ------------------------------------------------------------ default panels --
# (testcd, test, category, unit, mean, sd, low, high, specimen)
LB_PANEL = [
    ("HGB", "Hemoglobin", "HEMATOLOGY", "g/L", 135, 14, 120, 170, "BLOOD"),
    ("WBC", "Leukocytes", "HEMATOLOGY", "10^9/L", 6.5, 1.4, 4.0, 11.0, "BLOOD"),
    ("NEUT", "Neutrophils", "HEMATOLOGY", "10^9/L", 4.0, 1.1, 1.8, 7.5, "BLOOD"),
    ("LYM", "Lymphocytes", "HEMATOLOGY", "10^9/L", 1.9, 0.5, 1.0, 4.0, "BLOOD"),
    ("PLAT", "Platelets", "HEMATOLOGY", "10^9/L", 250, 55, 150, 400, "BLOOD"),
    ("ALT", "Alanine Aminotransferase", "CHEMISTRY", "U/L", 24, 8, 7, 45, "SERUM"),
    ("AST", "Aspartate Aminotransferase", "CHEMISTRY", "U/L", 23, 7, 8, 40, "SERUM"),
    ("ALP", "Alkaline Phosphatase", "CHEMISTRY", "U/L", 80, 18, 40, 130, "SERUM"),
    ("BILI", "Bilirubin", "CHEMISTRY", "umol/L", 10, 3.5, 3, 21, "SERUM"),
    ("CREAT", "Creatinine", "CHEMISTRY", "umol/L", 78, 14, 50, 110, "SERUM"),
    ("ALB", "Albumin", "CHEMISTRY", "g/L", 41, 3.5, 35, 50, "SERUM"),
    ("SODIUM", "Sodium", "CHEMISTRY", "mmol/L", 140, 2.2, 135, 145, "SERUM"),
    ("K", "Potassium", "CHEMISTRY", "mmol/L", 4.2, 0.32, 3.5, 5.1, "SERUM"),
    ("GLUC", "Glucose", "CHEMISTRY", "mmol/L", 5.4, 0.7, 3.9, 7.8, "SERUM"),
]
# (testcd, test, unit, mean, sd, decimals, position)
VS_PANEL = [
    ("SYSBP", "Systolic Blood Pressure", "mmHg", 126, 13, 0, "SITTING"),
    ("DIABP", "Diastolic Blood Pressure", "mmHg", 78, 8, 0, "SITTING"),
    ("PULSE", "Pulse Rate", "beats/min", 74, 9, 0, "SITTING"),
    ("RESP", "Respiratory Rate", "breaths/min", 16, 1.8, 0, None),
    ("TEMP", "Temperature", "C", 36.7, 0.25, 1, None),
    ("WEIGHT", "Weight", "kg", None, None, 1, None),
]
# (testcd, test, unit, mean, sd)
EG_PANEL = [
    ("EGHRMN", "ECG Mean Heart Rate", "beats/min", 72, 9),
    ("PRAG", "PR Interval, Aggregate", "msec", 160, 18),
    ("QRSAG", "QRS Duration, Aggregate", "msec", 92, 9),
    ("QTAG", "QT Interval, Aggregate", "msec", 390, 22),
    ("QTCFAG", "QTcF Interval, Aggregate", "msec", 410, 15),
]
# AE term fragment -> (domain, testcd, direction). Values are pushed outside the
# reference range while the AE is ongoing, so AE and findings tell the same story.
AE_FINDING_LINKS = [
    ("neutropenia", "LB", "NEUT", "low"), ("neutrophil count decreased", "LB", "NEUT", "low"),
    ("anaemia", "LB", "HGB", "low"), ("anemia", "LB", "HGB", "low"),
    ("thrombocytopenia", "LB", "PLAT", "low"), ("platelet count decreased", "LB", "PLAT", "low"),
    ("leukopenia", "LB", "WBC", "low"), ("white blood cell count decreased", "LB", "WBC", "low"),
    ("lymphopenia", "LB", "LYM", "low"), ("lymphocyte count decreased", "LB", "LYM", "low"),
    ("alanine aminotransferase increased", "LB", "ALT", "high"),
    ("aspartate aminotransferase increased", "LB", "AST", "high"),
    ("blood alkaline phosphatase increased", "LB", "ALP", "high"),
    ("blood bilirubin increased", "LB", "BILI", "high"), ("hyperbilirubinaemia", "LB", "BILI", "high"),
    ("blood creatinine increased", "LB", "CREAT", "high"), ("acute kidney injury", "LB", "CREAT", "high"),
    ("hypoalbuminaemia", "LB", "ALB", "low"), ("hypoalbuminemia", "LB", "ALB", "low"),
    ("hyponatraemia", "LB", "SODIUM", "low"), ("hypokalaemia", "LB", "K", "low"),
    ("hyperglycaemia", "LB", "GLUC", "high"), ("hypertension", "VS", "SYSBP", "high"),
    ("pyrexia", "VS", "TEMP", "high"), ("electrocardiogram qt prolonged", "EG", "QTCFAG", "high"),
]
COMORBIDITIES = [  # term, SOC, base prevalence, concomitant medication (name, dose, unit, freq, route)
    ("Hypertension", "Vascular disorders", 0.33, ("AMLODIPINE", 5, "mg", "QD", "ORAL")),
    ("Hyperlipidaemia", "Metabolism and nutrition disorders", 0.22, ("ATORVASTATIN", 20, "mg", "QD", "ORAL")),
    ("Type 2 diabetes mellitus", "Metabolism and nutrition disorders", 0.12,
     ("METFORMIN", 1000, "mg", "BID", "ORAL")),
    ("Gastrooesophageal reflux disease", "Gastrointestinal disorders", 0.10, ("OMEPRAZOLE", 20, "mg", "QD", "ORAL")),
    ("Osteoarthritis", "Musculoskeletal and connective tissue disorders", 0.10,
     ("PARACETAMOL", 1000, "mg", "PRN", "ORAL")),
    ("Hypothyroidism", "Endocrine disorders", 0.05, ("LEVOTHYROXINE", 50, "ug", "QD", "ORAL")),
    ("Depression", "Psychiatric disorders", 0.06, ("SERTRALINE", 50, "mg", "QD", "ORAL")),
    ("Asthma", "Respiratory, thoracic and mediastinal disorders", 0.05,
     ("SALBUTAMOL", 100, "ug", "PRN", "RESPIRATORY (INHALATION)")),
]
AE_TREATMENTS = [  # AE term fragment -> rescue medication
    ("nausea", ("ONDANSETRON", 8, "mg", "PRN", "ORAL")), ("vomiting", ("ONDANSETRON", 8, "mg", "PRN", "ORAL")),
    ("diarrhoea", ("LOPERAMIDE", 2, "mg", "PRN", "ORAL")), ("diarrhea", ("LOPERAMIDE", 2, "mg", "PRN", "ORAL")),
    ("rash", ("HYDROCORTISONE", 1, "%", "BID", "TOPICAL")), ("dermatitis", ("HYDROCORTISONE", 1, "%", "BID", "TOPICAL")),
    ("paronychia", ("MUPIROCIN", 2, "%", "TID", "TOPICAL")), ("pyrexia", ("PARACETAMOL", 1000, "mg", "PRN", "ORAL")),
    ("headache", ("PARACETAMOL", 1000, "mg", "PRN", "ORAL")), ("pain", ("PARACETAMOL", 1000, "mg", "PRN", "ORAL")),
    ("pneumonia", ("AMOXICILLIN", 500, "mg", "TID", "ORAL")), ("infection", ("AMOXICILLIN", 500, "mg", "TID", "ORAL")),
    ("constipation", ("MACROGOL", 10, "g", "QD", "ORAL")), ("insomnia", ("ZOLPIDEM", 5, "mg", "QD", "ORAL")),
]
UNSCHED_BASE = 1000  # unscheduled visits get VISITNUM <previous scheduled>.1, .2 ...


# ------------------------------------------------------------------ helpers --

def iso(d: date | None) -> str | None:
    return d.isoformat() if d else None


def study_day(d: date | None, rf: date | None) -> int | None:
    if d is None or rf is None:
        return None
    n = (d - rf).days
    return n + 1 if n >= 0 else n  # there is no day 0


def pick(rng, dist: dict):
    keys = list(dist)
    p = np.array([float(dist[k]) for k in keys])
    return keys[rng.choice(len(keys), p=p / p.sum())]


def load_spec(path) -> dict:
    path = Path(path)
    txt = path.read_text()
    if path.suffix in (".yaml", ".yml"):
        import yaml
        return yaml.safe_load(txt)
    return json.loads(txt)


@dataclass
class Visit:
    visitnum: float
    visit: str
    planned_day: int | None  # study day (1 = first dose)
    window: int = 0
    assess: list = field(default_factory=list)
    kind: str = "scheduled"  # screening | scheduled | eot | fu | unscheduled


# ------------------------------------------------------------------ design ---

def build_visit_plan(spec) -> tuple[list[Visit], dict]:
    v = spec["visits"]
    plan: list[Visit] = []
    s = v["screening"]
    plan.append(Visit(1, s["visit"], s["day"], s.get("window", 0), s.get("assess", []), "screening"))
    if "repeating" in v:
        r = v["repeating"]
        every = r.get("assess_every", {})
        for n in range(1, r["max_repeats"] + 1):
            day = r["start_day"] + (n - 1) * r["interval_days"]
            assess = list(r.get("assess", [])) + [k for k, e in every.items() if (n - 1) % e == 0]
            plan.append(Visit(100 + n, r["pattern"].format(n=n), day, 0 if n == 1 else r.get("window", 0),
                              assess))
    for i, sv in enumerate(v.get("scheduled", []), start=2):
        plan.append(Visit(i, sv["visit"], sv["day"], sv.get("window", 0), sv.get("assess", [])))
    e = v.get("end_of_treatment")
    if e:
        plan.append(Visit(900, e["visit"], None, 3, e.get("assess", []), "eot"))
    for k, f in enumerate(v.get("follow_up", [])):
        plan.append(Visit(901 + k, f["visit"], None, 3, f.get("assess", []), "fu"))
    rs = v.get("response")
    return plan, rs


def trial_design(spec, plan) -> dict[str, pd.DataFrame]:
    st, arms = spec["study"], spec["arms"]
    sid = st["studyid"]
    te = [{"ETCD": "SCRN", "ELEMENT": "Screening", "TESTRL": "Informed consent",
           "TEENRL": "First dose of study treatment or screen failure", "TEDUR": f"P{abs(plan[0].planned_day)}D"}]
    ta, tv = [], []
    for a in arms:
        names = " + ".join(i["name"].title() for i in a["interventions"])
        te.append({"ETCD": f"TRT{a['armcd']}", "ELEMENT": f"Treatment {a['armcd']}: {names}"[:200],
                   "TESTRL": f"First dose of {names}"[:200], "TEENRL": "Last dose of study treatment",
                   "TEDUR": f"P{st['planned_treatment_days']}D" if st.get("planned_treatment_days") else None})
        for o, (etcd, el, ep) in enumerate([("SCRN", "Screening", "SCREENING"),
                                            (f"TRT{a['armcd']}", te[-1]["ELEMENT"], "TREATMENT"),
                                            ("FU", "Follow-up", "FOLLOW-UP")], start=1):
            ta.append({"STUDYID": sid, "DOMAIN": "TA", "ARMCD": a["armcd"], "ARM": a["arm"], "TAETORD": o,
                       "ETCD": etcd, "ELEMENT": el,
                       "TABRANCH": f"Randomized to {a['arm']}"[:200] if o == 1 else None,
                       "TATRANS": "If treatment is discontinued, go to Follow-up" if o == 2 else None,
                       "EPOCH": ep})
    te.append({"ETCD": "FU", "ELEMENT": "Follow-up", "TESTRL": "Day after last dose of study treatment",
               "TEENRL": "End of study participation",
               "TEDUR": None})
    te = [{"STUDYID": sid, "DOMAIN": "TE", **r} for r in te]
    for p in plan:
        if p.kind in ("eot", "fu"):
            rule = ("Within 7 days after last dose" if p.kind == "eot" else f"{p.visit}: after last dose")
        else:
            rule = f"Planned study day {p.planned_day}"
        tv.append({"STUDYID": sid, "DOMAIN": "TV", "VISITNUM": p.visitnum, "VISIT": p.visit,
                   "VISITDY": p.planned_day, "TVSTRL": rule[:200]})
    ti = [{"STUDYID": sid, "DOMAIN": "TI", "IETESTCD": c["code"], "IETEST": c["text"], "IECAT": c["cat"],
           "TIVERS": "1"} for c in spec.get("eligibility", [])]
    return {"TA": pd.DataFrame(ta), "TE": pd.DataFrame(te), "TV": pd.DataFrame(tv), "TI": pd.DataFrame(ti)}


def trial_summary(spec, n_rand, cutoff) -> pd.DataFrame:
    st, pop, arms = spec["study"], spec["population"], spec["arms"]
    trts = sorted({i["name"] for a in arms if a.get("type", "").startswith("EXPERIMENTAL")
                   for i in a["interventions"] if "PLACEBO" not in i["name"]})
    comps = sorted({i["name"] for a in arms if not a.get("type", "").startswith("EXPERIMENTAL")
                    for i in a["interventions"] if "PLACEBO" not in i["name"]})
    sexpop = "BOTH" if len(pop["sex"]) > 1 else ("F" if "F" in pop["sex"] else "M")
    has_pbo = any("PLACEBO" in i["name"] for a in arms for i in a["interventions"])
    rows = [
        ("TITLE", "Trial Title", f"[SYNTHETIC] {st['title']}"),
        ("ACRONYM", "Trial Acronym", st.get("acronym")),
        ("REGID", "Registry Identifier", st.get("source_nct")),
        ("SPONSOR", "Clinical Study Sponsor", "FICTIONAL SPONSOR (synthetic data)"),
        ("TPHASE", "Trial Phase Classification", st["phase"]),
        ("STYPE", "Study Type", st.get("study_type", "INTERVENTIONAL")),
        ("RANDOM", "Trial is Randomized", "Y" if st.get("randomized") else "N"),
        ("TBLIND", "Trial Blinding Schema", st.get("blinding")),
        ("INTMODEL", "Intervention Model", st.get("intervention_model")),
        ("TCNTRL", "Control Type", "PLACEBO" if has_pbo and not comps else ("ACTIVE" if comps else "NONE")),
        ("NARMS", "Planned Number of Arms", str(len(arms))),
        ("PLANSUB", "Planned Number of Subjects", str(spec["generation"]["n_randomized"])),
        ("ACTSUB", "Actual Number of Subjects", str(n_rand)),
        ("AGEMIN", "Planned Minimum Age of Subjects", f"P{pop['age_min']}Y"),
        ("AGEMAX", "Planned Maximum Age of Subjects", f"P{pop['age_max']}Y"),
        ("SEXPOP", "Sex of Participants", sexpop),
        ("SSTDTC", "Study Start Date", st["study_start"]),
        ("LENGTH", "Trial Length", f"P{abs(spec['visits']['screening']['day']) + st['planned_treatment_days'] + int(st.get('follow_up_days', 30))}D"
         if st.get("planned_treatment_days") else None),
        ("DCUTDTC", "Data Cutoff Date", iso(cutoff)),
        ("DCUTDESC", "Data Cutoff Description", "PRIMARY ANALYSIS" if st.get("study_end") is None else "FINAL ANALYSIS"),
        ("SENDTC", "Study End Date", st.get("study_end")),
        ("THERAREA", "Therapeutic Area", st.get("therapeutic_area_name")),
        ("SDTIGVER", "SDTM IG Version", "3.4"),
        ("SDTMVER", "SDTM Version", "2.0"),
    ]
    rows += [("TDIGRP", "Diagnosis Group", c) for c in st.get("conditions", [])[:3]]
    rows += [("INDIC", "Trial Disease/Condition Indication", c) for c in st.get("conditions", [])[:3]]
    rows += [("FCNTRY", "Planned Country of Investigational Sites", c)
             for c in dict.fromkeys(s["country"] for s in spec.get("sites", []))]
    rows += [("TRT", "Investigational Therapy or Treatment", t) for t in trts]
    rows += [("COMPTRT", "Comparative Treatment Name", t) for t in comps]
    out, seq = [], {}
    for cd, name, val in rows:
        if val is None and cd in ("LENGTH", "SENDTC", "THERAREA", "ACRONYM"):
            continue  # open-ended trial / study not yet ended / unknown area
        seq[cd] = seq.get(cd, 0) + 1
        rec = {"STUDYID": st["studyid"], "DOMAIN": "TS", "TSSEQ": seq[cd], "TSPARMCD": cd,
               "TSPARM": name, "TSVAL": val, "TSVALNF": None if val else "NA"}
        if val and len(val) > 200:  # SDTMIG: text beyond 200 chars continues in TSVAL1, TSVAL2, ...
            chunks = [val[i:i + 200] for i in range(0, len(val), 200)]
            rec["TSVAL"] = chunks[0]
            rec.update({f"TSVAL{k}": c for k, c in enumerate(chunks[1:], start=1)})
        out.append(rec)
    return pd.DataFrame(out)


# ---------------------------------------------------------------- subjects ---

class Generator:
    def __init__(self, spec: dict, n_override: int | None = None):
        self.spec = spec
        self.st = spec["study"]
        self.rng = np.random.default_rng(spec["generation"].get("seed", 1))
        self.n_rand = n_override or int(spec["generation"]["n_randomized"])
        self.start = date.fromisoformat(str(self.st["study_start"]))
        self.cutoff = date.fromisoformat(str(self.st["data_cutoff"]))
        self.oncology = self.st.get("therapeutic_area", "").upper() == "ONCOLOGY"
        self.plan, self.rs_plan = build_visit_plan(spec)
        self.arms = {a["armcd"]: a for a in spec["arms"]}
        self.disp = spec["disposition"]
        self.fu_days = int(self.st.get("follow_up_days", 30))
        self.rows: dict[str, list] = {d: [] for d in
                                      ["DM", "DS", "SE", "SV", "IE", "EX", "AE", "MH", "CM", "VS", "LB", "EG", "RS"]}
        self.ae_terms = spec.get("adverse_events", {}).get("terms", [])
        self.sites = self._sites()

    # ---- sites / arm allocation ------------------------------------------
    def _sites(self):
        out, n = [], 100
        for s in self.spec.get("sites") or [{"country": "USA", "weight": 1, "n_sites": 5}]:
            k = max(1, min(int(s.get("n_sites", 1)), 60))
            for _ in range(k):
                n += 1
                out.append((str(n), s["country"], float(s["weight"]) / k))
        return out

    def _allocation(self):
        arms = list(self.arms.values())
        block = [a["armcd"] for a in arms for _ in range(int(a.get("ratio", 1)))]
        seq = []
        while len(seq) < self.n_rand:  # permuted blocks keep the ratio exact
            b = list(block)
            self.rng.shuffle(b)
            seq += b
        return seq[: self.n_rand]

    # ---- per-subject timeline ---------------------------------------------
    def run(self) -> dict[str, pd.DataFrame]:
        sf_rate = float(self.disp.get("screen_failure_rate", 0.2))
        n_screen = int(round(self.n_rand / (1 - sf_rate)))
        alloc = iter(self._allocation())
        site_w = np.array([w for *_, w in self.sites])
        site_w /= site_w.sum()
        enrol_days = int(self.st.get("enrollment_period_days", 365))
        consent_offsets = np.sort(self.rng.integers(0, enrol_days, n_screen))
        is_sf = np.zeros(n_screen, bool)
        is_sf[self.rng.choice(n_screen, n_screen - self.n_rand, replace=False)] = True
        site_counter: dict[str, int] = {}
        for i in range(n_screen):
            siteid, country, _ = self.sites[self.rng.choice(len(self.sites), p=site_w)]
            site_counter[siteid] = site_counter.get(siteid, 0) + 1
            subjid = f"{siteid}{site_counter[siteid]:04d}"
            consent = self.start + timedelta(days=int(consent_offsets[i]))
            if consent > self.cutoff - timedelta(days=45):
                consent = self.cutoff - timedelta(days=45 + int(self.rng.integers(0, 30)))
            self.subject(subjid, siteid, country, consent, None if is_sf[i] else next(alloc))
        return {d: pd.DataFrame(r) for d, r in self.rows.items() if r}

    def subject(self, subjid, siteid, country, consent: date, armcd: str | None):
        rng, sid = self.rng, self.st["studyid"]
        usubjid = f"{sid}-{subjid}"
        pop = self.spec["population"]
        sex = pick(rng, pop["sex"])
        age = int(np.clip(round(rng.normal(pop["age_mean"], pop.get("age_sd", 10))), pop["age_min"],
                          pop["age_max"]))
        S = dict(usubjid=usubjid, subjid=subjid, siteid=siteid, country=country, sex=sex, age=age,
                 consent=consent, armcd=armcd, race=pick(rng, pop["race"]), ethnic=pick(rng, pop["ethnicity"]))
        screen_len = int(rng.integers(7, abs(self.plan[0].planned_day) + 1))
        S["screen_date"] = consent + timedelta(days=int(rng.integers(0, 3)))
        S["baseline"] = self._baselines(sex)
        self._medical_history(S)
        if armcd is None:
            return self._screen_failure(S, consent + timedelta(days=screen_len))
        S["rand"] = consent + timedelta(days=screen_len)
        if rng.random() < float(self.disp.get("randomized_not_treated", 0.015)):
            return self._not_treated(S)
        S["rf"] = S["rand"] + timedelta(days=int(rng.integers(0, 3)))
        self._timeline(S)
        self._adverse_events(S)
        self._finalise_timeline(S)
        self._exposure(S)
        self._visits_and_findings(S)
        self._disposition(S)
        self._elements(S)
        self._demographics(S)
        self._conmeds(S)

    # ---- core timeline -----------------------------------------------------
    def _timeline(self, S):
        rng, arm, rf = self.rng, S["armcd"], S["rf"]
        horizon = (self.cutoff - rf).days + 1  # last possible study day
        planned_trt = self.st.get("planned_treatment_days")
        if planned_trt:  # fixed-duration study: nobody stays beyond planned treatment + follow-up
            horizon = min(horizon, planned_trt + self.fu_days)
        death = None
        if rng.random() < self.disp.get("death", {}).get(arm, 0):
            death = int(rng.integers(30, max(31, horizon + 1)))
            death = death if death <= horizon else None
        withdraw = None
        for reason, p in self.disp.get("study_withdrawal", {}).get(arm, {}).items():
            if withdraw is None and rng.random() < p:
                d = int(rng.integers(15, max(16, horizon + 1)))
                if d <= horizon:
                    withdraw = (reason, d)
        trt_disc = None
        for reason, p in self.disp.get("treatment_discontinuation", {}).get(arm, {}).items():
            if trt_disc is None and rng.random() < p:
                d = int(rng.integers(28, max(29, horizon + 1)))
                if reason == "PROGRESSIVE DISEASE" and self.rs_plan:  # PD found at a tumour assessment
                    f, k = self.rs_plan["first_day"], self.rs_plan["interval_days"]
                    d = f + max(0, math.ceil((d - f) / k)) * k
                if d < horizon:  # an event on the cutoff day is not yet reflected in DS
                    trt_disc = (reason, d)
        ends = [("DEATH", death)] if death else []
        if withdraw:
            ends.append(withdraw)
        study_end_reason, study_end = min(ends, key=lambda x: x[1]) if ends else (None, None)
        S_cut = (self.cutoff - rf).days + 1
        trt_end, trt_reason = horizon, None
        cands = [(trt_disc[1], trt_disc[0])] if trt_disc else []
        if study_end:
            cands.append((study_end, study_end_reason))
        if planned_trt:
            cands.append((planned_trt, "COMPLETED"))
        if cands:
            d, r = min(cands)
            if d <= horizon:
                trt_end, trt_reason = d, r
        if planned_trt and study_end is None:
            done = planned_trt + self.fu_days
            if done <= S_cut:
                study_end, study_end_reason = done, "COMPLETED"
        S.update(cutoff_day=(self.cutoff - rf).days + 1, horizon=horizon, death=death, trt_end=trt_end, trt_reason=trt_reason,
                 study_end=study_end, study_end_reason=study_end_reason, pd_day=(
                     trt_disc[1] if trt_disc and trt_disc[0] == "PROGRESSIVE DISEASE" and trt_reason ==
                     "PROGRESSIVE DISEASE" else None))

    def _adverse_events(self, S):
        rng, arm = self.rng, S["armcd"]
        window_end = min(S["trt_end"] + self.fu_days, S["study_end"] or S["horizon"], S["horizon"])
        exposure = max(1, S["trt_end"])
        aes = []
        for t in self.ae_terms:
            p = float(t["incidence"].get(arm, 0))
            if p <= 0:
                continue
            p_eff = p * min(1.0, (exposure / 180) ** 0.5)
            if rng.random() >= p_eff:
                continue
            onset = 1 + int(min(window_end - 1, rng.exponential(min(90, max(7, exposure / 3)))))
            dur = max(1, int(rng.lognormal(math.log(12), 0.9)))
            serious = rng.random() < float(t.get("serious_fraction", {}).get(arm, 0))
            aes.append(self._ae_record(t, onset, dur, serious, S))
        # a share of deaths is attributed to a fatal serious AE
        if S["death"] and rng.random() < 0.35 and self.ae_terms:
            w = np.array([max(1e-4, t["incidence"].get(arm, 0) * t.get("serious_fraction", {}).get(arm, 0))
                          for t in self.ae_terms])
            t = self.ae_terms[rng.choice(len(w), p=w / w.sum())]
            onset = max(1, S["death"] - int(rng.integers(0, 14)))
            r = self._ae_record(t, onset, S["death"] - onset, True, S)
            r.update(fatal=True, out="FATAL", grade=5)
            if onset >= S["death"]:
                r["acn"] = "NOT APPLICABLE"  # died the day it started: no action with study treatment
            aes.append(r)
        # a registry-reported "withdrawn due to AE" needs the AE that explains it
        if S["trt_reason"] == "ADVERSE EVENT" and self.ae_terms and not any(
                x["acn"] == "DRUG WITHDRAWN" and x["on"] <= S["trt_end"] for x in aes):
            w = np.array([max(1e-4, t["incidence"].get(arm, 0)) for t in self.ae_terms])
            t = self.ae_terms[rng.choice(len(w), p=w / w.sum())]
            r = self._ae_record(t, S["trt_end"], max(1, int(rng.lognormal(math.log(12), 0.9))),
                                rng.random() < 0.3, S)
            r["acn"] = "DRUG WITHDRAWN"
            aes.append(r)
        # AE-driven withdrawal shortens treatment (and is the EOT reason)
        on_trt = [a for a in aes if a["on"] <= S["trt_end"]]
        wd = [a for a in on_trt if a["acn"] == "DRUG WITHDRAWN"]
        if wd:
            first = min(wd, key=lambda a: a["on"])
            if first["on"] <= S["trt_end"]:  # same-day tie: the AE is the documented reason
                S["trt_end"], S["trt_reason"], S["pd_day"] = first["on"], "ADVERSE EVENT", None
                if not self.oncology and S["study_end"] is None or (
                        not self.oncology and S["study_end_reason"] == "COMPLETED"):
                    done = first["on"] + self.fu_days
                    if done <= S["horizon"]:
                        S["study_end"], S["study_end_reason"] = done, "ADVERSE EVENT"
        S["aes"] = aes

    def _ae_record(self, t, onset, dur, serious, S):
        rng = self.rng
        if self.oncology:
            grade = int(rng.choice([3, 4], p=[.8, .2])) if serious else int(rng.choice([1, 2, 3], p=[.55, .35, .1]))
            sev = None
        else:
            grade = None
            sev = (pick(rng, {"MODERATE": .5, "SEVERE": .5}) if serious
                   else pick(rng, {"MILD": .6, "MODERATE": .32, "SEVERE": .08}))
        heavy = serious or (grade or 0) >= 3 or sev == "SEVERE"
        acn = pick(rng, {"DOSE NOT CHANGED": .45, "DRUG INTERRUPTED": .3, "DOSE REDUCED": .1,
                         "DRUG WITHDRAWN": .15} if heavy else
                   {"DOSE NOT CHANGED": .9, "DRUG INTERRUPTED": .07, "DOSE REDUCED": .03})
        return dict(term=t["term"], bodsys=t.get("bodsys"), on=onset, off=onset + dur, serious=serious,
                    grade=grade, sev=sev, acn=acn, fatal=False, out=None,
                    rel=pick(rng, {"RELATED": .45, "NOT RELATED": .55}), hosp=serious and rng.random() < .8)

    def _finalise_timeline(self, S):
        """Apply death/cutoff truncation once AEs are known."""
        last = min(x for x in [S["study_end"], S["horizon"]] if x)
        S["last"] = last
        S["trt_end"] = min(S["trt_end"], last)
        keep = []
        for a in S["aes"]:
            if a["on"] > min(last, S["trt_end"] + self.fu_days):
                continue
            if a["on"] > S["trt_end"]:
                a["acn"] = "NOT APPLICABLE"
            if a["fatal"]:
                a["off"] = S["death"]
            elif a["off"] > last:
                a["off"] = None  # ongoing at last contact
                a["out"] = "NOT RECOVERED/NOT RESOLVED"
            else:
                a["out"] = "RECOVERED/RESOLVED" if self.rng.random() < .95 else "RECOVERED/RESOLVED WITH SEQUELAE"
            if S["death"] and a["off"] is None:
                a["off"], a["out"] = None, "NOT RECOVERED/NOT RESOLVED"
            keep.append(a)
        S["aes"] = sorted(keep, key=lambda a: (a["on"], a["term"]))

    # ---- domains -------------------------------------------------------------
    def D(self, S, day):  # study day -> date
        return S["rf"] + timedelta(days=day - 1 if day > 0 else day)

    def _exposure(self, S):
        """EX from the timeline: interruptions and reductions come from AEACN, dosing stops at trt_end."""
        arm = self.arms[S["armcd"]]
        # day 1 is always dosed (it defines RFXSTDTC); interruptions start the next day at the earliest
        interrupts = [(max(2, a["on"]), min(a["off"] or a["on"] + 14, a["on"] + 14)) for a in S["aes"]
                      if a["acn"] == "DRUG INTERRUPTED"]
        reductions = sorted(a["on"] for a in S["aes"] if a["acn"] == "DOSE REDUCED")
        interval = self.spec["visits"].get("repeating", {}).get("interval_days", 28)
        out = []
        for iv in arm["interventions"]:
            def state(day):  # None = no dosing that day, else (dose, EXADJ)
                if any(s <= day <= e for s, e in interrupts):
                    return None
                k = sum(1 for r in reductions if r < day)
                return round(float(iv["dose"]) * 0.75 ** k, 1), ("ADVERSE EVENT" if k else None)
            every = int(iv.get("every_days", 1))
            if every == 1:  # continuous dosing -> one record per dispensing interval and dose level
                seg, seg_start = None, None
                for day in range(1, S["trt_end"] + 2):
                    cur = state(day) if day <= S["trt_end"] else None
                    new_interval = (day - 1) % interval == 0
                    if seg is not None and (cur != seg or new_interval):
                        out.append((iv, seg_start, day - 1, *seg))
                        seg = None
                    if cur is not None and seg is None:
                        seg, seg_start = cur, day
            else:  # infusions / injections -> one record per administration
                for day in range(1, S["trt_end"] + 1, every):
                    cur = state(day)
                    if cur is not None:
                        out.append((iv, day, day, *cur))
        if not out:
            iv = arm["interventions"][0]
            out.append((iv, 1, 1, float(iv["dose"]), None))
        S["last_dose"] = max(e for _, _, e, _, _ in out)
        for iv, s, e, dose, adj in sorted(out, key=lambda x: (x[1], x[0]["name"])):
            self.rows["EX"].append({"USUBJID": S["usubjid"], "EXTRT": iv["name"], "EXDOSE": dose,
                                    "EXDOSU": iv.get("unit", "mg"), "EXDOSFRM": iv.get("dosfrm"),
                                    "EXDOSFRQ": iv.get("frequency"), "EXROUTE": iv.get("route"),
                                    "EXADJ": adj, "EXSTDTC": iso(self.D(S, s)), "EXENDTC": iso(self.D(S, e)),
                                    "_rf": S["rf"]})

    def _baselines(self, sex):
        rng = self.rng
        b = {t[0]: max(t[6] * 0.6, rng.normal(t[4], t[5] * 0.8)) for t in LB_PANEL}
        for t in VS_PANEL:
            if t[0] == "WEIGHT":
                b[t[0]] = rng.normal(64 if sex == "F" else 77, 11)
            else:
                b[t[0]] = rng.normal(t[3], t[4] * 0.8)
        b["HEIGHT"] = rng.normal(160 if sex == "F" else 172, 7)
        for t in EG_PANEL:
            b[t[0]] = rng.normal(t[3], t[4] * 0.8)
        return b

    def _value(self, S, dom, testcd, day, sd, low=None, high=None):
        v = S["baseline"][testcd] + self.rng.normal(0, sd * 0.45)
        for a in S["aes"]:
            if a["off"] is not None and not (a["on"] <= day <= a["off"]):
                continue
            if a["off"] is None and day < a["on"]:
                continue
            for frag, ldom, lt, direction in AE_FINDING_LINKS:
                if ldom == dom and lt == testcd and frag in a["term"].lower():
                    sev = 1 + (a["grade"] or {"MILD": 1, "MODERATE": 2, "SEVERE": 3}.get(a["sev"], 1)) / 3
                    if direction == "low" and low is not None:
                        v = min(v, low * self.rng.uniform(0.5, 0.9) / sev ** 0.3)
                    elif direction == "high":
                        ref = high if high is not None else S["baseline"][testcd] * 1.1
                        v = max(v, ref * self.rng.uniform(1.15, 1.6) * sev ** 0.4)
        return v

    def _visits_and_findings(self, S):
        rng, sched = self.rng, []
        last, trt_end = S["last"], S["trt_end"]
        scr = self.plan[0]
        sched.append((scr, (S["screen_date"] - S["rf"]).days))  # negative study-day offset
        for p in self.plan[1:]:
            if p.kind == "scheduled" and (p.planned_day <= trt_end or p.planned_day == S.get("pd_day")):
                jitter = int(rng.integers(-p.window, p.window + 1)) if p.window else 0
                d = max(1, min(trt_end, p.planned_day + jitter)) if p.planned_day > 1 else 1
                if p.planned_day == S.get("pd_day"):
                    d = trt_end  # PD found at this assessment -> treatment stops that day
                if p.planned_day > 1 and rng.random() < 0.03 and p.planned_day != S.get("pd_day"):
                    continue  # missed visit
                sched.append((p, d))
        ended = trt_end < S["horizon"] and S["trt_reason"] is not None
        for p in self.plan:
            if p.kind == "eot" and ended:
                d = trt_end + int(rng.integers(1, 8))
                if d <= last and (not S["death"] or d < S["death"]):
                    sched.append((p, d))
            if p.kind == "fu" and ended:
                k = int(p.visitnum) - 901
                off = self.spec["visits"]["follow_up"][k].get("offset_days", 30)
                d = trt_end + off + int(rng.integers(-3, 4))
                if d <= last and (not S["death"] or d < S["death"]):
                    sched.append((p, d))
        # findings that must exist because an AE is linked to them -> unscheduled visit
        sched.sort(key=lambda x: x[1])
        extra = []
        for a in S["aes"]:
            for frag, dom, testcd, _ in AE_FINDING_LINKS:
                if frag not in a["term"].lower():
                    continue
                end = a["off"] if a["off"] is not None else last
                if any(dom in p.assess and a["on"] <= d <= end for p, d in sched + extra):
                    continue
                d = min(a["on"] + 1, last)
                prev = max([p.visitnum for p, dd in sched if dd <= d and p.kind != "unscheduled"] or [1])
                n = sum(1 for p, _ in extra if int(p.visitnum * 10) // 10 == int(prev)) + 1
                vn = round(int(prev) + n / 10, 1)
                extra.append((Visit(vn, f"UNSCHEDULED {vn}", None, 0, [dom], "unscheduled"), d))
        S["sv"] = sorted(sched + extra, key=lambda x: (x[1], x[0].visitnum))
        for p, d in S["sv"]:
            dt = self.D(S, d) if d >= 1 else S["rf"] + timedelta(days=d)
            self.rows["SV"].append({"USUBJID": S["usubjid"], "VISITNUM": p.visitnum, "VISIT": p.visit,
                                    "VISITDY": p.planned_day, "SVPRESP": None if p.kind == "unscheduled" else "Y",
                                    "SVOCCUR": None if p.kind == "unscheduled" else "Y",
                                    "SVSTDTC": iso(dt), "SVENDTC": iso(dt), "_rf": S["rf"]})
            self._findings_at(S, p, d, dt)
        if self.rs_plan and "RS" in self.spec["generation"].get("domains", []):
            self._response(S)

    def _findings_at(self, S, p, d, dt):
        U = S["usubjid"]
        base = dict(USUBJID=U, VISITNUM=p.visitnum, VISIT=p.visit, VISITDY=p.planned_day, _rf=S["rf"])
        if "VS" in p.assess:
            for cd, test, unit, mean, sd, dec, pos in VS_PANEL:
                v = self._value(S, "VS", cd, d, sd if sd else 1.5, high=140 if cd == "SYSBP" else (
                    37.5 if cd == "TEMP" else None))
                if cd == "TEMP" and v > 37.5:
                    v = min(v, 39.8)
                v = round(v, dec)
                self.rows["VS"].append({**base, "VSTESTCD": cd, "VSTEST": test, "VSPOS": pos,
                                        "VSORRES": str(v), "VSORRESU": unit, "VSSTRESC": str(v), "VSSTRESN": v,
                                        "VSSTRESU": unit, "VSDTC": iso(dt)})
            if p.kind == "screening":
                h = round(S["baseline"]["HEIGHT"], 1)
                self.rows["VS"].append({**base, "VSTESTCD": "HEIGHT", "VSTEST": "Height", "VSPOS": None,
                                        "VSORRES": str(h), "VSORRESU": "cm", "VSSTRESC": str(h), "VSSTRESN": h,
                                        "VSSTRESU": "cm", "VSDTC": iso(dt)})
        if "LB" in p.assess:
            for cd, test, cat, unit, mean, sd, lo, hi, spec in LB_PANEL:
                v = max(0.01, self._value(S, "LB", cd, d, sd, lo, hi))
                dec = 0 if mean >= 50 else (1 if mean >= 5 else 2)
                v = round(v, dec)
                nr = "LOW" if v < lo else ("HIGH" if v > hi else "NORMAL")
                self.rows["LB"].append({**base, "LBTESTCD": cd, "LBTEST": test, "LBCAT": cat, "LBORRES": str(v),
                                        "LBORRESU": unit, "LBORNRLO": str(lo), "LBORNRHI": str(hi),
                                        "LBSTRESC": str(v), "LBSTRESN": v, "LBSTRESU": unit, "LBSTNRLO": lo,
                                        "LBSTNRHI": hi, "LBNRIND": nr, "LBSPEC": spec, "LBDTC": iso(dt)})
        if "EG" in p.assess:
            abn = False
            for cd, test, unit, mean, sd in EG_PANEL:
                v = int(round(self._value(S, "EG", cd, d, sd, high=450 if cd == "QTCFAG" else None)))
                abn |= cd == "QTCFAG" and v > 450
                self.rows["EG"].append({**base, "EGTESTCD": cd, "EGTEST": test, "EGPOS": "SUPINE",
                                        "EGORRES": str(v), "EGORRESU": unit, "EGSTRESC": str(v), "EGSTRESN": v,
                                        "EGSTRESU": unit, "EGDTC": iso(dt)})
            interp = "ABNORMAL" if abn else "NORMAL"
            self.rows["EG"].append({**base, "EGTESTCD": "INTP", "EGTEST": "Interpretation", "EGPOS": "SUPINE",
                                    "EGORRES": interp, "EGORRESU": None, "EGSTRESC": interp, "EGSTRESN": None,
                                    "EGSTRESU": None, "EGDTC": iso(dt)})

    def _response(self, S):
        """Overall response at tumour-assessment visits; PD exactly where treatment stopped for PD."""
        rng = self.rng
        best = pick(rng, {"PR": .55, "SD": .35, "CR": .05, "PD": .05}) if S["pd_day"] is None else \
            pick(rng, {"PR": .5, "SD": .5})
        for p, d in S["sv"]:
            if p.kind != "scheduled" or p.planned_day is None or p.planned_day < self.rs_plan["first_day"]:
                continue
            if (p.planned_day - self.rs_plan["first_day"]) % self.rs_plan["interval_days"]:
                continue
            is_pd = S["pd_day"] is not None and p.planned_day == S["pd_day"]
            res = "PD" if is_pd else (best if best != "PD" else "SD")
            if S["pd_day"] is not None and p.planned_day > S["pd_day"]:
                break
            dt = self.D(S, d)
            self.rows["RS"].append({"USUBJID": S["usubjid"], "RSTESTCD": "OVRLRESP", "RSTEST": "Overall Response",
                                    "RSCAT": "RECIST 1.1", "RSORRES": res, "RSSTRESC": res, "RSEVAL": "INVESTIGATOR",
                                    "VISITNUM": p.visitnum, "VISIT": p.visit, "VISITDY": p.planned_day,
                                    "RSDTC": iso(dt), "_rf": S["rf"]})

    def _disposition(self, S):
        U, rows = S["usubjid"], self.rows["DS"]
        rows.append({"USUBJID": U, "DSTERM": "INFORMED CONSENT OBTAINED", "DSDECOD": "INFORMED CONSENT OBTAINED",
                     "DSCAT": "PROTOCOL MILESTONE", "DSSTDTC": iso(S["consent"]), "_rf": S.get("rf")})
        rows.append({"USUBJID": U, "DSTERM": "RANDOMIZED", "DSDECOD": "RANDOMIZED", "DSCAT": "PROTOCOL MILESTONE",
                     "DSSTDTC": iso(S["rand"]), "_rf": S.get("rf")})
        if S.get("trt_reason") and S["trt_end"] < S["horizon"]:
            r = S["trt_reason"]
            rows.append({"USUBJID": U, "DSTERM": r, "DSDECOD": r, "DSCAT": "DISPOSITION EVENT",
                         "DSSCAT": "STUDY TREATMENT", "DSSTDTC": iso(self.D(S, S["trt_end"])), "_rf": S["rf"]})
        if S.get("study_end") and S["study_end"] <= S["horizon"]:
            r = S["study_end_reason"]
            rows.append({"USUBJID": U, "DSTERM": r, "DSDECOD": r, "DSCAT": "DISPOSITION EVENT",
                         "DSSCAT": "STUDY PARTICIPATION", "DSSTDTC": iso(self.D(S, S["study_end"])), "_rf": S["rf"]})
        # AE domain written here so it shares the finalised timeline
        for a in S["aes"]:
            self.rows["AE"].append({
                "USUBJID": U, "AETERM": a["term"].upper(), "AEDECOD": a["term"], "AEBODSYS": a["bodsys"],
                "AESEV": a["sev"], "AETOXGR": str(a["grade"]) if a["grade"] else None,
                "AESER": "Y" if a["serious"] else "N", "AEACN": a["acn"], "AEREL": a["rel"], "AEOUT": a["out"],
                "AESDTH": "Y" if a["fatal"] else ("N" if a["serious"] else None),
                "AESHOSP": ("Y" if a["hosp"] else "N") if a["serious"] else None,
                "AESTDTC": iso(self.D(S, a["on"])), "AEENDTC": iso(self.D(S, a["off"])) if a["off"] else None,
                "_rf": S["rf"]})

    def _elements(self, S):
        U, rows = S["usubjid"], self.rows["SE"]
        last_date = self.D(S, S["last"])
        rows.append({"USUBJID": U, "ETCD": "SCRN", "ELEMENT": "Screening", "TAETORD": 1, "EPOCH": "SCREENING",
                     "SESTDTC": iso(S["consent"]), "SEENDTC": iso(S["rf"]), "_rf": S["rf"]})
        te = next(r for r in self._te_cache() if r["ETCD"] == f"TRT{S['armcd']}")
        trt_stop = self.D(S, S["trt_end"] + 1)
        rows.append({"USUBJID": U, "ETCD": te["ETCD"], "ELEMENT": te["ELEMENT"], "TAETORD": 2,
                     "EPOCH": "TREATMENT", "SESTDTC": iso(S["rf"]),
                     "SEENDTC": iso(min(trt_stop, last_date) if trt_stop <= last_date else last_date),
                     "_rf": S["rf"]})
        if trt_stop <= last_date:
            rows.append({"USUBJID": U, "ETCD": "FU", "ELEMENT": "Follow-up", "TAETORD": 3, "EPOCH": "FOLLOW-UP",
                         "SESTDTC": iso(trt_stop), "SEENDTC": iso(last_date), "_rf": S["rf"]})

    def _te_cache(self):
        if not hasattr(self, "_te"):
            self._te = trial_design(self.spec, self.plan)["TE"].to_dict("records")
        return self._te

    def _demographics(self, S):
        a = self.arms.get(S["armcd"]) if S["armcd"] else None
        treated = "rf" in S and S.get("treated", True)
        last = self.D(S, S["last"]) if "last" in S else S.get("end_date")
        self.rows["DM"].append({
            "USUBJID": S["usubjid"], "SUBJID": S["subjid"], "SITEID": S["siteid"],
            "RFSTDTC": iso(S.get("rf")), "RFENDTC": iso(last if S.get("rf") else None),
            "RFXSTDTC": iso(S["rf"]) if treated else None,
            "RFXENDTC": iso(self.D(S, S["last_dose"])) if treated else None,
            "RFICDTC": iso(S["consent"]), "RFPENDTC": iso(last),
            "DTHDTC": iso(self.D(S, S["death"])) if S.get("death") and S["death"] <= S.get("last", 0) else None,
            "DTHFL": "Y" if S.get("death") and S["death"] <= S.get("last", 0) else None,
            "AGE": S["age"], "AGEU": "YEARS", "SEX": S["sex"], "RACE": S["race"], "ETHNIC": S["ethnic"],
            "ARMCD": a["armcd"] if a else None, "ARM": a["arm"] if a else None,
            "ACTARMCD": a["armcd"] if a and treated else None, "ACTARM": a["arm"] if a and treated else None,
            "ARMNRS": None if a and treated else ("ASSIGNED, NOT TREATED" if a else "SCREEN FAILURE"),
            "COUNTRY": S["country"], "DMDTC": iso(S["consent"]), "_rf": S.get("rf")})

    def _medical_history(self, S):
        rng = self.rng
        S["mh"] = []
        for m in self.spec.get("medical_history", []):
            if rng.random() < m.get("prob", 1):
                S["mh"].append((m["term"], m.get("bodsys"), "PRIMARY DIAGNOSIS" if m.get("indication") else
                                "GENERAL", int(rng.integers(20, 400)), None))
        age_factor = min(2.0, max(0.3, (S["age"] - 30) / 30))
        for term, soc, prev, med in COMORBIDITIES:
            if rng.random() < prev * age_factor:
                S["mh"].append((term, soc, "GENERAL", int(rng.integers(365, 365 * 15)), med))
        for term, soc, cat, days_before, _ in S["mh"]:
            self.rows["MH"].append({"USUBJID": S["usubjid"], "MHTERM": term, "MHDECOD": term, "MHBODSYS": soc,
                                    "MHCAT": cat, "MHSTDTC": iso(S["consent"] - timedelta(days=days_before)),
                                    "MHENRTPT": "ONGOING", "MHENTPT": "SCREENING", "MHDTC": iso(S["consent"]),
                                    "_rf": None})

    def _conmeds(self, S):
        rng, U = self.rng, S["usubjid"]
        last = self.D(S, S["last"]) if "last" in S else S["end_date"]
        for term, _, _, days_before, med in S["mh"]:
            if med and rng.random() < 0.85:
                name, dose, unit, frq, route = med
                start = max(S["consent"] - timedelta(days=days_before) + timedelta(days=int(rng.integers(0, 60))),
                            S["consent"] - timedelta(days=days_before))
                self.rows["CM"].append({"USUBJID": U, "CMTRT": name, "CMDECOD": name, "CMINDC": term,
                                        "CMDOSE": dose, "CMDOSU": unit, "CMDOSFRQ": frq, "CMROUTE": route,
                                        "CMSTDTC": iso(min(start, S["consent"])), "CMENDTC": None,
                                        "CMENRTPT": "ONGOING", "CMENTPT": "LAST CONTACT", "_rf": S.get("rf")})
        for a in S.get("aes", []):
            for frag, med in AE_TREATMENTS:
                if frag in a["term"].lower() and rng.random() < 0.7:
                    name, dose, unit, frq, route = med
                    end = self.D(S, a["off"]) if a["off"] else None
                    self.rows["CM"].append({"USUBJID": U, "CMTRT": name, "CMDECOD": name, "CMINDC": a["term"],
                                            "CMDOSE": dose, "CMDOSU": unit, "CMDOSFRQ": frq, "CMROUTE": route,
                                            "CMSTDTC": iso(self.D(S, a["on"])), "CMENDTC": iso(end),
                                            "CMENRTPT": None if end else "ONGOING",
                                            "CMENTPT": None if end else "LAST CONTACT", "_rf": S["rf"]})
                    break

    # ---- non-treated paths --------------------------------------------------
    def _screen_failure(self, S, end: date):
        rng, U = self.rng, S["usubjid"]
        crit = self.spec.get("eligibility") or [{"code": "INCL01", "text": "Meets all inclusion criteria",
                                                 "cat": "INCLUSION"}]
        c = crit[rng.integers(len(crit))]
        self.rows["IE"].append({"USUBJID": U, "IETESTCD": c["code"], "IETEST": c["text"], "IECAT": c["cat"],
                                "IEORRES": "N" if c["cat"] == "INCLUSION" else "Y",
                                "IESTRESC": "N" if c["cat"] == "INCLUSION" else "Y",
                                "VISITNUM": 1.0, "VISIT": self.plan[0].visit, "IEDTC": iso(S["screen_date"]),
                                "_rf": None})
        self.rows["DS"].append({"USUBJID": U, "DSTERM": "INFORMED CONSENT OBTAINED",
                                "DSDECOD": "INFORMED CONSENT OBTAINED", "DSCAT": "PROTOCOL MILESTONE",
                                "DSSTDTC": iso(S["consent"]), "_rf": None})
        self.rows["DS"].append({"USUBJID": U, "DSTERM": "SCREEN FAILURE", "DSDECOD": "SCREEN FAILURE",
                                "DSCAT": "DISPOSITION EVENT", "DSSCAT": "STUDY PARTICIPATION",
                                "DSSTDTC": iso(end), "_rf": None})
        self.rows["SE"].append({"USUBJID": U, "ETCD": "SCRN", "ELEMENT": "Screening", "TAETORD": 1,
                                "EPOCH": "SCREENING", "SESTDTC": iso(S["consent"]), "SEENDTC": iso(end), "_rf": None})
        p = self.plan[0]
        self.rows["SV"].append({"USUBJID": U, "VISITNUM": p.visitnum, "VISIT": p.visit, "VISITDY": p.planned_day,
                                "SVPRESP": "Y", "SVOCCUR": "Y", "SVSTDTC": iso(S["screen_date"]),
                                "SVENDTC": iso(S["screen_date"]), "_rf": None})
        S.update(aes=[], rf=None, end_date=end)
        S_f = dict(S, rf=S["screen_date"])  # findings need a reference date only for value generation
        self._findings_at(S_f, p, 0, S["screen_date"])
        for dom in ("VS", "LB", "EG"):
            for r in self.rows[dom][-30:]:
                if r["USUBJID"] == U:
                    r["_rf"] = None
        S["rf"] = None
        self._demographics_sf(S, end)
        self._conmeds_sf(S, end)

    def _demographics_sf(self, S, end):
        self.rows["DM"].append({
            "USUBJID": S["usubjid"], "SUBJID": S["subjid"], "SITEID": S["siteid"], "RFSTDTC": None,
            "RFENDTC": None, "RFXSTDTC": None, "RFXENDTC": None, "RFICDTC": iso(S["consent"]),
            "RFPENDTC": iso(end), "DTHDTC": None, "DTHFL": None, "AGE": S["age"], "AGEU": "YEARS",
            "SEX": S["sex"], "RACE": S["race"], "ETHNIC": S["ethnic"], "ARMCD": None, "ARM": None,
            "ACTARMCD": None, "ACTARM": None, "ARMNRS": "SCREEN FAILURE", "COUNTRY": S["country"],
            "DMDTC": iso(S["consent"]), "_rf": None})

    def _conmeds_sf(self, S, end):
        S["last_date"] = end
        for term, _, _, days_before, med in S["mh"]:
            if med and self.rng.random() < 0.85:
                name, dose, unit, frq, route = med
                self.rows["CM"].append({"USUBJID": S["usubjid"], "CMTRT": name, "CMDECOD": name, "CMINDC": term,
                                        "CMDOSE": dose, "CMDOSU": unit, "CMDOSFRQ": frq, "CMROUTE": route,
                                        "CMSTDTC": iso(S["consent"] - timedelta(days=days_before)),
                                        "CMENDTC": None, "CMENRTPT": "ONGOING", "CMENTPT": "LAST CONTACT", "_rf": None})

    def _not_treated(self, S):
        """Randomized but never dosed: RFSTDTC = randomization date, no EX, ARMNRS set."""
        rng, U = self.rng, S["usubjid"]
        S["rf"] = S["rand"]
        end_day = int(rng.integers(1, 30))
        S.update(aes=[], treated=False, horizon=(self.cutoff - S["rf"]).days + 1)
        S["last"] = min(end_day, S["horizon"])
        S["study_end"], S["study_end_reason"] = S["last"], "WITHDRAWAL BY SUBJECT"
        S["trt_reason"], S["trt_end"] = None, 0
        self.rows["DS"].append({"USUBJID": U, "DSTERM": "INFORMED CONSENT OBTAINED",
                                "DSDECOD": "INFORMED CONSENT OBTAINED", "DSCAT": "PROTOCOL MILESTONE",
                                "DSSTDTC": iso(S["consent"]), "_rf": S["rf"]})
        self.rows["DS"].append({"USUBJID": U, "DSTERM": "RANDOMIZED", "DSDECOD": "RANDOMIZED",
                                "DSCAT": "PROTOCOL MILESTONE", "DSSTDTC": iso(S["rand"]), "_rf": S["rf"]})
        self.rows["DS"].append({"USUBJID": U, "DSTERM": "WITHDRAWAL BY SUBJECT", "DSDECOD": "WITHDRAWAL BY SUBJECT",
                                "DSCAT": "DISPOSITION EVENT", "DSSCAT": "STUDY PARTICIPATION",
                                "DSSTDTC": iso(self.D(S, S["last"])), "_rf": S["rf"]})
        self.rows["SE"].append({"USUBJID": U, "ETCD": "SCRN", "ELEMENT": "Screening", "TAETORD": 1,
                                "EPOCH": "SCREENING", "SESTDTC": iso(S["consent"]), "SEENDTC": iso(S["rf"]),
                                "_rf": S["rf"]})
        self.rows["SE"].append({"USUBJID": U, "ETCD": "FU", "ELEMENT": "Follow-up", "TAETORD": 3,
                                "EPOCH": "FOLLOW-UP", "SESTDTC": iso(S["rf"]),
                                "SEENDTC": iso(self.D(S, S["last"])), "_rf": S["rf"]})
        p = self.plan[0]
        self.rows["SV"].append({"USUBJID": U, "VISITNUM": p.visitnum, "VISIT": p.visit, "VISITDY": p.planned_day,
                                "SVPRESP": "Y", "SVOCCUR": "Y", "SVSTDTC": iso(S["screen_date"]),
                                "SVENDTC": iso(S["screen_date"]), "_rf": S["rf"]})
        self._findings_at(S, p, (S["screen_date"] - S["rf"]).days, S["screen_date"])
        self._demographics(S)
        self._conmeds(S)


# ----------------------------------------------------------------- derive ----

def epoch_lookup(se: pd.DataFrame):
    by = {}
    for r in se.itertuples():
        by.setdefault(r.USUBJID, []).append((date.fromisoformat(r.SESTDTC), date.fromisoformat(r.SEENDTC), r.EPOCH))

    def f(usubjid, dtc):
        if not dtc:
            return None
        d = date.fromisoformat(dtc[:10])
        els = by.get(usubjid, [])
        for i, (s, e, ep) in enumerate(els):  # element end == next element start; last element is inclusive
            if s <= d < e or (i == len(els) - 1 and s <= d <= e):
                return ep
        return None
    return f


def derive(domains: dict[str, pd.DataFrame], sid: str) -> dict[str, pd.DataFrame]:
    ep = epoch_lookup(domains["SE"])
    dm = domains["DM"]
    to_d = lambda v: date.fromisoformat(v[:10]) if isinstance(v, str) else None
    rf_map = {u: to_d(v) for u, v in zip(dm["USUBJID"], dm["RFSTDTC"])}
    rfx_map = {u: to_d(v) for u, v in zip(dm["USUBJID"], dm["RFXSTDTC"])}
    dtc_col = {"DS": "DSSTDTC", "SV": "SVSTDTC", "EX": "EXSTDTC", "AE": "AESTDTC", "CM": None, "MH": None,
               "VS": "VSDTC", "LB": "LBDTC", "EG": "EGDTC", "RS": "RSDTC", "IE": "IEDTC", "SE": None, "DM": None}
    for dom, df in domains.items():
        if dom in ("TS", "TA", "TE", "TV", "TI"):
            continue
        df.insert(0, "DOMAIN", dom)
        df.insert(0, "STUDYID", sid)
        df.pop("_rf") if "_rf" in df else None
        # --SEQ
        if dom not in ("DM", "SV"):
            sort_cols = ["USUBJID"] + [c for c in df.columns if c.endswith("DTC")][:1]
            df = df.sort_values(sort_cols, kind="stable", na_position="first")
            df[f"{dom}SEQ"] = df.groupby("USUBJID").cumcount() + 1
        # study days
        for c in [c for c in df.columns if c.endswith("DTC") and c not in ("RFICDTC",)]:
            if dom == "DM" or c in ("DMDTC",):
                continue
            target = c[:-3] + "DY"
            rf = df["USUBJID"].map(rf_map)
            if c.endswith("STDTC") or c.endswith("ENDTC") or c == f"{dom}DTC":
                df[target] = [study_day(date.fromisoformat(v[:10]) if isinstance(v, str) else None, r)
                              for v, r in zip(df[c], rf)]
        if dom == "DM":
            df["DMDY"] = [study_day(date.fromisoformat(d), date.fromisoformat(r) if isinstance(r, str) else None)
                          for d, r in zip(df["DMDTC"], df["RFSTDTC"])]
        # EPOCH
        c = dtc_col.get(dom)
        if c and c in df:
            df["EPOCH"] = [ep(u, v) for u, v in zip(df["USUBJID"], df[c])]
        # last observation before exposure flag
        if dom in ("VS", "LB", "EG"):
            fl = f"{dom}LOBXFL"
            df[fl] = None
            dtc = f"{dom}DTC"
            ok = [rfx_map.get(u) is not None and date.fromisoformat(v[:10]) <= rfx_map[u]
                  for u, v in zip(df["USUBJID"], df[dtc])]
            cand = df[ok]
            idx = cand.sort_values(dtc).groupby(["USUBJID", f"{dom}TESTCD"]).tail(1).index
            df.loc[idx, fl] = "Y"
        domains[dom] = df.reset_index(drop=True)
    return domains


EXPECTED_NULL = {  # Core=Exp variables we cannot populate truthfully -> present but null
    "AE": ["AELLT", "AELLTCD", "AEPTCD", "AEHLT", "AEHLTCD", "AEHLGT", "AEHLGTCD", "AEBDSYCD", "AESOCCD"],
    "DM": ["ACTARMUD"], "TS": ["TSVALCD", "TSVCDREF", "TSVCDVER"], "TV": ["ARMCD"],
}  # MedDRA codes need a licensed dictionary; TV visits apply to all arms
PERMISSIBLE_NULL = {  # Perm variables that downstream models (e.g. metric views) commonly reference
    "LB": ["LBSTAT", "LBTPT"], "VS": ["VSCAT", "VSSTAT", "VSDRVFL", "VSTPT"], "TS": ["TSGRPID"], "TV": ["ARM"],
}  # null = test done / no time point / not derived / no grouping / visit applies to all arms
CM_CLASS = {  # ATC level-4 class names for the built-in medication list (illustrative, not WHODrug-coded)
    "AMLODIPINE": "DIHYDROPYRIDINE DERIVATIVES", "ATORVASTATIN": "HMG COA REDUCTASE INHIBITORS",
    "METFORMIN": "BIGUANIDES", "OMEPRAZOLE": "PROTON PUMP INHIBITORS", "PARACETAMOL": "ANILIDES",
    "LEVOTHYROXINE": "THYROID HORMONES", "SERTRALINE": "SELECTIVE SEROTONIN REUPTAKE INHIBITORS",
    "SALBUTAMOL": "SELECTIVE BETA-2-ADRENORECEPTOR AGONISTS", "ONDANSETRON": "SEROTONIN (5HT3) ANTAGONISTS",
    "LOPERAMIDE": "ANTIPROPULSIVES", "HYDROCORTISONE": "CORTICOSTEROIDS, WEAK (GROUP I)",
    "MUPIROCIN": "OTHER ANTIBIOTICS FOR TOPICAL USE", "AMOXICILLIN": "PENICILLINS WITH EXTENDED SPECTRUM",
    "MACROGOL": "OSMOTICALLY ACTING LAXATIVES", "ZOLPIDEM": "BENZODIAZEPINE RELATED DRUGS",
}


def order_columns(domains):
    if "CM" in domains:
        domains["CM"]["CMCLAS"] = domains["CM"]["CMDECOD"].map(CM_CLASS)
    for dom, cols in {**EXPECTED_NULL, **{k: EXPECTED_NULL.get(k, []) + v for k, v in PERMISSIBLE_NULL.items()}}.items():
        if dom in domains:
            for c in cols:
                if c not in domains[dom]:
                    domains[dom][c] = None
    if "AE" in domains:
        domains["AE"]["AESOC"] = domains["AE"]["AEBODSYS"]  # primary SOC
    if not VARIABLES_CSV.exists():
        return domains
    order = {}
    with open(VARIABLES_CSV, newline="") as f:
        for r in csv.DictReader(f):
            order.setdefault(r["Dataset Name"], []).append(r["Variable Name"])
    for dom, df in domains.items():
        std = order.get(dom, [])
        cols = [c for c in std if c in df.columns] + [c for c in df.columns if c not in std]
        domains[dom] = df[cols]
    return domains


def generate(spec: dict, n: int | None = None) -> dict[str, pd.DataFrame]:
    g = Generator(spec, n)
    subj = g.run()
    n_rand = int((subj["DM"]["ARMCD"].notna()).sum())
    design = trial_design(spec, g.plan)
    design["TS"] = trial_summary(spec, n_rand, g.cutoff)
    subj = derive(subj, spec["study"]["studyid"])
    wanted = set(spec["generation"].get("domains", [])) | {"TS", "TA", "TE", "TV", "TI", "DM", "DS", "SE", "SV"}
    out = {k: v for k, v in {**design, **subj}.items() if k in wanted and len(v)}
    return order_columns(out)


INT_SUFFIXES = ("SEQ", "DY", "TAETORD")  # SDTM Num variables that are always whole numbers


def sdtm_types(domains) -> dict[str, dict[str, str]]:
    """Column -> 'string' | 'int' | 'double', from the SDTMIG Type (Char/Num) in variables.csv."""
    num = {}
    if VARIABLES_CSV.exists():
        with open(VARIABLES_CSV, newline="") as f:
            for r in csv.DictReader(f):
                num[(r["Dataset Name"], r["Variable Name"])] = r["Type"] == "Num"
    out = {}
    for dom, df in domains.items():
        out[dom] = {}
        for c in df.columns:
            is_num = num.get((dom, c), pd.api.types.is_numeric_dtype(df[c]) and df[c].notna().any())
            out[dom][c] = ("int" if c.endswith(INT_SUFFIXES) or c == "AGE" else "double") if is_num else "string"
    return out


def typed(df: pd.DataFrame, types: dict[str, str]) -> pd.DataFrame:
    """Explicit dtypes so all-null columns don't become NULL/void columns in parquet or Delta."""
    df = df.copy()
    for c, t in types.items():
        if t == "int":
            df[c] = pd.to_numeric(df[c], errors="coerce").round().astype("Int64")
        elif t == "double":
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("float64")
        else:
            df[c] = df[c].map(lambda v: None if v is None or (isinstance(v, float) and math.isnan(v))
                              else (str(int(v)) if isinstance(v, float) and v.is_integer() else str(v))
                              ).astype("string")
    return df


def write(domains, out: Path | None, uc: str | None, spec: dict, spark=None):
    """Write CSV/parquet and/or Unity Catalog Delta tables.

    UC tables are POOLED across studies (one table per domain, rows identified by STUDYID).
    Each run replaces only this study's rows (`replaceWhere STUDYID = ...`) and merges new
    columns, so loading a second study never touches the first.
    """
    types = sdtm_types(domains)
    sid = spec["study"]["studyid"]
    if out:
        out.mkdir(parents=True, exist_ok=True)
        for dom, df in domains.items():
            df.to_csv(out / f"{dom.lower()}.csv", index=False)
            try:
                typed(df, types[dom]).to_parquet(out / f"{dom.lower()}.parquet", index=False)
            except ImportError:
                pass
    if uc:
        from pyspark.sql import types as T
        if spark is None:  # in a notebook/job the active session; locally pass a DatabricksSession
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
        st = {"string": T.StringType(), "int": T.LongType(), "double": T.DoubleType()}
        assert "'" not in sid
        for dom, df in domains.items():
            name = f"{uc}.{dom.lower()}"
            tdf = typed(df, types[dom])
            schema = T.StructType([T.StructField(c, st[types[dom][c]], True) for c in tdf.columns])
            sdf = spark.createDataFrame(tdf, schema)
            if spark.catalog.tableExists(name):
                (sdf.write.format("delta").mode("overwrite").option("replaceWhere", f"STUDYID = '{sid}'")
                 .option("mergeSchema", "true").saveAsTable(name))
            else:
                sdf.write.format("delta").saveAsTable(name)
                spark.sql(f"COMMENT ON TABLE {name} IS 'SYNTHETIC SDTMIG 3.4 {dom} domain. Fictional data, "
                          f"pooled across studies; filter by STUDYID.'")
                spark.sql(f"ALTER TABLE {name} SET TBLPROPERTIES ('sdtm.domain'='{dom}', 'sdtm.version'='3.4', "
                          f"'sdtm.synthetic'='true')")
            print(f"  {name}: {len(df):,} rows for {sid}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--uc", help="catalog.schema to write Delta tables (Databricks)")
    ap.add_argument("--n", type=int, help="override number of randomized subjects")
    a = ap.parse_args(argv)
    if not (a.out or a.uc):
        ap.error("give --out and/or --uc")
    spec = load_spec(a.spec)
    doms = generate(spec, a.n)
    write(doms, a.out, a.uc, spec)
    for d, df in doms.items():
        print(f"{d:4s} {len(df):>8,d} rows")


if __name__ == "__main__":
    sys.exit(main())
