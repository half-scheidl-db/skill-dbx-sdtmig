# PP — Pharmacokinetics Parameters

**Class:** Findings  
**Structure:** One record per PK parameter per time-concentration profile per modeling method per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | PP | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. \n |
| 4 | PPSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | PPGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain to support relationships within the domain and between domains. |
| 6 | PPTESTCD | Parameter Short Name | Char | Topic | Req | C85839 |  |  |  | Short name of the pharmacokinetic parameter. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PPTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PPTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "AUCALL", "TMAX", "CMAX". |
| 7 | PPTEST | Parameter Name | Char | Synonym Qualifier | Req | C85493 |  |  |  | Name of the pharmacokinetic parameter. The value in PPTEST cannot be longer than 40 characters. Examples: "AUC All", "Time of CMAX", "Max Conc". |
| 8 | PPCAT | Parameter Category | Char | Grouping Qualifier | Exp |  |  |  |  | Used to define a category of related records. For PP, this should be the name of the analyte in PCTEST whose profile the parameter is associated with. |
| 9 | PPSCAT | Parameter Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | Categorization of the model type used to calculate the PK parameters. Examples: "COMPARTMENTAL", "NON-COMPARTMENTAL". |
| 10 | PPORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 11 | PPORRESU | Original Units | Char | Variable Qualifier | Exp | C85494; C128684; C128683; C128685; C128686 |  |  |  | Original units in which the data were collected. The unit for PPORRES. Example: "ng/L". See PP Assumption 3. |
| 12 | PPSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from PPORRES in a standard format or standard units. PPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in PPSTRESN. |
| 13 | PPSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from PPSTRESC. PPSTRESN should store all numeric test results or findings. |
| 14 | PPSTRESU | Standard Units | Char | Variable Qualifier | Exp | C85494; C128684; C128683; C128685; C128686 |  |  |  | Standardized unit used for PPSTRESC and PPSTRESN. See PP Assumption 3. |
| 15 | PPSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a parameter was not calculated. Should be null if a result exists in PPORRES. |
| 16 | PPREASND | Reason Parameter Not Calculated | Char | Record Qualifier | Perm |  |  |  |  | Describes why a parameter was not calculated, such as "INSUFFICIENT DATA". Used in conjunction with PPSTAT when value is "NOT DONE". |
| 17 | PPSPEC | Specimen Material Type | Char | Record Qualifier | Exp | C78734 |  |  |  | Defines the type of specimen used for a measurement. If multiple specimen types are used for a calculation (e.g., serum and urine for renal clearance), then this field should be left blank. Examples: "SERUM", "PLASMA", "URINE". |
| 18 | PPANMETH | Analysis Method | Char | Record Qualifier | Perm | C172330 |  |  |  | Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result. Example: A named formula used to calculate AUC, such as "LIN-LOG TRAPEZOIDAL METHOD". \n Sponsor-defined formulas can also be represented by this variable. Example: Calculating ratio AUCs where the PPANMETH may be "DRUG METABOLITE 1 TO DRUG PARENT" or "DRUG METABOLITE 2 TO METABOLITE 1". |
| 19 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 20 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected. |
| 21 | PPDTC | Date/Time of Parameter Calculations | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Nominal date/time of parameter calculations. |
| 22 | PPDY | Study Day of Parameter Calculations | Num | Timing | Perm |  |  |  |  | Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. |
| 23 | PPTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | The description of a time point that acts as a fixed reference for a series of planned time points. |
| 24 | PPRFTDTC | Date/Time of Reference Point | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of the reference time point from the PC records used to calculate a parameter record. The values in PPRFTDTC should be the same as that in PCRFTDTC for related records. |
| 25 | PPSTINT | Planned Start of Assessment Interval | Char | Timing | Perm |  |  | ISO 8601 duration |  | The start of a planned evaluation or assessment interval relative to the time point reference. |
| 26 | PPENINT | Planned End of Assessment Interval | Char | Timing | Perm |  |  | ISO 8601 duration |  | The end of a planned evaluation or assessment interval relative to the time point reference. |
