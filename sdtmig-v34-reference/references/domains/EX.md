# EX — Exposure

**Class:** Interventions  
**Structure:** One record per protocol-specified study treatment, constant-dosing interval, per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | EX | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | EXSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | EXGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | EXREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external identifier (e.g., kit number, bottle label, vial identifier). |
| 7 | EXSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page. |
| 8 | EXLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. |
| 9 | EXLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related, grouped records across domains. |
| 10 | EXTRT | Name of Treatment | Char | Topic | Req |  |  |  |  | Name of the protocol-specified study treatment given during the dosing period for the observation. |
| 11 | EXCAT | Category of Treatment | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of EXTRT values. |
| 12 | EXSCAT | Subcategory of Treatment | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of EXCAT values. |
| 13 | EXDOSE | Dose | Num | Record Qualifier | Exp |  |  |  |  | Amount of EXTRT when numeric. Not populated when EXDOSTXT is populated. |
| 14 | EXDOSTXT | Dose Description | Char | Record Qualifier | Perm |  |  |  |  | Amount of EXTRT when non-numeric. Dosing amounts or a range of dosing information collected in text form. Example: "200-400". Not populated when EXDOSE is populated. |
| 15 | EXDOSU | Dose Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Units for EXDOSE, EXDOSTOT, or EXDOSTXT representing protocol-specified values. Examples: "ng", "mg", "mg/kg", "mg/m2". |
| 16 | EXDOSFRM | Dose Form | Char | Variable Qualifier | Exp | C66726 |  |  |  | Dose form for EXTRT. Examples: "TABLET", "LOTION". |
| 17 | EXDOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier | Perm | C71113 |  |  |  | Usually expressed as the number of repeated administrations of EXDOSE within a specific time period. Examples: "Q2H", "QD", "BID". |
| 18 | EXDOSRGM | Intended Dose Regimen | Char | Record Qualifier | Perm |  |  |  |  | Text description of the intended schedule or regimen for the Intervention. Example: "TWO WEEKS ON, TWO WEEKS OFF". |
| 19 | EXROUTE | Route of Administration | Char | Variable Qualifier | Perm | C66729 |  |  |  | Route of administration for the intervention. Examples: "ORAL", "INTRAVENOUS". |
| 20 | EXLOT | Lot Number | Char | Record Qualifier | Perm |  |  |  |  | Lot number of the intervention product. |
| 21 | EXLOC | Location of Dose Administration | Char | Record Qualifier | Perm | C74456 |  |  |  | Specifies location of administration. Examples: "ARM", "LIP". |
| 22 | EXLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location further detailing laterality of the intervention administration. Examples: "LEFT", "RIGHT". |
| 23 | EXDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL", "UPPER". |
| 24 | EXFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify fasting status. Examples: "Y", "N". |
| 25 | EXADJ | Reason for Dose Adjustment | Char | Record Qualifier | Perm |  |  |  |  | Describes reason or explanation of why a dose is adjusted. |
| 26 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 27 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Trial epoch of the exposure record. Examples: "RUN-IN", "TREATMENT". |
| 28 | EXSTDTC | Start Date/Time of Treatment | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | The date/time when administration of the treatment indicated by EXTRT and EXDOSE began. |
| 29 | EXENDTC | End Date/Time of Treatment | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | The date/time when administration of the treatment indicated by EXTRT and EXDOSE ended. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, EXSTDTC should be copied to EXENDTC as the standard representation. |
| 30 | EXSTDY | Study Day of Start of Treatment | Num | Timing | Perm |  |  |  |  | Study day of EXSTDTC relative to DM.RFSTDTC. |
| 31 | EXENDY | Study Day of End of Treatment | Num | Timing | Perm |  |  |  |  | Study day of EXENDTC relative to DM.RFSTDTC. |
| 32 | EXDUR | Duration of Treatment | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration of administration. Used only if collected on the CRF and not derived from start and end date/times. |
| 33 | EXTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when administration should occur. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See EXTPTNUM and EXTPTREF. |
| 34 | EXTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of EXTPT to aid in sorting. |
| 35 | EXELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to the planned fixed reference (EXTPTREF). This variable is useful where there are repetitive measures. Not a clock time. |
| 36 | EXTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by EXELTM, EXTPTNUM, and EXTPT. Examples: PREVIOUS DOSE, PREVIOUS MEAL. |
| 37 | EXRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by EXTPTREF. |
