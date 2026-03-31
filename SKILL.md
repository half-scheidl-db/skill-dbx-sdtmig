---
name: sdtmig-v34-reference
description: Use this skill when the user needs SDTMIG v3.4 domain, dataset, variable, role, core, codelist, or structure lookup, or when mapping clinical trial data into SDTM-oriented semantics. Use it for quick reference, implementation guidance, and consistency checks against the uploaded SDTMIG v3.4 workbook.
license: Proprietary source content from user-provided workbook; package structure and instructions authored here.
metadata:
  source: user-uploaded SDTMIG_v3.4.xlsx workbook
  scope: SDTMIG v3.4 workbook metadata only
  version: "1.0"
---

# SDTMIG v3.4 Reference Skill

## What this skill is for

Use this skill to answer questions that depend on the uploaded **SDTMIG v3.4 workbook metadata**:
- which datasets exist in SDTMIG v3.4
- what structure a dataset uses
- which variables belong to a dataset
- variable role, core status, datatype, codelist, value list, and notes
- how to stay aligned with SDTM-style semantic structures when designing analytical models

This skill is a **reference skill**, not a data-processing script.

## Important limitation

This package contains the **uploaded workbook-derived metadata**, not the full prose of the SDTM Implementation Guide book.  
Use it as a fast normative metadata reference. If the user asks for explanatory narrative, examples, assumptions, or interpretation that would normally come from the full SDTMIG text, say that this package only includes the workbook content and answer from the available metadata.

## How to use this skill

1. Start with `references/datasets.md` when the user asks about domain coverage, classes, or record structure.
2. Use `references/variables.md` when the user asks about variable presence, order, role, datatype, codelists, notes, or core status.
3. Use `references/workbook-readme.md` when the user needs column definitions or clarification of workbook fields.
4. When answering, distinguish clearly between:
   - **Dataset / domain meaning**
   - **Variable metadata**
   - **Analytical interpretation or implementation advice**
5. When the question is about implementation in a platform such as Databricks, treat the SDTM workbook as the **stable semantic reference**, then explain the platform-specific design choice separately.

## Recommended response pattern

When appropriate, structure answers like this:
- **Dataset / domain**
- **Relevant variables**
- **Record structure / grain**
- **Constraints or caveats from the workbook**
- **Implementation implication**

## Available references

- `references/datasets.md` — dataset list, class, label, and record structure
- `references/variables.md` — variable-level metadata grouped by dataset
- `references/workbook-readme.md` — workbook column definitions
- `references/datasets.csv` — machine-readable dataset metadata
- `references/variables.csv` — machine-readable variable metadata

## Cautions

- Do not claim the package includes the complete SDTMIG prose unless that source is separately provided.
- Do not invent sponsor-specific interpretations and present them as CDISC-standard facts.
- Be careful with similarly named concepts across domains; rely on the dataset-specific variable listing.
- If the user asks about SEND or another IG version, say this skill is scoped to **SDTMIG v3.4 workbook metadata** only.
