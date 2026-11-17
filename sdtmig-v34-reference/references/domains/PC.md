# PC — Pharmacokinetics Concentrations

**Class:** Findings  
**Structure:** One record per sample characteristic or time-point concentration per reference time point or per analyte per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | PC | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | PCSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | PCGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain to support relationships within the domain and between domains. |
| 6 | PCREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external specimen identifier. |
| 7 | PCSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. |
| 8 | PCTESTCD | Pharmacokinetic Test Short Name | Char | Topic | Req |  |  |  |  | Short name of the analyte or specimen characteristic. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PCTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PCTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "ASA", "VOL", "SPG". |
| 9 | PCTEST | Pharmacokinetic Test Name | Char | Synonym Qualifier | Req |  |  |  |  | Name of the analyte or specimen characteristic. Note any test normally performed by a clinical laboratory is considered a lab test. The value in PCTEST cannot be longer than 40 characters. Examples: "Acetylsalicylic Acid", "Volume", "Specific Gravity". |
| 10 | PCCAT | Test Category | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. Examples: "ANALYTE", "SPECIMEN PROPERTY". |
| 11 | PCSCAT | Test Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of a test category. |
| 12 | PCORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 13 | PCORRESU | Original Units | Char | Variable Qualifier | Exp | C85494 |  |  |  | Original units in which the data were collected. The unit for PCORRES. Example: "mg/L". |
| 14 | PCSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from PCORRES in a standard format or standard units. PCSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in PCSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in PCORRES, and these results effectively have the same meaning, they could be represented in standard format in PCSTRESC as "NEGATIVE". For other examples, see general assumptions. |
| 15 | PCSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from PCSTRESC. PCSTRESN should store all numeric test results or findings. |
| 16 | PCSTRESU | Standard Units | Char | Variable Qualifier | Exp | C85494 |  |  |  | Standardized unit used for PCSTRESC and PCSTRESN. |
| 17 | PCSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate a result was not obtained. Should be null if a result exists in PCORRES. |
| 18 | PCREASND | Reason Test Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a result was not obtained, such as "SPECIMEN LOST". Used in conjunction with PCSTAT when value is "NOT DONE". |
| 19 | PCNAM | Vendor Name | Char | Record Qualifier | Exp |  |  |  |  | Name or identifier of the laboratory or vendor who provides the test results. |
| 20 | PCSPEC | Specimen Material Type | Char | Record Qualifier | Exp | C78734 |  |  |  | Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE". |
| 21 | PCSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |  |  |  | Free or standardized text describing the condition of the specimen. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC". |
| 22 | PCMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: "HPLC/MS", "ELISA". This should contain sufficient information and granularity to allow differentiation of various methods that might have been used within a study. |
| 23 | PCFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify fasting status. |
| 24 | PCDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, which do not come from the CRF, are examples of records that would be derived for the submission datasets. If PCDRVFL = "Y", then PCORRES may be null with PCSTRESC, and PCSTRESN (if the result is numeric) having the derived value. |
| 25 | PCLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Exp |  |  |  |  | Indicates the lower limit of quantitation for an assay. Units should be those used in PCSTRESU. |
| 26 | PCULOQ | Upper Limit of Quantitation | Num | Variable Qualifier | Perm |  |  |  |  | Indicates the upper limit of quantitation for an assay. Units should be those used in PCSTRESU. |
| 27 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 28 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 29 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 30 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 31 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected. |
| 32 | PCDTC | Date/Time of Specimen Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of specimen collection represented in ISO 8601 character format. If there is no end time, then this will be the collection time. |
| 33 | PCENDTC | End Date/Time of Specimen Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | End date/time of specimen collection represented in ISO 8601 character format. If there is no end time, the collection time should be stored in PCDTC, and PCENDTC should be null. |
| 34 | PCDY | Actual Study Day of Specimen Collection | Num | Timing | Perm |  |  |  |  | Study day of specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| 35 | PCENDY | Study Day of End of Observation | Num | Timing | Perm |  |  |  |  | Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 36 | PCTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See PCTPTNUM and PCTPTREF. Examples: "Start", "5 min post". |
| 37 | PCTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of PCTPT to aid in sorting. |
| 38 | PCELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to a planned fixed reference (PCTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. |
| 39 | PCTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point used as a basis for PCTPT, PCTPTNUM, and PCELTM. Example: "MOST RECENT DOSE". |
| 40 | PCRFTDTC | Date/Time of Reference Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time of the reference time point described by PCTPTREF. |
| 41 | PCEVLINT | Evaluation Interval | Char | Timing | Perm |  |  | ISO 8601 duration or interval |  | Evaluation Interval associated with a PCTEST record represented in ISO 8601 character format. Example: "-PT2H" to represent an evaluation interval of 2 hours prior to a PCTPT. |
