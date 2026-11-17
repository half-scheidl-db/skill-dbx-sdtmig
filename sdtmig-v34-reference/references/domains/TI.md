# TI — Trial Inclusion/Exclusion Criteria

**Class:** Trial Design  
**Structure:** One record per I/E criterion

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TI | Two-character abbreviation for the domain. |
| 3 | IETESTCD | Incl/Excl Criterion Short Name | Char | Topic | Req |  |  |  |  | Short name IETEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). IETESTCD cannot contain characters other than letters, numbers, or underscores. The prefix "IE" is used to ensure consistency with the IE domain. |
| 4 | IETEST | Inclusion/Exclusion Criterion | Char | Synonym Qualifier | Req |  |  |  |  | Full text of the inclusion or exclusion criterion. The prefix "IE" is used to ensure consistency with the IE domain. |
| 5 | IECAT | Inclusion/Exclusion Category | Char | Grouping Qualifier | Req | C66797 |  |  |  | Used for categorization of the inclusion or exclusion criteria. |
| 6 | IESCAT | Inclusion/Exclusion Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of the exception criterion. Can be used to distinguish criteria for a sub-study or to categorize as major or minor exceptions. Examples: "MAJOR", "MINOR". |
| 7 | TIRL | Inclusion/Exclusion Criterion Rule | Char | Rule | Perm |  |  |  |  | Rule that expresses the criterion in computer-executable form. See Assumption 4. |
| 8 | TIVERS | Protocol Criteria Versions | Char | Record Qualifier | Perm |  |  |  |  | The number of this version of the Inclusion/Exclusion criteria. May be omitted if there is only 1 version. |
