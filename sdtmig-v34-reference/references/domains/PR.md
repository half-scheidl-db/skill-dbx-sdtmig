# PR — Procedures

**Class:** Interventions  
**Structure:** One record per recorded procedure per occurrence per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | PR | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | PRSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | PRGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records within a subject in a domain. |
| 6 | PRSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. Example: preprinted line identifier on a CRF, record identifier defined in the sponsor's operational database. |
| 7 | PRLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Used to facilitate identification of relationships between records. |
| 8 | PRLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Used to facilitate identification of relationships between records. |
| 9 | PRTRT | Reported Name of Procedure | Char | Topic | Req |  |  |  |  | Name of procedure performed, either preprinted or collected on a CRF. |
| 10 | PRDECOD | Standardized Procedure Name | Char | Synonym Qualifier | Perm | C101858 |  |  |  | Standardized or dictionary-derived name of PRTRT. If the codelist "PROCEDUR" is not used, the sponsor is expected to provide the dictionary name and version used to map the terms in the external codelist element in the Define-XML document. If an intervention term does not have a decode value, then PRDECOD will be null. |
| 11 | PRCAT | Category | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of procedure values. |
| 12 | PRSCAT | Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of PRCAT values. |
| 13 | PRPRESP | Pre-specified | Char | Variable Qualifier | Perm | C66742 |  |  |  | Used when a specific procedure is pre-specified on a CRF. Values should be "Y" or null. |
| 14 | PROCCUR | Occurrence | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to record whether a prespecified procedure occurred when information about the occurrence of a specific procedure is solicited. |
| 15 | PRINDC | Indication | Char | Record Qualifier | Perm |  |  |  |  | Denotes the indication for the procedure (e.g., why the procedure was performed). |
| 16 | PRDOSE | Dose | Num | Record Qualifier | Perm |  |  |  |  | Amount of PRTRT administered. Not populated when PRDOSTXT is populated. |
| 17 | PRDOSTXT | Dose Description | Char | Record Qualifier | Perm |  |  |  |  | Dosing information collected in text form. Examples: "<1", "200-400". Not populated when PRDOSE is populated. |
| 18 | PRDOSU | Dose Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Units for PRDOSE, PRDOSTOT, or PRDOSTXT. |
| 19 | PRDOSFRM | Dose Form | Char | Variable Qualifier | Perm | C66726 |  |  |  | Dose form for PRTRT. |
| 20 | PRDOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier | Perm | C71113 |  |  |  | Usually expressed as the number of doses given per a specific interval. |
| 21 | PRDOSRGM | Intended Dose Regimen | Char | Record Qualifier | Perm |  |  |  |  | Text description of the intended schedule or regimen for the procedure. |
| 22 | PRROUTE | Route of Administration | Char | Variable Qualifier | Perm | C66729 |  |  |  | Route of administration for PRTRT. |
| 23 | PRLOC | Location of Procedure | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location of a procedure. |
| 24 | PRLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. |
| 25 | PRDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality. |
| 26 | PRPORTOT | Portion or Totality | Char | Variable Qualifier | Perm | C99075 |  |  |  | Qualifier for anatomical location or specimen further detailing the distribution, which means arrangement of, apportioning of. |
| 27 | VISITNUM | Visit Number | Num | Timing | Perm |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 28 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 29 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 30 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 31 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the procedure. |
| 32 | PRSTDTC | Start Date/Time of Procedure | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Start date/time of the procedure represented in ISO 8601 character format. |
| 33 | PRENDTC | End Date/Time of Procedure | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | End date/time of the procedure represented in ISO 8601 character format. |
| 34 | PRSTDY | Study Day of Start of Procedure | Num | Timing | Perm |  |  |  |  | Study day of start of procedure expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 35 | PRENDY | Study Day of End of Procedure | Num | Timing | Perm |  |  |  |  | Study day of end of procedure expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 36 | PRDUR | Duration of Procedure | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration of a procedure represented in ISO 8601 character format. Used only if collected on the CRF and not derived from start and end date/times. |
| 37 | PRTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a procedure should be performed. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See PRTPTNUM and PRTPTREF. |
| 38 | PRTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of planned time point used in sorting. |
| 39 | PRELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time in ISO 8601 format relative to a planned fixed reference (PRTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 40 | PRTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by PRELTM, PRTPTNUM, and PRTPT. |
| 41 | PRRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by PRTRTREF in ISO 8601 character format. |
| 42 | PRSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the start of the observation as being before or after the sponsor-defined reference time point defined by variable PRSTTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 43 | PRSTTPT | Start Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by PRSTRTPT. Examples: "2003-12-15", "VISIT 1". |
| 44 | PRENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the end of the observation as being before or after the sponsor-defined reference time point defined by variable PRENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 45 | PRENTPT | End Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by PRENRTPT. Examples: "2003-12-25", "VISIT 2". |
