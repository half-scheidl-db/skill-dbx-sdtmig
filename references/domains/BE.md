# BE — Biospecimen Events

**Class:** Events  
**Structure:** One record per instance per biospecimen event per biospecimen identifier per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | BE | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier for a device. |
| 5 | BESEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| 6 | BEGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 7 | BEREFID | Reference ID | Char | Identifier | Exp |  |  |  |  | Internal or external identifier for the specimen affected or created by the event. |
| 8 | BESPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Optional sponsor-defined reference number. Example: Line number on a CRF page. |
| 9 | BETERM | Reported Term for the Biospecimen Event | Char | Topic | Req |  |  |  |  | Topic variable for an event observation, which is the verbatim or pre-specified name of the event. |
| 10 | BEMODIFY | Modified Reported Term | Char | Synonym Qualifier | Perm |  |  |  |  | If the value for BETERM is modified for coding purposes, then the modified text is placed here. |
| 11 | BEDECOD | Dictionary-Derived Term | Char | Synonym Qualifier | Perm | C124297 |  |  |  | Dictionary-derived text description of BETERM or BEMODIFY, if applicable. |
| 12 | BECAT | Category for Biospecimen Event | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. Example: COLLECTION, PREPARATION, TRANSPORT. |
| 13 | BESCAT | Subcategory for Biospecimen Event | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of BECAT values. |
| 14 | BELOC | Anatomical Location of Event | Char | Record Qualifier | Perm | C74456 |  |  |  | Describes the anatomical location relevant for the event (e.g. BRAIN, LUNG). |
| 15 | BEPARTY | Accountable Party | Char | Record Qualifier | Perm |  |  |  |  | Party accountable for the transferable object (e.g. specimen) as a result of the activity performed in the associated BETERM variable. The party could be an individual (e.g., subject), an organization (e.g., sponsor), or a location that is a proxy for an individual or organization (e.g., site). It is usually a somewhat general term that is further identified in the BEPRTYID variable. |
| 16 | BEPRTYID | Identification of Accountable Party | Char | Record Qualifier | Perm |  |  |  |  | Identification of the specific party accountable for the transferable object (e.g. Specimen) after the action in BETERM is taken. Used in conjunction with BEPARTY. |
| 17 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 18 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. |
| 19 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 20 | BEDTC | Date/Time of Specimen Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date and time of specimen collection. |
| 21 | BESTDTC | Start Date/Time of Biospecimen Event | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Start date/time of the event. |
| 22 | BEENDTC | End Date/Time of Biospecimen Event | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | End date/time of the event. |
| 23 | BESTDY | Study Day of Start of Biospecimen Event | Num | Timing | Perm |  |  |  |  | Actual study day of start of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 24 | BEENDY | Study Day of End of Biospecimen Event | Num | Timing | Perm |  |  |  |  | Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 25 | BEDUR | Duration of Biospecimen Event | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration and unit of a biospecimen event. Used only if collected on the CRF and not derived from start and end date/times. Example: P1DT2H (for 1 day, 2 hours). |
