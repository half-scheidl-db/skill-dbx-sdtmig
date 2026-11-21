# RP — Reproductive System Findings

**Class:** Findings  
**Structure:** One record per finding or result per time point per visit per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | RP | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | RPSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1. |
| 5 | RPGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. Also used to link together a block of related records in the Trial Summary dataset. |
| 6 | RPREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external identifier (e.g., lab specimen ID, UUID for an ECG waveform or a medical image). |
| 7 | RPSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. Example: Preprinted line identifier on a CRF. |
| 8 | RPLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 9 | RPLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 10 | RPTESTCD | Short Name of Reproductive Test | Char | Topic | Req | C106479 |  |  |  | Short character value for RPTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Examples: "CHILDPOT", "BCMETHOD", "MENARAGE". |
| 11 | RPTEST | Name of Reproductive Test | Char | Synonym Qualifier | Req | C106478 |  |  |  | Long name For RPTESTCD. Examples: "Childbearing Potential", "Birth Control Method", "Menarche Age". |
| 12 | RPCAT | Category for Reproductive Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. Example: "No use case to date, but values would be relative to reproduction tests grouping". |
| 13 | RPSCAT | Subcategory for Reproductive Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of RPCAT values. Example: "No use case to date, but values would be relative to reproduction tests grouping". |
| 14 | RPORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. Examples: "120", "<1", "POS". |
| 15 | RPORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Unit for RPORRES. Examples: "in", "LB", "kg/L". |
| 16 | RPSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from RPORRES, in a standard format or in standard units. RPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in RPSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in RPORRES, and these results effectively have the same meaning, they could be represented in standard format in RPSTRESC as "NEGATIVE". |
| 17 | RPSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from RPSTRESC. RPSTRESN should store all numeric test results or findings. |
| 18 | RPSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for RPSTRESC and RPSTRESN. Example: "mol/L". |
| 19 | RPSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 20 | RPREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with RPSTAT when value is "NOT DONE". |
| 21 | RPLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 22 | RPBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that RPBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 23 | RPDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record. The value should be "Y" or null. Records which represent the average of other records or which do not come from the CRF are examples of records that would be derived for the submission datasets. If RPDRVFL = "Y", then RPORRES may be null, with RPSTRESC and (if numeric) RPSTRESN having the derived value. |
| 24 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 25 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 26 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 27 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 28 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 29 | RPDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of an observation. |
| 30 | RPDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 31 | RPDUR | Duration | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration of an event, intervention, or finding represented in ISO 8601 character format. Used only if collected on the CRF and not derived. |
| 32 | RPTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. |
| 33 | RPTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 34 | RPELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time in ISO 8601 character format relative to a planned fixed reference (RPTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 35 | RPTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by RPELTM, RPTPTNUM, and RPTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 36 | RPRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by RPTPTREF in ISO 8601 character format. |
