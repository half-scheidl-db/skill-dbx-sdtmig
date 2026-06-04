# TM — Trial Disease Milestones

**Class:** Trial Design  
**Structure:** One record per Disease Milestone type

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TM | Two-character abbreviation for the domain, which must be TM. |
| 3 | MIDSTYPE | Disease Milestone Type | Char | Topic | Req |  |  |  |  | The type of disease milestone. Example: "HYPOGLYCEMIC EVENT". |
| 4 | TMDEF | Disease Milestone Definition | Char | Variable Qualifier | Req |  |  |  |  | Definition of the disease milestone. |
| 5 | TMRPT | Disease Milestone Repetition Indicator | Char | Record Qualifier | Req | C66742 |  |  |  | Indicates whether this is a disease milestone that can occur only once ("N") or a type of disease milestone that can occur multiple times ("Y"). |
