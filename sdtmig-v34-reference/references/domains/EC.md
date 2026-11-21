# EC — Exposure as Collected

**Class:** Interventions  
**Structure:** One record per protocol-specified study treatment, collected-dosing interval, per subject, per mood

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | EC | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | ECSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | ECGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | ECREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external identifier (e.g., kit number, bottle label, vial identifier). |
| 7 | ECSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page. |
| 8 | ECLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. |
| 9 | ECLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related, grouped records across domains. |
| 10 | ECTRT | Name of Treatment | Char | Topic | Req |  |  |  |  | Name of the intervention treatment known to the subject and/or administrator. |
| 11 | ECMOOD | Mood | Char | Record Qualifier | Perm | C125923 |  |  |  | Mode or condition of the record specifying whether the intervention (activity) is intended to happen or has happened. Values align with BRIDG pillars (e.g., scheduled context, performed context) and HL7 activity moods (e.g., intent, event). Examples: "SCHEDULED", "PERFORMED". |
| 12 | ECCAT | Category of Treatment | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related ECTRT values. |
| 13 | ECSCAT | Subcategory of Treatment | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of ECCAT values. |
| 14 | ECPRESP | Pre-Specified | Char | Variable Qualifier | Perm | C66742 |  |  |  | Used when a specific intervention is prespecified. Values should be "Y" or null. |
| 15 | ECOCCUR | Occurrence | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate whether a treatment occurred when information about the occurrence is solicited. ECOCCUR = "N" when a treatment was not taken, not given, or missed. |
| 16 | ECREASOC | Reason for Occur Value | Char | Record Qualifier | Perm |  |  |  |  | The reason for the value in --OCCUR. If --OCCUR = "N", this is the reason the exposure did not occur. |
| 17 | ECDOSE | Dose | Num | Record Qualifier | Exp |  |  |  |  | Amount of ECTRT when numeric. Not populated when ECDOSTXT is populated. |
| 18 | ECDOSTXT | Dose Description | Char | Record Qualifier | Perm |  |  |  |  | Amount of ECTRT when non-numeric. Dosing amounts or a range of dosing information collected in text form. Example: "200-400". Not populated when ECDOSE is populated. |
| 19 | ECDOSU | Dose Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Units for ECDOSE, ECDOSTOT, or ECDOSTXT. |
| 20 | ECDOSFRM | Dose Form | Char | Variable Qualifier | Exp | C66726 |  |  |  | Dose form for ECTRT. Examples: "TABLET", "LOTION". |
| 21 | ECDOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier | Perm | C71113 |  |  |  | Usually expressed as the number of repeated administrations of ECDOSE within a specific time period. Examples: "Q2H", "QD", "BID". |
| 22 | ECDOSTOT | Total Daily Dose | Num | Record Qualifier | Perm |  |  |  |  | Total daily dose of ECTRT using the units in ECDOSU. Used when dosing is collected as total daily dose. |
| 23 | ECDOSRGM | Intended Dose Regimen | Char | Record Qualifier | Perm |  |  |  |  | Text description of the intended schedule or regimen for the Intervention. Example: "TWO WEEKS ON", "TWO WEEKS OFF". |
| 24 | ECROUTE | Route of Administration | Char | Variable Qualifier | Perm | C66729 |  |  |  | Route of administration for the intervention. Examples: "ORAL", "INTRAVENOUS". |
| 25 | ECLOT | Lot Number | Char | Record Qualifier | Perm |  |  |  |  | Lot number of the ECTRT product. |
| 26 | ECLOC | Location of Dose Administration | Char | Record Qualifier | Perm | C74456 |  |  |  | Specifies location of administration. Example: "ARM", "LIP". |
| 27 | ECLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location further detailing laterality of the intervention administration. Examples: "LEFT", "RIGHT". |
| 28 | ECDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL", "UPPER". |
| 29 | ECPORTOT | Portion or Totality | Char | Variable Qualifier | Perm | C99075 |  |  |  | Qualifier for anatomical location further detailing distribution (i.e., arrangement of, apportioning of). Examples: "ENTIRE", "SINGLE", "SEGMENT". |
| 30 | ECFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify fasting status. Examples: "Y", "N". |
| 31 | ECPSTRG | Pharmaceutical Strength | Num | Record Qualifier | Perm |  |  |  |  | Amount of an active ingredient expressed quantitatively per dosage unit, per unit of volume, or per unit of weight, according to the pharmaceutical dose form. |
| 32 | ECPSTRGU | Pharmaceutical Strength Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Unit for ECPSTRG. Examples: "mg/TABLET", "mg/mL". |
| 33 | ECADJ | Reason for Dose Adjustment | Char | Record Qualifier | Perm |  |  |  |  | Describes reason or explanation of why a dose is adjusted. |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Trial epoch of the exposure as collected record. Examples: "RUN-IN", "TREATMENT". |
| 36 | ECSTDTC | Start Date/Time of Treatment | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | The date/time when administration of the treatment indicated by ECTRT and ECDOSE began. |
| 37 | ECENDTC | End Date/Time of Treatment | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | The date/time when administration of the treatment indicated by ECTRT and ECDOSE ended. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, ECSTDTC should be copied to ECENDTC as the standard representation. |
| 38 | ECSTDY | Study Day of Start of Treatment | Num | Timing | Perm |  |  |  |  | Study day of ECSTDTC relative to the sponsor-defined DM.RFSTDTC. |
| 39 | ECENDY | Study Day of End of Treatment | Num | Timing | Perm |  |  |  |  | Study day of ECENDTC relative to the sponsor-defined DM.RFSTDTC. |
| 40 | ECDUR | Duration of Treatment | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration of administration. Used only if collected on the CRF and not derived from start and end date/times. |
| 41 | ECTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when administration should occur. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See ECTPTNUM and ECTPTREF. |
| 42 | ECTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of ECTPT to aid in sorting. |
| 43 | ECELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to the planned fixed reference (ECTPTREF). This variable is useful where there are repetitive measures. Not a clock time. |
| 44 | ECTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by ECELTM, ECTPTNUM, and ECTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 45 | ECRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by ECTPTREF. |
