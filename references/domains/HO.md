# HO — Healthcare Encounters

**Class:** Events  
**Structure:** One record per healthcare encounter per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | HO | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | HOSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | HOGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | HOREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external healthcare encounter identifier. |
| 7 | HOSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Healthcare Encounters CRF page. |
| 8 | HOTERM | Healthcare Encounter Term | Char | Topic | Req |  |  |  |  | Verbatim or preprinted CRF term for the healthcare encounter. |
| 9 | HODECOD | Dictionary-Derived Term | Char | Synonym Qualifier | Perm | C171444 |  |  |  | Dictionary or sponsor-defined derived text description of HOTERM or the modified topic variable (HOMODIFY). |
| 10 | HOCAT | Category for Healthcare Encounter | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-related values. |
| 11 | HOSCAT | Subcategory for Healthcare Encounter | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of HOCAT values. |
| 12 | HOPRESP | Pre-Specified Healthcare Encounter | Char | Variable Qualifier | Perm | C66742 |  |  |  | A value of "Y" indicates that this healthcare encounter event was prespecified on the CRF. Values are null for spontaneously reported events (i.e., those collected as free-text verbatim terms). |
| 13 | HOOCCUR | Healthcare Encounter Occurrence | Char | Record Qualifier | Perm | C66742 |  |  |  | Used when the occurrence of specific healthcare encounters is solicited, to indicate whether an encounter occurred. Values are null for spontaneously reported events. |
| 14 | HOSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | The status indicates that the prespecified question was not answered. |
| 15 | HOREASND | Reason Healthcare Encounter Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes the reason data for a prespecified event were not collected. Used in conjunction with HOSTAT when value is "NOT DONE". |
| 16 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 17 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the healthcare encounter. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP". |
| 18 | HODTC | Date/Time of Event Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Collection date and time of the healthcare encounter. |
| 19 | HOSTDTC | Start Date/Time of Healthcare Encounter | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Start date/time of the healthcare encounter (e.g., date of admission). |
| 20 | HOENDTC | End Date/Time of Healthcare Encounter | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | End date/time of the healthcare encounter (e.g., date of discharge). |
| 21 | HODY | Study Day of Event Collection | Num | Timing | Perm |  |  |  |  | Study day of event collection relative to the sponsor-defined RFSTDTC. |
| 22 | HOSTDY | Study Day of Start of Encounter | Num | Timing | Perm |  |  |  |  | Study day of the start of the healthcare encounter relative to the sponsor-defined RFSTDTC. |
| 23 | HOENDY | Study Day of End of Healthcare Encounter | Num | Timing | Perm |  |  |  |  | Study day of the end of the healthcare encounter relative to the sponsor-defined RFSTDTC. |
| 24 | HODUR | Duration of Healthcare Encounter | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration of the healthcare encounter. Used only if collected on the CRF and not derived from the start and end date/times. Example: "P1DT2H" (for 1 day, 2 hours). |
| 25 | HOSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the start of the observation as being before or after the sponsor-defined reference time point defined by variable --STTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 26 | HOSTTPT | Start Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by STRTPT. Examples: "2003-12-15", "VISIT 1". |
| 27 | HOENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the end of the event as being before or after the reference time point defined by variable HOENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 28 | HOENTPT | End Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the reference point referred to by HOENRTPT. Examples: "2003-12-25", "VISIT 2". |
