# SM — Subject Disease Milestones

**Class:** Special-Purpose  
**Structure:** One record per Disease Milestone per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | SM | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SMSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of subject records. Should be assigned to be consistent chronological order. |
| 5 | MIDS | Disease Milestone Instance Name | Char | Topic | Req |  |  |  |  | Name of the specific disease milestone. For types of disease milestones that can occur multiple times, the name will end with a sequence number. Example: "HYPO1". |
| 6 | MIDSTYPE | Disease Milestone Type | Char | Record Qualifier | Req |  |  |  |  | The type of disease milestone. Example: "HYPOGLYCEMIC EVENT". |
| 7 | SMSTDTC | Start Date/Time of Milestone | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Start date/time of milestone instance (if milestone is an intervention or event) or date of milestone (if Milestone is a finding). |
| 8 | SMENDTC | End Date/Time of Milestone | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | End date/time of disease milestone instance. |
| 9 | SMSTDY | Study Day of Start of Milestone | Num | Timing | Exp |  |  |  |  | Study day of start of disease milestone instance, relative to the sponsor-defined RFSTDTC. |
| 10 | SMENDY | Study Day of End of Milestone | Num | Timing | Exp |  |  |  |  | Study day of end of disease milestone instance, relative to the sponsor-defined RFSTDTC. |
