# SV — Subject Visits

**Class:** Special-Purpose  
**Structure:** One record per actual or planned visit per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | SV | Two-character abbreviation for the domain most relevant to the observation. The domain abbreviation is also used as a prefix for variables to ensure uniqueness when datasets are merged. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | VISITNUM | Visit Number | Num | Topic | Req |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 5 | VISIT | Visit Name | Char | Synonym Qualifier | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 6 | SVPRESP | Pre-specified | Char | Variable Qualifier | Exp | C66742 |  |  |  | Used to indicate whether the visit was planned (i.e., visits specified in the TV domain). Value is "Y" for planned visits, null for unplanned visits. |
| 7 | SVOCCUR | Occurrence | Char | Record Qualifier | Exp | C66742 |  |  |  | Used to record whether a planned visit occurred. The value is null for unplanned visits. |
| 8 | SVREASOC | Reason for Occur Value | Char | Record Qualifier | Perm |  |  |  |  | The reason for the value in SVOCCUR. If SVOCCUR="N", SVREASOC is the reason the visit did not occur. |
| 9 | SVCNTMOD | Contact Mode | Char | Record Qualifier | Perm | C171445 |  |  |  | The way in which the visit was conducted. Examples: "IN PERSON", "TELEPHONE CALL", "IVRS". |
| 10 | SVEPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicates whether the visit was changed due to an epidemic or pandemic. |
| 11 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 12 | SVSTDTC | Start Date/Time of Observation | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Start date/time of an observation represented in IS0 8601 character format. |
| 13 | SVENDTC | End Date/Time of Observation | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | End date/time of the observation represented in IS0 8601 character format. |
| 14 | SVSTDY | Study Day of Start of Observation | Num | Timing | Perm |  |  |  |  | Actual study day of start of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 15 | SVENDY | Study Day of End of Observation | Num | Timing | Perm |  |  |  |  | Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 16 | SVUPDES | Description of Unplanned Visit | Char | Record Qualifier | Perm |  |  |  |  | Description of what happened to the subject during an unplanned visit. Only populated for unplanned visits. |
