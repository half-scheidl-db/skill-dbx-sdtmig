# PE — Physical Examination

**Class:** Findings  
**Structure:** One record per body system or abnormality per visit per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | PE | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | PESEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number. |
| 5 | PEGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records in a single domain for a subject. |
| 6 | PESPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. Perhaps preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF. |
| 7 | PETESTCD | Body System Examined Short Name | Char | Topic | Req |  |  |  |  | Short name of a part of the body examined in a physical examination. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "HEAD", "ENT". If the results of the entire physical examination are represented in one record, value should be "PHYSEXAM". |
| 8 | PETEST | Body System Examined | Char | Synonym Qualifier | Req |  |  |  |  | Long name of a part of the body examined in a physical examination. The value in PETEST cannot be longer than 40 characters. Examples: "Head", "Ear/Nose/Throat". If the results of the entire physical examination are represented in one record, value should be "Physical Examination". |
| 9 | PEMODIFY | Modified Reported Term | Char | Synonym Qualifier | Perm |  |  |  |  | If the value of PEORRES is modified for coding purposes, then the modified text is placed here. |
| 10 | PECAT | Category for Examination | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. Example: "GENERAL". |
| 11 | PESCAT | Subcategory for Examination | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of --CAT values. |
| 12 | PEBODSYS | Body System or Organ Class | Char | Record Qualifier | Perm |  |  |  |  | Body system or organ class (e.g., MedDRA SOC) that is involved for a finding from the standard hierarchy for dictionary-coded results. |
| 13 | PEORRES | Verbatim Examination Finding | Char | Result Qualifier | Exp |  |  |  |  | Text description of any abnormal findings. If the examination was completed and there were no abnormal findings, the value should be "NORMAL". If the examination was not performed on a particular body system, or at the subject level, then the value should be null, and "NOT DONE" should appear in PESTAT. |
| 14 | PEORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. The unit for PEORRES. |
| 15 | PESTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | If there are findings for a body system, then either the dictionary preferred term (if findings are coded using a dictionary) or PEORRES (if findings are not encoded) should appear here. If PEORRES is null, PESTRESC must be null. |
| 16 | PESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate exam not done. Must be null if a result exists in PEORRES/PESTRESC. |
| 17 | PEREASND | Reason Not Examined | Char | Record Qualifier | Perm |  |  |  |  | Describes why an examination was not performed or why a body system was not examined. Example: "SUBJECT REFUSED". Used in conjunction with PESTAT when value is "NOT DONE". |
| 18 | PELOC | Location of Physical Exam Finding | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. Example: "ARM" for skin rash. |
| 19 | PELAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterallity. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 20 | PEMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: "PALPATION", "PERCUSSION". |
| 21 | PELOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| 22 | PEBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | A baseline defined by the sponsor (could be derived in the same manner as PELOBXFL or ABLFL, but is not required to be). The value should be "Y" or null. Note that PEBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 23 | PEEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Example: "INVESTIGATOR". |
| 24 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 25 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 26 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 27 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 28 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the observation date/time of the physical exam finding. |
| 29 | PEDTC | Date/Time of Examination | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date and time of the physical examination represented in ISO 8601 character format. |
| 30 | PEDY | Study Day of Examination | Num | Timing | Perm |  |  |  |  | Study day of physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
