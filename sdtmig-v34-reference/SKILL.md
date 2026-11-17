---
name: sdtmig-v34-reference
description: Use this skill for SDTMIG v3.4 domain, dataset, variable, role, core, or codelist lookups, when mapping clinical trial data into SDTM-compliant structures on Databricks, or when generating a coherent fictional SDTM dataset from ClinicalTrials.gov trial metadata (NCT ID). Also use for CDISC Therapeutic Area User Guide (TAUG) coverage queries and for validating cross-domain consistency of SDTM data. Covers ai_query patterns only when the context is SDTM or clinical trial data.
license: Metadata derived from the CDISC SDTMIG v3.4 metadata workbook; subject to CDISC terms of use. Skill structure and instructions are original.
metadata:
  source: CDISC SDTMIG v3.4 metadata workbook (SDTMIG_v3.4.xlsx)
  scope: SDTMIG v3.4 workbook metadata and CDISC Therapeutic Area index
  version: "2.1"
---

# SDTMIG v3.4 Reference Skill

A **reference skill** for SDTMIG v3.4 metadata. It gives you datasets, variables, roles, core status, controlled terminology and the TAUG index, plus SDTM-specific Databricks patterns. It also has a **synthetic study generator**: scripts that turn a ClinicalTrials.gov record into a reviewed study spec and then into a coherent, validated, fictional SDTM dataset.

## What this skill contains (and what it doesn't)

- It has **workbook metadata**, not the prose of the SDTM Implementation Guide: no assumptions, examples or narrative guidance. If the user asks for interpretation that normally comes from the IG text, say so and answer from the metadata.
- The Therapeutic Area file is an **index** of TAUGs (name, version, standards covered, link). The full TAUG documents aren't included.
- The codelist file covers **common** CDISC CT codelists only. For any other codelist, give the codelist code from the domain file and point the user to NCI EVS / CDISC Library for the current values.

## Step-by-step

1. **Identify the question type**, then open only the files you need:

   | Question | File |
   |---|---|
   | Which domains exist, their class, label, record structure | `references/datasets.md` |
   | Variables in a domain: order, label, type, role, core, codelist, notes | `references/domains/{DOMAIN}.md` (e.g. `references/domains/AE.md`) |
   | Allowed values for a common codelist (SEX, RACE, ETHNIC, NY, EPOCH, ACN, AEOUT, AESEV, POSITION, LAT, DIR, VSTESTCD, LBTEST, UNIT) | `references/codelists-common.md` |
   | Meaning of a workbook column (Core, Role, Value List…) | `references/workbook-readme.md` |
   | Which therapeutic areas have TAUGs and which standards they cover | `references/cdisc_therapeutic_areas.md` |
   | Building SDTM tables, pipelines, DQ expectations, XPT ingestion, synthetic data on Databricks | `references/databricks-patterns.md` |
   | Using `ai_query` for MedDRA coding, epoch checks, narrative extraction | `references/ai-query-templates.md` |
   | **Generating a coherent synthetic SDTM study** (from an NCT ID or trial design) | `references/synthetic-study-generation.md` **first**, then `references/ctgov-mapping.md` and `assets/study-spec-template.yaml` |
   | Checking an SDTM dataset for cross-domain consistency (dates, death, EPOCH, AE↔EX, ranges) | `references/coherence-rules.md` + `scripts/validate_sdtm.py` |

2. **Don't read the CSV files whole.** `references/variables.csv` is ~430 KB and would fill the context window. Use it only from code (Spark/pandas) or filter it, for example `grep -E '^[^,]*,[0-9]+,[^,]*,AE,'`. The per-domain Markdown files hold the same content in small pieces.
3. **Cross-domain questions** (e.g. "which domains use `--LOINC`?") are best answered by filtering `variables.csv` in code rather than opening many domain files.
4. **Keep these apart in the answer:**
   - **Dataset / domain meaning**: from the workbook
   - **Variable metadata**: from the workbook
   - **Therapeutic area context**: from the TAUG index
   - **Implementation advice**: your own recommendation; label it as such
5. **Platform questions:** treat the SDTM metadata as the stable semantic reference, then explain the Databricks design choice separately. For generic Databricks tasks (pipeline mechanics, dashboards, jobs), rely on the built-in Databricks skills. This skill adds only the SDTM-specific layer.

## Synthetic data: non-negotiables

When the user asks for synthetic or fictional SDTM data:
1. **Spec first.** Run `scripts/ctgov_to_spec.py <NCT>` (or start from `assets/study-spec-template.yaml`), then review the `review:` items with the user. The schedule of activities, doses and treatment-stop reasons are the usual gaps.
2. **Code generates, not the LLM.** Run `scripts/generate_sdtm.py`. Don't write SDTM rows in a prompt or with `ai_query`, because the domains won't agree with each other.
3. **Validate.** Run `scripts/validate_sdtm.py` and repeat until there are 0 errors. Fix the spec or the generator, never the output rows.
4. **Label it fictional.** STUDYID `SYN-…`, a `[SYNTHETIC]` title and a fictional sponsor, plus the `sdtm.synthetic=true` table property in UC. Never present the output as real trial data.

## Response pattern

When appropriate, structure answers as:
- **Therapeutic area** (if disease-specific)
- **Dataset / domain**
- **Relevant variables** (name, role, core, codelist)
- **Record structure / grain**
- **Constraints or caveats from the workbook**
- **Implementation implication** (Databricks, `ai_query`, synthetic data)

## Examples

**Q: Is AEDECOD required in AE, and what populates it?**
Open `references/domains/AE.md`. AEDECOD is Char, role *Synonym Qualifier*, core **Req**. Per the CDISC notes it is the dictionary-derived text description of AETERM (typically the MedDRA Preferred Term). Implementation note: populate it from a licensed MedDRA coding process. Don't use LLM output as the coded value.

**Q: What is the grain of LB and which variables identify a record?**
Open `references/datasets.md` for the structure (*one record per lab test per time point per visit per subject*). Then open `references/domains/LB.md` for the identifiers (STUDYID, DOMAIN, USUBJID, LBSEQ), the topic (LBTESTCD), and the timing variables that complete the grain (VISITNUM, LBTPTNUM, LBDTC).

**Q: Which oncology TAUGs cover both SDTM and ADaM?**
Open `references/cdisc_therapeutic_areas.md`, go to the *Oncology* category table, keep the rows whose *Standards* column lists both SDTM and ADaM, and return name, version and link.

**Q: Generate DLT expectations from Core=Req for VS.**
Use `references/databricks-patterns.md` §3. It derives the required variables from `variables.csv`, so the rules stay in sync with the workbook instead of a hand-maintained list.

**Q: Create a full, coherent SDTM sample modelled on MARIPOSA (NCT04487080).**
Follow `references/synthetic-study-generation.md`: draft the spec (it gets the 2:2:1 ratio, demographics, per-arm AE incidence and death rates from the posted results), confirm the visit template and doses with the user, generate, validate to 0 errors, and report what was assumed.

## Edge cases

- **Non-standard variables** belong in SUPP-- datasets (`references/domains/SUPPQUAL.md`), not as extra columns in the parent domain.
- **Relationships** between records or datasets use RELREC / RELSPEC / RELSUB.
- **Findings About (FA)** holds findings about events or interventions. Don't add finding variables to AE/CM.
- **Custom domains**: SDTMIG defines how to model them by class, but they aren't in this metadata. Say so, and base the model on the closest general-observation class.
- **`--` prefix variables**: the domain files list concrete names (e.g. AESEQ). The generic `--SEQ` form is the domain prefix pattern.
- **Other standards or versions** (SEND, SDTMIG v3.3/3.2, SDTM v2.x model, ADaM, CDASH): out of scope. Say the skill covers **SDTMIG v3.4 workbook metadata** only.
- **Synthetic data**: the CDISC Library API serves standards metadata. It doesn't generate patient data. Use the generator workflow above. The `ai_query` synthetic-record template and the PySpark AE generator in `databricks-patterns.md` §5 are quick single-domain demos and aren't coherent across domains.

## Cautions

- Don't claim the package includes the complete SDTMIG prose.
- Don't present sponsor-specific conventions as CDISC-standard facts.
- Similarly named variables differ across domains. Always use the dataset-specific listing.
- Full TAUG documents require access via CDISC.
- LLM output (`ai_query`) is a **suggestion**. MedDRA/WHODrug coding and any controlled-terminology values must be validated against the licensed dictionaries and CDISC CT before regulatory use.
- When suggesting `ai_query` prompts, include enough SDTM context (domain, variable definitions, allowed codelist values) for standards-aligned output.
