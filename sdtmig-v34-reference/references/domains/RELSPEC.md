# RELSPEC — Related Specimens

**Class:** Relationship  
**Structure:** One record per specimen identifier per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 3 | REFID | Specimen ID | Char | Identifier | Req |  |  |  |  | Specimen identifier, unique within USUBJID. |
| 4 | SPEC | Specimen Type | Char | Variable Qualifier | Perm | C78734; C111114 |  |  |  | Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE", "SOFT TISSUE". |
| 5 | PARENT | Specimen Parent | Char | Identifier | Exp |  |  |  |  | Identifies the REFID of the parent of a specimen to support tracking its genealogy. |
| 6 | LEVEL | Specimen Level | Num | Variable Qualifier | Req |  |  |  |  | Identifies the generation number of the sample where the collected sample is considered the first generation. |
