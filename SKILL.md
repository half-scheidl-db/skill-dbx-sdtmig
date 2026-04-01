---
name: sdtmig-v34-reference
description: Use this skill when the user needs SDTMIG v3.4 domain, dataset, variable, role, core, codelist, or structure lookup, or when mapping clinical trial data into SDTM-oriented semantics. Also use when the user asks about CDISC Therapeutic Area User Guides (TAUGs), needs disease-specific standards coverage, wants to generate synthetic clinical data via the CDISC API, or is using LLMs and Databricks ai_query to enrich, classify, or validate clinical trial data against SDTM or TAUG semantics. Use it for quick reference, implementation guidance, and consistency checks against the uploaded SDTMIG v3.4 workbook.
license: Proprietary source content from user-provided workbook; package structure and instructions authored here.
metadata:
  source: user-uploaded SDTMIG_v3.4.xlsx workbook
  scope: SDTMIG v3.4 workbook metadata and CDISC Therapeutic Area index
  version: "1.1"
---

# SDTMIG v3.4 Reference Skill

## What this skill is for

Use this skill to answer questions that depend on the uploaded **SDTMIG v3.4 workbook metadata**:
- which datasets exist in SDTMIG v3.4
- what structure a dataset uses
- which variables belong to a dataset
- variable role, core status, datatype, codelist, value list, and notes
- how to stay aligned with SDTM-style semantic structures when designing analytical models

Use the **Therapeutic Area** reference when the user:
- asks which CDISC Therapeutic Area User Guides (TAUGs) exist and what standards they cover
- needs to identify which TAUGs include SDTM, CDASH, ADaM, or Terminology guidance
- is generating **synthetic clinical datasets** via the CDISC Library API and needs to know valid therapeutic areas and their domain coverage
- is using **Databricks `ai_query`** or other LLM functions to classify, enrich, validate, or generate clinical data aligned with SDTM/TAUG semantics (e.g., mapping free-text adverse events to MedDRA terms within a specific therapeutic area, generating domain-compliant test records, or validating that a dataset covers the expected domains for a given disease area)
- is designing a data model or semantic layer scoped to a specific disease area

This skill is a **reference skill**, not a data-processing script.

## Important limitation

This package contains the **uploaded workbook-derived metadata**, not the full prose of the SDTM Implementation Guide book.  
Use it as a fast normative metadata reference. If the user asks for explanatory narrative, examples, assumptions, or interpretation that would normally come from the full SDTMIG text, say that this package only includes the workbook content and answer from the available metadata.

The Therapeutic Area reference is an **index of TAUGs** (names, versions, standards coverage, and CDISC links). It does not contain the full TAUG documents themselves.

## How to use this skill

1. Start with `references/datasets.md` when the user asks about domain coverage, classes, or record structure.
2. Use `references/variables.md` when the user asks about variable presence, order, role, datatype, codelists, notes, or core status.
3. Use `references/workbook-readme.md` when the user needs column definitions or clarification of workbook fields.
4. Use `references/cdisc_therapeutic_areas.md` when the user asks about:
   - which therapeutic areas have CDISC TAUGs
   - what standards (SDTM, CDASH, ADaM, Terminology) a therapeutic area covers
   - which TAUGs are most mature (full standards coverage) for end-to-end implementation
   - generating synthetic data via the CDISC Library API — use the therapeutic area list to scope the request to valid disease areas and identify relevant domains
   - using `ai_query` or LLMs for clinical data tasks — use the TAUG index to provide therapeutic-area context (e.g., prompt the model with the relevant domains and variables for a given disease area)
5. When answering, distinguish clearly between:
   - **Dataset / domain meaning**
   - **Variable metadata**
   - **Therapeutic area context**
   - **Analytical interpretation or implementation advice**
6. When the question is about implementation in a platform such as Databricks, treat the SDTM workbook as the **stable semantic reference**, then explain the platform-specific design choice separately.

## Recommended response pattern

When appropriate, structure answers like this:
- **Therapeutic area** (if disease-specific)
- **Dataset / domain**
- **Relevant variables**
- **Record structure / grain**
- **Constraints or caveats from the workbook**
- **Implementation implication** (including ai_query or synthetic data patterns if relevant)

## Available references

- `references/datasets.md` — dataset list, class, label, and record structure
- `references/variables.md` — variable-level metadata grouped by dataset
- `references/workbook-readme.md` — workbook column definitions
- `references/datasets.csv` — machine-readable dataset metadata
- `references/variables.csv` — machine-readable variable metadata
- `references/cdisc_therapeutic_areas.md` — CDISC Therapeutic Area User Guide index (47 TAUGs with versions, standards coverage, categories, and links)

## Cautions

- Do not claim the package includes the complete SDTMIG prose unless that source is separately provided.
- Do not invent sponsor-specific interpretations and present them as CDISC-standard facts.
- Be careful with similarly named concepts across domains; rely on the dataset-specific variable listing.
- If the user asks about SEND or another IG version, say this skill is scoped to **SDTMIG v3.4 workbook metadata** only.
- The therapeutic area file is a reference index only. The full TAUG documents require CDISC membership or purchase.
- When suggesting `ai_query` patterns, ensure the prompt includes enough SDTM/TAUG context (domain names, variable definitions, codelists) for the LLM to produce standards-aligned output.
