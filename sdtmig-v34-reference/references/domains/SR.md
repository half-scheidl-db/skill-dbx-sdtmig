# SR — Skin Response

**Class:** Findings About  
**Structure:** One record per finding, per object, per time point, per visit per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | SR | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SRSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | SRGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | SRREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external specimen identifier. Example: "Specimen ID". |
| 7 | SRSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 8 | SRTESTCD | Skin Response Test or Exam Short Name | Char | Topic | Req | C112024 |  |  |  | Short name of the measurement, test, or examination described in SRTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SRTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SRTESTCD cannot contain characters other than letters, numbers, or underscores. |
| 9 | SRTEST | Skin Response Test or Examination Name | Char | Synonym Qualifier | Req | C112023 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in SRTEST cannot be longer than 40 characters. Example: "Wheal Diameter". |
| 10 | SROBJ | Object of the Observation | Char | Record Qualifier | Req |  |  |  |  | Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the dose of the immunogenic material or the allergen associated with the response (e.g., "Johnson Grass IgE 0.15 BAU mL"). |
| 11 | SRCAT | Category for Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values across subjects. |
| 12 | SRSCAT | Subcategory for Test | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of SRCAT values. |
| 13 | SRORRES | Results or Findings in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Results of measurement or finding as originally received or collected. |
| 14 | SRORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Original units in which the data were collected. The unit for SRORRES. Example: "mm". |
| 15 | SRSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from SRORRES, in a standard format or in standard units. SRSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in SRSTRESN. |
| 16 | SRSTRESN | Numeric Results/Findings in Std. Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from SRSTRESC. SRSTRESN should store all numeric test results or findings. |
| 17 | SRSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Standardized units used for SRSTRESC and SRSTRESN. Example: "mm". |
| 18 | SRSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate exam not done. Should be null if a result exists in SRORRES. |
| 19 | SRREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a measurement or test was not performed. Used in conjunction with SRSTAT when value is "NOT DONE". |
| 20 | SRNAM | Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the laboratory or vendor who provided the test results. |
| 21 | SRSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734 |  |  |  | Defines the types of specimen used for a measurement. Example: "SKIN". |
| 22 | SRLOC | Location Used for Measurement | Char | Record Qualifier | Perm | C74456 |  |  |  | Location relevant to the collection of the measurement. |
| 23 | SRLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location further detailing laterality of intervention administration. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 24 | SRMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of test or examination. Examples: "ELISA", "EIA", "MICRONEUTRALIZATION ASSAY", "PLAQUE REDUCTION NEUTRALIZATION ASSAY". |
| 25 | SRLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 26 | SRBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. The value should be "Y" or null. Note that SRBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 27 | SREVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of person who provided evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR". |
| 28 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 29 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 30 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 31 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 32 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", and "FOLLOW-UP". |
| 33 | SRDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of an observation represented in ISO 8601. |
| 34 | SRDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to sponsor- defined RFSTDTC in Demographics. |
| 35 | SRTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See SRTPTNUM and SRTPTREF. Examples: "START", "5 MIN POST". |
| 36 | SRTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of SRTPT to aid in sorting. |
| 37 | SRELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to a fixed time point reference (SRTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by SRTPTREF. |
| 38 | SRTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by SRELTM, SRTPTNUM, and SRTPT. Example: "INTRADERMAL INJECTION". |
| 39 | SRRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time of the reference time point, SRTPTREF. |
