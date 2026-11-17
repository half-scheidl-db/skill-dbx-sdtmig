# Generating a coherent synthetic SDTM study

Use this workflow when the user wants a **fictional but internally consistent** SDTM dataset, typically modelled on a real trial from ClinicalTrials.gov. Coherence (every domain telling the same story about each subject) matters more than volume.

## Golden rule

**Never let the LLM write SDTM records.** The LLM's job is turning registry free text into a structured **study spec** and helping the user review it. Records come from `scripts/generate_sdtm.py`, which derives every domain from one per-subject timeline using a fixed seed. Row-by-row LLM generation produces AEs outside exposure, visits after death and EPOCHs that contradict SE, and none of that can be fixed afterwards.

## Minimal input

| Input | Required | Default if missing |
|---|---|---|
| NCT ID **or** a ClinicalTrials.gov JSON record | **yes** | — |
| Number of randomized subjects | no | `enrollmentInfo.count` |
| Data cutoff | no | primary completion date |
| Seed | no | fixed |
| Screen-failure rate | no | 0.25 |
| Target location (folder or `catalog.schema`) | ask | — |
| Protocol schedule of activities (SoA) | no, but **strongly recommended** | therapeutic-area template |

An NCT ID is enough to start. Everything else gets a default that is listed under `review:` in the drafted spec.

## Workflow

1. **Fetch and draft the spec**
   ```bash
   python scripts/ctgov_to_spec.py NCT04487080 --out-dir ./study
   ```
   Writes `NCT…json` (raw record) and `NCT…_spec.yaml`. If compute has no internet egress, download the JSON elsewhere (`https://clinicaltrials.gov/api/v2/studies/<NCT>`), upload it to a Volume, and run with `--from-file`.

2. **Review the spec with the user.** This is the only step that needs judgement. Walk through the `review:` list and fix at least:
   - **arms[].interventions**: dose, unit, route and frequency are parsed from free text. Check placebo doses and weight-based or split dosing.
   - **visits**: CT.gov has no SoA. Replace the template with the protocol SoA if the user has one; an ICH M11 / CDISC USDM protocol maps directly onto `visits`.
   - **disposition.treatment_discontinuation**: the registry only reports *study* withdrawal, so treatment-stop reasons are therapeutic-area defaults.
   - **sites**: countries without an ISO 3166 alpha-3 mapping are dropped. Add them.
   - **study.planned_treatment_days**: `null` means open-ended (treat until event, typical for oncology). A number means a fixed-duration study with completers.

   Edit the YAML; don't regenerate it. Field reference: `assets/study-spec-template.yaml`.

3. **Generate**
   ```bash
   python scripts/generate_sdtm.py ./study/NCT04487080_spec.yaml --out ./study/sdtm        # CSV + parquet
   python scripts/generate_sdtm.py ./study/NCT04487080_spec.yaml --uc main.sdtm_syn       # Delta in UC
   ```
   Use `--n 100` for a fast first pass.

4. **Validate, and repeat until clean**
   ```bash
   python scripts/validate_sdtm.py ./study/sdtm
   ```
   Every rule is described in `coherence-rules.md`. If a rule fails, fix the **spec or the generator**, then regenerate. Never patch generated rows by hand or with an LLM; the next run would lose the fix and the data could drift out of coherence.

5. **Report** domains, row counts, the validation summary and the spec assumptions to the user. State clearly that the data is **fictional**: STUDYID is `SYN-<NCT>`, TS TITLE starts with `[SYNTHETIC]`, the sponsor is fictional, and UC tables are tagged `sdtm.synthetic=true`.

## How coherence is achieved (dependency order)

```
1. Trial design     TS TA TE TV TI                          <- spec
2. Subject spine    consent -> randomization -> first dose -> end of treatment -> follow-up -> end/death/cutoff
                    DM DS SE SV IE                          <- one timeline per subject
3. Events           AE   (incidence per arm from posted results; AEACN=DRUG WITHDRAWN shortens treatment
                          and becomes the EOT reason; fatal AE <-> death)
4. Interventions    EX   (stops at end of treatment; interruptions/reductions follow AEACN)
                    CM MH (comorbidity -> concomitant medication; AE -> rescue medication with CMINDC)
5. Findings         VS LB EG at SV visits only; values move outside the reference range during linked AEs
                    (e.g. Neutropenia -> low NEUT); an unscheduled visit is added if no visit covers the AE.
                    RS: PD exactly at the assessment where treatment stopped for PD.
6. Derived          --SEQ, --DY (no day 0), EPOCH from SE, --LOBXFL, RFXSTDTC/RFXENDTC from EX
```

## Domain scope

`generation.domains` controls which domains are written. Default: TS TA TE TV TI DM IE DS SE SV EX AE MH CM VS LB EG, plus RS for oncology. Add domains only when the design calls for them (see `cdisc_therapeutic_areas.md` for TA-specific domains). Domains you can't generate coherently yet (TU/TR, PC/PP, QS) should be raised with the user, not invented.

## Known simplifications (tell the user)

- MedDRA codes (AEPTCD, AELLTCD, …) are empty because they need a licensed dictionary. AEDECOD/AEBODSYS reuse the registry's MedDRA-style terms.
- CMDECOD is the generic name and isn't WHODrug-coded.
- Complex regimens (loading doses, weight-based dosing, split first infusions) are reduced to a single dose and frequency per intervention.
- Efficacy findings beyond overall response (RS) aren't modelled yet: no TU/TR, QS scales or PK.
- Subjects ongoing at the cutoff have no end-of-study DS record, and RFENDTC/RFPENDTC equal their last contact.

## Running in Databricks / Genie Code

- In a notebook: `%pip install pyyaml` if needed, then
  `import sys; sys.path.append("<skill folder>/scripts"); import generate_sdtm as g; doms = g.generate(g.load_spec(path)); g.write(doms, None, "catalog.schema", g.load_spec(path))`.
- Store the spec next to the data (e.g. in a Volume) so the dataset can be reproduced exactly.
- Writing to UC needs `CREATE TABLE` on the target schema. Suggest a dedicated schema such as `<catalog>.sdtm_synthetic`.
