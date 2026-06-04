# NV — Nervous System Findings

**Class:** Findings  
**Structure:** One record per finding per location per time point per visit per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | NV | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | FOCID | Focus of Study-Specific Interest | Char | Identifier | Perm |  |  |  |  | Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed, such as a drug application site (e.g., "Injection site 1", "Biopsy site 1", "Treated site 1") or a more specific focus (e.g., "OD" (right eye), "Upper left quadrant of the back"). The value in this variable should have inherent semantic meaning. |
| 5 | NVSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 6 | NVGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 7 | NVREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external procedure identifier. |
| 8 | NVSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the Procedure or Test page. |
| 9 | NVLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link a procedure to the assessment results over the course of the study. |
| 10 | NVLNKGRP | Link Group | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 11 | NVTESTCD | Short Name of Nervous System Test | Char | Topic | Req | C116104 |  |  |  | Short name of the measurement, test, or examination described in NVTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in NVTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). NVTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SUVR", "N75LAT", "P100LAT","N145LAT". |
| 12 | NVTEST | Name of Nervous System Test | Char | Synonym Qualifier | Req | C116103 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in NVTEST cannot be longer than 40 characters. Examples: "Standard Uptake Value Ratio", "N75 Latency", "P100 Latency", "N145 Latency". |
| 13 | NVCAT | Category for Nervous System Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. Example: "VISUAL EVOKED POTENTIAL". |
| 14 | NVSCAT | Subcategory for Nervous System Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of NVCAT values. |
| 15 | NVORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the procedure measurement or finding as originally received or collected. |
| 16 | NVORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. The unit for NVORRES. |
| 17 | NVSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from NVORRES, in a standard format or standard units. NVSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in NVSTRESN. |
| 18 | NVSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from NVSTRESC. NVSTRESN should store all numeric test results or findings. |
| 19 | NVSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized unit used for NVSTRESC or NVSTRESN. |
| 20 | NVSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate a test was not done, or a measurement was not taken. Should be null if a result exists in NVORRES. |
| 21 | NVREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with NVSTAT when value is "NOT DONE". |
| 22 | NVLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. Examples: "BRAIN", "EYE", "PRECUNEUS", "CINGULATE CORTEX". |
| 23 | NVLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 24 | NVDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 25 | NVMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: "EEG", "PET/CT SCAN ", "FDGPET". |
| 26 | NVLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 27 | NVBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that NVBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 28 | NVDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 29 | NVEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| 30 | NVEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in NVEVAL. Examples: "RADIOLOGIST 1", "RADIOLOGIST 2". |
| 31 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 32 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 33 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 36 | NVDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date of procedure or test. |
| 37 | NVDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Study day of the procedure or test, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| 38 | NVTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See NVTPTNUM and NVTPTREF. Examples: "START", "5 MIN POST". |
| 39 | NVTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of NVTPT to aid in sorting. |
| 40 | NVELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to a fixed time point reference (NVTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by NVTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by NVTPTREF. |
| 41 | NVTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by NVELTM, NVTPTNUM, and NVTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 42 | NVRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by --TPTREF in ISO 8601 character format. |
