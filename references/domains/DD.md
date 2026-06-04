# DD — Death Details

**Class:** Findings  
**Structure:** One record per finding per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | DD | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | DDSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | DDTESTCD | Death Detail Assessment Short Name | Char | Topic | Req | C116108 |  |  |  | Short name of the measurement, test, or examination described in DDTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in DDTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). DDTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRCDTH", "SECDTH". |
| 6 | DDTEST | Death Detail Assessment Name | Char | Synonym Qualifier | Req | C116107 |  |  |  | Long name for DDTESTCD. The value in DDTEST cannot be longer than 40 characters. Examples: "Primary Cause of Death", "Secondary Cause of Death". |
| 7 | DDORRES | Result or Finding as Collected | Char | Result Qualifier | Exp |  |  |  |  | Result of the test defined in DDTEST, as originally received or collected. |
| 8 | DDSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result or finding copied or derived from DDORRES in a standard format. |
| 9 | DDRESCAT | Result Category | Char | Variable Qualifier | Perm |  |  |  |  | Used to categorize the result of a finding. Examples: "TREATMENT RELATED", "NONTREATMENT RELATED", "UNDETERMINED", "ACCIDENTAL". |
| 10 | DDEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. |
| 11 | DDDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of collection of the diagnosis or other death assessment data in ISO 8601 format. This is not necessarily the date of death. |
| 12 | DDDY | Study Day of Collection | Num | Timing | Perm |  |  |  |  | Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. |
