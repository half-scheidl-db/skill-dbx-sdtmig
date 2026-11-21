# CE — Clinical Events

**Class:** Events  
**Structure:** One record per event per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | CE | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | CESEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | CEGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records for a subject within a domain. |
| 6 | CEREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external identifier (e.g., lab specimen ID, UUID for an ECG waveform or medical image). |
| 7 | CESPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 8 | CETERM | Reported Term for the Clinical Event | Char | Topic | Req |  |  |  |  | Term for the medical condition or event. Most likely preprinted on CRF. |
| 9 | CEDECOD | Dictionary-Derived Term | Char | Synonym Qualifier | Perm |  |  |  |  | Controlled terminology for the name of the clinical event. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. |
| 10 | CECAT | Category for the Clinical Event | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. |
| 11 | CESCAT | Subcategory for the Clinical Event | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of the condition or event. |
| 12 | CEPRESP | Clinical Event Pre-specified | Char | Variable Qualifier | Perm | C66742 |  |  |  | Used to indicate whether the event in CETERM was prespecified. Value is "Y" for prespecified events and null for spontaneously reported events. |
| 13 | CEOCCUR | Clinical Event Occurrence | Char | Record Qualifier | Perm | C66742 |  |  |  | Used when the occurrence of specific events is solicited, to indicate whether or not a clinical event occurred. Values are null for spontaneously reported events. |
| 14 | CESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | The status indicates that a question from a prespecified list was not answered. |
| 15 | CEREASND | Reason Clinical Event Not Collected | Char | Record Qualifier | Perm |  |  |  |  | Describes the reason clinical event data was not collected. Used in conjunction with CESTAT when value is "NOT DONE". |
| 16 | CEBODSYS | Body System or Organ Class | Char | Record Qualifier | Perm |  |  |  |  | Dictionary-derived. Body system or organ class that is involved in an event or measurement from a standard hierarchy (e.g., MedDRA). When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables, which may not necessarily be the primary SOC. |
| 17 | CESEV | Severity/Intensity | Char | Record Qualifier | Perm | C165643 |  |  |  | The severity or intensity of the event. Examples: "MILD", "MODERATE", "SEVERE". |
| 18 | CETOXGR | Standard Toxicity Grade | Char | Record Qualifier | Perm |  |  |  |  | Toxicity grade according to a standard toxicity scale (e.g., Common Terminology Criteria for Adverse Events (CTCAE) v3.0). Sponsor should specify name of the scale and version used in the metadata. If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2"). |
| 19 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the clinical event started. |
| 20 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the clinical event. |
| 21 | CEDTC | Date/Time of Event Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Collection date and time for the clinical event observation represented in ISO 8601 character format. |
| 22 | CESTDTC | Start Date/Time of Clinical Event | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Start date/time of the clinical event represented in ISO 8601 character format. |
| 23 | CEENDTC | End Date/Time of Clinical Event | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | End date/time of the clinical event, represented in ISO 8601 character format. |
| 24 | CEDY | Study Day of Event Collection | Num | Timing | Perm |  |  |  |  | Study day of clinical event collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |
| 25 | CESTDY | Study Day of Start of Event | Num | Timing | Perm |  |  |  |  | Actual study day of start of the clinical event expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 26 | CEENDY | Study Day of End of Event | Num | Timing | Perm |  |  |  |  | Actual study day of end of the clinical event expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 27 | CESTRF | Start Relative to Reference Period | Char | Timing | Perm | C66728 |  |  |  | Describes the start of the clinical event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 28 | CEENRF | End Relative to Reference Period | Char | Timing | Perm | C66728 |  |  |  | Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 29 | CESTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the start of the observation as being before or after the reference time point defined by variable CESTTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 30 | CESTTPT | Start Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by --STRTPT. Examples: "2003-12-15", "VISIT 1". |
| 31 | CEENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the end of the observation as being before or after the sponsor-defined reference time point defined by variable CEENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 32 | CEENTPT | End Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the reference point referred to by CEENRTPT. Examples: "2003-12-25", "VISIT 2". |
