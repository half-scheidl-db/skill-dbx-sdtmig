# FT — Functional Tests

**Class:** Findings  
**Structure:** One record per Functional Test finding per time point per visit per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | FT | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | FTSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number. |
| 5 | FTGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 6 | FTREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external identifier. |
| 7 | FTSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the Test page. |
| 8 | FTTESTCD | Short Name of Test | Char | Topic | Req |  |  |  |  | Short character value for FTTEST, which can be used as a column name when converting a dataset from a vertical format to a horizontal format. The value cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). FTTESTCD cannot contain characters other than letters, numbers, or underscores. \n Controlled terminology for FTTESTCD is published in separate codelists for each instrument. See https://www.cdisc.org/standards/terminology/controlled-terminology for values for FTTESTCD. Examples: "W250101", "W25F0102". |
| 9 | FTTEST | Name of Test | Char | Synonym Qualifier | Req |  |  |  |  | Verbatim name of the question used to obtain the finding. The value in FTTEST cannot be longer than 40 characters. \n Controlled terminology for FTTEST is published in separate codelists for each instrument. See https://www.cdisc.org/standards/terminology/controlled-terminology for values for FTTEST. Examples: "W2501-25 Foot Walk Time", "W25F-More Than Two Attempts". |
| 10 | FTCAT | Category | Char | Grouping Qualifier | Req | C115304 |  |  |  | Used to specify the functional test in which the functional test question identified by FTTEST and FTTESTCD was included. |
| 11 | FTSCAT | Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of FTCAT values. |
| 12 | FTPOS | Position of Subject During Observation | Char | Record Qualifier | Perm | C71148 |  |  |  | Position of the subject during the test. Examples: "SUPINE", "STANDING", "SITTING". |
| 13 | FTORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 14 | FTORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. Unit for FTORRES. |
| 15 | FTSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from FTORRES in a standard format or in standard units. FTSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in FTSTRESN. |
| 16 | FTSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from FTSTRESC. FTSTRESN should store all numeric test results or findings. |
| 17 | FTSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for FTSTRESC and FTSTRESN. |
| 18 | FTSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 19 | FTREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a test was not done, or a test was attempted but did not generate a result. Used in conjunction with FTSTAT when value is "NOT DONE". |
| 20 | FTXFN | External File Path | Char | Record Qualifier | Perm |  |  |  |  | File path to an external file. |
| 21 | FTNAM | Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the vendor or laboratory that provided the test results. |
| 22 | FTMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C158113 |  |  |  | Method of the test or examination. |
| 23 | FTLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 24 | FTBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | A baseline defined by the sponsor (could be derived in the same manner as FTLOBXFL or ABLFL, but is not required to be). The value should be "Y" or null. Note that FTBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 25 | FTDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 26 | FTREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |  |  |  | The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample. |
| 27 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 28 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 29 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT based upon RFSTDTC in Demographics. Should be an integer. |
| 30 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 31 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the observation date/time of the functional tests finding. |
| 32 | FTDTC | Date/Time of Test | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of functional test. |
| 33 | FTDY | Study Day of Test | Num | Timing | Perm |  |  |  |  | Actual study day of test expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 34 | FTTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See FTTPTNUM and FTTPTREF. |
| 35 | FTTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 36 | FTELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to a planned fixed reference (FTTPTREF). Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 37 | FTTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by FTELTM, FTTPTNUM, and FTTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 38 | FTRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by FTTPTREF. |
