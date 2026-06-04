# RE — Respiratory System Findings

**Class:** Findings  
**Structure:** One record per finding or result per time point per visit per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | RE | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier for a device. |
| 5 | RESEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| 6 | REGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 7 | REREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external procedure identifier. |
| 8 | RESPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. |
| 9 | RELNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 10 | RELNKGRP | Link Group | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 11 | RETESTCD | Short Name of Respiratory Test | Char | Topic | Req | C111106 |  |  |  | Short name of the measurement, test, or examination. It can be used as a column name when converting a dataset from a vertical format to a horizontal format. The value in RETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). RETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "FEV1", "FVC". |
| 12 | RETEST | Name of Respiratory Test | Char | Synonym Qualifier | Req | C111107 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in RETEST cannot be longer than 40 characters. Examples: "Forced Expiratory Volume in 1 Second", "Forced Vital Capacity". |
| 13 | RECAT | Category for Respiratory Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to categorize observations across subjects. |
| 14 | RESCAT | Subcategory for Respiratory Test | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization. |
| 15 | REPOS | Position of Subject During Observation | Char | Record Qualifier | Perm | C71148 |  |  |  | Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING". |
| 16 | REORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the procedure measurement or finding as originally received or collected. |
| 17 | REORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. The unit for REORRES and REORREF. |
| 18 | REORREF | Reference Result in Original Units | Char | Variable Qualifier | Perm |  |  |  |  | Reference result for continuous measurements in original units. Should be collected only for continuous results. |
| 19 | RESTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from REORRES in a standard format or in standard units. RESTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in RESTRESN. |
| 20 | RESTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from RESTRESC. RESTRESN should store all numeric test results or findings. |
| 21 | RESTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized unit used for RESTRESC, RESTRESN and RESTREFN. |
| 22 | RESTREFC | Character Reference Result | Char | Variable Qualifier | Perm |  |  |  |  | Reference value for the result or finding copied or derived from --ORREF in a standard format. |
| 23 | RESTREFN | Numeric Reference Result in Std Units | Num | Variable Qualifier | Perm |  |  |  |  | Reference result for continuous measurements in standard units. Should be populated only for continuous results. |
| 24 | RESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a test was not done or a measurement was not taken. Should be null if a result exists in REORRES. |
| 25 | REREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with RESTAT when value is "NOT DONE". |
| 26 | RELOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. Examples: "LUNG", "BRONCHUS". |
| 27 | RELAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Side of the body used to collect measurement. Examples: "RIGHT", "LEFT". |
| 28 | REDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 29 | REMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method used to create the result. |
| 30 | RELOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 31 | REBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be Y or null. Note that REBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 32 | REDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record. Should be "Y" or null. Records that represent the average of other records, or that do not come from the CRF, or are not as originally collected or received are examples of records that would be derived for the submission datasets. If REDRVFL = "Y", then REORRES could be null, with RESTRESC and (if numeric) RESTRESN having the derived value. |
| 33 | REEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| 34 | REEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in REEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". |
| 35 | REREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |  |  |  | The instance number of a test that is repeated within a given time frame for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Example: multiple measurements of pulmonary function. |
| 36 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 37 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 38 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 39 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 40 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 41 | REDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of procedure or test. |
| 42 | REDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 43 | RETPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See RETPTNUM and RETPTREF. Examples: "START", "5 MINUTES POST". |
| 44 | RETPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of RETPT to aid in sorting. |
| 45 | REELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to a planned fixed reference (RETPTREF). Not a clock time or a date/time variable, but an interval, represented as ISO duration. Examples: "-PT15M" to represent 15 minutes prior to the reference time point indicated by RETPTREF, "PT8H" to represent 8 hours after the reference time point represented by RETPTREF. |
| 46 | RETPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by REELTM, RETPTNUM, and RETPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 47 | RERFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by RETPTREF. |
