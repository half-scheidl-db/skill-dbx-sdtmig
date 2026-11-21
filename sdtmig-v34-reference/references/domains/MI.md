# MI — Microscopic Findings

**Class:** Findings  
**Structure:** One record per finding per specimen per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | MI | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | MISEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | MIGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. This is not the treatment group number. |
| 6 | MIREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external specimen identifier. Example: specimen barcode number. |
| 7 | MISPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be printed on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: line number from the MI Findings page. |
| 8 | MITESTCD | Microscopic Examination Short Name | Char | Topic | Req | C132263 |  |  |  | Short name of the measurement, test, or examination described in MITEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MITESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MITESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "HER2", "BRCA1", "TTF1". |
| 9 | MITEST | Microscopic Examination Name | Char | Synonym Qualifier | Req | C132262 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in MITEST cannot be longer than 40 characters. Examples: "Human Epidermal Growth Factor Receptor 2", "Breast Cancer Susceptibility Gene 1", "Thyroid Transcription Factor 1". |
| 10 | MITSTDTL | Microscopic Examination Detail | Char | Record Qualifier | Perm | C125922 |  |  |  | Further description of the test performed in producing the MI result. This would be used to represent specific attributes, such as intensity score or percentage of cells displaying presence of the biomarker or compound. |
| 11 | MICAT | Category for Microscopic Finding | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. |
| 12 | MISCAT | Subcategory for Microscopic Finding | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of MICAT. |
| 13 | MIORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the histopathology measurement or finding as originally received or collected. |
| 14 | MIORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original unit for MIORRES. |
| 15 | MISTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from MIORRES in a standard format or standard units. MISTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MISTRESN. |
| 16 | MISTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from MISTRESC. MISTRESN should store all numeric test results or findings. |
| 17 | MISTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized unit used for MISTRESC and MISTRESN. |
| 18 | MIRESCAT | Result Category | Char | Variable Qualifier | Perm |  |  |  |  | Used to categorize the result of a finding. Examples: "MALIGNANT" or "BENIGN" for tumor findings. |
| 19 | MISTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate examination not done or result is missing. Should be null if a result exists in MIORRES or have a value of "NOT DONE" when MIORRES = "NULL". |
| 20 | MIREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with MISTAT when value is NOT DONE. Examples: "SAMPLE AUTOLYZED", "SPECIMEN LOST". |
| 21 | MINAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the vendor (e.g., laboratory) that provided the test results. |
| 22 | MISPEC | Specimen Material Type | Char | Record Qualifier | Req | C78734 |  |  |  | Subject of the observation. Defines the type of specimen used for a measurement. Examples: "TISSUE", "BLOOD", "BONE MARROW". |
| 23 | MISPCCND | Specimen Condition | Char | Record Qualifier | Exp | C78733 |  |  |  | Free or standardized text describing the condition of the specimen. Example: "AUTOLYZED". |
| 24 | MILOC | Specimen Collection Location | Char | Record Qualifier | Perm | C74456 |  |  |  | Location relevant to the collection of the specimen. Examples: "LUNG", "KNEE JOINT", "ARM", "THIGH". |
| 25 | MILAT | Specimen Laterality within Subject | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for laterality of the location of the specimen in MILOC. Examples: "LEFT", "RIGHT", "BILATERAL". |
| 26 | MIDIR | Specimen Directionality within Subject | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for directionality of the location of the specimen in MILOC. Examples: "DORSAL", "PROXIMAL". |
| 27 | MIMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. This could include the technique or type of staining used for the slides. Examples: "IHC", "Crystal violet", "Safranin", "Trypan blue", or "Propidium iodide". |
| 28 | MILOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 29 | MIBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. The value should be "Y" or null. Note that MIBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 30 | MIEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Example: "PATHOLOGIST", "PEER REVIEW", "SPONSOR PATHOLOGIST". |
| 31 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 32 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 33 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the specimen was collected. |
| 36 | MIDTC | Date/Time of Specimen Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of specimen collection, in ISO 8601 format. |
| 37 | MIDY | Study Day of Specimen Collection | Num | Timing | Perm |  |  |  |  | Study day of specimen collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. |
