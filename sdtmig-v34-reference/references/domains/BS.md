# BS — Biospecimen Findings

**Class:** Findings  
**Structure:** One record per measurement per biospecimen identifier per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | BS | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier for a device. |
| 5 | BSSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| 6 | BSGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 7 | BSREFID | Reference ID | Char | Identifier | Exp |  |  |  |  | Internal or external identifier such as lab specimen ID. |
| 8 | BSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 9 | BSTESTCD | Biospecimen Test Short Name | Char | Topic | Req | C124300 |  |  |  | Short character value for BSTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Examples: VOLUME, RIN. |
| 10 | BSTEST | Biospecimen Test Name | Char | Synonym Qualifier | Req | C124299 |  |  |  | Long name for BSTESTCD. Examples: Volume, RNA Integrity Number. |
| 11 | BSCAT | Category for Biospecimen Test | Char | Grouping Qualifier | Exp |  |  |  |  | Used to define a category of topic-variable values. Example: MEASUREMENT, QUALITY. |
| 12 | BSSCAT | Subcategory for Biospecimen Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of BSCAT values. |
| 13 | BSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 14 | BSORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Unit for BSORRES. Examples: mg, mL. |
| 15 | BSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from BSORRES in a standard format or standard units. BSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in BSSTRESN. |
| 16 | BSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from BSSTRESC. BSSTRESN should store all numeric test results or findings. |
| 17 | BSSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Standardized unit used for BSSTRESC and BSSTRESN. |
| 18 | BSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a test was not done, or was attempted but did not generate a result. Should be null or have a value of NOT DONE. |
| 19 | BSREASND | Reason Test Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with BSSTAT when value is NOT DONE. |
| 20 | BSNAM | Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the vendor (e.g., laboratory) that provided the test results. |
| 21 | BSSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734; C111114 |  |  |  | Defines the type of specimen used for a measurement. Examples: SERUM, PLASMA, URINE, SOFT TISSUE. |
| 22 | BSANTREG | Anatomical Region of Specimen | Char | Variable Qualifier | Perm |  |  |  |  | Defines the specific anatomical or biological region of a tissue, organ specimen or the region from which the specimen is obtained, as defined in the protocol, such as a section or part of what is described in the BSSPEC variable. Examples: CORTEX, MEDULLA, MUCOSA. |
| 23 | BSSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |  |  |  | Defines the condition of the specimen. Examples: HEMOLYZED, ICTERIC, LIPEMIC. |
| 24 | BSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: SPECTROPHOTOMETRY, ELECTROPHORESIS. |
| 25 | BSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. |
| 26 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 27 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. |
| 28 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 29 | BSDTC | Date/Time of Specimen Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date and time of specimen collection. |
| 30 | BSDY | Study Day of Specimen Collection | Num | Timing | Perm |  |  |  |  | Study day of specimen collection relative to the sponsor-defined RFSTDTC. |
| 31 | BSTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See BSTPTNUM and BSTPTREF. |
| 32 | BSTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of BSTPT used in sorting. |
| 33 | BSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Elapsed time relative to a planned fixed reference (BSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration. |
| 34 | BSTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by BSELTM, BSTPTNUM, and BSTPT. Examples: PREVIOUS DOSE, PREVIOUS MEAL. |
| 35 | BSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by BSTPTREF. |
