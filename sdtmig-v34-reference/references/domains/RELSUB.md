# RELSUB — Related Subjects

**Class:** Relationship  
**Structure:** One record per relationship per related subject per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | USUBJID | Unique Subject Identifier | Char | Identifier | Exp |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. Either USUBJID or POOLID must be populated. |
| 3 | POOLID | Pool Identifier | Char | Identifier | Perm |  |  |  |  | Identifier used to identify a pool of subjects. If POOLID is entered, POOLDEF records must exist for each subject in the pool and USUBJID must be null. Either USUBJID or POOLID must be populated. |
| 4 | RSUBJID | Related Subject or Pool Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to identify a related subject or pool of subjects. RSUBJID will be populated with either the USUBJID of the related subject or the POOLID of the related pool. |
| 5 | SREL | Subject Relationship | Char | Record Qualifier | Req | C100130 |  |  |  | Describes the relationship of the subject identified in USUBJID or the pool identified in POOLID to the subject or pool identified in RSUBJID. |
