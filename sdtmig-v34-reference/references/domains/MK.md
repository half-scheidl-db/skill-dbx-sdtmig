# MK — Musculoskeletal System Findings

**Class:** Findings  
**Structure:** One record per assessment per visit per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | MK | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | MKSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1. |
| 5 | MKGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records within a subject in a domain. |
| 6 | MKREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external identifier such as lab specimen ID or a medical image. |
| 7 | MKSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. Example: Preprinted line identifier on a Concomitant Medications page. |
| 8 | MKLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 9 | MKLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 10 | MKTESTCD | Short Name of Musculoskeletal Test | Char | Topic | Req | C127269 |  |  |  | Short character value for MKTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The value in MKTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MKTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TNDRIND", "SWLLIND", "SGJSNSCR". |
| 11 | MKTEST | Name of Musculoskeletal Test | Char | Synonym Qualifier | Req | C127270 |  |  |  | Long name For MKTESTCD. Examples: "Tenderness Indicator", "Swollen Indicator", "Sharp/Genant JSN Score". |
| 12 | MKCAT | Category for Musculoskeletal Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. Examples: "SWOLLEN/TENDER JOINT ASSESSMENT". |
| 13 | MKSCAT | Subcategory for Musculoskeletal Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of MKCAT values. |
| 14 | MKPOS | Position of Subject | Char | Record Qualifier | Perm | C71148 |  |  |  | Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING". |
| 15 | MKORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 16 | MKORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Unit for MKORRES. |
| 17 | MKSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from MKORRES in a standard format or in standard units. MKSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MKSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in MKORRES and these results effectively have the same meaning, they could be represented in standard format in MKSTRESC as "NEGATIVE". |
| 18 | MKSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from MKSTRESC. MKSTRESN should store all numeric test results or findings. |
| 19 | MKSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for MKSTRESC and MKSTRESN. |
| 20 | MKSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or that a test was attempted but did not generate a result. Should be null if a result exists in MKORRES. |
| 21 | MKREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with MKSTAT when value is "NOT DONE". |
| 22 | MKLOC | Location Used for the Measurement | Char | Record Qualifier | Exp | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. Examples: "INTERPHALANGEAL JOINT 1", "SHOULDER JOINT". |
| 23 | MKLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 24 | MKDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 25 | MKMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: "X-RAY", "MRI", "CT SCAN". |
| 26 | MKLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 27 | MKBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that MKBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 28 | MKDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 29 | MKEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| 30 | MKEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in MKEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2". |
| 31 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 32 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 33 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 36 | MKDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of an observation. |
| 37 | MKDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 38 | MKTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See MKTPTNUM and MKTPTREF. |
| 39 | MKTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 40 | MKELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned Elapsed time relative to a planned fixed reference (MKTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 41 | MKTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by MKELTM, MKTPTNUM, and MKTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 42 | MKRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by MKTPTREF. |
