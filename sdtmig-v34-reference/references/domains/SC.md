# SC — Subject Characteristics

**Class:** Findings  
**Structure:** One record per characteristic per visit per subject.

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | SC | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SCSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | SCGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | SCSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. |
| 7 | SCTESTCD | Subject Characteristic Short Name | Char | Topic | Req | C74559 |  |  |  | Short name of the measurement, test, or examination described in SCTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SCTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SCTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MARISTAT", "NATORIG". |
| 8 | SCTEST | Subject Characteristic | Char | Synonym Qualifier | Req | C103330 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in SCTEST cannot be longer than 40 characters. Examples: "Marital Status", "National Origin". |
| 9 | SCCAT | Category for Subject Characteristic | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. |
| 10 | SCSCAT | Subcategory for Subject Characteristic | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of the subject characteristic. |
| 11 | SCORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the subject characteristic as originally received or collected. |
| 12 | SCORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original unit in which the data were collected. The unit for SCORRES. |
| 13 | SCSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from SCORRES, in a standard format or standard units. SCSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in SCSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in SCORRES, and these results effectively have the same meaning, they could be represented in standard format in SCSTRESC as "NEGATIVE". |
| 14 | SCSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from SCSTRESC. SCSTRESN should store all numeric test results or findings. |
| 15 | SCSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized unit used for SCSTRESC or SCSTRESN. |
| 16 | SCSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that the measurement was not done. Should be null if a result exists in SCORRES. |
| 17 | SCREASND | Reason Not Performed | Char | Record Qualifier | Perm |  |  |  |  | Describes why the observation has no result. Example: "Subject refused". Used in conjunction with SCSTAT when value is "NOT DONE". |
| 18 | VISITNUM | Visit Number | Num | Timing | Perm |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 19 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 20 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 21 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 22 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time at which the assessment was made. |
| 23 | SCDTC | Date/Time of Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Collection date and time of the subject characteristic represented in ISO 8601 character format. |
| 24 | SCDY | Study Day of Examination | Num | Timing | Perm |  |  |  |  | Study day of collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
