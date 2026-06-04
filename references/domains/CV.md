# CV — Cardiovascular System Findings

**Class:** Findings  
**Structure:** One record per finding or result per time point per visit per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | CV | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | CVSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| 5 | CVGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 6 | CVREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external identifier. |
| 7 | CVSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. Example: a preprinted line identifier on a CRF. |
| 8 | CVLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 9 | CVLNKGRP | Link Group | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 10 | CVTESTCD | Short Name of Cardiovascular Test | Char | Topic | Req | C101847 |  |  |  | Short name of the measurement, test, or examination described in CVTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in CVTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" would not be valid). CVTESTCD cannot contain characters other than letters, numbers, or underscores. |
| 11 | CVTEST | Name of Cardiovascular Test | Char | Synonym Qualifier | Req | C101846 |  |  |  | Long name For CVTESTCD. The value in CVTEST cannot be longer than 40 characters. |
| 12 | CVCAT | Category for Cardiovascular Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. |
| 13 | CVSCAT | Subcategory for Cardiovascular Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of CVCAT values. |
| 14 | CVPOS | Position of Subject During Observation | Char | Record Qualifier | Perm | C71148 |  |  |  | Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING". |
| 15 | CVORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 16 | CVORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. Unit for CVORRES. |
| 17 | CVSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived, from CVORRES in a standard format or in standard units. CVSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in CVSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in CVORRES and these results effectively have the same meaning, they could be represented in standard format in CVSTRESC as "NEGATIVE". |
| 18 | CVSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from CVSTRESC. CVSTRESN should store all numeric test results or findings. |
| 19 | CVSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for CVSTRESC and CVSTRESN. |
| 20 | CVSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 21 | CVREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a measurement or test was not performed (e.g., "BROKEN EQUIPMENT", "SUBJECT REFUSED"). Used in conjunction with CVSTAT when value is "NOT DONE". |
| 22 | CVLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. Examples: "HEART", "LEFT VENTRICLE". |
| 23 | CVLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL", "UNILATERAL". |
| 24 | CVDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 25 | CVMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method used to create the result. |
| 26 | CVLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 27 | CVBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that CVBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 28 | CVDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (i.e., a record that represents the average of other records, such as a computed baseline). Should be "Y" or null. |
| 29 | CVEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", " INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| 30 | CVEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in CVEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2". |
| 31 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 32 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 33 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 36 | CVDTC | Date/Time of Test | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of an observation. |
| 37 | CVDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 38 | CVTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See CVTPTNUM and CVTPTREF. |
| 39 | CVTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 40 | CVELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to a planned fixed reference (CVTPTREF). Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 41 | CVTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by CVELTM, CVTPTNUM, and CVTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 42 | CVRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by CVTPTREF. |
