# TU — Tumor/Lesion Identification

**Class:** Findings  
**Structure:** One record per identified tumor per subject per assessor

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TU | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | TUSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number. |
| 5 | TUGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records within a subject in a domain. Can be used to group split or merged tumors/lesions which have been identified. |
| 6 | TUREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external identifier (e.g., medical image ID number). |
| 7 | TUSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 8 | TULNKID | Link ID | Char | Identifier | Exp |  |  |  |  | Identifier used to link identified tumor/lesion/location of interest to the assessment results (in TR domain) over the course of the study. |
| 9 | TULNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 10 | TUTESTCD | Tumor/Lesion ID Short Name | Char | Topic | Req | C96784 |  |  |  | Short name of the TEST in TUTEST. TUTESTCD cannot be longer than 8 characters nor can start with a number. TUTESTCD cannot contain characters other than letters, numbers, or underscores. Example: "TUMIDENT". See assumption 3. |
| 11 | TUTEST | Tumor/Lesion ID Test Name | Char | Synonym Qualifier | Req | C96783 |  |  |  | Verbatim name of the test for the tumor/lesion identification. The value in TUTEST cannot be longer than 40 characters. Example: "Tumor identification". See assumption 3. |
| 12 | TUORRES | Tumor/Lesion ID Result | Char | Result Qualifier | Exp |  |  |  |  | Result of the tumor/lesion identification. The result of tumor/lesion identification is a classification of the identified tumor/lesion. Example: When TUTESTCD = "TUMIDENT", values of TUORRES might be "TARGET", "NON-TARGET", "NEW", or "BENIGN ABNORMALITY". |
| 13 | TUSTRESC | Tumor/Lesion ID Result Std. Format | Char | Result Qualifier | Exp | C123650 |  |  |  | Contains the result value for all findings copied or derived from TUORRES in a standard format. |
| 14 | TUNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | The name or identifier of the vendor that performed the tumor/lesion Identification. This column can be left null when the investigator provides the complete set of data in the domain. |
| 15 | TULOC | Location of the Tumor/Lesion | Char | Record Qualifier | Exp | C74456 |  |  |  | Used to specify the anatomical location of the identified tumor/lesion (e.g., "LIVER"). \n Note: When anatomical location is broken down and collected as distinct pieces of data that when combined provide the overall location information (e.g., laterality/directionality/distribution), then additional anatomical location qualifiers should be used. See assumption 3. |
| 16 | TULAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality (e.g., "LEFT", "RIGHT", "BILATERAL"). |
| 17 | TUDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality (e.g., "UPPER", "INTERIOR"). |
| 18 | TUPORTOT | Portion or Totality | Char | Variable Qualifier | Perm | C99075 |  |  |  | Qualifier for anatomical location or specimen further detailing the distribution, which means arrangement of, or apportioning of. Examples: "ENTIRE", "SINGLE", "SEGMENT", "MULTIPLE". |
| 19 | TUMETHOD | Method of Identification | Char | Record Qualifier | Exp | C85492 |  |  |  | Method used to identify the tumor/lesion. Examples: "MRI", "CT SCAN". |
| 20 | TULOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| 21 | TUBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that TUBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 22 | TUEVAL | Evaluator | Char | Record Qualifier | Exp | C78735 |  |  |  | Role of the person who provided the evaluation. Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR". \n This column can be left null when the investigator provides the complete set of data in the domain. However, the column should contain no null values when data from 1 or more independent assessors is included. For example, the rows attributed to the investigator should contain a value of "INVESTIGATOR". |
| 23 | TUEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in --EVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumption 9. |
| 24 | TUACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATION COMMITTEE") provide independent assessments at the same time point, this flag identifies the record that is considered to be the accepted assessment. |
| 25 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 26 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 27 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. Should be an integer. |
| 28 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 29 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 30 | TUDTC | Date/Time of Tumor/Lesion Identification | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | TUDTC variable represents the date of the scan/image/physical exam. TUDTC does not represent the date that the image was read to identify tumors. TUDTC also does not represent the VISIT date. |
| 31 | TUDY | Study Day of Tumor/Lesion Identification | Num | Timing | Perm |  |  |  |  | Study day of the scan/image/physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
