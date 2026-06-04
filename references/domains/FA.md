# FA — Findings About Events or Interventions

**Class:** Findings About  
**Structure:** One record per finding, per object, per time point, per visit per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | FA | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | FASEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | FAGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | FASPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF. |
| 7 | FATESTCD | Findings About Test Short Name | Char | Topic | Req | C101832 |  |  |  | Short name of the measurement, test, or examination described in FATEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in FATESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). FATESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SEV", "OCCUR". Note that controlled terminology is in a FATESTCD general codelist and in several therapeutic area-specific codelists. |
| 8 | FATEST | Findings About Test Name | Char | Synonym Qualifier | Req | C101833 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in FATEST cannot be longer than 40 characters. Examples: "Severity/Intensity", "Occurrence". Note that controlled terminology is in a FATEST general codelist and in several therapeutic area-specific codelists. |
| 9 | FAOBJ | Object of the Observation | Char | Record Qualifier | Req |  |  |  |  | Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the term (e.g., "Acne") describing a clinical sign or symptom that is being measured by a severity test; an event (e.g., "VOMIT, where the volume of vomit is being measured by a VOLUME test). |
| 10 | FACAT | Category for Findings About | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. Examples: "GERD", "PRE-SPECIFIED AE". |
| 11 | FASCAT | Subcategory for Findings About | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of FACAT. |
| 12 | FAORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the test as originally received or collected. |
| 13 | FAORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. The unit for FAORRES. |
| 14 | FASTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from FAORRES in a standard format or standard units. FASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in FASTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in FAORRES, and these results effectively have the same meaning; they could be represented in standard format in FASTRESC as "NEGATIVE". |
| 15 | FASTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from FASTRESC. FASTRESN should store all numeric test results or findings. |
| 16 | FASTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized unit used for FASTRESC and FASTRESN. |
| 17 | FASTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that the measurement was not done. Should be null if a result exists in FAORRES. |
| 18 | FAREASND | Reason Not Performed | Char | Record Qualifier | Perm |  |  |  |  | Describes why a question was not answered. Example: "Subject refused". Used in conjunction with FASTAT when value is "NOT DONE". |
| 19 | FALOC | Location of the Finding About | Char | Record Qualifier | Perm | C74456 |  |  |  | Used to specify the location of the clinical evaluation. Example: "ARM". |
| 20 | FALAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 21 | FALOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 22 | FABLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. The value should be "Y" or null. Note that FABLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 23 | FAEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR". |
| 24 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | 1. Clinical encounter number. \n 2. Numeric version of VISIT, used for sorting. |
| 25 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | 1. Protocol-defined description of clinical encounter. \n 2. May be used in addition to VISITNUM and/or VISITDY. |
| 26 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 27 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 28 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP". |
| 29 | FADTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of findings assessment represented in ISO 8601 character format. |
| 30 | FADY | Study Day of Collection | Num | Timing | Perm |  |  |  |  | 1. Study day of collection, measured as integer days. \n 2. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |
