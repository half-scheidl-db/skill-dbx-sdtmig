# SS — Subject Status

**Class:** Findings  
**Structure:** One record per status per visit per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | SS | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SSSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | SSGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | SSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the Procedure or Test page. |
| 7 | SSTESTCD | Status Short Name | Char | Topic | Req | C124305 |  |  |  | Short name of the status assessment described in SSTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SSTESTCD cannot contain characters other than letters, numbers, or underscores. Example: "SURVSTAT". |
| 8 | SSTEST | Status Name | Char | Synonym Qualifier | Req | C124306 |  |  |  | Verbatim name of the status assessment used to obtain the finding. The value in SSTEST cannot be longer than 40 characters. Example: "Survival Status". |
| 9 | SSCAT | Category for Assessment | Char | Grouping Qualifier | Perm |  |  |  |  | Used to categorize observations across subjects. |
| 10 | SSSCAT | Subcategory for Assessment | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization. |
| 11 | SSORRES | Result or Finding Original Result | Char | Result Qualifier | Exp |  |  |  |  | Result of the status assessment finding as originally received or collected. |
| 12 | SSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C124304 |  |  |  | Contains the result value for all findings copied or derived from SSORRES, in a standard format. |
| 13 | SSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate a status assessment was not done. Should be null if a result exists in SSORRES. |
| 14 | SSREASND | Reason Assessment Not Performed | Char | Record Qualifier | Perm |  |  |  |  | Describes why an assessment was not performed. Example: "Subject refused". Used in conjunction with SSSTAT when value is "NOT DONE". |
| 15 | SSEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "CAREGIVER", "ADJUDICATION COMMITTEE", "FRIEND". |
| 16 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 17 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 18 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 19 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 20 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the subject status assessment. |
| 21 | SSDTC | Date/Time of Assessment | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date and time of the subject status assessment represented in ISO 8601 character format. |
| 22 | SSDY | Study Day of Assessment | Num | Timing | Perm |  |  |  |  | Study day of the subject status assessment, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
