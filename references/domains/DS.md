# DS — Disposition

**Class:** Events  
**Structure:** One record per disposition status or protocol milestone per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | DS | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | DSSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | DSGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | DSREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external identifier. |
| 7 | DSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Disposition page. |
| 8 | DSTERM | Reported Term for the Disposition Event | Char | Topic | Req |  |  |  |  | Verbatim name of the event or protocol milestone. Some terms in DSTERM will match DSDECOD, but others, such as "Subject moved", will map to controlled terminology in DSDECOD, such as "LOST TO FOLLOW-UP". |
| 9 | DSDECOD | Standardized Disposition Term | Char | Synonym Qualifier | Req | C66727; C114118; C150811 |  |  |  | Controlled terminology for the name of disposition event or protocol milestone. Examples of protocol milestones: "INFORMED CONSENT OBTAINED", "RANDOMIZED". There are separate codelists used for DSDECOD where the choice depends on the value of DSCAT. Codelist "NCOMPLT" is used for disposition events, codelist "PROTMLST" is used for protocol milestones, and codelist "OTHEVENT" is used for other events. |
| 10 | DSCAT | Category for Disposition Event | Char | Grouping Qualifier | Exp | C74558 |  |  |  | Used to define a category of related records. |
| 11 | DSSCAT | Subcategory for Disposition Event | Char | Grouping Qualifier | Perm | C170443 |  |  |  | A further categorization of DSCAT (e.g., "STUDY PARTICIPATION", "STUDY TREATMENT" when DSCAT = "DISPOSITION EVENT"). The variable may be subject to controlled terminology for other categories of disposition event records. |
| 12 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the event. |
| 13 | DSDTC | Date/Time of Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Collection date and time of the disposition observation represented in ISO 8601 character format. |
| 14 | DSSTDTC | Start Date/Time of Disposition Event | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Start date/time of the disposition event in ISO 8601 character format. |
| 15 | DSDY | Study Day of Collection | Num | Timing | Perm |  |  |  |  | Study day of collection of event relative to the sponsor-defined RFSTDTC. |
| 16 | DSSTDY | Study Day of Start of Disposition Event | Num | Timing | Exp |  |  |  |  | Study day of start of event relative to the sponsor-defined RFSTDTC. |
