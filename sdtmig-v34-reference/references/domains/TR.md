# TR — Tumor/Lesion Results

**Class:** Findings  
**Structure:** One record per tumor measurement/assessment per visit per subject per assessor

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TR | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | TRSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number. |
| 5 | TRGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records within a subject in a domain. |
| 6 | TRREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external identifier. |
| 7 | TRSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 8 | TRLNKID | Link ID | Char | Identifier | Exp |  |  |  |  | Identifier used to link the assessment result records to the individual tumor/lesion identification record in TU domain. |
| 9 | TRLNKGRP | Link Group | Char | Identifier | Perm |  |  |  |  | Used to group and link all of the measurement/assessment records used in the assessment of the response record in the RS domain. |
| 10 | TRTESTCD | Tumor/Lesion Assessment Short Name | Char | Topic | Req | C96779 |  |  |  | Short name of the TEST in TRTEST. TRTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TUMSTATE", "DIAMETER", "LESSCIND", "LESRVIND". See assumption 3. |
| 11 | TRTEST | Tumor/Lesion Assessment Test Name | Char | Synonym Qualifier | Req | C96778 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in TRTEST cannot be longer than 40 characters. Examples: "Tumor State", "Diameter", "Volume", "Lesion Success Indicator", "Lesion Revascularization Indicator". See assumption 3. |
| 12 | TRORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the tumor/lesion measurement/assessment as originally received or collected. |
| 13 | TRORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Original units in which the data were collected. The unit for TRORRES. Example: "mm". |
| 14 | TRSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C124309 |  |  |  | Contains the result value for all findings copied or derived from TRORRES, in a standard format or standard units. TRSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in TRSTRESN. |
| 15 | TRSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from TRSTRESC. TRSTRESN should store all numeric test results or findings. |
| 16 | TRSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Standardized unit used for TRSTRESN. |
| 17 | TRSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate a scan/image/physical exam was not performed or a tumor/lesion measurement was not taken. Should be null if a result exists in TRORRES. |
| 18 | TRREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a scan/image/physical exam was not performed or a tumor/lesion measurement was not taken. Examples: "SCAN NOT PERFORMED", "NOT ASSESSABLE: IMAGE OBSCURED TUMOR". Used in conjunction with TRSTAT when value is "NOT DONE". |
| 19 | TRNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | The name or identifier of the vendor that performed the tumor/lesion measurement or assessment. This column can be left null when the investigator provides the complete set of data in the domain. |
| 20 | TRMETHOD | Method Used to Identify the Tumor/Lesion | Char | Record Qualifier | Exp | C85492 |  |  |  | Method used to measure the tumor/lesion/location of interest. Examples: "MRI", "CT SCAN", "PET SCAN", "Coronary angiography". |
| 21 | TRLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| 22 | TRBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that TRBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 23 | TREVAL | Evaluator | Char | Record Qualifier | Exp | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR". |
| 24 | TREVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in TREVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumption 6. |
| 25 | TRACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATION COMMITTEE") provide independent assessments at the same time point, this flag identifies the record that is considered to be the accepted assessment. |
| 26 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 27 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 28 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 29 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 30 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the element in the planned sequence of elements for the arm to which the subject was assigned. |
| 31 | TRDTC | Date/Time of Tumor/Lesion Measurement | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | The date of the scan/image/physical exam. TRDTC does not represent the date that the image was read to identify tumors/lesions. TRDTC also does not represent the VISIT date. |
| 32 | TRDY | Study Day of Tumor/Lesion Measurement | Num | Timing | Perm |  |  |  |  | Study day of the scan/image/physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
