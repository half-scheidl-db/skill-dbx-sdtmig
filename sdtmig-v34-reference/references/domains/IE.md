# IE — Inclusion/Exclusion Criteria Not Met

**Class:** Findings  
**Structure:** One record per inclusion/exclusion criterion not met per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | IE | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | IESEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | IESPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Inclusion or exclusion criteria number from CRF. |
| 6 | IETESTCD | Inclusion/Exclusion Criterion Short Name | Char | Topic | Req |  |  |  |  | Short name of the criterion described in IETEST. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). IETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "IN01", "EX01". |
| 7 | IETEST | Inclusion/Exclusion Criterion | Char | Synonym Qualifier | Req |  |  |  |  | Verbatim description of the inclusion or exclusion criterion that was the exception for the subject within the study. IETEST cannot be longer than 200 characters. |
| 8 | IECAT | Inclusion/Exclusion Category | Char | Grouping Qualifier | Req | C66797 |  |  |  | Used to define a category of related records across subjects. |
| 9 | IESCAT | Inclusion/Exclusion Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of the exception criterion. Can be used to distinguish criteria for a sub-study or for to categorize as a major or minor exceptions. Examples: "MAJOR", "MINOR". |
| 10 | IEORRES | I/E Criterion Original Result | Char | Result Qualifier | Req | C66742 |  |  |  | Original response to inclusion/exclusion criterion question, i.e., whether the inclusion or exclusion criterion was met. |
| 11 | IESTRESC | I/E Criterion Result in Std Format | Char | Result Qualifier | Req | C66742 |  |  |  | Response to inclusion/exclusion criterion result, in standard format. |
| 12 | VISITNUM | Visit Number | Num | Timing | Perm |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 13 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 14 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 15 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 16 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the observation date/time of the inclusion/exclusion finding. |
| 17 | IEDTC | Date/Time of Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Collection date and time of the inclusion/exclusion criterion represented in ISO 8601 character format. |
| 18 | IEDY | Study Day of Collection | Num | Timing | Perm |  |  |  |  | Study day of collection of the inclusion/exclusion exceptions, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |
