# UR — Urinary System Findings

**Class:** Findings  
**Structure:** One record per finding per location per per visit per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | UR | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | URSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| 5 | URGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 6 | URREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external identifier (e.g., lab specimen ID, universally unique identifier (UUID) for a medical image). |
| 7 | URSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. Example: Preprinted line identifier. |
| 8 | URLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 9 | URLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 10 | URTESTCD | Short Name of Urinary Test | Char | Topic | Req | C129942 |  |  |  | Short character value for URTEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in URTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). URTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "COUNT", "LENGTH", "RBLDFLW". |
| 11 | URTEST | Name of Urinary Test | Char | Synonym Qualifier | Req | C129941 |  |  |  | Long name For URTESTCD. Examples: "Count", "Length", "Renal Blood Flow". |
| 12 | URTSTDTL | Urinary Test Detail | Char | Variable Qualifier | Perm |  |  |  |  | Further description of URTESTCD and URTEST. |
| 13 | URCAT | Category for Urinary Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. |
| 14 | URSCAT | Subcategory for Urinary Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of URCAT values. |
| 15 | URORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 16 | URORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Unit for URORRES. |
| 17 | URSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from URORRES, in a standard format or in standard units. URSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in URSTRESN. |
| 18 | URSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from URSTRESC. URSTRESN should store all numeric test results or findings. |
| 19 | URSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for URSTRESC and URSTRESN. |
| 20 | URRESCAT | Result Category | Char | Variable Qualifier | Perm |  |  |  |  | Used to categorize the result of a finding. |
| 21 | URSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 22 | URREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with URSTAT when value is "NOT DONE". |
| 23 | URLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. |
| 24 | URLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 25 | URDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 26 | URMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. |
| 27 | URLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 28 | URBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | A baseline defined by the sponsor The value should be "Y" or null. Note that URBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 29 | URDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 30 | UREVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| 31 | UREVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in UREVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". |
| 32 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 33 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 34 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 35 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the observation was made. |
| 36 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the observation was made. |
| 37 | URDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of an observation. |
| 38 | URDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 39 | URTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See URTPTNUM and URTPTREF. |
| 40 | URTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 41 | URELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to a planned fixed reference (URTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 42 | URTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by URELTM, URTPTNUM, and URTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 43 | URRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by URTPTREF. |
