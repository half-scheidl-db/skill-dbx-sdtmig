# RELREC — Related Records

**Class:** Relationship  
**Structure:** One record per related record, group of records or dataset

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | RDOMAIN | Related Domain Abbreviation | Char | Identifier | Req | C66734 |  |  |  | Abbreviation for the domain of the parent record(s). |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Exp |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | IDVAR | Identifying Variable | Char | Identifier | Req |  |  |  |  | Name of the identifying variable in the general-observation-class dataset that identifies the related record(s). Examples: --SEQ, --GRPID. |
| 5 | IDVARVAL | Identifying Variable Value | Char | Identifier | Exp |  |  |  |  | Value of identifying variable described in IDVAR. If --SEQ is the variable being used to describe this record, then the value of --SEQ would be entered here. |
| 6 | RELTYPE | Relationship Type | Char | Record Qualifier | Exp | C78737 |  |  |  | Identifies the hierarchical level of the records in the relationship. Values should be either "ONE" or "MANY". Used only when identifying a relationship between datasets (as described in Section 8.3, Relating Datasets). |
| 7 | RELID | Relationship Identifier | Char | Record Qualifier | Req |  |  |  |  | Unique value within USUBJID that identifies the relationship. All records for the same USUBJID that have the same RELID are considered related/associated. RELID can be any value the sponsor chooses, and is only meaningful within the RELREC dataset to identify the related/associated domain records. |
