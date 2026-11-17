# MH — Medical History

**Class:** Events  
**Structure:** One record per medical history event per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | MH | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | MHSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | MHGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | MHREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external medical history identifier. |
| 7 | MHSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Medical History CRF page. |
| 8 | MHTERM | Reported Term for the Medical History | Char | Topic | Req |  |  |  |  | Verbatim or preprinted CRF term for the medical condition or event. |
| 9 | MHMODIFY | Modified Reported Term | Char | Synonym Qualifier | Perm |  |  |  |  | If MHTERM is modified to facilitate coding, then MHMODIFY will contain the modified text. |
| 10 | MHDECOD | Dictionary-Derived Term | Char | Synonym Qualifier | Perm |  |  |  |  | Dictionary-derived text description of MHTERM or MHMODIFY. Equivalent to the Preferred Term (PT in MedDRA). The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. |
| 11 | MHEVDTYP | Medical History Event Date Type | Char | Variable Qualifier | Perm | C124301 |  |  |  | Specifies the aspect of the medical condition or event by which MHSTDTC and/or the MHENDTC is defined. Examples: "DIAGNOSIS", "SYMPTOMS", "RELAPSE", "INFECTION". |
| 12 | MHCAT | Category for Medical History | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. Examples: "CARDIAC", "GENERAL". |
| 13 | MHSCAT | Subcategory for Medical History | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of the condition or event. |
| 14 | MHPRESP | Medical History Event Pre-Specified | Char | Variable Qualifier | Perm | C66742 |  |  |  | A value of "Y" indicates that this medical history event was prespecified on the CRF. Values are null for spontaneously reported events (i.e., those collected as free-text verbatim terms). |
| 15 | MHOCCUR | Medical History Occurrence | Char | Record Qualifier | Perm | C66742 |  |  |  | Used when the occurrence of specific medical history conditions is solicited, to indicate whether ("Y"/"N") a medical condition (MHTERM) had ever occurred. Values are null for spontaneously reported events. |
| 16 | MHSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | The status indicates that the prespecified question was not asked/answered. |
| 17 | MHREASND | Reason Medical History Not Collected | Char | Record Qualifier | Perm |  |  |  |  | Describes the reason why data for a prespecified condition was not collected. Used in conjunction with MHSTAT when value is "NOT DONE". |
| 18 | MHBODSYS | Body System or Organ Class | Char | Record Qualifier | Perm |  |  |  |  | Dictionary-derived. Body system or organ class that is involved in an event or measurement from a standard hierarchy (e.g., MedDRA). When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables which may not necessarily be the primary SOC. |
| 19 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 20 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the medical history event. |
| 21 | MHDTC | Date/Time of History Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Collection date and time of the medical history observation represented in ISO 8601 character format. |
| 22 | MHSTDTC | Start Date/Time of Medical History Event | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Start date/time of the medical history event represented in ISO 8601 character format. |
| 23 | MHENDTC | End Date/Time of Medical History Event | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | End date/time of the medical history event. |
| 24 | MHDY | Study Day of History Collection | Num | Timing | Perm |  |  |  |  | Study day of medical history collection, measured as integer day. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |
| 25 | MHENRF | End Relative to Reference Period | Char | Timing | Perm | C66728 |  |  |  | Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 26 | MHENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the end of the event as being before or after the reference time point defined by variable MHENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 27 | MHENTPT | End Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the reference point referred to by MHENRTPT. Examples: "2003-12-25", "VISIT 2". |
