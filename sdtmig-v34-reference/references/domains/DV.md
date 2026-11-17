# DV — Protocol Deviations

**Class:** Events  
**Structure:** One record per protocol deviation per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | DV | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | DVSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | DVREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external identifier. |
| 6 | DVSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page. |
| 7 | DVTERM | Protocol Deviation Term | Char | Topic | Req |  |  |  |  | Verbatim name of the protocol deviation criterion. Example: "IVRS PROCESS DEVIATION - NO DOSE CALL PERFORMED". DVTERM values will map to the controlled terminology in DVDECOD (e.g., "TREATMENT DEVIATION"). |
| 8 | DVDECOD | Protocol Deviation Coded Term | Char | Synonym Qualifier | Perm |  |  |  |  | Controlled terminology for the name of the protocol deviation. Examples: "SUBJECT NOT WITHDRAWN AS PER PROTOCOL", "SELECTION CRITERIA NOT MET", "EXCLUDED CONCOMITANT MEDICATION", "TREATMENT DEVIATION". |
| 9 | DVCAT | Category for Protocol Deviation | Char | Grouping Qualifier | Perm |  |  |  |  | Category of the protocol deviation criterion. |
| 10 | DVSCAT | Subcategory for Protocol Deviation | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of the protocol deviation. |
| 11 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 12 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the deviation. Examples: "TREATMENT", "SCREENING", "FOLLOW-UP". |
| 13 | DVSTDTC | Start Date/Time of Deviation | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Start date/time of deviation represented in ISO 8601 character format. |
| 14 | DVENDTC | End Date/Time of Deviation | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | End date/time of deviation represented in ISO 8601 character format. |
| 15 | DVSTDY | Study Day of Start of Deviation Event | Num | Timing | Perm |  |  |  |  | Study day of start of event relative to the sponsor-defined RFSTDTC. |
| 16 | DVENDY | Study Day of End of Deviation Event | Num | Timing | Perm |  |  |  |  | Study day of end of event relative to the sponsor-defined RFSTDTC. |
