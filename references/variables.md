# SDTMIG v3.4 Variables reference

This file is derived from the uploaded SDTMIG v3.4 workbook. It preserves the workbook metadata in Markdown form.

- Rows: 1917
- Datasets: 63

## AE (Events)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | AE | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |  |  |  | A sequence of characters used by the sponsor to uniquely identify a specific device. Used to represent a device associated in some way with the adverse event. SPDEVID values are defined in the Device Identifiers (DI) domain. |
| 5 | AESEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 6 | AEGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 7 | AEREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external identifier such as a serial number on an SAE reporting form. |
| 8 | AESPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. It may be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on an Adverse Events CRF page. |
| 9 | AETERM | Reported Term for the Adverse Event | Char | Topic | Req |  |  |  |  | Verbatim name of the event. |
| 10 | AEMODIFY | Modified Reported Term | Char | Synonym Qualifier | Perm |  |  |  |  | If AETERM is modified to facilitate coding, then AEMODIFY will contain the modified text. |
| 11 | AELLT | Lowest Level Term | Char | Variable Qualifier | Exp |  |  | MedDRA |  | Dictionary-derived text description of the lowest level term. |
| 12 | AELLTCD | Lowest Level Term Code | Num | Variable Qualifier | Exp |  |  | MedDRA |  | Dictionary-derived code for the lowest level term. |
| 13 | AEDECOD | Dictionary-Derived Term | Char | Synonym Qualifier | Req |  |  | MedDRA |  | Dictionary-derived text description of AETERM or AEMODIFY. Equivalent to the Preferred Term (PT in MedDRA). The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. |
| 14 | AEPTCD | Preferred Term Code | Num | Variable Qualifier | Exp |  |  | MedDRA |  | Dictionary-derived code for the preferred term. |
| 15 | AEHLT | High Level Term | Char | Variable Qualifier | Exp |  |  | MedDRA |  | Dictionary-derived text description of the high level term for the primary system organ class (SOC). |
| 16 | AEHLTCD | High Level Term Code | Num | Variable Qualifier | Exp |  |  | MedDRA |  | Dictionary-derived code for the high level term for the primary SOC. |
| 17 | AEHLGT | High Level Group Term | Char | Variable Qualifier | Exp |  |  | MedDRA |  | Dictionary-derived text description of the high level group term for the primary SOC. |
| 18 | AEHLGTCD | High Level Group Term Code | Num | Variable Qualifier | Exp |  |  | MedDRA |  | Dictionary-derived code for the high level group term for the primary SOC. |
| 19 | AECAT | Category for Adverse Event | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. Examples: "BLEEDING", "NEUROPSYCHIATRIC". |
| 20 | AESCAT | Subcategory for Adverse Event | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of adverse event. Example: "NEUROLOGIC". |
| 21 | AEPRESP | Pre-Specified Adverse Event | Char | Variable Qualifier | Perm | C66742 |  |  |  | A value of "Y" indicates that this adverse event was prespecified on the CRF. Values are null for spontaneously reported events (i.e., those collected as free-text verbatim terms). |
| 22 | AEBODSYS | Body System or Organ Class | Char | Record Qualifier | Exp |  |  |  |  | Dictionary derived. Body system or organ class used by the sponsor from the coding dictionary (e.g., MedDRA). When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables, which may not necessarily be the primary SOC. |
| 23 | AEBDSYCD | Body System or Organ Class Code | Num | Variable Qualifier | Exp |  |  | MedDRA |  | Dictionary derived. Code for the body system or organ class used by the sponsor. When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables, which may not necessarily be the primary SOC. |
| 24 | AESOC | Primary System Organ Class | Char | Variable Qualifier | Exp |  |  | MedDRA |  | Dictionary-derived text description of the primary SOC. Will be the same as AEBODSYS if the primary SOC was used for analysis. |
| 25 | AESOCCD | Primary System Organ Class Code | Num | Variable Qualifier | Exp |  |  | MedDRA |  | Dictionary-derived code for the primary SOC. Will be the same as AEBDSYCD if the primary SOC was used for analysis. |
| 26 | AELOC | Location of Event | Char | Record Qualifier | Perm | C74456 |  |  |  | Describes anatomical location relevant for the event (e.g., "ARM" for skin rash). |
| 27 | AESEV | Severity/Intensity | Char | Record Qualifier | Perm | C66769 |  |  |  | The severity or intensity of the event. Examples: "MILD", "MODERATE", "SEVERE". |
| 28 | AESER | Serious Event | Char | Record Qualifier | Exp | C66742 |  |  |  | Is this a serious event? Valid values are "Y" and "N". |
| 29 | AEACN | Action Taken with Study Treatment | Char | Record Qualifier | Exp | C66767 |  |  |  | Describes changes to the study treatment as a result of the event. AEACN is specifically for the relationship to study treatment. AEACNOTH is for actions unrelated to dose adjustments of study treatment. Examples of AEACN values include ICH E2B values: "DRUG WITHDRAWN", "DOSE REDUCED", "DOSE INCREASED", "DOSE NOT CHANGED", "UNKNOWN" and "NOT APPLICABLE". |
| 30 | AEACNOTH | Other Action Taken | Char | Record Qualifier | Perm |  |  |  |  | Describes other actions taken as a result of the event that are unrelated to dose adjustments of study treatment. Usually reported as free text. Example: "TREATMENT UNBLINDED. PRIMARY CARE PHYSICIAN NOTIFIED". |
| 31 | AEACNDEV | Action Taken with Device | Char | Record Qualifier | Perm | C111110 |  |  |  | An action taken with a device as the result of the event. The device may or may not be a device under study. |
| 32 | AEREL | Causality | Char | Record Qualifier | Exp |  |  |  |  | Records the investigator's opinion as to the causality of the event to the treatment. ICH does not establish any required or recommended terms for non-device relatedness. ICH E2A and E2B examples include (up-cased here for alignment to SDTM conventions) terms such as "NOT RELATED", "UNLIKELY RELATED", "POSSIBLY RELATED", "RELATED", but these example terms do not establish any conventions or expectations. Controlled terminology may be defined in the future. Check with regulatory authority for population of this variable. |
| 33 | AERLDEV | Relationship of Event to Device | Char | Record Qualifier | Perm |  |  |  |  | A judgment as to the likelihood that the device caused the adverse event. The relationship is to a device identified in the data (i.e., has an SPDEVID). The device may be ancillary or under study. \n Terminology: \n * In the EU, follow the European Commission Guidelines on Medical Devices, Clinical Investigations: SAE Reporting (MEDDEV 2.7/3) (e.g., Not Related, Unlikely, Possible, Probable, Causal Relationship), with device-specific definitions. \n * No required Controlled Terminology in US. |
| 34 | AERELNST | Relationship to Non-Study Treatment | Char | Record Qualifier | Perm |  |  |  |  | Records the investigator's opinion as to whether the event may have been due to a treatment other than study drug. May be reported as free text. Example: "MORE LIKELY RELATED TO ASPIRIN USE". |
| 35 | AEPATT | Pattern of Adverse Event | Char | Record Qualifier | Perm |  |  |  |  | Used to indicate the pattern of the event over time. Examples: "INTERMITTENT", "CONTINUOUS", "SINGLE EVENT". |
| 36 | AEOUT | Outcome of Adverse Event | Char | Record Qualifier | Perm | C66768 |  |  |  | Description of the outcome of an event. |
| 37 | AESCAN | Involves Cancer | Char | Record Qualifier | Perm | C66742 |  |  |  | Was the serious event associated with the development of cancer? Valid values are "Y" and "N". This is a legacy seriousness criterion. It is not included in ICH E2A or E2B. |
| 38 | AESCONG | Congenital Anomaly or Birth Defect | Char | Record Qualifier | Perm | C66742 |  |  |  | Was the serious event associated with congenital anomaly or birth defect? Valid values are "Y" and "N". |
| 39 | AESDISAB | Persist or Signif Disability/Incapacity | Char | Record Qualifier | Perm | C66742 |  |  |  | Did the serious event result in persistent or significant disability/incapacity? Valid values are "Y" and "N". |
| 40 | AESDTH | Results in Death | Char | Record Qualifier | Perm | C66742 |  |  |  | Did the serious event result in death? Valid values are "Y" and "N". |
| 41 | AESHOSP | Requires or Prolongs Hospitalization | Char | Record Qualifier | Perm | C66742 |  |  |  | Did the serious event require or prolong hospitalization? Valid values are "Y" and "N". |
| 42 | AESLIFE | Is Life Threatening | Char | Record Qualifier | Perm | C66742 |  |  |  | Was the serious event life-threatening? Valid values are "Y" and "N". |
| 43 | AESOD | Occurred with Overdose | Char | Record Qualifier | Perm | C66742 |  |  |  | Did the serious event occur with an overdose? Valid values are "Y" and "N". This is a legacy seriousness criterion. It is not included in ICH E2A or E2B. |
| 44 | AESMIE | Other Medically Important Serious Event | Char | Record Qualifier | Perm | C66742 |  |  |  | Do additional categories for seriousness apply? Valid values are "Y" and "N". |
| 45 | AESINTV | Needs Intervention to Prevent Impairment | Char | Record Qualifier | Perm | C66742 |  |  |  | Records whether medical or surgical intervention was necessary to preclude permanent impairment of a body function, or to prevent permanent damage to a body structure, with either situation suspected to be due to the use of a medical product. This variable is used in conjunction with the other "seriousness" variables (e.g., fatal, life-threatening). It is part of the US federal government definition of a serious adverse event; see 21 CFR Part 803.3(w)(3). |
| 46 | AEUNANT | Unanticipated Adverse Device Effect | Char | Record Qualifier | Perm | C66742 |  |  |  | Any serious adverse effect on health or safety or any life-threatening problem or death caused by or associated with a device, if that effect, problem, or death was not previously identified in nature, severity, or degree of incidence in the investigational plan or application (including a supplementary plan or application), \n or \n any other unanticipated serious problem associated with a device that relates to the rights, safety, or welfare of subjects. (21 CFR Part 812.3(s)). \n This variable applies only to serious AEs and should hold collected data; if the value is derived, it should be held in ADaM. |
| 47 | AERLPRT | Rel of AE to Non-Dev-Rel Study Activity | Char | Record Qualifier | Perm |  |  |  |  | The investigator's opinion as to the causality of the event as related to other protocol-required activities, actions, or assessments (e.g., medication changes, tests/assessments, other procedures). The relationship is to a protocol-specified, non-device-related activity where the device is identified in the data (i.e., has an SPDEVID). The device may be ancillary or under study. \n Terminology: \n * In the EU, follow the European Commission Guidelines on Medical Devices, Clinical Investigations: SAE Reporting (MEDDEV 2.7/3) (e.g., Not Related, Unlikely, Possible, Probable, Causal Relationship), with device-specific definitions. \n * No required Controlled Terminology in US. |
| 48 | AERLPRC | Rel of AE to Device-Related Procedure | Char | Record Qualifier | Perm |  |  |  |  | The investigator's opinion as to the likelihood that the device-related study procedure (e.g., implant/insertion, revision/adjustment, explant/removal) caused the AE. The relationship is to a device-related procedure where the device is identified in the data (i.e., has an SPDEVID). The device may be ancillary or under study. \n Terminology: \n * In the EU, follow the European Commission Guidelines on Medical Devices, Clinical Investigations: SAE Reporting (MEDDEV 2.7/3) (e.g., Not Related, Unlikely, Possible, Probable, Causal Relationship), with device-specific definitions. \n * No required Controlled Terminology in US. |
| 49 | AECONTRT | Concomitant or Additional Trtmnt Given | Char | Record Qualifier | Perm | C66742 |  |  |  | Was another treatment given because of the occurrence of the event? Valid values are "Y" and "N". |
| 50 | AETOXGR | Standard Toxicity Grade | Char | Record Qualifier | Perm |  |  |  |  | Toxicity grade according to a standard toxicity scale (e.g., Common Terminology Criteria for Adverse Events, CTCAE). Sponsors should specify the name of the scale and version used in the metadata (see assumption 7d). If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2"). |
| 51 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 52 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the adverse event. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP". |
| 53 | AESTDTC | Start Date/Time of Adverse Event | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Start date/time of the adverse event represented in ISO 8601 character format. |
| 54 | AEENDTC | End Date/Time of Adverse Event | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | End date/time of the adverse event represented in ISO 8601 character format. |
| 55 | AESTDY | Study Day of Start of Adverse Event | Num | Timing | Perm |  |  |  |  | Study day of start of adverse event relative to the sponsor-defined RFSTDTC. |
| 56 | AEENDY | Study Day of End of Adverse Event | Num | Timing | Perm |  |  |  |  | Study day of end of event relative to the sponsor-defined RFSTDTC. |
| 57 | AEDUR | Duration of Adverse Event | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration and unit of an adverse event. Used only if collected on the CRF and not derived from start and end date/times. Example: "P1DT2H" (for 1 day, 2 hours). |
| 58 | AEENRF | End Relative to Reference Period | Char | Timing | Perm | C66728 |  |  |  | Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point (RFSTDTC) and a discrete ending point (RFENDTC) of the trial. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 59 | AEENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the end of the event as being before or after the reference time point defined by variable AEENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 60 | AEENTPT | End Reference Time Point | Char | Timing | Perm |  |  |  |  | Description of date/time in ISO 8601 character format of the reference point referred to by AEENRTPT. Examples: "2003-12-25", "VISIT 2". |

## BE (Events)

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

## CE (Events)

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

## DS (Events)

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

## DV (Events)

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

## HO (Events)

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

## MH (Events)

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

## BS (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | BS | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier for a device. |
| 5 | BSSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| 6 | BSGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 7 | BSREFID | Reference ID | Char | Identifier | Exp |  |  |  |  | Internal or external identifier such as lab specimen ID. |
| 8 | BSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 9 | BSTESTCD | Biospecimen Test Short Name | Char | Topic | Req | C124300 |  |  |  | Short character value for BSTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Examples: VOLUME, RIN. |
| 10 | BSTEST | Biospecimen Test Name | Char | Synonym Qualifier | Req | C124299 |  |  |  | Long name for BSTESTCD. Examples: Volume, RNA Integrity Number. |
| 11 | BSCAT | Category for Biospecimen Test | Char | Grouping Qualifier | Exp |  |  |  |  | Used to define a category of topic-variable values. Example: MEASUREMENT, QUALITY. |
| 12 | BSSCAT | Subcategory for Biospecimen Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of BSCAT values. |
| 13 | BSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 14 | BSORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Unit for BSORRES. Examples: mg, mL. |
| 15 | BSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from BSORRES in a standard format or standard units. BSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in BSSTRESN. |
| 16 | BSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from BSSTRESC. BSSTRESN should store all numeric test results or findings. |
| 17 | BSSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Standardized unit used for BSSTRESC and BSSTRESN. |
| 18 | BSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a test was not done, or was attempted but did not generate a result. Should be null or have a value of NOT DONE. |
| 19 | BSREASND | Reason Test Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with BSSTAT when value is NOT DONE. |
| 20 | BSNAM | Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the vendor (e.g., laboratory) that provided the test results. |
| 21 | BSSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734; C111114 |  |  |  | Defines the type of specimen used for a measurement. Examples: SERUM, PLASMA, URINE, SOFT TISSUE. |
| 22 | BSANTREG | Anatomical Region of Specimen | Char | Variable Qualifier | Perm |  |  |  |  | Defines the specific anatomical or biological region of a tissue, organ specimen or the region from which the specimen is obtained, as defined in the protocol, such as a section or part of what is described in the BSSPEC variable. Examples: CORTEX, MEDULLA, MUCOSA. |
| 23 | BSSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |  |  |  | Defines the condition of the specimen. Examples: HEMOLYZED, ICTERIC, LIPEMIC. |
| 24 | BSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: SPECTROPHOTOMETRY, ELECTROPHORESIS. |
| 25 | BSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. |
| 26 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 27 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. |
| 28 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 29 | BSDTC | Date/Time of Specimen Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date and time of specimen collection. |
| 30 | BSDY | Study Day of Specimen Collection | Num | Timing | Perm |  |  |  |  | Study day of specimen collection relative to the sponsor-defined RFSTDTC. |
| 31 | BSTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See BSTPTNUM and BSTPTREF. |
| 32 | BSTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of BSTPT used in sorting. |
| 33 | BSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Elapsed time relative to a planned fixed reference (BSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration. |
| 34 | BSTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by BSELTM, BSTPTNUM, and BSTPT. Examples: PREVIOUS DOSE, PREVIOUS MEAL. |
| 35 | BSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by BSTPTREF. |

## CP (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | CP | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | CPSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | CPGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | CPREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external specimen identifier. |
| 7 | CPSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the lab page. |
| 8 | CPLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 9 | CPLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 10 | CPTESTCD | Test or Examination Short Name | Char | Topic | Req | C181173 |  |  |  | Short name of the measurement, test, or examination described in CPTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in CPTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). CPTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MONO", "MNS". |
| 11 | CPTEST | Name of Measurement, Test or Examination | Char | Synonym Qualifier | Req | C181174 |  |  |  | Long name for CPTESTCD. For cell phenotyping, the name (often abbreviated) of the cell population, as it is generally accepted by the scientific community, is populated (rather than a colloquial designation based on a primary marker, e.g., TLym Help rather than CD4). When the test is for a sublineage which can only be identified by specifying additional markers (i.e., has not been given a name) or which is further restricted to a subpopulation based on a particular cell state (e.g., activated, proliferating, apoptotic), the Sublineage Marker String (CPSBMRKS), Cell State (CPCELSTA), and Cell State Marker String (CPCSMRKS) variables are additionally populated and the value in CPTEST is suffixed with "Sub" to denote that it is a subset of the population identified in CPTEST (e.g., Monocytes Sub). \n The value in CPTEST cannot be longer than 40 characters. |
| 12 | CPSBMRKS | Sublineage Marker String | Char | Variable Qualifier | Perm |  |  |  |  | Used to further subset the cell population identified in CPTEST based on the use of additional marker(s) that define a sublineage. The value in CPSBMRKS is used in combination with values in CPTEST and CPCELSTA to fully describe the cell population being measured. As such, it is an essential component of the full test name. \n For example, three unnamed sublineages of monocytes have been identified as: CCR2+CD16-, CCR2-CD16+, and CCR2+CD16+. Whereas the entire monocyte cell population can be defined as CD14+ cells, the additional CCR2 and CD16 markers are used to differentiate one sublineage from another. As none of these sublineages have been given names, they are only known by the CCR2 and CD16 marker combinations. By associating the CPTEST value of "Monocytes Sub" with, for example, a value of "CCR2+CD16-" in CPSBMRKS, the full test is defined to be the CCR2+CD16- monocyte subpopulation. |
| 13 | CPCELSTA | Cell State | Char | Variable Qualifier | Perm | C181172 |  |  |  | A textual description of a subset of the cell population identified in CPTEST based on a particular functional and/or biological state (e.g., "ACTIVATED", "PROLIFERATING", "SENESCENT"). When populated, the values in CPCELSTA and CPSMRKS, in combination with the values in CPTEST and CPSBMRKS, fully describe the cell population being measured. |
| 14 | CPCSMRKS | Cell State Marker String | Char | Variable Qualifier | Perm |  |  |  |  | Identifies the marker(s) or indicator(s) used to define the cell state (i.e., the value in CPCELSTA). \n For example, when Ki67 expression is used to determine that a cell population is in a proliferating state (i.e., CPCELSTA value="PROLIFERATING"), the value "Ki67+" in CPCSMRKS indicates that positive expression of Ki67 was used to define the population as proliferating. Similarly, a value of "Ki67-" in CPCSMRKS would indicate that lack of expression of Ki67 defined the "NON-PROLIFERATING" cell state in CPCELSTA. The CPCSMRKS value is useful for quickly determining which marker(s) were used to classify (i.e., operationally define) a cell population based on a functional/biological state. |
| 15 | CPTSTCND | Test Condition | Char | Variable Qualifier | Perm | C181175 |  |  |  | Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed. --TSTCND is generally used to distinguish between two or more records where the same assay is performed under varying (as opposed to fixed) conditions, usually for the purpose of making a comparison. For example, when the same assay (identified in --TEST) is performed under stimulated and non-stimulated conditions, the --TSTCND variable is used distinguish between the records. |
| 16 | CPCNDAGT | Test Condition Agent | Char | Record Qualifier | Perm |  |  |  |  | The textual description of the agent, if applicable, used to impose the condition identified in CPTSTCND. For example, records might be produced for the same assay run under stimulating (CPTSTCND value = "STIMULATED") conditions produced by different stimulating agents (e.g., phorbol myristate acetate, concanavalin A, PHA-P, TNF-alpha, Ionomycin, candida antigen). |
| 17 | CPBDAGNT | Binding Agent | Char | Record Qualifier | Perm |  |  |  |  | The textual description of the agent that is binding to the entity in the CPTEST variable. The CPBDAGNT variable is used to indicate that there is a binding relationship between the entities in the CPTEST and CPBDAGNT variables, regardless of direction. \n The binding agent may be, but is not limited to, a test article; a portion of a test article; a substance related to a test article; an endogenous molecule; an allergen; an infectious agent; or a reagent (e.g., primary antibody) that confers the binding specificity for the measurement defined in CPTEST when it is needed to uniquely identify the test. |
| 18 | CPABCLID | Antibody Clone Identifier | Char | Record Qualifier | Perm |  |  |  |  | Identifies the antibody clone (e.g., supplier-provided catalog name) used to confer specificity for the binding agent specified in CPBDAGNT. |
| 19 | CPMRKSTR | Marker String | Char | Record Qualifier | Exp |  |  |  |  | The text string identifying the full set of markers/indicators used by the laboratory to operationally define the complete test based on the combination of CPTEST, CPSBMRKS, and CPCELSTA. Because laboratories often use different markers/indicators to identify a cell population, the relationship between a named cell population in CPTEST (as combined with CPSBMRKS and CPCELSTA values) and the set of markers used to identify that population is many-to-one. To ensure nuances important for accurately interpreting the data are accounted for and which arise from the use of different sets of markers, it is necessary to operationally define the test in terms of the complete set of markers/indicators used to perform that test. |
| 20 | CPGATE | Gate | Char | Record Qualifier | Perm |  |  |  |  | The sponsor-defined name assigned to a gate. Gates are electronic (i.e., a device setting or software-defined) boundaries set by a user to virtually parse a specimen into discrete populations based on a set of defined characteristics (e.g., presence, absence, or intensity of expression of various markers; physical size; internal complexity or granularity). Gates are used to constrain data collection or analysis to a specific cell population or region of interest within the specimen. |
| 21 | CPGATDEF | Gate Definition | Char | Record Qualifier | Perm |  |  |  |  | The text string identifying the set of parameters and the order in which they are applied to define the gating strategy. In practice, a series of 2-dimensional sub-gates based on different cell characteristics (i.e., markers/indicators/physical properties) are most often combined until the cell population of interest is sufficiently resolved (i.e., electronically isolated) from other cell populations contained within the specimen. \n For complex analyses, differences in gating strategies can produce subtle differences in results obtained for a test. To ensure nuances important for accurately interpreting the data are accounted for and which arise from the use of different gating strategies, it is often necessary to qualify the test in terms of the gating strategy. For some purposes, however, and at the discretion of the sponsor, only the ultimate or penultimate gate is identified. When specifying the gating strategy in CPGATDEF, each sub-gate should be listed in the order it was applied and separated from the next sub-gate using the pipe/vertical line ("\|") character. |
| 22 | CPSPTSTD | Sponsor Test Description | Char | Record Qualifier | Perm |  |  |  |  | Sponsor's description of a test. The variable is intended to contain highly structured test description metadata used by a sponsor to unambiguously define (label) a test. Such values generally reside in a sponsor/laboratory test metadata repository. CPSPTSTD is not intended for unstructured (spontaneous) free text. \n An example of appropriate usage is when it is necessary to include identifying information for a target cell population on which a test is conducted when the target population is not part of the test name, e.g., tests for quantitative expression of a particular marker on a specific cell population. |
| 23 | CPCAT | Category | Char | Grouping Qualifier | Perm | C181171 |  |  |  | Used to define a category of topic-variable values across subjects. Examples: "IMMUNOPHENOTYPING", "CELL FUNCTION", "TARGET ENGAGEMENT". |
| 24 | CPSCAT | Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of CPCAT. |
| 25 | CPTSTPNL | Test Panel | Char | Grouping Qualifier | Perm |  |  |  |  | Sponsor-defined textual description used to group tests run together as part of a test panel. Can be used with --GRPID to ensure that relationships between associated tests are accurately identified. |
| 26 | CPORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 27 | CPORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. The unit for CPORRES. Examples: "10^6/L", "%", "MESF". |
| 28 | CPRESSCL | Result Scale | Char | Record Qualifier | Perm | C177910 |  |  |  | Classifies the scale of the original result value with respect to whether the result is quantitative, ordinal, nominal, or narrative. |
| 29 | CPRESTYP | Result Type | Char | Record Qualifier | Perm | C179588 |  |  |  | Classifies the kind of result (i.e., property type) originally reported for the test. Examples: "NUMBER CONCENTRATION", "NUMBER FRACTION", "RATIO". |
| 30 | CPCOLSRT | Collected Summary Result Type | Char | Record Qualifier | Perm | C177908 |  |  |  | Used to indicate the type of collected summary result. This includes source summary results collected on a CRF or provided by an external vendor (e.g., central lab). If the summary result is derived using individual source data records, this summary result should be represented in ADaM. If a sponsor has both a collected summary result and a derived summary result, the collected summary result should be represented in SDTM and the derived summary result should be represented in ADaM. |
| 31 | CPORNRLO | Reference Range Lower Limit in Orig Unit | Char | Variable Qualifier | Perm |  |  |  |  | Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results. |
| 32 | CPORNRHI | Reference Range Upper Limit in Orig Unit | Char | Variable Qualifier | Perm |  |  |  |  | Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results. |
| 33 | CPSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from CPORRES in a standard format or in standard units. CPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in CPSTRESN. |
| 34 | CPSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from CPSTRESC. CPSTRESN should store all numeric test results or findings. |
| 35 | CPSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized unit used for CPSTRESC or CPSTRESN. |
| 36 | CPSTNRLO | Reference Range Lower Limit-Std Units | Num | Variable Qualifier | Perm |  |  |  |  | Lower end of reference range for continuous measurements for CPSTRESC/CPSTRESN in standardized units. Should be populated only for continuous results. |
| 37 | CPSTNRHI | Reference Range Upper Limit-Std Units | Num | Variable Qualifier | Perm |  |  |  |  | Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results. |
| 38 | CPNRIND | Reference Range Indicator | Char | Variable Qualifier | Perm | C78736 |  |  |  | Indicates where the value falls with respect to reference range defined by CPORNRLO and CPORNRHI, CPSTNRLO and CPSTNRHI, or by CPSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether CPNRIND refers to the original or standard reference ranges and results. CPNRIND should not be used to indicate clinical significance. |
| 39 | CPSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that the test was not performed or that it was attempted but did not generate a result. Should be null if a result exists in CPORRES. |
| 40 | CPREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a test was not performed, e.g., "BROKEN EQUIPMENT", "SUBJECT REFUSED", "SPECIMEN LOST". Used in conjunction with CPSTAT when value is "NOT DONE". |
| 41 | CPNAM | Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | The name or identifier of the laboratory that performed the test. |
| 42 | CPLOINC | LOINC Code | Char | Synonym Qualifier | Perm |  |  | LOINC |  | Code for the test from the LOINC code system. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the Define-XML external codelist attributes. |
| 43 | CPSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734 |  |  |  | Defines the type of specimen used for a measurement. Examples: "BLOOD", "BONE MARROW". |
| 44 | CPSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |  |  |  | The physical state or quality of a specimen for an assessment. Example: "CLOTTED". |
| 45 | CPMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Example: "FLOW CYTOMETRY". |
| 46 | CPANMETH | Analysis Method | Char | Record Qualifier | Perm |  |  |  |  | Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result. |
| 47 | CPLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 48 | CPBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. The value should be "Y" or null. |
| 49 | CPDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or do not come from the CRF, or are not as originally received or collected are examples of records that might be derived for the submission datasets. If CPDRVFL = "Y", then CPORRES may be null, with CPSTRESC and (if numeric) CPSTRESN having the derived value. |
| 50 | CPCLSIG | Clinically Significant, Collected | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate whether a collected observation is clinically significant based on judgement. |
| 51 | VISITNUM | Visit Number | Num | Timing | Perm |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 52 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 53 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. Should be an integer. |
| 54 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 55 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected. |
| 56 | CPDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of specimen collection represented in ISO 8601 character format. |
| 57 | CPDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Study day of specimen collection, measured in integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC value in Demographics. |
| 58 | CPTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a specimen is to be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (i.e., to the value in CPTPTREF). Example: "1 hour post". |
| 59 | CPTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of CPTPT to aid in sorting. When CPTPT is represented as an elapsed time relative to a fixed reference point (i.e., to the value in CPTPTREF), the values in CPTPTNUM should be assigned in ascending order relative to the value in CPTPTREF. For example, records for time points where CPTPT = "5 minutes post", 1 hour post", and "4 hours post" could be represented in CPTPTNUM as "1", "2", and "3", which maintains the order between CPTPT and CPTPTNUM with respect to the fixed time point reference in CPTPTREF. |
| 60 | CPELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to the planned fixed reference value in CPTPTREF, represented in ISO 8601 duration format. Examples: "-PT15M" to represent 15 minutes prior to the reference time point indicated by CPTPTREF, "T8H" to represent 8 hours after the reference time point represented by CPTPTREF. |
| 61 | CPTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Descriptive name of the fixed reference point referred to by CPTPT, CPTPTNUM, and CPELTM. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 62 | CPRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by CPTPTREF. |

## CV (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | CV | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | CVSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| 5 | CVGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 6 | CVREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external identifier. |
| 7 | CVSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. Example: a preprinted line identifier on a CRF. |
| 8 | CVLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 9 | CVLNKGRP | Link Group | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 10 | CVTESTCD | Short Name of Cardiovascular Test | Char | Topic | Req | C101847 |  |  |  | Short name of the measurement, test, or examination described in CVTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in CVTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" would not be valid). CVTESTCD cannot contain characters other than letters, numbers, or underscores. |
| 11 | CVTEST | Name of Cardiovascular Test | Char | Synonym Qualifier | Req | C101846 |  |  |  | Long name For CVTESTCD. The value in CVTEST cannot be longer than 40 characters. |
| 12 | CVCAT | Category for Cardiovascular Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. |
| 13 | CVSCAT | Subcategory for Cardiovascular Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of CVCAT values. |
| 14 | CVPOS | Position of Subject During Observation | Char | Record Qualifier | Perm | C71148 |  |  |  | Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING". |
| 15 | CVORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 16 | CVORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. Unit for CVORRES. |
| 17 | CVSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived, from CVORRES in a standard format or in standard units. CVSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in CVSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in CVORRES and these results effectively have the same meaning, they could be represented in standard format in CVSTRESC as "NEGATIVE". |
| 18 | CVSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from CVSTRESC. CVSTRESN should store all numeric test results or findings. |
| 19 | CVSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for CVSTRESC and CVSTRESN. |
| 20 | CVSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 21 | CVREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a measurement or test was not performed (e.g., "BROKEN EQUIPMENT", "SUBJECT REFUSED"). Used in conjunction with CVSTAT when value is "NOT DONE". |
| 22 | CVLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. Examples: "HEART", "LEFT VENTRICLE". |
| 23 | CVLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL", "UNILATERAL". |
| 24 | CVDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 25 | CVMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method used to create the result. |
| 26 | CVLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 27 | CVBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that CVBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 28 | CVDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (i.e., a record that represents the average of other records, such as a computed baseline). Should be "Y" or null. |
| 29 | CVEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", " INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| 30 | CVEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in CVEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2". |
| 31 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 32 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 33 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 36 | CVDTC | Date/Time of Test | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of an observation. |
| 37 | CVDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 38 | CVTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See CVTPTNUM and CVTPTREF. |
| 39 | CVTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 40 | CVELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to a planned fixed reference (CVTPTREF). Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 41 | CVTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by CVELTM, CVTPTNUM, and CVTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 42 | CVRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by CVTPTREF. |

## DA (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study within the submission. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | DA | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | DASEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | DAGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | DAREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external identifier such as a code from the product packaging (e.g., bottle label, package label, kit label). |
| 7 | DASPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Examples: Line number on the Product Accountability CRF page, a code from the product packaging (e.g., bottle label, package label, kit label). |
| 8 | DALNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 9 | DALNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 10 | DATESTCD | Short Name of Accountability Assessment | Char | Topic | Req | C78732 |  |  |  | Short character value for DATEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters and cannot begin with a number or contain characters other than letters, numbers, or underscores. Examples: "DISPAMT", "RETAMT". |
| 11 | DATEST | Name of Accountability Assessment | Char | Synonym Qualifier | Req | C78731 |  |  |  | Verbatim name corresponding to the topic variable of the test or examination used to obtain the product accountability assessment. The value in DATEST cannot be longer than 40 characters. Examples: "Dispensed Amount", "Returned Amount". |
| 12 | DACAT | Category | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. Examples: "STUDY MEDICATION", "RESCUE MEDICATION". |
| 13 | DASCAT | Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization level for a group of related records. |
| 14 | DAORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the product accountability assessment as originally received or collected. |
| 15 | DAORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Unit for DAORRES. |
| 16 | DASTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all product accountability assessments copied or derived from DAORRES, in a standard format or in standard units. DASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in DASTRESN. |
| 17 | DASTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from DASTRESC. DASTRESN should store all numeric test results or findings. |
| 18 | DASTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for DASTRESC and DASTRESN. |
| 19 | DASTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a product accountability assessment was not done. Should be null or have a value of "NOT DONE". |
| 20 | DAREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with DASTAT when value is "NOT DONE". |
| 21 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 22 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 23 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit, based upon RFSTDTC in Demographics. |
| 24 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm (see Section 7.2.1, Trial Arms). |
| 25 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected. |
| 26 | DADTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date and time of the product accountability assessment represented in ISO 8601 character format. |
| 27 | DADY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Study day of product accountability assessment, measured in integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC in Demographics. |

## DD (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | DD | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | DDSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | DDTESTCD | Death Detail Assessment Short Name | Char | Topic | Req | C116108 |  |  |  | Short name of the measurement, test, or examination described in DDTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in DDTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). DDTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRCDTH", "SECDTH". |
| 6 | DDTEST | Death Detail Assessment Name | Char | Synonym Qualifier | Req | C116107 |  |  |  | Long name for DDTESTCD. The value in DDTEST cannot be longer than 40 characters. Examples: "Primary Cause of Death", "Secondary Cause of Death". |
| 7 | DDORRES | Result or Finding as Collected | Char | Result Qualifier | Exp |  |  |  |  | Result of the test defined in DDTEST, as originally received or collected. |
| 8 | DDSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result or finding copied or derived from DDORRES in a standard format. |
| 9 | DDRESCAT | Result Category | Char | Variable Qualifier | Perm |  |  |  |  | Used to categorize the result of a finding. Examples: "TREATMENT RELATED", "NONTREATMENT RELATED", "UNDETERMINED", "ACCIDENTAL". |
| 10 | DDEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. |
| 11 | DDDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of collection of the diagnosis or other death assessment data in ISO 8601 format. This is not necessarily the date of death. |
| 12 | DDDY | Study Day of Collection | Num | Timing | Perm |  |  |  |  | Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. |

## EG (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | EG | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier for a device. |
| 5 | EGSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 6 | EGGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 7 | EGREFID | ECG Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external ECG identifier. Example: "334PT89". |
| 8 | EGSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be printed on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the ECG page. |
| 9 | EGBEATNO | ECG Beat Number | Num | Identifier | Perm |  |  |  |  | A sequence number that identifies the beat within an ECG. |
| 10 | EGTESTCD | ECG Test or Examination Short Name | Char | Topic | Req | C71153; C120523 |  |  |  | Short name of the measurement, test, or examination described in EGTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in EGTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). EGTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRAG", "QRSAG". \n Test codes are in 2 separate codelists, 1 for tests based on regular 10-second ECGs (EGTESTCD) and one 1 tests based on Holter monitoring (HETESTCD). |
| 11 | EGTEST | ECG Test or Examination Name | Char | Synonym Qualifier | Req | C71152; C120524 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in EGTEST cannot be longer than 40 characters. Examples: "PR Interval, Aggregate", "QRS Duration, Aggregate". \n Test names are in 2 separate codelists, 1 for tests based on regular 10-second ECGs (EGTEST) and 1 for tests based on Holter monitoring (HETEST). |
| 12 | EGCAT | Category for ECG | Char | Grouping Qualifier | Perm |  |  |  |  | Used to categorize ECG observations across subjects. Examples: "MEASUREMENT", "FINDING", "INTERVAL". |
| 13 | EGSCAT | Subcategory for ECG | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of the ECG. |
| 14 | EGPOS | ECG Position of Subject | Char | Record Qualifier | Perm | C71148 |  |  |  | Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING". |
| 15 | EGORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the ECG measurement or finding as originally received or collected. Examples of expected values are "62" or "0.151" when the result is an interval or measurement, or "ATRIAL FIBRILLATION" or "QT PROLONGATION" when the result is a finding. |
| 16 | EGORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. The unit for EGORRES. Examples: "sec", "msec". |
| 17 | EGSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C71150; C120522; C101834 |  |  |  | Contains the result value for all findings copied or derived from EGORRES, in a standard format or standard units. EGSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in EGSTRESN. For example, if a test has results of 62 beats/min, then EGORRES = "62", EGORRESU = "beats/min", EGSTRESC = "62", EGSTRESN = 62, and EGSTRESU = "beats/min" . For other examples, see Original and Standardized Results. Additional examples of result data: "SINUS BRADYCARDIA", "ATRIAL FLUTTER", "ATRIAL FIBRILLATION". \n Test results are in 3 separate codelists: EGSTRESC for abnormal test results based on regular 10-second ECGs; HESTRESC for abnormal test results based on Holter monitoring, and NORMABNM for generic test results and/or responses to EGTEST = "Interpretation". |
| 18 | EGSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from EGSTRESC. EGSTRESN should store all numeric test results or findings. |
| 19 | EGSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for EGSTRESC and EGSTRESN. |
| 20 | EGSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate an ECG was not done, or an ECG measurement was not taken. Should be null if a result exists in EGORRES. |
| 21 | EGREASND | Reason ECG Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with EGSTAT when value is "NOT DONE". |
| 22 | EGXFN | ECG External File Path | Char | Record Qualifier | Perm |  |  |  |  | File name and path for the external ECG waveform file. |
| 23 | EGNAM | Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the laboratory or vendor providing the test results. |
| 24 | EGMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C71151 |  |  |  | Method of the ECG test. Example: "12-LEAD STANDARD". |
| 25 | EGLEAD | Lead Location Used for Measurement | Char | Record Qualifier | Perm | C90013 |  |  |  | The lead used for the measurement. Examples: "LEAD 1", "LEAD 2", "LEAD rV2", "LEAD V1". |
| 26 | EGLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 27 | EGBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that EGBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 28 | EGDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or that do not come from the CRF, or are not as originally collected or received are examples of records that would be derived for the submission datasets. If EGDRVFL="Y", then EGORRES could be null, with EGSTRESC and EGSTRESN (if the result is numeric) having the derived value. |
| 29 | EGEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR". |
| 30 | EGEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in EGEVAL. Examples: "RADIOLOGIST 1" or "RADIOLOGIST 2". |
| 31 | EGCLSIG | Clinically Significant, Collected | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate whether a collected observation is clinically significant based on judgment. |
| 32 | EGREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |  |  |  | The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample. |
| 33 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 34 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 35 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 36 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 37 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 38 | EGDTC | Date/Time of ECG | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/Time of ECG. |
| 39 | EGDY | Study Day of ECG | Num | Timing | Perm |  |  |  |  | Study day of the ECG, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| 40 | EGTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See EGTPTNUM and EGTPTREF. Examples: "Start", "5 min post". |
| 41 | EGTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of EGTPT to aid in sorting. |
| 42 | EGELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to a fixed time point reference (EGTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by EGTPTREF. |
| 43 | EGTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by EGELTM, EGTPTNUM, and EGTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 44 | EGRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by EGTPTREF. |

## FT (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | FT | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | FTSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number. |
| 5 | FTGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 6 | FTREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external identifier. |
| 7 | FTSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the Test page. |
| 8 | FTTESTCD | Short Name of Test | Char | Topic | Req |  |  |  |  | Short character value for FTTEST, which can be used as a column name when converting a dataset from a vertical format to a horizontal format. The value cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). FTTESTCD cannot contain characters other than letters, numbers, or underscores. \n Controlled terminology for FTTESTCD is published in separate codelists for each instrument. See https://www.cdisc.org/standards/terminology/controlled-terminology for values for FTTESTCD. Examples: "W250101", "W25F0102". |
| 9 | FTTEST | Name of Test | Char | Synonym Qualifier | Req |  |  |  |  | Verbatim name of the question used to obtain the finding. The value in FTTEST cannot be longer than 40 characters. \n Controlled terminology for FTTEST is published in separate codelists for each instrument. See https://www.cdisc.org/standards/terminology/controlled-terminology for values for FTTEST. Examples: "W2501-25 Foot Walk Time", "W25F-More Than Two Attempts". |
| 10 | FTCAT | Category | Char | Grouping Qualifier | Req | C115304 |  |  |  | Used to specify the functional test in which the functional test question identified by FTTEST and FTTESTCD was included. |
| 11 | FTSCAT | Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of FTCAT values. |
| 12 | FTPOS | Position of Subject During Observation | Char | Record Qualifier | Perm | C71148 |  |  |  | Position of the subject during the test. Examples: "SUPINE", "STANDING", "SITTING". |
| 13 | FTORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 14 | FTORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. Unit for FTORRES. |
| 15 | FTSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from FTORRES in a standard format or in standard units. FTSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in FTSTRESN. |
| 16 | FTSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from FTSTRESC. FTSTRESN should store all numeric test results or findings. |
| 17 | FTSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for FTSTRESC and FTSTRESN. |
| 18 | FTSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 19 | FTREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a test was not done, or a test was attempted but did not generate a result. Used in conjunction with FTSTAT when value is "NOT DONE". |
| 20 | FTXFN | External File Path | Char | Record Qualifier | Perm |  |  |  |  | File path to an external file. |
| 21 | FTNAM | Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the vendor or laboratory that provided the test results. |
| 22 | FTMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C158113 |  |  |  | Method of the test or examination. |
| 23 | FTLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 24 | FTBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | A baseline defined by the sponsor (could be derived in the same manner as FTLOBXFL or ABLFL, but is not required to be). The value should be "Y" or null. Note that FTBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 25 | FTDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 26 | FTREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |  |  |  | The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample. |
| 27 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 28 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 29 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT based upon RFSTDTC in Demographics. Should be an integer. |
| 30 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 31 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the observation date/time of the functional tests finding. |
| 32 | FTDTC | Date/Time of Test | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of functional test. |
| 33 | FTDY | Study Day of Test | Num | Timing | Perm |  |  |  |  | Actual study day of test expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 34 | FTTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See FTTPTNUM and FTTPTREF. |
| 35 | FTTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 36 | FTELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to a planned fixed reference (FTTPTREF). Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 37 | FTTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by FTELTM, FTTPTNUM, and FTTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 38 | FTRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by FTTPTREF. |

## GF (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | GF | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier for a device. |
| 5 | NHOID | Non-Host Organism Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears. |
| 6 | GFSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| 7 | GFGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records within a subject in a domain. |
| 8 | GFREFID | Reference ID | Char | Identifier | Exp |  |  |  |  | A unique identifier for the assayed genetic specimen. |
| 9 | GFSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 10 | GFLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 11 | GFLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 12 | GFTESTCD | Short Name of Genomic Measurement | Char | Topic | Req | C181178 |  |  |  | Short name of the measurement, test, or examination described in GFTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in GFTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). GFTESTCD cannot contain characters other than letters, numbers, or underscores. |
| 13 | GFTEST | Name of Genomic Measurement | Char | Synonym Qualifier | Req | C181179 |  |  |  | Long name for GFTESTCD. The value in GFTEST cannot be longer than 40 characters. |
| 14 | GFTSTDTL | Measurement, Test, or Examination Detail | Char | Variable Qualifier | Perm | C181180 |  |  |  | Description of a reportable qualifying the assessment in GFTESTCD and GFTEST. |
| 15 | GFCAT | Category for Genomic Finding | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. |
| 16 | GFSCAT | Subcategory for Genomic Finding | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of GFCAT values. |
| 17 | GFORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 18 | GFORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Unit for GFORRES. |
| 19 | GFORREF | Reference Result in Original Units | Char | Variable Qualifier | Perm |  |  |  |  | Reference value for the result or finding as originally received or collected. GFORREF uses the same units as GFORRES, if applicable. |
| 20 | GFSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from GFORRES, in a standard format or in standard units. GFSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in GFSTRESN. |
| 21 | GFSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from GFSTRESC. GFSTRESN should store all numeric test results or findings. |
| 22 | GFSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for GFSTRESC, GFSTRESN, GFSTREFC, and GFSTREFN. |
| 23 | GFSTREFC | Reference Result in Standard Format | Char | Variable Qualifier | Perm |  |  |  |  | Reference value for the result or finding copied or derived from GFORREF in a standard format. |
| 24 | GFSTREFN | Numeric Reference Result in Std Units | Num | Variable Qualifier | Perm |  |  |  |  | Reference value for continuous or numeric results or findings in standard format or in standard units. GFSTREFN uses the same units as GFSTRESN, if applicable. |
| 25 | GFRESCAT | Result Category | Char | Variable Qualifier | Perm |  |  |  |  | Used to categorize the result of a finding. |
| 26 | GFINHERT | Inheritability | Char | Variable Qualifier | Perm | C181177 |  |  |  | Identifies whether the variation can be passed to the next generation. |
| 27 | GFGENREF | Genome Reference | Char | Variable Qualifier | Perm |  |  |  |  | An identifier for the genome reference used to generate the reported result. For example, Genome Reference Consortium Human Build 38 patch release 13 may be represented as "GRCh38.p13". |
| 28 | GFCHROM | Chromosome Identifier | Char | Variable Qualifier | Perm |  |  |  |  | The designation (name or number) of the chromosome or contig on which the variant or other feature appears (e.g., "17"; "X"). |
| 29 | GFSYM | Genomic Symbol | Char | Variable Qualifier | Perm |  |  |  |  | A published symbol for the portion of the genome serving as a locus for the experiment/test. |
| 30 | GFSYMTYP | Genomic Symbol Type | Char | Variable Qualifier | Perm | C181176 |  |  |  | A description of the type of genomic entity that is represented by the published symbol in GFSYM. |
| 31 | GFGENLOC | Genetic Location | Char | Variable Qualifier | Perm |  |  |  |  | Specifies the location within a sequence for the observed value in GFORRES. |
| 32 | GFGENSR | Genetic Sub-Region | Char | Variable Qualifier | Perm |  |  |  |  | The portion of the locus in which the variation was found. Examples: "Exon 15", "Kinase domain". |
| 33 | GFSEQID | Sequence Identifier \n | Char | Variable Qualifier | Perm |  |  |  |  | A unique identifier for the sequence used as the reference to identify the genetic variation in the result. Examples: "NM_001234", "ENSG00000182533", "ENST00000343849.2". |
| 34 | GFPVRID | Published Variant Identifier | Char | Variable Qualifier | Perm |  |  |  |  | A unique identifier for the variation that has been publicly characterized in an external database. Examples: "rs2231142", "COSM41596". |
| 35 | GFCOPYID | Copy Identifier | Char | Variable Qualifier | Perm |  |  |  |  | An arbitrary identifier used to differentiate between copies of a genetic target of interest present on homologous chromosomes. |
| 36 | GFSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 37 | GFREASND | Reason Test Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with GFSTAT when value is "NOT DONE". |
| 38 | GFXFN | External File Path | Char | Record Qualifier | Perm |  |  |  |  | The filename and/or path to external data not stored in the same format and possibly not the same location as the other data for a study. |
| 39 | GFNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the vendor that provided the test result. When more than 1 vendor is involved in the generation of the result, additional vendors should be represented as supplemental qualifiers. |
| 40 | GFSPEC | Specimen Material Type | Char | Record Qualifier | Perm | C111114 |  |  |  | Identifies the type of genetic material used for the measurement. |
| 41 | GFMETHOD | Method of Test or Examination | Char | Record Qualifier | Exp | C85492 |  |  |  | The test method by which the examination is performed by the wet lab in order to yield the result reported in the dataset. |
| 42 | GFRUNID | Run ID | Char | Record Qualifier | Perm |  |  |  |  | A unique identifier for a particular run of a test performed by the wet lab on a particular batch of samples. This identifier can be used to distinguish between records for the same test performed at different times. |
| 43 | GFANMETH | Analysis Method | Char | Record Qualifier | Perm | C181181 |  |  |  | The method of secondary processing performed by the dry lab to yield the result reported in the dataset. |
| 44 | GFBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. |
| 45 | GFDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 46 | GFLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Perm |  |  |  |  | Indicates the lower limit of quantitation for an assay. Units will be those used for GFSTRESU. |
| 47 | GFREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |  |  |  | The instance number of a test that is repeated within a given timeframe for the same test performed by the wet lab. |
| 48 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 49 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. |
| 50 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 51 | GFDTC | Date/Time of Specimen Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date and time of specimen collection. |
| 52 | GFDY | Study Day of Specimen Collection | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 53 | GFTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See GFTPTNUM and GFTPTREF. |
| 54 | GFTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of GFTPT used in sorting. |
| 55 | GFELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Elapsed time relative to a planned fixed reference (GFTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration. |
| 56 | GFTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by GFELTM, GFTPTNUM, and GFTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 57 | GFRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by GFTPTREF. |

## IE (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | IE | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | IESEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | IESPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Inclusion or exclusion criteria number from CRF. |
| 6 | IETESTCD | Inclusion/Exclusion Criterion Short Name | Char | Topic | Req |  |  |  |  | Short name of the criterion described in IETEST. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). IETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "IN01", "EX01". |
| 7 | IETEST | Inclusion/Exclusion Criterion | Char | Synonym Qualifier | Req |  |  |  |  | Verbatim description of the inclusion or exclusion criterion that was the exception for the subject within the study. IETEST cannot be longer than 200 characters. |
| 8 | IECAT | Inclusion/Exclusion Category | Char | Grouping Qualifier | Req | C66797 |  |  |  | Used to define a category of related records across subjects. |
| 9 | IESCAT | Inclusion/Exclusion Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of the exception criterion. Can be used to distinguish criteria for a sub-study or for to categorize as a major or minor exceptions. Examples: "MAJOR", "MINOR". |
| 10 | IEORRES | I/E Criterion Original Result | Char | Result Qualifier | Req | C66742 |  |  |  | Original response to inclusion/exclusion criterion question, i.e., whether the inclusion or exclusion criterion was met. |
| 11 | IESTRESC | I/E Criterion Result in Std Format | Char | Result Qualifier | Req | C66742 |  |  |  | Response to inclusion/exclusion criterion result, in standard format. |
| 12 | VISITNUM | Visit Number | Num | Timing | Perm |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 13 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 14 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 15 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 16 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the observation date/time of the inclusion/exclusion finding. |
| 17 | IEDTC | Date/Time of Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Collection date and time of the inclusion/exclusion criterion represented in ISO 8601 character format. |
| 18 | IEDY | Study Day of Collection | Num | Timing | Perm |  |  |  |  | Study day of collection of the inclusion/exclusion exceptions, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |

## IS (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | IS | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | NHOID | Non-host Organism ID | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears. |
| 5 | ISSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| 6 | ISGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 7 | ISREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external specimen identifier. Example: "458975-01". |
| 8 | ISSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 9 | ISTESTCD | Immunogenicity Test/Exam Short Name | Char | Topic | Req | C120525 |  |  |  | Short name of the measurement, test, or examination described in ISTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in ISTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). ISTESTCD cannot contain characters other than letters, numbers, or underscores. |
| 10 | ISTEST | Immunogenicity Test or Examination Name | Char | Synonym Qualifier | Req | C120526 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in ISTEST cannot be longer than 40 characters. Example: "Immunoglobulin E". |
| 11 | ISTSTCND | Test Condition | Char | Variable Qualifier | Perm | C181175 |  |  |  | Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed. |
| 12 | ISCNDAGT | Test Condition Agent | Char | Record Qualifier | Perm |  |  |  |  | The textual description of the agent used to impose a test condition. Examples are different stimulating agents used in immunoassays such as those in the Interferon Gamma Response assay (e.g., Mycobacterium tuberculosis ESAT-6, CFP-10, TB 7.7, Mitogen). |
| 13 | ISBDAGNT | Binding Agent | Char | Variable Qualifier | Perm | C85491; C181169 |  |  |  | Text description of the agent that is binding to the entity in the ISTEST variable. ISBDAGNT is used to indicate that there is a binding relationship between the entities in the ISTEST and ISBDAGNT variables, regardless of direction. \n ISBDAGNT is not a method qualifier. It should only be used when the actual interest of the measurement is the binding interaction between the 2 entities in ISTEST and ISBDAGNT. In other words, the combination of ISTEST and ISBDAGNT should describe the entity or the analyte being measured, without the need for additional variables. \n The binding agent may be (but is not limited to) a test article, a portion of the test article, a related compound, an endogenous molecule, an allergen, or an infectious agent. |
| 14 | ISTSTOPO | Test Operational Objective | Char | Variable Qualifier | Perm | C181170 |  |  |  | Text description of the high-level purpose of the test at the operational level. If populated, valid values are "SCREEN", "CONFIRM", and "QUANTIFY". |
| 15 | ISMSCBCE | Molecule Secreted by Cells | Char | Variable Qualifier | Perm |  |  |  |  | Text description of the entity secreted by the cells represented in ISTEST. The combination of ISTEST and ISMSCBCE should describe the entity or the analyte being measured, without the need for additional variables. |
| 16 | ISTSTDTL | Test Detail | Char | Variable Qualifier | Perm |  |  |  |  | Further description of ISTESTCD and ISTEST. |
| 17 | ISCAT | Category for Immunogenicity Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values across subjects. Example: "SEROLOGY". |
| 18 | ISSCAT | Subcategory for Immunogenicity Test | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of ISCAT. |
| 19 | ISORRES | Results or Findings in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 20 | ISORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Original units in which the data were collected. The unit for ISORRES. Examples: "Index Value", "gpELISA", "unit/mL". |
| 21 | ISORNRLO | Reference Range Lower Limit in Orig Unit | Char | Variable Qualifier | Exp |  |  |  |  | Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results. |
| 22 | ISORNRHI | Reference Range Upper Limit in Orig Unit | Char | Variable Qualifier | Exp |  |  |  |  | Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results. |
| 23 | ISSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from ISORRES, in a standard format or in standard units. ISSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in ISSTRESN. |
| 24 | ISSTRESN | Numeric Results/Findings in Std. Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from ISSTRESC. ISSTRESN should store all numeric test results or findings. |
| 25 | ISSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Standardized units used for ISSTRESC and ISSTRESN. Examples: "Index Value", "gpELISA", "unit/mL". |
| 26 | ISSTNRLO | Reference Range Lower Limit-Std Units | Num | Variable Qualifier | Exp |  |  |  |  | Lower end of reference range for continuous measurements for ISSTRESC/ISSTRESN in standardized units. Should be populated only for continuous results. |
| 27 | ISSTNRHI | Reference Range Upper Limit-Std Units | Num | Variable Qualifier | Exp |  |  |  |  | Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results. |
| 28 | ISSTNRC | Reference Range for Char Rslt-Std Units | Char | Variable Qualifier | Perm |  |  |  |  | For normal range values that are character in ordinal scale or if categorical ranges were supplied. Examples: "-1 to +1", "NEGATIVE TO TRACE". |
| 29 | ISNRIND | Reference Range Indicator | Char | Variable Qualifier | Exp | C78736 |  |  |  | Indicates where the value falls with respect to reference range defined by ISORNRLO and ISORNRHI, ISSTNRLO and ISSTNRHI, or by ISSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". \n Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether ISNRIND refers to the original or standard reference ranges and results. \n Should not be used to indicate clinical significance. |
| 30 | ISSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate a test was not done. Should be null if a result exists in ISORRES. |
| 31 | ISREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a measurement or test was not performed. Used in conjunction with ISSTAT when value is "NOT DONE". |
| 32 | ISNAM | Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the laboratory or vendor who provided the test results. |
| 33 | ISSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734 |  |  |  | Defines the types of specimen used for a measurement. Example: "SERUM". |
| 34 | ISSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |  |  |  | Free or standardized text describing the condition of the specimen. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC". |
| 35 | ISSPCUFL | Specimen Usability for the Test | Char | Record Qualifier | Perm | C66742 |  |  |  | Describes the usability of the specimen for the test. The value will be "N" if the specimen is not usable, and null if the specimen is usable. |
| 36 | ISMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: "ELISA", "ELISPOT". |
| 37 | ISLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 38 | ISBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that ISBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 39 | ISDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record. The value should be "Y" or null. Examples of records that might be derived for the submission datasets include those that represent the average of other records, do not come from the CRF, or are not as originally received or collected. If ISDRVFL="Y", then ISORRES may be null, with ISSTRESC and (if numeric) ISSTRESN having the derived value. |
| 40 | ISLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Exp |  |  |  |  | Indicates the lower limit of quantitation for an assay. Units will be those used for ISSTRESU. |
| 41 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 42 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 43 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 44 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 45 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected. |
| 46 | ISDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of an observation. |
| 47 | ISENDTC | End Date/Time of Specimen Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | End date/time of the observation. |
| 48 | ISDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to sponsor-defined RFSTDTC in Demographics. |
| 49 | ISENDY | Study Day of End of Specimen Collection | Num | Timing | Perm |  |  |  |  | Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 50 | ISTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See ISTPTNUM and ISTPTREF. Examples: "Start", "5 min post". |
| 51 | ISTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of ISTPT to aid in sorting. |
| 52 | ISELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to a planned fixed reference (ISTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable. Represented as ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by ISTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by ISTPTREF. |
| 53 | ISTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by ISELTM, ISTPTNUM, and ISTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 54 | ISRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time of the reference time point, ISTPTREF. |

## LB (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | LB | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | LBSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | LBGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | LBREFID | Specimen ID | Char | Identifier | Perm |  |  |  |  | Internal or external specimen identifier. Example: specimen ID. |
| 7 | LBSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the Lab page. |
| 8 | LBTESTCD | Lab Test or Examination Short Name | Char | Topic | Req | C65047 |  |  |  | Short name of the measurement, test, or examination described in LBTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in LBTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). LBTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "ALT", "LDH". |
| 9 | LBTEST | Lab Test or Examination Name | Char | Synonym Qualifier | Req | C67154 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. Note: Any test normally performed by a clinical laboratory is considered a lab test. The value in LBTEST cannot be longer than 40 characters. Examples: "Alanine Aminotransferase", "Lactate Dehydrogenase". |
| 10 | LBTSTCND | Test Condition | Char | Variable Qualifier | Perm | C181175 |  |  |  | Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed. |
| 11 | LBBDAGNT | Binding Agent | Char | Variable Qualifier | Perm |  |  |  |  | The textual description of the agent that is binding to the entity in the LBTEST variable. The LBBDAGNT variable is used to indicate that there is a binding relationship between the entities in the LBTEST and LBBDAGNT variables, regardless of direction. \n LBBDAGNT is not a method qualifier. It should only be used when the actual interest of the measurement is the binding interaction between the 2 entities in LBTEST and LBBDAGNT. In other words, the combination of LBTEST and LBBDAGNT should describe the thing, the entity, or the analyte being measured, without the need for additional variables. \n The binding agent may be (but is not limited to) a test article, a portion of the test article, a related compound, or an endogenous molecule. |
| 12 | LBTSTOPO | Test Operational Objective | Char | Variable Qualifier | Perm | C181170 |  |  |  | Text description of the high-level purpose of the test at the operational level. |
| 13 | LBCAT | Category for Lab Test | Char | Grouping Qualifier | Exp |  |  |  |  | Used to define a category of related records across subjects. Examples: "HEMATOLOGY", "URINALYSIS", "CHEMISTRY". |
| 14 | LBSCAT | Subcategory for Lab Test | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of a test category. Examples: "DIFFERENTIAL", "COAGULATION", "LIVER FUNCTION", "ELECTROLYTES". |
| 15 | LBORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 16 | LBORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Original units in which the data were collected. The unit for LBORRES. Example: "g/L". |
| 17 | LBRESSCL | Result Scale | Char | Record Qualifier | Perm | C177910 |  |  |  | Classifies the scale of the original result value; for example, whether the result is ordinal, nominal, quantitative, or narrative. |
| 18 | LBRESTYP | Result Type | Char | Record Qualifier | Perm | C179588 |  |  |  | Classifies the kind of result (i.e., property type) originally reported for the test. Examples include substance concentration, proportion, mass rate, and arbitrary concentration. |
| 19 | LBCOLSRT | Collected Summary Result Type | Char | Record Qualifier | Perm | C177908 |  |  |  | Used to indicate the type of collected summary result. This includes source summary results collected on a CRF or provided by an external vendor (e.g., central lab). If the summary result is derived by the sponsor using individual source data records from SDTM, the derived summary result is represented in ADaM. If the summary result is produced and reported by the lab, the collected summary result is represented in SDTM. |
| 20 | LBORNRLO | Reference Range Lower Limit in Orig Unit | Char | Variable Qualifier | Exp |  |  |  |  | Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results. |
| 21 | LBORNRHI | Reference Range Upper Limit in Orig Unit | Char | Variable Qualifier | Exp |  |  |  |  | Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results. |
| 22 | LBLLOD | Lower Limit of Detection | Char | Variable Qualifier | Perm |  |  |  |  | The lowest threshold (as originally received or collected) for reliably detecting the presence or absence of substance measured by a specific test. The value for the field will be as described in documentation from the instrument or lab vendor. |
| 23 | LBSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C102580 |  |  |  | Contains the result value for all findings, copied or derived from LBORRES in a standard format or standard units. LBSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in LBSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in LBORRES and these results effectively have the same meaning, they could be represented in standard format in LBSTRESC as "NEGATIVE". For other examples, see Original and Standardized Results. |
| 24 | LBSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from LBSTRESC. LBSTRESN should store all numeric test results or findings. |
| 25 | LBSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Standardized unit used for LBSTRESC or LBSTRESN. |
| 26 | LBSTNRLO | Reference Range Lower Limit-Std Units | Num | Variable Qualifier | Exp |  |  |  |  | Lower end of reference range for continuous measurements for LBSTRESC/LBSTRESN in standardized units. Should be populated only for continuous results. |
| 27 | LBSTNRHI | Reference Range Upper Limit-Std Units | Num | Variable Qualifier | Exp |  |  |  |  | Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results. |
| 28 | LBSTNRC | Reference Range for Char Rslt-Std Units | Char | Variable Qualifier | Perm |  |  |  |  | For normal range values that are character in ordinal scale or if categorical ranges were supplied. Examples: "-1 to +1", "NEGATIVE TO TRACE". |
| 29 | LBNRIND | Reference Range Indicator | Char | Variable Qualifier | Exp | C78736 |  |  |  | Indicates where the value falls with respect to reference range defined by LBORNRLO and LBORNRHI, LBSTNRLO and LBSTNRHI, or by LBSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether LBNRIND refers to the original or standard reference ranges and results. LBNRIND is not used to indicate clinical significance. |
| 30 | LBSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate exam not done. Should be null if a result exists in LBORRES. |
| 31 | LBREASND | Reason Test Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED", or "SPECIMEN LOST". Used in conjunction with LBSTAT when value is "NOT DONE". |
| 32 | LBNAM | Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | The name or identifier of the laboratory that performed the test. |
| 33 | LBLOINC | LOINC Code | Char | Synonym Qualifier | Perm |  |  | LOINC |  | Code for the lab test from the LOINC code system. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the Define-XML external codelist attributes. |
| 34 | LBSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734 |  |  |  | Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE". |
| 35 | LBSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |  |  |  | The physical state or quality of a sample for an assessment. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC". |
| 36 | LBSPCUFL | Specimen Usability for the Test | Char | Record Qualifier | Perm | C66742 |  |  |  | Describes the usability of the specimen for the test. The value will be "N" if the specimen is not usable, and null if the specimen is usable. |
| 37 | LBMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: "EIA" (enzyme immunoassay), "ELECTROPHORESIS", "DIPSTICK". |
| 38 | LBANMETH | Analysis Method | Char | Record Qualifier | Perm | C160922 |  |  |  | Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result (e.g., a calculation used to measure eGFR). |
| 39 | LBTMTHSN | Test Method Sensitivity | Char | Record Qualifier | Perm | C179589 |  |  |  | The sensitivity of the test methodology with respect to observation, detection, or quantification. |
| 40 | LBLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 41 | LBBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that LBBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 42 | LBFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify fasting status. Examples: "Y", "N". |
| 43 | LBDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or do not come from the CRF, or are not as originally received or collected are examples of records that might be derived for the submission datasets. If LBDRVFL="Y", then LBORRES may be null, with LBSTRESC and (if numeric) LBSTRESN having the derived value. |
| 44 | LBTOX | Toxicity | Char | Variable Qualifier | Perm |  |  |  |  | Description of toxicity quantified by LBTOXGR. The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document. |
| 45 | LBTOXGR | Standard Toxicity Grade | Char | Record Qualifier | Perm |  |  |  |  | Records toxicity grade value using a standard toxicity scale (e.g., the NCI CTCAE). If value is from a numeric scale, represent only the number (e.g., "2" not "Grade 2"). The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document. |
| 46 | LBCLSIG | Clinically Significant, Collected | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate whether a collected observation is clinically significant based on judgment. |
| 47 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 48 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 49 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 50 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 51 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected. |
| 52 | LBDTC | Date/Time of Specimen Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of specimen collection represented in ISO 8601 character format. |
| 53 | LBENDTC | End Date/Time of Specimen Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | End date/time of specimen collection represented in ISO 8601 character format. |
| 54 | LBDY | Study Day of Specimen Collection | Num | Timing | Perm |  |  |  |  | Study day of specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |
| 55 | LBENDY | Study Day of End of Observation | Num | Timing | Perm |  |  |  |  | Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 56 | LBTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See LBTPTNUM and LBTPTREF. Examples: "Start", "5 min post". |
| 57 | LBTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of LBTPT to aid in sorting. |
| 58 | LBELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to a planned fixed reference (LBTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable. Represented as ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by LBTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by LBTPTREF. |
| 59 | LBTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by LBELTM, LBTPTNUM, and LBTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 60 | LBRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time of the reference time point, LBTPTREF. |
| 61 | LBPTFL | Point in Time Flag | Char | Timing | Perm | C66742 |  |  |  | An indication that the specimen was collected at a single point in time. The value is "Y" or null. The intent of this variable in the LB domain is to aid mapping to LOINC codes in the dataset, when LOINC part "Time Aspect" = "Pt". |
| 62 | LBPDUR | Planned Duration | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned duration of specimen collection. If LBPTFL is "Y" then LBPDUR is null. |

## MB (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | MB | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | FOCID | Focus of Study-Specific Interest | Char | Identifier | Perm |  |  |  |  | Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed. The value in this variable should have inherent semantic meaning. |
| 5 | MBSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number. |
| 6 | MBGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 7 | MBREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external specimen identifier (e.g., sample ID for a subject sample from which a microbial culture was generated). |
| 8 | MBSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. |
| 9 | MBLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. For example, it may be used to link genetic findings (in the PF domain) about a microbe to the original culture of that microbe (in MB), or to susceptibility records (in MS) if needed. |
| 10 | MBLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 11 | MBTESTCD | Microbiology Test or Finding Short Name | Char | Topic | Req | C120527 |  |  |  | Short name of the measurement, test, or finding described in MBTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MBTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MBTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MCORGIDN" for Microbial Organism Identification "GMNCOC" for Gram Negative Cocci. |
| 12 | MBTEST | Microbiology Test or Finding Name | Char | Synonym Qualifier | Req | C120528 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in MBTEST cannot be longer than 40 characters. Examples: "Microbial Organism Identification", "Gram Negative Cocci", "HIV-1 RNA". |
| 13 | MBTSTDTL | Measurement, Test or Examination Detail | Char | Variable Qualifier | Perm | C174225 |  |  |  | Further description of MBTESTCD and MBTEST. Example: "VIRAL LOAD" when MBTESTCD represents viral genetic material, such as "HCRNA", "QUANTIFICATION" when MBTESTCD represents any organism being quantified. |
| 14 | MBCAT | Category | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. |
| 15 | MBSCAT | Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of MBCAT values. |
| 16 | MBORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the microbiology measurement or finding as originally received or collected. Examples for "GRAM STAIN" findings: "+3 MODERATE", "+2 FEW", "<10". Examples for "CULTURE PLATE" findings: "KLEBSIELLA PNEUMONIAE", "STREPTOCOCCUS PNEUMONIAE". |
| 17 | MBORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original unit for MBORRES. Example: "mcg/mL". |
| 18 | MBSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from MBORRES, in a standard format or standard units. MBSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MBSTRESN. For example, if a test has results "+3 MODERATE", "MOD", and "MODERATE" in MBORRES and these results effectively have the same meaning, they could be represented in standard format in MBSTRESC as "MODERATE". |
| 19 | MBSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from MBSTRESC. MBSTRESN should store all numeric test results or findings. |
| 20 | MBSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for MBSTRESC and MBSTRESN. |
| 21 | MBRESCAT | Result Category | Char | Variable Qualifier | Perm |  |  |  |  | Used to categorize the result of a finding in a standard format. |
| 22 | MBSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or that a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 23 | MBREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with MBSTAT when value is NOT DONE. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". |
| 24 | MBNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the vendor (e.g., laboratory) that provided the test results. |
| 25 | MBLOINC | LOINC Code | Char | Synonym Qualifier | Perm |  |  |  |  | Logical Observation Identifiers Names and Codes (LOINC) code for the topic variable (e.g., lab test). |
| 26 | MBSPEC | Specimen Material Type | Char | Record Qualifier | Perm | C78734 |  |  |  | Defines the type of specimen used for a measurement. Examples: "SPUTUM", "BLOOD", "PUS". |
| 27 | MBSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |  |  |  | Free or standardized text describing the condition of the specimen. Example: "CONTAMINATED". |
| 28 | MBLOC | Specimen Collection Location | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location relevant to the collection of the measurement. |
| 29 | MBLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for specimen collection location further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 30 | MBDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for specimen collection location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 31 | MBMETHOD | Method of Test or Examination | Char | Record Qualifier | Exp | C85492 |  |  |  | Method of the test or examination. Examples: "GRAM STAIN", "MICROBIAL CULTURE, LIQUID", "QUANTITATIVE REVERSE TRANSCRIPTASE POLYMERASE CHAIN REACTION". |
| 32 | MBLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 33 | MBBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that MBBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 34 | MBFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify fasting status. Valid values include "Y", "N", "U", or null if not relevant. |
| 35 | MBDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 36 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 37 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 38 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 39 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element which the specimen collection occurred. |
| 40 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the specimen was collected. |
| 41 | MBDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of specimen collection. |
| 42 | MBDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Study day of the specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |
| 43 | MBTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See MBTPTNUM and MBTPTREF. Examples: "Start", "5 min post". |
| 44 | MBTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of MBTPT used in sorting. |
| 45 | MBELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to a planned fixed reference (MBTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by MBTPTREF, or "PT8H" to represent the period of 8 hours after the reference point indicated by MBTPTREF. |
| 46 | MBTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by MBELTM, MBTPTNUM, and MBTPT. Example: "PREVIOUS DOSE". |
| 47 | MBRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point, MBTPTREF. |

## MI (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | MI | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | MISEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | MIGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. This is not the treatment group number. |
| 6 | MIREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external specimen identifier. Example: specimen barcode number. |
| 7 | MISPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be printed on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: line number from the MI Findings page. |
| 8 | MITESTCD | Microscopic Examination Short Name | Char | Topic | Req | C132263 |  |  |  | Short name of the measurement, test, or examination described in MITEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MITESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MITESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "HER2", "BRCA1", "TTF1". |
| 9 | MITEST | Microscopic Examination Name | Char | Synonym Qualifier | Req | C132262 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in MITEST cannot be longer than 40 characters. Examples: "Human Epidermal Growth Factor Receptor 2", "Breast Cancer Susceptibility Gene 1", "Thyroid Transcription Factor 1". |
| 10 | MITSTDTL | Microscopic Examination Detail | Char | Record Qualifier | Perm | C125922 |  |  |  | Further description of the test performed in producing the MI result. This would be used to represent specific attributes, such as intensity score or percentage of cells displaying presence of the biomarker or compound. |
| 11 | MICAT | Category for Microscopic Finding | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. |
| 12 | MISCAT | Subcategory for Microscopic Finding | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of MICAT. |
| 13 | MIORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the histopathology measurement or finding as originally received or collected. |
| 14 | MIORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original unit for MIORRES. |
| 15 | MISTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from MIORRES in a standard format or standard units. MISTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MISTRESN. |
| 16 | MISTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from MISTRESC. MISTRESN should store all numeric test results or findings. |
| 17 | MISTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized unit used for MISTRESC and MISTRESN. |
| 18 | MIRESCAT | Result Category | Char | Variable Qualifier | Perm |  |  |  |  | Used to categorize the result of a finding. Examples: "MALIGNANT" or "BENIGN" for tumor findings. |
| 19 | MISTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate examination not done or result is missing. Should be null if a result exists in MIORRES or have a value of "NOT DONE" when MIORRES = "NULL". |
| 20 | MIREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with MISTAT when value is NOT DONE. Examples: "SAMPLE AUTOLYZED", "SPECIMEN LOST". |
| 21 | MINAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the vendor (e.g., laboratory) that provided the test results. |
| 22 | MISPEC | Specimen Material Type | Char | Record Qualifier | Req | C78734 |  |  |  | Subject of the observation. Defines the type of specimen used for a measurement. Examples: "TISSUE", "BLOOD", "BONE MARROW". |
| 23 | MISPCCND | Specimen Condition | Char | Record Qualifier | Exp | C78733 |  |  |  | Free or standardized text describing the condition of the specimen. Example: "AUTOLYZED". |
| 24 | MILOC | Specimen Collection Location | Char | Record Qualifier | Perm | C74456 |  |  |  | Location relevant to the collection of the specimen. Examples: "LUNG", "KNEE JOINT", "ARM", "THIGH". |
| 25 | MILAT | Specimen Laterality within Subject | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for laterality of the location of the specimen in MILOC. Examples: "LEFT", "RIGHT", "BILATERAL". |
| 26 | MIDIR | Specimen Directionality within Subject | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for directionality of the location of the specimen in MILOC. Examples: "DORSAL", "PROXIMAL". |
| 27 | MIMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. This could include the technique or type of staining used for the slides. Examples: "IHC", "Crystal violet", "Safranin", "Trypan blue", or "Propidium iodide". |
| 28 | MILOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 29 | MIBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. The value should be "Y" or null. Note that MIBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 30 | MIEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Example: "PATHOLOGIST", "PEER REVIEW", "SPONSOR PATHOLOGIST". |
| 31 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 32 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 33 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the specimen was collected. |
| 36 | MIDTC | Date/Time of Specimen Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of specimen collection, in ISO 8601 format. |
| 37 | MIDY | Study Day of Specimen Collection | Num | Timing | Perm |  |  |  |  | Study day of specimen collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. |

## MK (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | MK | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | MKSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1. |
| 5 | MKGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records within a subject in a domain. |
| 6 | MKREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external identifier such as lab specimen ID or a medical image. |
| 7 | MKSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. Example: Preprinted line identifier on a Concomitant Medications page. |
| 8 | MKLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 9 | MKLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 10 | MKTESTCD | Short Name of Musculoskeletal Test | Char | Topic | Req | C127269 |  |  |  | Short character value for MKTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The value in MKTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MKTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TNDRIND", "SWLLIND", "SGJSNSCR". |
| 11 | MKTEST | Name of Musculoskeletal Test | Char | Synonym Qualifier | Req | C127270 |  |  |  | Long name For MKTESTCD. Examples: "Tenderness Indicator", "Swollen Indicator", "Sharp/Genant JSN Score". |
| 12 | MKCAT | Category for Musculoskeletal Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. Examples: "SWOLLEN/TENDER JOINT ASSESSMENT". |
| 13 | MKSCAT | Subcategory for Musculoskeletal Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of MKCAT values. |
| 14 | MKPOS | Position of Subject | Char | Record Qualifier | Perm | C71148 |  |  |  | Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING". |
| 15 | MKORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 16 | MKORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Unit for MKORRES. |
| 17 | MKSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from MKORRES in a standard format or in standard units. MKSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MKSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in MKORRES and these results effectively have the same meaning, they could be represented in standard format in MKSTRESC as "NEGATIVE". |
| 18 | MKSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from MKSTRESC. MKSTRESN should store all numeric test results or findings. |
| 19 | MKSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for MKSTRESC and MKSTRESN. |
| 20 | MKSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or that a test was attempted but did not generate a result. Should be null if a result exists in MKORRES. |
| 21 | MKREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with MKSTAT when value is "NOT DONE". |
| 22 | MKLOC | Location Used for the Measurement | Char | Record Qualifier | Exp | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. Examples: "INTERPHALANGEAL JOINT 1", "SHOULDER JOINT". |
| 23 | MKLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 24 | MKDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 25 | MKMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: "X-RAY", "MRI", "CT SCAN". |
| 26 | MKLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 27 | MKBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that MKBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 28 | MKDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 29 | MKEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| 30 | MKEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in MKEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2". |
| 31 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 32 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 33 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 36 | MKDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of an observation. |
| 37 | MKDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 38 | MKTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See MKTPTNUM and MKTPTREF. |
| 39 | MKTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 40 | MKELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned Elapsed time relative to a planned fixed reference (MKTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 41 | MKTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by MKELTM, MKTPTNUM, and MKTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 42 | MKRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by MKTPTREF. |

## MS (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | MS | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | NHOID | Non-host Organism ID | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears. |
| 5 | MSSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1. |
| 6 | MSGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. In SDTMIG v3.2 this was an Expected variable. In this version, the core designation has been changed to Permissible. |
| 7 | MSREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external identifier (e.g., an identifier for the culture/isolate being tested for susceptibility). |
| 8 | MSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. |
| 9 | MSLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. For example, it may be used to link genetic findings (in the PF domain) about a microbe to the original culture of that microbe (in MB), or to susceptibility records (in MS) if needed. |
| 10 | MSTESTCD | Short Name of Assessment | Char | Topic | Req | C128688 |  |  |  | Short character value for MSTEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MIC" for Minimum Inhibitory Concentration; "MICROSUS" for Microbial Susceptibility. |
| 11 | MSTEST | Name of Assessment | Char | Synonym Qualifier | Req | C128687 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in MSTEST cannot be longer than 40 characters. Examples: "Minimum Inhibitory Concentration", "Microbial Susceptibility". |
| 12 | MSAGENT | Agent Name | Char | Variable Qualifier | Exp |  |  |  |  | The name of the agent for which resistance is tested. The agent specified may be based on genetic markers or direct phenotypic drug sensitivity testing. Examples: "Penicillin", name of study drug. |
| 13 | MSCONC | Agent Concentration | Num | Variable Qualifier | Perm |  |  |  |  | Numeric concentration of agent listed in MSAGENT. |
| 14 | MSCONCU | Agent Concentration Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Units for value of the agent concentration listed in MSCONC. Example: "mg/L". |
| 15 | MSTSTDTL | Measurement, Test or Examination Detail | Char | Variable Qualifier | Perm |  |  |  |  | Further description of MSTESTCD and MSTEST. |
| 16 | MSCAT | Category | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of MSTEST values. |
| 17 | MSSCAT | Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of MSCAT values. |
| 18 | MSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 19 | MSORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Unit for MSORRES. Examples: "ug/mL". |
| 20 | MSSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from MSORRES in a standard format or in standard units. MSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MSSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in MSORRES and these results effectively have the same meaning, they could be represented in standard format in MSSTRESC as "NEGATIVE". |
| 21 | MSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from MSSTRESC. MSSTRESN should store all numeric test results or findings. |
| 22 | MSSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for MSSTRESC and MSSTRESN. Example: "mol/L". |
| 23 | MSNRIND | Normal/Reference Range Indicator | Char | Variable Qualifier | Perm | C78736 |  |  |  | Used to indicate the value is outside the normal range or reference range. May be defined by MSORNRLO and MSORNRHI or other objective criteria. Examples: "Y", "N", "HIGH", "LOW", "NORMAL". "ABNORMAL". |
| 24 | MSRESCAT | Result Category | Char | Variable Qualifier | Perm | C85495 |  |  |  | Used to categorize the result of a finding. In SDTMIG v3.2, MSRESCAT was used to categorize a numeric susceptibility result represented in MSORRES as either "SUSCEPTIBLE", "INTERMEDIATE", or "RESISTANT". However, results from some susceptibility tests may report only a categorical result and not a numeric result. Thus, in order for susceptibility results to be represented consistently, MSRESCAT should no longer be used for this purpose. In this version, the core designation has been changed from Expected to Permissible. |
| 25 | MSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 26 | MSREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with MSSTAT when value is "NOT DONE". |
| 27 | MSXFN | External File Path | Char | Record Qualifier | Perm |  |  |  |  | Filename for an external file. |
| 28 | MSNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the vendor (e.g., laboratory) that provided the test results. |
| 29 | MSLOINC | LOINC Code | Char | Synonym Qualifier | Perm |  |  |  |  | Logical Observation Identifiers Names and Codes (LOINC) code for the topic variable such as a lab test. |
| 30 | MSSPEC | Specimen Material Type | Char | Record Qualifier | Perm | C78734 |  |  |  | Defines the type of specimen used for a measurement. Example: "SPUTUM". |
| 31 | MSSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |  |  |  | Defines the condition of the specimen. Example: "CLOUDY". |
| 32 | MSLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. |
| 33 | MSLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 34 | MSDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 35 | MSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: "EPSILOMETER", "MACRO BROTH DILUTION". |
| 36 | MSANMETH | Analysis Method | Char | Record Qualifier | Perm |  |  |  |  | Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result (e.g., an image or a genetic sequence). |
| 37 | MSLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 38 | MSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that MSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 39 | MSFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify fasting status. Valid values include "Y", "N", "U", or null if not relevant. |
| 40 | MSDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 41 | MSEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "MICROSCOPIST". |
| 42 | MSEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in MSEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2". |
| 43 | MSACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | In cases where more than 1 assessor provides an evaluation of a result or response, this flag identifies the record that is considered, by an independent assessor, to be the accepted evaluation. Expected to be "Y" or null. |
| 44 | MSLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Perm |  |  |  |  | Indicates the lower limit of quantitation for an assay. Units will be those used for MSSTRESU. |
| 45 | MSULOQ | Upper Limit of Quantitation | Num | Variable Qualifier | Perm |  |  |  |  | Indicates the upper limit of quantitation for an assay. Units will be those used for MSSTRESU. |
| 46 | MSREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |  |  |  | The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample. |
| 47 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 48 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 49 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 50 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the specimen was collected. |
| 51 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the specimen was collected. |
| 52 | MSDTC | Date/Time of Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Collection date and time of an observation. |
| 53 | MSDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 54 | MSDUR | Duration | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration of an event, intervention, or finding. Used only if collected on the CRF and not derived. |
| 55 | MSTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See MSTPTNUM and MSTPTREF. |
| 56 | MSTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 57 | MSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to a planned fixed reference (MSTPTREF; e.g., previous dose, previous meal). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 58 | MSTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by MSELTM, MSTPTNUM, and MSTPT. Example: "PREVIOUS DOSE". |
| 59 | MSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by MSTPTREF. |
| 60 | MSEVLINT | Evaluation Interval | Char | Timing | Perm |  |  | ISO 8601 duration or interval |  | Duration of interval associated with an observation such as a finding MSTESTCD. Example: "-P2M" to represent a period of the past 2 months before the assessment. |
| 61 | MSEVINTX | Evaluation Interval Text | Char | Timing | Perm |  |  |  |  | Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS". |

## NV (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | NV | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | FOCID | Focus of Study-Specific Interest | Char | Identifier | Perm |  |  |  |  | Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed, such as a drug application site (e.g., "Injection site 1", "Biopsy site 1", "Treated site 1") or a more specific focus (e.g., "OD" (right eye), "Upper left quadrant of the back"). The value in this variable should have inherent semantic meaning. |
| 5 | NVSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 6 | NVGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 7 | NVREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external procedure identifier. |
| 8 | NVSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the Procedure or Test page. |
| 9 | NVLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link a procedure to the assessment results over the course of the study. |
| 10 | NVLNKGRP | Link Group | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 11 | NVTESTCD | Short Name of Nervous System Test | Char | Topic | Req | C116104 |  |  |  | Short name of the measurement, test, or examination described in NVTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in NVTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). NVTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SUVR", "N75LAT", "P100LAT","N145LAT". |
| 12 | NVTEST | Name of Nervous System Test | Char | Synonym Qualifier | Req | C116103 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in NVTEST cannot be longer than 40 characters. Examples: "Standard Uptake Value Ratio", "N75 Latency", "P100 Latency", "N145 Latency". |
| 13 | NVCAT | Category for Nervous System Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. Example: "VISUAL EVOKED POTENTIAL". |
| 14 | NVSCAT | Subcategory for Nervous System Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of NVCAT values. |
| 15 | NVORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the procedure measurement or finding as originally received or collected. |
| 16 | NVORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. The unit for NVORRES. |
| 17 | NVSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from NVORRES, in a standard format or standard units. NVSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in NVSTRESN. |
| 18 | NVSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from NVSTRESC. NVSTRESN should store all numeric test results or findings. |
| 19 | NVSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized unit used for NVSTRESC or NVSTRESN. |
| 20 | NVSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate a test was not done, or a measurement was not taken. Should be null if a result exists in NVORRES. |
| 21 | NVREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with NVSTAT when value is "NOT DONE". |
| 22 | NVLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. Examples: "BRAIN", "EYE", "PRECUNEUS", "CINGULATE CORTEX". |
| 23 | NVLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 24 | NVDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 25 | NVMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: "EEG", "PET/CT SCAN ", "FDGPET". |
| 26 | NVLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 27 | NVBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that NVBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 28 | NVDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 29 | NVEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| 30 | NVEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in NVEVAL. Examples: "RADIOLOGIST 1", "RADIOLOGIST 2". |
| 31 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 32 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 33 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 36 | NVDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date of procedure or test. |
| 37 | NVDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Study day of the procedure or test, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| 38 | NVTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See NVTPTNUM and NVTPTREF. Examples: "START", "5 MIN POST". |
| 39 | NVTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of NVTPT to aid in sorting. |
| 40 | NVELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to a fixed time point reference (NVTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by NVTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by NVTPTREF. |
| 41 | NVTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by NVELTM, NVTPTNUM, and NVTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 42 | NVRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by --TPTREF in ISO 8601 character format. |

## OE (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | OE | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | FOCID | Focus of Study-Specific Interest | Char | Identifier | Perm | C119013 |  |  |  | Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed. |
| 5 | OESEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 6 | OEGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 7 | OELNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 8 | OELNKGRP | Link Group | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 9 | OETESTCD | Short Name of Ophthalmic Test or Exam | Char | Topic | Req | C117743 |  |  |  | Short character value for OETEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in OETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). OETESTCD cannot contain characters other than letters, numbers, or underscores. Example: "NUMLCOR". |
| 10 | OETEST | Name of Ophthalmic Test or Exam | Char | Synonym Qualifier | Req | C117742 |  |  |  | Long name for the test or examination used to obtain the measurement or finding. The value in OETEST cannot be longer than 40 characters. Example: "Number of Letters Correct" for OETESTCD = "NUMLCOR". |
| 11 | OETSTDTL | Ophthalmic Test or Exam Detail | Char | Variable Qualifier | Perm |  |  |  |  | Further description of OETESTCD and OETEST. |
| 12 | OECAT | Category for Ophthalmic Test or Exam | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. Examples: "VISUAL ACUITY", "CONTRAST SENSITIVITY", "OCULAR COMFORT". |
| 13 | OESCAT | Subcategory for Ophthalmic Test or Exam | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of OECAT values. Example: "HIGH CONTRAST" or "LOW CONTRAST" when OECAT is "VISUAL ACUITY". |
| 14 | OEORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. Examples: "120", "<1, NORMAL", "RED SPOT VISIBLE". |
| 15 | OEORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Original unit for OEORRES. Examples: "mm", "um". |
| 16 | OEORNRLO | Normal Range Lower Limit-Original Units | Char | Variable Qualifier | Perm |  |  |  |  | Lower end of normal range or reference range for results stored in OEORRES. |
| 17 | OEORNRHI | Normal Range Upper Limit-Original Units | Char | Variable Qualifier | Perm |  |  |  |  | Upper end of normal range or reference range for results stored in OEORRES. |
| 18 | OESTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from OEORRES, in a standard format or in standard units. OESTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in OESTRESN. |
| 19 | OESTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from OESTRESC. OESTRESN should store all numeric test results or findings. |
| 20 | OESTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Standardized units used for OESTRESC and OESTRESN. Examples: "mm", "um". |
| 21 | OESTNRLO | Normal Range Lower Limit-Standard Units | Num | Variable Qualifier | Perm |  |  |  |  | Lower end of normal range or reference range for standardized results (e.g., OESTRESC, OESTRESN) represented in standardized units (OESTRESU). |
| 22 | OESTNRHI | Normal Range Upper Limit-Standard Units | Num | Variable Qualifier | Perm |  |  |  |  | Upper end of normal range or reference range for standardized results (e.g., OESTRESC, OESTRESN) represented in standardized units (OESTRESU). |
| 23 | OESTNRC | Normal Range for Character Results | Char | Variable Qualifier | Perm |  |  |  |  | Normal range or reference range for results stored in OESTRESC that are character in ordinal or categorical scale. Example: "Negative to Trace". |
| 24 | OENRIND | Normal/Reference Range Indicator | Char | Variable Qualifier | Perm | C78736 |  |  |  | Used to indicate the value is outside the normal range or reference range. May be defined by OEORNRLO and OEORNRHI or other objective criteria. Examples: "Y", "N"; "HIGH", "LOW"; "NORMAL", "ABNORMAL". |
| 25 | OERESCAT | Result Category | Char | Variable Qualifier | Perm |  |  |  |  | Used to categorize the result of a finding or medical status per interpretation of test results. Examples: "POSITIVE", "NEGATIVE". The variable OERESCAT is not meant to replace the use of OENRIND for cases where normal ranges are provided. |
| 26 | OESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 27 | OEREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with OESTAT when value is "NOT DONE". |
| 28 | OEXFN | External File Path | Char | Record Qualifier | Perm |  |  |  |  | Filename for an external file, such as one for a retinal OCT image. |
| 29 | OELOC | Location Used for the Measurement | Char | Record Qualifier | Exp | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. Examples: "EYE" for a finding record relative to the complete eye, "RETINA" for a measurement or assessment of only the retina. |
| 30 | OELAT | Laterality | Char | Variable Qualifier | Exp | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 31 | OEDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 32 | OEPORTOT | Portion or Totality | Char | Variable Qualifier | Perm | C99075 |  |  |  | Qualifier for anatomical location or specimen further detailing the distribution (i.e., arrangement of, apportioning of). Examples: "ENTIRE", "SINGLE", "SEGMENT", "MANY". |
| 33 | OEMETHOD | Method of Test or Examination | Char | Record Qualifier | Exp | C85492 |  |  |  | Method of the test or examination. Example: "ETDRS EYE CHART" for OETESTCD = "NUMLCOR". The different methods may offer different functionality or granularity, affecting the set of results and associated meaning. |
| 34 | OELOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 35 | OEBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that OEBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 36 | OEDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 37 | OEEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "INDEPENDENT ASSESSOR", "INVESTIGATOR". |
| 38 | OEEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in OEEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". |
| 39 | OEACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | In cases where more than one assessor provides an evaluation of a result or response, this flag identifies the record that is considered, by an independent assessor, to be the accepted evaluation. Expected to be "Y" or null. |
| 40 | OEREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |  |  |  | The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample. |
| 41 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 42 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 43 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 44 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 45 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 46 | OEDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date/time of the observation. |
| 47 | OEDY | Study Day of Visit/Collection/Exam | Num | Timing | Exp |  |  |  |  | Actual study day of observation/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 48 | OETPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point. |
| 49 | OETPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 50 | OEELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to a planned fixed reference (OETPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 51 | OETPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by OETPT, OETPTNUM, and OEELTM. |
| 52 | OERFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time of the reference time point, OETPTREF. |

## PC (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | PC | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | PCSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | PCGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain to support relationships within the domain and between domains. |
| 6 | PCREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external specimen identifier. |
| 7 | PCSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. |
| 8 | PCTESTCD | Pharmacokinetic Test Short Name | Char | Topic | Req |  |  |  |  | Short name of the analyte or specimen characteristic. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PCTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PCTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "ASA", "VOL", "SPG". |
| 9 | PCTEST | Pharmacokinetic Test Name | Char | Synonym Qualifier | Req |  |  |  |  | Name of the analyte or specimen characteristic. Note any test normally performed by a clinical laboratory is considered a lab test. The value in PCTEST cannot be longer than 40 characters. Examples: "Acetylsalicylic Acid", "Volume", "Specific Gravity". |
| 10 | PCCAT | Test Category | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. Examples: "ANALYTE", "SPECIMEN PROPERTY". |
| 11 | PCSCAT | Test Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of a test category. |
| 12 | PCORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 13 | PCORRESU | Original Units | Char | Variable Qualifier | Exp | C85494 |  |  |  | Original units in which the data were collected. The unit for PCORRES. Example: "mg/L". |
| 14 | PCSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from PCORRES in a standard format or standard units. PCSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in PCSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in PCORRES, and these results effectively have the same meaning, they could be represented in standard format in PCSTRESC as "NEGATIVE". For other examples, see general assumptions. |
| 15 | PCSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from PCSTRESC. PCSTRESN should store all numeric test results or findings. |
| 16 | PCSTRESU | Standard Units | Char | Variable Qualifier | Exp | C85494 |  |  |  | Standardized unit used for PCSTRESC and PCSTRESN. |
| 17 | PCSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate a result was not obtained. Should be null if a result exists in PCORRES. |
| 18 | PCREASND | Reason Test Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a result was not obtained, such as "SPECIMEN LOST". Used in conjunction with PCSTAT when value is "NOT DONE". |
| 19 | PCNAM | Vendor Name | Char | Record Qualifier | Exp |  |  |  |  | Name or identifier of the laboratory or vendor who provides the test results. |
| 20 | PCSPEC | Specimen Material Type | Char | Record Qualifier | Exp | C78734 |  |  |  | Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE". |
| 21 | PCSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |  |  |  | Free or standardized text describing the condition of the specimen. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC". |
| 22 | PCMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: "HPLC/MS", "ELISA". This should contain sufficient information and granularity to allow differentiation of various methods that might have been used within a study. |
| 23 | PCFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify fasting status. |
| 24 | PCDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, which do not come from the CRF, are examples of records that would be derived for the submission datasets. If PCDRVFL = "Y", then PCORRES may be null with PCSTRESC, and PCSTRESN (if the result is numeric) having the derived value. |
| 25 | PCLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Exp |  |  |  |  | Indicates the lower limit of quantitation for an assay. Units should be those used in PCSTRESU. |
| 26 | PCULOQ | Upper Limit of Quantitation | Num | Variable Qualifier | Perm |  |  |  |  | Indicates the upper limit of quantitation for an assay. Units should be those used in PCSTRESU. |
| 27 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 28 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 29 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 30 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 31 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected. |
| 32 | PCDTC | Date/Time of Specimen Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of specimen collection represented in ISO 8601 character format. If there is no end time, then this will be the collection time. |
| 33 | PCENDTC | End Date/Time of Specimen Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | End date/time of specimen collection represented in ISO 8601 character format. If there is no end time, the collection time should be stored in PCDTC, and PCENDTC should be null. |
| 34 | PCDY | Actual Study Day of Specimen Collection | Num | Timing | Perm |  |  |  |  | Study day of specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| 35 | PCENDY | Study Day of End of Observation | Num | Timing | Perm |  |  |  |  | Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 36 | PCTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See PCTPTNUM and PCTPTREF. Examples: "Start", "5 min post". |
| 37 | PCTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of PCTPT to aid in sorting. |
| 38 | PCELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to a planned fixed reference (PCTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. |
| 39 | PCTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point used as a basis for PCTPT, PCTPTNUM, and PCELTM. Example: "MOST RECENT DOSE". |
| 40 | PCRFTDTC | Date/Time of Reference Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time of the reference time point described by PCTPTREF. |
| 41 | PCEVLINT | Evaluation Interval | Char | Timing | Perm |  |  | ISO 8601 duration or interval |  | Evaluation Interval associated with a PCTEST record represented in ISO 8601 character format. Example: "-PT2H" to represent an evaluation interval of 2 hours prior to a PCTPT. |

## PE (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | PE | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | PESEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number. |
| 5 | PEGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records in a single domain for a subject. |
| 6 | PESPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. Perhaps preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF. |
| 7 | PETESTCD | Body System Examined Short Name | Char | Topic | Req |  |  |  |  | Short name of a part of the body examined in a physical examination. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "HEAD", "ENT". If the results of the entire physical examination are represented in one record, value should be "PHYSEXAM". |
| 8 | PETEST | Body System Examined | Char | Synonym Qualifier | Req |  |  |  |  | Long name of a part of the body examined in a physical examination. The value in PETEST cannot be longer than 40 characters. Examples: "Head", "Ear/Nose/Throat". If the results of the entire physical examination are represented in one record, value should be "Physical Examination". |
| 9 | PEMODIFY | Modified Reported Term | Char | Synonym Qualifier | Perm |  |  |  |  | If the value of PEORRES is modified for coding purposes, then the modified text is placed here. |
| 10 | PECAT | Category for Examination | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. Example: "GENERAL". |
| 11 | PESCAT | Subcategory for Examination | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of --CAT values. |
| 12 | PEBODSYS | Body System or Organ Class | Char | Record Qualifier | Perm |  |  |  |  | Body system or organ class (e.g., MedDRA SOC) that is involved for a finding from the standard hierarchy for dictionary-coded results. |
| 13 | PEORRES | Verbatim Examination Finding | Char | Result Qualifier | Exp |  |  |  |  | Text description of any abnormal findings. If the examination was completed and there were no abnormal findings, the value should be "NORMAL". If the examination was not performed on a particular body system, or at the subject level, then the value should be null, and "NOT DONE" should appear in PESTAT. |
| 14 | PEORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. The unit for PEORRES. |
| 15 | PESTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | If there are findings for a body system, then either the dictionary preferred term (if findings are coded using a dictionary) or PEORRES (if findings are not encoded) should appear here. If PEORRES is null, PESTRESC must be null. |
| 16 | PESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate exam not done. Must be null if a result exists in PEORRES/PESTRESC. |
| 17 | PEREASND | Reason Not Examined | Char | Record Qualifier | Perm |  |  |  |  | Describes why an examination was not performed or why a body system was not examined. Example: "SUBJECT REFUSED". Used in conjunction with PESTAT when value is "NOT DONE". |
| 18 | PELOC | Location of Physical Exam Finding | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. Example: "ARM" for skin rash. |
| 19 | PELAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterallity. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 20 | PEMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. Examples: "PALPATION", "PERCUSSION". |
| 21 | PELOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| 22 | PEBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | A baseline defined by the sponsor (could be derived in the same manner as PELOBXFL or ABLFL, but is not required to be). The value should be "Y" or null. Note that PEBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 23 | PEEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Example: "INVESTIGATOR". |
| 24 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 25 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 26 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 27 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 28 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the observation date/time of the physical exam finding. |
| 29 | PEDTC | Date/Time of Examination | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date and time of the physical examination represented in ISO 8601 character format. |
| 30 | PEDY | Study Day of Examination | Num | Timing | Perm |  |  |  |  | Study day of physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |

## PP (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | PP | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. \n |
| 4 | PPSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | PPGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain to support relationships within the domain and between domains. |
| 6 | PPTESTCD | Parameter Short Name | Char | Topic | Req | C85839 |  |  |  | Short name of the pharmacokinetic parameter. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PPTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PPTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "AUCALL", "TMAX", "CMAX". |
| 7 | PPTEST | Parameter Name | Char | Synonym Qualifier | Req | C85493 |  |  |  | Name of the pharmacokinetic parameter. The value in PPTEST cannot be longer than 40 characters. Examples: "AUC All", "Time of CMAX", "Max Conc". |
| 8 | PPCAT | Parameter Category | Char | Grouping Qualifier | Exp |  |  |  |  | Used to define a category of related records. For PP, this should be the name of the analyte in PCTEST whose profile the parameter is associated with. |
| 9 | PPSCAT | Parameter Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | Categorization of the model type used to calculate the PK parameters. Examples: "COMPARTMENTAL", "NON-COMPARTMENTAL". |
| 10 | PPORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 11 | PPORRESU | Original Units | Char | Variable Qualifier | Exp | C85494; C128684; C128683; C128685; C128686 |  |  |  | Original units in which the data were collected. The unit for PPORRES. Example: "ng/L". See PP Assumption 3. |
| 12 | PPSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from PPORRES in a standard format or standard units. PPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in PPSTRESN. |
| 13 | PPSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from PPSTRESC. PPSTRESN should store all numeric test results or findings. |
| 14 | PPSTRESU | Standard Units | Char | Variable Qualifier | Exp | C85494; C128684; C128683; C128685; C128686 |  |  |  | Standardized unit used for PPSTRESC and PPSTRESN. See PP Assumption 3. |
| 15 | PPSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a parameter was not calculated. Should be null if a result exists in PPORRES. |
| 16 | PPREASND | Reason Parameter Not Calculated | Char | Record Qualifier | Perm |  |  |  |  | Describes why a parameter was not calculated, such as "INSUFFICIENT DATA". Used in conjunction with PPSTAT when value is "NOT DONE". |
| 17 | PPSPEC | Specimen Material Type | Char | Record Qualifier | Exp | C78734 |  |  |  | Defines the type of specimen used for a measurement. If multiple specimen types are used for a calculation (e.g., serum and urine for renal clearance), then this field should be left blank. Examples: "SERUM", "PLASMA", "URINE". |
| 18 | PPANMETH | Analysis Method | Char | Record Qualifier | Perm | C172330 |  |  |  | Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result. Example: A named formula used to calculate AUC, such as "LIN-LOG TRAPEZOIDAL METHOD". \n Sponsor-defined formulas can also be represented by this variable. Example: Calculating ratio AUCs where the PPANMETH may be "DRUG METABOLITE 1 TO DRUG PARENT" or "DRUG METABOLITE 2 TO METABOLITE 1". |
| 19 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 20 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected. |
| 21 | PPDTC | Date/Time of Parameter Calculations | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Nominal date/time of parameter calculations. |
| 22 | PPDY | Study Day of Parameter Calculations | Num | Timing | Perm |  |  |  |  | Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. |
| 23 | PPTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | The description of a time point that acts as a fixed reference for a series of planned time points. |
| 24 | PPRFTDTC | Date/Time of Reference Point | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of the reference time point from the PC records used to calculate a parameter record. The values in PPRFTDTC should be the same as that in PCRFTDTC for related records. |
| 25 | PPSTINT | Planned Start of Assessment Interval | Char | Timing | Perm |  |  | ISO 8601 duration |  | The start of a planned evaluation or assessment interval relative to the time point reference. |
| 26 | PPENINT | Planned End of Assessment Interval | Char | Timing | Perm |  |  | ISO 8601 duration |  | The end of a planned evaluation or assessment interval relative to the time point reference. |

## QS (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | QS | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | QSSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | QSGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | QSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Question number on a questionnaire. |
| 7 | QSTESTCD | Question Short Name | Char | Topic | Req |  |  |  |  | Topic variable for QS. Short name for the value in QSTEST, which can be used as a column name when converting the dataset from a vertical format to a horizontal format. The value in QSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). QSTESTCD cannot contain characters other than letters, numbers, or underscores. \n Controlled terminology for QSTESTCD is published in separate codelists for each questionnaire. See https://www.cdisc.org/standards/semantics/terminology for values for QSTESTCD. Examples: "ADCCMD01", "BPR0103". |
| 8 | QSTEST | Question Name | Char | Synonym Qualifier | Req |  |  |  |  | Verbatim name of the question or group of questions used to obtain the measurement or finding. The value in QSTEST cannot be longer than 40 characters. \n Controlled terminology for QSTEST is published in separate codelists for each questionnaire. See https://www.cdisc.org/standards/semantics/terminology for values for QSTEST. Example: "BPR01 - Emotional Withdrawal". |
| 9 | QSCAT | Category of Question | Char | Grouping Qualifier | Req | C100129 |  |  |  | Used to specify the questionnaire in which the question identified by QSTEST and QSTESTCD was included. Examples: "ADAS-COG", "MDS-UPDRS". |
| 10 | QSSCAT | Subcategory for Question | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of the questions within the category. Examples: "MENTAL HEALTH" , "DEPRESSION", "WORD RECALL". |
| 11 | QSORRES | Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Finding as originally received or collected (e.g., "RARELY", "SOMETIMES"). When sponsors apply codelist to indicate that code values are statistically meaningful standardized scores (which are defined by sponsors or by valid methodologies, e.g., SF36 questionnaires), QSORRES will contain the decode format; QSSTRESC and QSSTRESN may contain the standardized code values or scores. |
| 12 | QSORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. The unit for QSORRES, such as minutes or seconds or the units associated with a visual analog scale. |
| 13 | QSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the finding for all questions or subscores copied or derived from QSORRES, in a standard format or standard units. QSSTRESC should store all findings in character format; if findings are numeric, they should also be stored in numeric format in QSSTRESN. If question scores are derived from the original finding, then the standard format is the score. Examples: "0", "1". \n When sponsors apply codelist to indicate the code values are statistically meaningful standardized scores (which are defined by sponsors or by valid methodologies, e.g., SF36 questionnaires), QSORRES will contain the decode format; QSSTRESC and QSSTRESN may contain the standardized code values or scores. |
| 14 | QSSTRESN | Numeric Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric findings in standard format; copied in numeric format from QSSTRESC. QSSTRESN should store all numeric results or findings. |
| 15 | QSSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized unit used for QSSTRESC or QSSTRESN. |
| 16 | QSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not done or was not answered. Should be null if a result exists in QSORRES. |
| 17 | QSREASND | Reason Not Performed | Char | Record Qualifier | Perm |  |  |  |  | Describes why a question was not answered. Used in conjunction with QSSTAT when value is "NOT DONE". Example: "SUBJECT REFUSED". |
| 18 | QSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C158113 |  |  |  | Method of the test or examination. |
| 19 | QSLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| 20 | QSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that QSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 21 | QSDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records or questionnaire subscores that do not come from the CRF are examples of records that would be derived for the submission datasets. If QSDRVFL = "Y", then QSORRES may be null with QSSTRESC and (if numeric) QSSTRESN having the derived value. |
| 22 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 23 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 24 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 25 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 26 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the observation date/time of the physical exam finding. |
| 27 | QSDTC | Date/Time of Finding | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date of questionnaire. |
| 28 | QSDY | Study Day of Finding | Num | Timing | Perm |  |  |  |  | Study day of finding collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| 29 | QSTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when questionnaire should be administered. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See QSTPTNUM and QSTPTREF. |
| 30 | QSTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of QSTPT to aid in sorting. |
| 31 | QSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to a planned fixed reference (QSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by QSTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by QSTPTREF. |
| 32 | QSTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by QSELTM, QSTPTNUM, and QSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 33 | QSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time of the reference time point, QSTPTREF. |
| 34 | QSEVLINT | Evaluation Interval | Char | Timing | Perm |  |  | ISO 8601 duration or interval |  | Evaluation interval associated with a QSTEST question represented in ISO 8601 character format. Example: "-P2Y" to represent an interval of 2 years in the question "Have you experienced any episodes in the past 2 years?". |
| 35 | QSEVINTX | Evaluation Interval Text | Char | Timing | Perm |  |  |  |  | Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS". |

## RE (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | RE | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier for a device. |
| 5 | RESEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| 6 | REGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 7 | REREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external procedure identifier. |
| 8 | RESPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. |
| 9 | RELNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 10 | RELNKGRP | Link Group | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 11 | RETESTCD | Short Name of Respiratory Test | Char | Topic | Req | C111106 |  |  |  | Short name of the measurement, test, or examination. It can be used as a column name when converting a dataset from a vertical format to a horizontal format. The value in RETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). RETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "FEV1", "FVC". |
| 12 | RETEST | Name of Respiratory Test | Char | Synonym Qualifier | Req | C111107 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in RETEST cannot be longer than 40 characters. Examples: "Forced Expiratory Volume in 1 Second", "Forced Vital Capacity". |
| 13 | RECAT | Category for Respiratory Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to categorize observations across subjects. |
| 14 | RESCAT | Subcategory for Respiratory Test | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization. |
| 15 | REPOS | Position of Subject During Observation | Char | Record Qualifier | Perm | C71148 |  |  |  | Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING". |
| 16 | REORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the procedure measurement or finding as originally received or collected. |
| 17 | REORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. The unit for REORRES and REORREF. |
| 18 | REORREF | Reference Result in Original Units | Char | Variable Qualifier | Perm |  |  |  |  | Reference result for continuous measurements in original units. Should be collected only for continuous results. |
| 19 | RESTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from REORRES in a standard format or in standard units. RESTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in RESTRESN. |
| 20 | RESTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from RESTRESC. RESTRESN should store all numeric test results or findings. |
| 21 | RESTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized unit used for RESTRESC, RESTRESN and RESTREFN. |
| 22 | RESTREFC | Character Reference Result | Char | Variable Qualifier | Perm |  |  |  |  | Reference value for the result or finding copied or derived from --ORREF in a standard format. |
| 23 | RESTREFN | Numeric Reference Result in Std Units | Num | Variable Qualifier | Perm |  |  |  |  | Reference result for continuous measurements in standard units. Should be populated only for continuous results. |
| 24 | RESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a test was not done or a measurement was not taken. Should be null if a result exists in REORRES. |
| 25 | REREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with RESTAT when value is "NOT DONE". |
| 26 | RELOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. Examples: "LUNG", "BRONCHUS". |
| 27 | RELAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Side of the body used to collect measurement. Examples: "RIGHT", "LEFT". |
| 28 | REDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 29 | REMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method used to create the result. |
| 30 | RELOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 31 | REBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be Y or null. Note that REBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 32 | REDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record. Should be "Y" or null. Records that represent the average of other records, or that do not come from the CRF, or are not as originally collected or received are examples of records that would be derived for the submission datasets. If REDRVFL = "Y", then REORRES could be null, with RESTRESC and (if numeric) RESTRESN having the derived value. |
| 33 | REEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| 34 | REEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in REEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". |
| 35 | REREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |  |  |  | The instance number of a test that is repeated within a given time frame for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Example: multiple measurements of pulmonary function. |
| 36 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 37 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 38 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 39 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 40 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 41 | REDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of procedure or test. |
| 42 | REDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 43 | RETPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See RETPTNUM and RETPTREF. Examples: "START", "5 MINUTES POST". |
| 44 | RETPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of RETPT to aid in sorting. |
| 45 | REELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to a planned fixed reference (RETPTREF). Not a clock time or a date/time variable, but an interval, represented as ISO duration. Examples: "-PT15M" to represent 15 minutes prior to the reference time point indicated by RETPTREF, "PT8H" to represent 8 hours after the reference time point represented by RETPTREF. |
| 46 | RETPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by REELTM, RETPTNUM, and RETPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 47 | RERFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by RETPTREF. |

## RP (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | RP | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | RPSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1. |
| 5 | RPGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. Also used to link together a block of related records in the Trial Summary dataset. |
| 6 | RPREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external identifier (e.g., lab specimen ID, UUID for an ECG waveform or a medical image). |
| 7 | RPSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. Example: Preprinted line identifier on a CRF. |
| 8 | RPLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 9 | RPLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 10 | RPTESTCD | Short Name of Reproductive Test | Char | Topic | Req | C106479 |  |  |  | Short character value for RPTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Examples: "CHILDPOT", "BCMETHOD", "MENARAGE". |
| 11 | RPTEST | Name of Reproductive Test | Char | Synonym Qualifier | Req | C106478 |  |  |  | Long name For RPTESTCD. Examples: "Childbearing Potential", "Birth Control Method", "Menarche Age". |
| 12 | RPCAT | Category for Reproductive Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. Example: "No use case to date, but values would be relative to reproduction tests grouping". |
| 13 | RPSCAT | Subcategory for Reproductive Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of RPCAT values. Example: "No use case to date, but values would be relative to reproduction tests grouping". |
| 14 | RPORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. Examples: "120", "<1", "POS". |
| 15 | RPORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Unit for RPORRES. Examples: "in", "LB", "kg/L". |
| 16 | RPSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from RPORRES, in a standard format or in standard units. RPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in RPSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in RPORRES, and these results effectively have the same meaning, they could be represented in standard format in RPSTRESC as "NEGATIVE". |
| 17 | RPSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from RPSTRESC. RPSTRESN should store all numeric test results or findings. |
| 18 | RPSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for RPSTRESC and RPSTRESN. Example: "mol/L". |
| 19 | RPSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 20 | RPREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with RPSTAT when value is "NOT DONE". |
| 21 | RPLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 22 | RPBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that RPBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 23 | RPDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record. The value should be "Y" or null. Records which represent the average of other records or which do not come from the CRF are examples of records that would be derived for the submission datasets. If RPDRVFL = "Y", then RPORRES may be null, with RPSTRESC and (if numeric) RPSTRESN having the derived value. |
| 24 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 25 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 26 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 27 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 28 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 29 | RPDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of an observation. |
| 30 | RPDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 31 | RPDUR | Duration | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration of an event, intervention, or finding represented in ISO 8601 character format. Used only if collected on the CRF and not derived. |
| 32 | RPTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. |
| 33 | RPTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 34 | RPELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time in ISO 8601 character format relative to a planned fixed reference (RPTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 35 | RPTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by RPELTM, RPTPTNUM, and RPTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 36 | RPRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by RPTPTREF in ISO 8601 character format. |

## RS (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | RS | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | RSSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number. |
| 5 | RSGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records within a subject in a domain. |
| 6 | RSREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external identifier. |
| 7 | RSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 8 | RSLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | An identifier used to link the response assessment to the related measurement record in another domain which was used to determine the response result. LNKID values group records within USUBJID. |
| 9 | RSLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | A grouping identifier used to link the response assessment to a group of measurement/assessment records which were used in the assessment of the response. LNKGRP values group records within USUBJID. |
| 10 | RSTESTCD | Assessment Short Name | Char | Topic | Req | C96782 |  |  |  | Short name of the TEST in RSTEST. The value in RSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). RSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TRGRESP", "NTRGRESP", "OVRLRESP", "SYMPTDTR", "CPS0102". \n There are separate codelists used for RSTESTCD where the choice depends on the value of RSCAT. Codelist "ONCRTSCD" is used for oncology response criteria (when RSCAT is a term in codelist "ONCRSCAT"). Examples: TRGRESP, "NTRGRESP, "OVRLRESP". For Clinical Classifications (when RSCAT is a term in codelist "CCCAT"), QRS Naming Rules apply. These instruments have individual dedicated terminology codelists. |
| 11 | RSTEST | Assessment Name | Char | Synonym Qualifier | Req | C96781 |  |  |  | Verbatim name of the response assessment. The value in RSTEST cannot be longer than 40 characters. \n There are separate codelists used for RSTEST where the choice depends on the value of RSCAT. Codelist "ONCRTS" is used for oncology response criteria (when RSCAT is a term in codelist "ONCRSCAT"). Examples: "Target Response", "Non-target Response", "Overall Response", "Symptomatic Deterioration". For Clinical Classifications (when RSCAT is a term in codelist "CCCAT"), QRS Naming Rules apply. These instruments have individual dedicated terminology codelists. |
| 12 | RSCAT | Category for Assessment | Char | Grouping Qualifier | Exp | C124298; C118971 |  |  |  | Used to define a category of related records across subjects. Examples: "RECIST 1.1", "CHILD-PUGH CLASSIFICATION". There are separate codelists used for RSCAT where the choice depends on whether the related records are about an oncology response criterion or another clinical classification. \n RSCAT is required for clinical classifications other than oncology response criteria. |
| 13 | RSSCAT | Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of RSCAT values. |
| 14 | RSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the response assessment as originally received, collected, or calculated. |
| 15 | RSORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Unit for RSORRES. |
| 16 | RSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C96785 |  |  |  | Contains the result value for the response assessment, copied, or derived from RSORRES in a standard format or standard units. RSSTRESC should store all results or findings in character format. \n For Clinical Classifications, this may be a score. |
| 17 | RSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from --STRESC. --STRESN should store all numeric test results or findings. For Clinical Classifications, this may be a score. |
| 18 | RSSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for RSSTRESC and RSSTRESN. |
| 19 | RSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate the response assessment was not performed. Should be null if a result exists in RSORRES. |
| 20 | RSREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a response assessment was not performed. Examples: "All target tumors not evaluated", "Subject does not have non-target tumors". Used in conjunction with RSSTAT when value is "NOT DONE". |
| 21 | RSNAM | Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | The name or identifier of the vendor that performed the response assessment. This column can be left null when the investigator provides the complete set of data in the domain. |
| 22 | RSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C158113 |  |  |  | Method of the test or examination. |
| 23 | RSLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. \n When a clinical classification is assessed at multiple times, including baseline, RSLOBXFL should be included in the dataset. |
| 24 | RSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that --BLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 25 | RSDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 26 | RSEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST". \n RSEVAL is expected for oncology response criteria. It can be left null when the investigator provides the complete set of data in the domain. However, the column should contain no null values when data from one or more independent assessors is included, meaning that the rows attributed to the investigator should contain a value of "INVESTIGATOR". |
| 27 | RSEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in RSEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumptions in Section 6.3.9.3.1, Disease Response Use Case. |
| 28 | RSACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATOR") provides an evaluation of response, this flag identifies the record that is considered to be the accepted evaluation. |
| 29 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 30 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 31 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 32 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 33 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 34 | RSDTC | Date/Time of Assessment | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of the assessment represented in ISO 8601 character format. |
| 35 | RSDY | Study Day of Assessment | Num | Timing | Perm |  |  |  |  | Study day of the assessment, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| 36 | RSTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See RSTPTNUM and RSTPTREF. |
| 37 | RSTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 38 | RSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time in ISO 8601 character format relative to a planned fixed reference (RSTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 39 | RSTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by RSELTM, RSTPTNUM, and RSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 40 | RSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by RSTPTREF in ISO 8601 character format. |
| 41 | RSEVLINT | Evaluation Interval | Char | Timing | Perm |  |  | ISO 8601 duration or interval |  | Duration of interval associated with an observation such as a finding RSTESTCD, represented in ISO 8601 character format. Example: "-P2M" to represent a period of the past 2 months as the evaluation interval. |
| 42 | RSEVINTX | Evaluation Interval Text | Char | Timing | Perm |  |  |  |  | Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS". |
| 43 | RSSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the start of the observation as being before or after the sponsor-defined reference time point defined by variable RSSTTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 44 | RSSTTPT | Start Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by RSSTRTPT. Examples: "2003-12-15", "VISIT 1". |
| 45 | RSENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the end of the observation as being before or after the sponsor-defined reference time point defined by variable RSENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 46 | RSENTPT | End Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by RSENRTPT. Examples: "2003-12-25", "VISIT 2". |

## SC (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | SC | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SCSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | SCGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | SCSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. |
| 7 | SCTESTCD | Subject Characteristic Short Name | Char | Topic | Req | C74559 |  |  |  | Short name of the measurement, test, or examination described in SCTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SCTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SCTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MARISTAT", "NATORIG". |
| 8 | SCTEST | Subject Characteristic | Char | Synonym Qualifier | Req | C103330 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in SCTEST cannot be longer than 40 characters. Examples: "Marital Status", "National Origin". |
| 9 | SCCAT | Category for Subject Characteristic | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. |
| 10 | SCSCAT | Subcategory for Subject Characteristic | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of the subject characteristic. |
| 11 | SCORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the subject characteristic as originally received or collected. |
| 12 | SCORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original unit in which the data were collected. The unit for SCORRES. |
| 13 | SCSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from SCORRES, in a standard format or standard units. SCSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in SCSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in SCORRES, and these results effectively have the same meaning, they could be represented in standard format in SCSTRESC as "NEGATIVE". |
| 14 | SCSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from SCSTRESC. SCSTRESN should store all numeric test results or findings. |
| 15 | SCSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized unit used for SCSTRESC or SCSTRESN. |
| 16 | SCSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that the measurement was not done. Should be null if a result exists in SCORRES. |
| 17 | SCREASND | Reason Not Performed | Char | Record Qualifier | Perm |  |  |  |  | Describes why the observation has no result. Example: "Subject refused". Used in conjunction with SCSTAT when value is "NOT DONE". |
| 18 | VISITNUM | Visit Number | Num | Timing | Perm |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 19 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 20 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 21 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 22 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time at which the assessment was made. |
| 23 | SCDTC | Date/Time of Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Collection date and time of the subject characteristic represented in ISO 8601 character format. |
| 24 | SCDY | Study Day of Examination | Num | Timing | Perm |  |  |  |  | Study day of collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |

## SS (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | SS | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SSSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | SSGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | SSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the Procedure or Test page. |
| 7 | SSTESTCD | Status Short Name | Char | Topic | Req | C124305 |  |  |  | Short name of the status assessment described in SSTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SSTESTCD cannot contain characters other than letters, numbers, or underscores. Example: "SURVSTAT". |
| 8 | SSTEST | Status Name | Char | Synonym Qualifier | Req | C124306 |  |  |  | Verbatim name of the status assessment used to obtain the finding. The value in SSTEST cannot be longer than 40 characters. Example: "Survival Status". |
| 9 | SSCAT | Category for Assessment | Char | Grouping Qualifier | Perm |  |  |  |  | Used to categorize observations across subjects. |
| 10 | SSSCAT | Subcategory for Assessment | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization. |
| 11 | SSORRES | Result or Finding Original Result | Char | Result Qualifier | Exp |  |  |  |  | Result of the status assessment finding as originally received or collected. |
| 12 | SSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C124304 |  |  |  | Contains the result value for all findings copied or derived from SSORRES, in a standard format. |
| 13 | SSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate a status assessment was not done. Should be null if a result exists in SSORRES. |
| 14 | SSREASND | Reason Assessment Not Performed | Char | Record Qualifier | Perm |  |  |  |  | Describes why an assessment was not performed. Example: "Subject refused". Used in conjunction with SSSTAT when value is "NOT DONE". |
| 15 | SSEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "CAREGIVER", "ADJUDICATION COMMITTEE", "FRIEND". |
| 16 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 17 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 18 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 19 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 20 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the subject status assessment. |
| 21 | SSDTC | Date/Time of Assessment | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date and time of the subject status assessment represented in ISO 8601 character format. |
| 22 | SSDY | Study Day of Assessment | Num | Timing | Perm |  |  |  |  | Study day of the subject status assessment, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |

## TR (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TR | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | TRSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number. |
| 5 | TRGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records within a subject in a domain. |
| 6 | TRREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external identifier. |
| 7 | TRSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 8 | TRLNKID | Link ID | Char | Identifier | Exp |  |  |  |  | Identifier used to link the assessment result records to the individual tumor/lesion identification record in TU domain. |
| 9 | TRLNKGRP | Link Group | Char | Identifier | Perm |  |  |  |  | Used to group and link all of the measurement/assessment records used in the assessment of the response record in the RS domain. |
| 10 | TRTESTCD | Tumor/Lesion Assessment Short Name | Char | Topic | Req | C96779 |  |  |  | Short name of the TEST in TRTEST. TRTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TUMSTATE", "DIAMETER", "LESSCIND", "LESRVIND". See assumption 3. |
| 11 | TRTEST | Tumor/Lesion Assessment Test Name | Char | Synonym Qualifier | Req | C96778 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in TRTEST cannot be longer than 40 characters. Examples: "Tumor State", "Diameter", "Volume", "Lesion Success Indicator", "Lesion Revascularization Indicator". See assumption 3. |
| 12 | TRORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the tumor/lesion measurement/assessment as originally received or collected. |
| 13 | TRORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Original units in which the data were collected. The unit for TRORRES. Example: "mm". |
| 14 | TRSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C124309 |  |  |  | Contains the result value for all findings copied or derived from TRORRES, in a standard format or standard units. TRSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in TRSTRESN. |
| 15 | TRSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from TRSTRESC. TRSTRESN should store all numeric test results or findings. |
| 16 | TRSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Standardized unit used for TRSTRESN. |
| 17 | TRSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate a scan/image/physical exam was not performed or a tumor/lesion measurement was not taken. Should be null if a result exists in TRORRES. |
| 18 | TRREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a scan/image/physical exam was not performed or a tumor/lesion measurement was not taken. Examples: "SCAN NOT PERFORMED", "NOT ASSESSABLE: IMAGE OBSCURED TUMOR". Used in conjunction with TRSTAT when value is "NOT DONE". |
| 19 | TRNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | The name or identifier of the vendor that performed the tumor/lesion measurement or assessment. This column can be left null when the investigator provides the complete set of data in the domain. |
| 20 | TRMETHOD | Method Used to Identify the Tumor/Lesion | Char | Record Qualifier | Exp | C85492 |  |  |  | Method used to measure the tumor/lesion/location of interest. Examples: "MRI", "CT SCAN", "PET SCAN", "Coronary angiography". |
| 21 | TRLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| 22 | TRBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that TRBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 23 | TREVAL | Evaluator | Char | Record Qualifier | Exp | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR". |
| 24 | TREVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in TREVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumption 6. |
| 25 | TRACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATION COMMITTEE") provide independent assessments at the same time point, this flag identifies the record that is considered to be the accepted assessment. |
| 26 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 27 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 28 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 29 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 30 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the element in the planned sequence of elements for the arm to which the subject was assigned. |
| 31 | TRDTC | Date/Time of Tumor/Lesion Measurement | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | The date of the scan/image/physical exam. TRDTC does not represent the date that the image was read to identify tumors/lesions. TRDTC also does not represent the VISIT date. |
| 32 | TRDY | Study Day of Tumor/Lesion Measurement | Num | Timing | Perm |  |  |  |  | Study day of the scan/image/physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |

## TU (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TU | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | TUSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number. |
| 5 | TUGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records within a subject in a domain. Can be used to group split or merged tumors/lesions which have been identified. |
| 6 | TUREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external identifier (e.g., medical image ID number). |
| 7 | TUSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 8 | TULNKID | Link ID | Char | Identifier | Exp |  |  |  |  | Identifier used to link identified tumor/lesion/location of interest to the assessment results (in TR domain) over the course of the study. |
| 9 | TULNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 10 | TUTESTCD | Tumor/Lesion ID Short Name | Char | Topic | Req | C96784 |  |  |  | Short name of the TEST in TUTEST. TUTESTCD cannot be longer than 8 characters nor can start with a number. TUTESTCD cannot contain characters other than letters, numbers, or underscores. Example: "TUMIDENT". See assumption 3. |
| 11 | TUTEST | Tumor/Lesion ID Test Name | Char | Synonym Qualifier | Req | C96783 |  |  |  | Verbatim name of the test for the tumor/lesion identification. The value in TUTEST cannot be longer than 40 characters. Example: "Tumor identification". See assumption 3. |
| 12 | TUORRES | Tumor/Lesion ID Result | Char | Result Qualifier | Exp |  |  |  |  | Result of the tumor/lesion identification. The result of tumor/lesion identification is a classification of the identified tumor/lesion. Example: When TUTESTCD = "TUMIDENT", values of TUORRES might be "TARGET", "NON-TARGET", "NEW", or "BENIGN ABNORMALITY". |
| 13 | TUSTRESC | Tumor/Lesion ID Result Std. Format | Char | Result Qualifier | Exp | C123650 |  |  |  | Contains the result value for all findings copied or derived from TUORRES in a standard format. |
| 14 | TUNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | The name or identifier of the vendor that performed the tumor/lesion Identification. This column can be left null when the investigator provides the complete set of data in the domain. |
| 15 | TULOC | Location of the Tumor/Lesion | Char | Record Qualifier | Exp | C74456 |  |  |  | Used to specify the anatomical location of the identified tumor/lesion (e.g., "LIVER"). \n Note: When anatomical location is broken down and collected as distinct pieces of data that when combined provide the overall location information (e.g., laterality/directionality/distribution), then additional anatomical location qualifiers should be used. See assumption 3. |
| 16 | TULAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality (e.g., "LEFT", "RIGHT", "BILATERAL"). |
| 17 | TUDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality (e.g., "UPPER", "INTERIOR"). |
| 18 | TUPORTOT | Portion or Totality | Char | Variable Qualifier | Perm | C99075 |  |  |  | Qualifier for anatomical location or specimen further detailing the distribution, which means arrangement of, or apportioning of. Examples: "ENTIRE", "SINGLE", "SEGMENT", "MULTIPLE". |
| 19 | TUMETHOD | Method of Identification | Char | Record Qualifier | Exp | C85492 |  |  |  | Method used to identify the tumor/lesion. Examples: "MRI", "CT SCAN". |
| 20 | TULOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| 21 | TUBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that TUBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 22 | TUEVAL | Evaluator | Char | Record Qualifier | Exp | C78735 |  |  |  | Role of the person who provided the evaluation. Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR". \n This column can be left null when the investigator provides the complete set of data in the domain. However, the column should contain no null values when data from 1 or more independent assessors is included. For example, the rows attributed to the investigator should contain a value of "INVESTIGATOR". |
| 23 | TUEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in --EVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumption 9. |
| 24 | TUACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATION COMMITTEE") provide independent assessments at the same time point, this flag identifies the record that is considered to be the accepted assessment. |
| 25 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 26 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 27 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. Should be an integer. |
| 28 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| 29 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the assessment was made. |
| 30 | TUDTC | Date/Time of Tumor/Lesion Identification | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | TUDTC variable represents the date of the scan/image/physical exam. TUDTC does not represent the date that the image was read to identify tumors. TUDTC also does not represent the VISIT date. |
| 31 | TUDY | Study Day of Tumor/Lesion Identification | Num | Timing | Perm |  |  |  |  | Study day of the scan/image/physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |

## UR (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | UR | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | URSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| 5 | URGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 6 | URREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Optional internal or external identifier (e.g., lab specimen ID, universally unique identifier (UUID) for a medical image). |
| 7 | URSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. Example: Preprinted line identifier. |
| 8 | URLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 9 | URLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 10 | URTESTCD | Short Name of Urinary Test | Char | Topic | Req | C129942 |  |  |  | Short character value for URTEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in URTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). URTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "COUNT", "LENGTH", "RBLDFLW". |
| 11 | URTEST | Name of Urinary Test | Char | Synonym Qualifier | Req | C129941 |  |  |  | Long name For URTESTCD. Examples: "Count", "Length", "Renal Blood Flow". |
| 12 | URTSTDTL | Urinary Test Detail | Char | Variable Qualifier | Perm |  |  |  |  | Further description of URTESTCD and URTEST. |
| 13 | URCAT | Category for Urinary Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. |
| 14 | URSCAT | Subcategory for Urinary Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of URCAT values. |
| 15 | URORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 16 | URORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Unit for URORRES. |
| 17 | URSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from URORRES, in a standard format or in standard units. URSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in URSTRESN. |
| 18 | URSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from URSTRESC. URSTRESN should store all numeric test results or findings. |
| 19 | URSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for URSTRESC and URSTRESN. |
| 20 | URRESCAT | Result Category | Char | Variable Qualifier | Perm |  |  |  |  | Used to categorize the result of a finding. |
| 21 | URSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 22 | URREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with URSTAT when value is "NOT DONE". |
| 23 | URLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |  |  |  | Anatomical location of the subject relevant to the collection of the measurement. |
| 24 | URLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 25 | URDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |  |  |  | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| 26 | URMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of the test or examination. |
| 27 | URLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 28 | URBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | A baseline defined by the sponsor The value should be "Y" or null. Note that URBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 29 | URDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 30 | UREVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| 31 | UREVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in UREVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". |
| 32 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 33 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 34 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 35 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the observation was made. |
| 36 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time at which the observation was made. |
| 37 | URDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of an observation. |
| 38 | URDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 39 | URTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See URTPTNUM and URTPTREF. |
| 40 | URTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 41 | URELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time relative to a planned fixed reference (URTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| 42 | URTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by URELTM, URTPTNUM, and URTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 43 | URRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by URTPTREF. |

## VS (Findings)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | VS | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | VSSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | VSGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | VSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. |
| 7 | VSTESTCD | Vital Signs Test Short Name | Char | Topic | Req | C66741 |  |  |  | Short name of the measurement, test, or examination described in VSTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in VSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). VSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SYSBP", "DIABP", "BMI". |
| 8 | VSTEST | Vital Signs Test Name | Char | Synonym Qualifier | Req | C67153 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in VSTEST cannot be longer than 40 characters. Examples: "Systolic Blood Pressure", "Diastolic Blood Pressure", "Body Mass Index". |
| 9 | VSCAT | Category for Vital Signs | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. |
| 10 | VSSCAT | Subcategory for Vital Signs | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of a measurement or examination. |
| 11 | VSPOS | Vital Signs Position of Subject | Char | Record Qualifier | Perm | C71148 |  |  |  | Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING". |
| 12 | VSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the vital signs measurement as originally received or collected. |
| 13 | VSORRESU | Original Units | Char | Variable Qualifier | Exp | C66770 |  |  |  | Original units in which the data were collected. The unit for VSORRES. Examples: "in", "LB", "beats/min". |
| 14 | VSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from VSORRES in a standard format or standard units. VSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in VSSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in VSORRES, and these results effectively have the same meaning, they could be represented in standard format in VSSTRESC as "NEGATIVE". |
| 15 | VSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from VSSTRESC. VSSTRESN should store all numeric test results or findings. |
| 16 | VSSTRESU | Standard Units | Char | Variable Qualifier | Exp | C66770 |  |  |  | Standardized unit used for VSSTRESC and VSSTRESN. |
| 17 | VSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a vital sign measurement was not done. Should be null if a result exists in VSORRES. |
| 18 | VSREASND | Reason Not Performed | Char | Record Qualifier | Perm |  |  |  |  | Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with VSSTAT when value is "NOT DONE". |
| 19 | VSLOC | Location of Vital Signs Measurement | Char | Record Qualifier | Perm | C74456 |  |  |  | Location relevant to the collection of vital signs measurement. Example: "ARM" for blood pressure. |
| 20 | VSLAT | Laterality | Char | Result Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 21 | VSLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| 22 | VSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. Note that VSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| 23 | VSDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records or that do not come from the CRF are examples of records that would be derived for the submission datasets. If VSDRVFL = "Y," then VSORRES may be null, with VSSTRESC and (if numeric) VSSTRESN having the derived value. |
| 24 | VSTOX | Toxicity | Char | Variable Qualifier | Perm |  |  |  |  | Description of toxicity quantified by VSTOXGR. The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document. |
| 25 | VSTOXGR | Standard Toxicity Grade | Char | Record Qualifier | Perm |  |  |  |  | Records toxicity grade value using a standard toxicity scale (e.g., NCI CTCAE). If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2"). The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document. |
| 26 | VSCLSIG | Clinically Significant, Collected | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate whether a collected observation is clinically significant based on judgment. |
| 27 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 28 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 29 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 30 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 31 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time at which the assessment was made. |
| 32 | VSDTC | Date/Time of Measurements | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date and time of the vital signs assessment represented in ISO 8601 character format. |
| 33 | VSDY | Study Day of Vital Signs | Num | Timing | Perm |  |  |  |  | Study day of vital signs measurements, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| 34 | VSTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See VSTPTNUM and VSTPTREF. Examples: "START", "5 MIN POST". |
| 35 | VSTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of VSTPT to aid in sorting. |
| 36 | VSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to a planned fixed reference (VSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 Duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by VSTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by VSTPTREF. |
| 37 | VSTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by VSELTM, VSTPTNUM, and VSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 38 | VSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time of the reference time point, VSTPTREF. |

## FA (Findings About)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | FA | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | FASEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | FAGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | FASPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF. |
| 7 | FATESTCD | Findings About Test Short Name | Char | Topic | Req | C101832 |  |  |  | Short name of the measurement, test, or examination described in FATEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in FATESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). FATESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SEV", "OCCUR". Note that controlled terminology is in a FATESTCD general codelist and in several therapeutic area-specific codelists. |
| 8 | FATEST | Findings About Test Name | Char | Synonym Qualifier | Req | C101833 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in FATEST cannot be longer than 40 characters. Examples: "Severity/Intensity", "Occurrence". Note that controlled terminology is in a FATEST general codelist and in several therapeutic area-specific codelists. |
| 9 | FAOBJ | Object of the Observation | Char | Record Qualifier | Req |  |  |  |  | Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the term (e.g., "Acne") describing a clinical sign or symptom that is being measured by a severity test; an event (e.g., "VOMIT, where the volume of vomit is being measured by a VOLUME test). |
| 10 | FACAT | Category for Findings About | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. Examples: "GERD", "PRE-SPECIFIED AE". |
| 11 | FASCAT | Subcategory for Findings About | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of FACAT. |
| 12 | FAORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the test as originally received or collected. |
| 13 | FAORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Original units in which the data were collected. The unit for FAORRES. |
| 14 | FASTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from FAORRES in a standard format or standard units. FASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in FASTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in FAORRES, and these results effectively have the same meaning; they could be represented in standard format in FASTRESC as "NEGATIVE". |
| 15 | FASTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from FASTRESC. FASTRESN should store all numeric test results or findings. |
| 16 | FASTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized unit used for FASTRESC and FASTRESN. |
| 17 | FASTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that the measurement was not done. Should be null if a result exists in FAORRES. |
| 18 | FAREASND | Reason Not Performed | Char | Record Qualifier | Perm |  |  |  |  | Describes why a question was not answered. Example: "Subject refused". Used in conjunction with FASTAT when value is "NOT DONE". |
| 19 | FALOC | Location of the Finding About | Char | Record Qualifier | Perm | C74456 |  |  |  | Used to specify the location of the clinical evaluation. Example: "ARM". |
| 20 | FALAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 21 | FALOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 22 | FABLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. The value should be "Y" or null. Note that FABLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 23 | FAEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR". |
| 24 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | 1. Clinical encounter number. \n 2. Numeric version of VISIT, used for sorting. |
| 25 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | 1. Protocol-defined description of clinical encounter. \n 2. May be used in addition to VISITNUM and/or VISITDY. |
| 26 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 27 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 28 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP". |
| 29 | FADTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of findings assessment represented in ISO 8601 character format. |
| 30 | FADY | Study Day of Collection | Num | Timing | Perm |  |  |  |  | 1. Study day of collection, measured as integer days. \n 2. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |

## SR (Findings About)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | SR | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SRSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | SRGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | SRREFID | Reference ID | Char | Identifier | Perm |  |  |  |  | Internal or external specimen identifier. Example: "Specimen ID". |
| 7 | SRSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 8 | SRTESTCD | Skin Response Test or Exam Short Name | Char | Topic | Req | C112024 |  |  |  | Short name of the measurement, test, or examination described in SRTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SRTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SRTESTCD cannot contain characters other than letters, numbers, or underscores. |
| 9 | SRTEST | Skin Response Test or Examination Name | Char | Synonym Qualifier | Req | C112023 |  |  |  | Verbatim name of the test or examination used to obtain the measurement or finding. The value in SRTEST cannot be longer than 40 characters. Example: "Wheal Diameter". |
| 10 | SROBJ | Object of the Observation | Char | Record Qualifier | Req |  |  |  |  | Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the dose of the immunogenic material or the allergen associated with the response (e.g., "Johnson Grass IgE 0.15 BAU mL"). |
| 11 | SRCAT | Category for Test | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values across subjects. |
| 12 | SRSCAT | Subcategory for Test | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of SRCAT values. |
| 13 | SRORRES | Results or Findings in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Results of measurement or finding as originally received or collected. |
| 14 | SRORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Original units in which the data were collected. The unit for SRORRES. Example: "mm". |
| 15 | SRSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings copied or derived from SRORRES, in a standard format or in standard units. SRSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in SRSTRESN. |
| 16 | SRSTRESN | Numeric Results/Findings in Std. Units | Num | Result Qualifier | Exp |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from SRSTRESC. SRSTRESN should store all numeric test results or findings. |
| 17 | SRSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |  |  |  | Standardized units used for SRSTRESC and SRSTRESN. Example: "mm". |
| 18 | SRSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate exam not done. Should be null if a result exists in SRORRES. |
| 19 | SRREASND | Reason Not Done | Char | Record Qualifier | Perm |  |  |  |  | Describes why a measurement or test was not performed. Used in conjunction with SRSTAT when value is "NOT DONE". |
| 20 | SRNAM | Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the laboratory or vendor who provided the test results. |
| 21 | SRSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734 |  |  |  | Defines the types of specimen used for a measurement. Example: "SKIN". |
| 22 | SRLOC | Location Used for Measurement | Char | Record Qualifier | Perm | C74456 |  |  |  | Location relevant to the collection of the measurement. |
| 23 | SRLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |  |  |  | Qualifier for anatomical location further detailing laterality of intervention administration. Examples: "RIGHT", "LEFT", "BILATERAL". |
| 24 | SRMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |  |  |  | Method of test or examination. Examples: "ELISA", "EIA", "MICRONEUTRALIZATION ASSAY", "PLAQUE REDUCTION NEUTRALIZATION ASSAY". |
| 25 | SRLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| 26 | SRBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. The value should be "Y" or null. Note that SRBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| 27 | SREVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of person who provided evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR". |
| 28 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 29 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| 30 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 31 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm. |
| 32 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", and "FOLLOW-UP". |
| 33 | SRDTC | Date/Time of Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Collection date and time of an observation represented in ISO 8601. |
| 34 | SRDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to sponsor- defined RFSTDTC in Demographics. |
| 35 | SRTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See SRTPTNUM and SRTPTREF. Examples: "START", "5 MIN POST". |
| 36 | SRTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of SRTPT to aid in sorting. |
| 37 | SRELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to a fixed time point reference (SRTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by SRTPTREF. |
| 38 | SRTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by SRELTM, SRTPTNUM, and SRTPT. Example: "INTRADERMAL INJECTION". |
| 39 | SRRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time of the reference time point, SRTPTREF. |

## AG (Interventions)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | AG | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | AGSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | AGGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | AGSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the procedure or test page. |
| 7 | AGLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains.This may be a one-to-one or a one-to-many relationship. |
| 8 | AGLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains.This will usually be a many-to-one relationship. |
| 9 | AGTRT | Reported Agent Name | Char | Topic | Req |  |  |  |  | Verbatim medication name that is either preprinted or collected on a CRF. |
| 10 | AGMODIFY | Modified Reported Name | Char | Synonym Qualifier | Perm |  |  |  |  | If AGTRT is modified to facilitate coding, then AGMODIFY will contain the modified text. |
| 11 | AGDECOD | Standardized Agent Name | Char | Synonym Qualifier | Perm |  |  |  |  | Standardized or dictionary-derived text description of AGTRT or AGMODIFY. Equivalent to the generic medication name in WHO Drug. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. If an intervention term does not have a decode value in the dictionary, then AGDECOD will be left blank. |
| 12 | AGCAT | Category for Agent | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of agent. Examples: "CHALLENGE AGENT", "PET TRACER". |
| 13 | AGSCAT | Subcategory for Agent | Char | Grouping Qualifier | Perm |  |  |  |  | Further categorization of agent. |
| 14 | AGPRESP | AG Pre-Specified | Char | Variable Qualifier | Perm | C66742 |  |  |  | Used to indicate whether ("Y"/null) information about the use of a specific agent was solicited on the CRF. |
| 15 | AGOCCUR | AG Occurrence | Char | Record Qualifier | Perm | C66742 |  |  |  | When the use of specific agent is solicited, AGOCCUR is used to indicate whether ("Y"/"N") use of the agent occurred. Values are null for agents not specifically solicited. |
| 16 | AGSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question about a prespecified agent was not answered. Should be null or have a value of "NOT DONE". |
| 17 | AGREASND | Reason Procedure Agent Not Collected | Char | Record Qualifier | Perm |  |  |  |  | Describes the reason a response to a question about the occurrence of a procedure agent was not collected. Used in conjunction with AGSTAT when value is "NOT DONE". |
| 18 | AGCLAS | Agent Class | Char | Variable Qualifier | Perm |  |  |  |  | Drug class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, follow guidance in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit AGCLAS. |
| 19 | AGCLASCD | Agent Class Code | Char | Variable Qualifier | Perm |  |  |  |  | Class code corresponding to AGCLAS. Drug class. May be obtained from coding. When coding to a single class, populate with class code. If using a dictionary and coding to multiple classes, follow guidance in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit AGCLASCD. |
| 20 | AGDOSE | Dose per Administration | Num | Record Qualifier | Perm |  |  |  |  | Amount of AGTRT taken. |
| 21 | AGDOSTXT | Dose Description | Char | Record Qualifier | Perm |  |  |  |  | Dosing amounts or a range of dosing information collected in text form. Units may be stored in AGDOSU. Examples: "200-400", "15-20". |
| 22 | AGDOSU | Dose Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Units for AGDOSE and AGDOSTXT. Examples: "ng", "mg", "mg/kg". |
| 23 | AGDOSFRM | Dose Form | Char | Variable Qualifier | Perm | C66726 |  |  |  | Dose form for AGTRT. Examples: "TABLET", "AEROSOL". |
| 24 | AGDOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier | Perm | C71113 |  |  |  | Usually expressed as the number of repeated administrations of AGDOSE within a specific time period. Example: "ONCE". |
| 25 | AGROUTE | Route of Administration | Char | Variable Qualifier | Perm | C66729 |  |  |  | Route of administration for AGTRT. Example: "ORAL". |
| 26 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | 1. Clinical encounter number. \n 2. Numeric version of VISIT, used for sorting. |
| 27 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | 1. Protocol-defined description of clinical encounter. \n 2. May be used in addition to VISITNUM and/or VISITDY. |
| 28 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of the visit based upon RFSTDTC in Demographics. |
| 29 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the agent administration started. |
| 30 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the agent administration started. |
| 31 | AGSTDTC | Start Date/Time of Agent | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | The date/time when administration of the treatment indicated by AGTRT and the dosing variables began. |
| 32 | AGENDTC | End Date/Time of Agent | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | The date/time when administration of the treatment indicated by AGTRT and the dosing variables ended. |
| 33 | AGSTDY | Study Day of Start of Agent | Num | Timing | Perm |  |  |  |  | Study day of start of agent relative to the sponsor-defined RFSTDTC. |
| 34 | AGENDY | Study Day of End of Agent | Num | Timing | Perm |  |  |  |  | Study day of end of agent relative to the sponsor-defined RFSTDTC. |
| 35 | AGDUR | Duration of Agent | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration for an agent episode. Used only if collected on the CRF and not derived from start and end date/times. |
| 36 | AGSTRF | Start Relative to Reference Period | Char | Timing | Perm | C66728 |  |  |  | Describes the start of the agent relative to sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into AGSTRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 37 | AGENRF | End Relative to Reference Period | Char | Timing | Perm | C66728 |  |  |  | Describes the end of the agent relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into AGENRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 38 | AGSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the start of the agent as being before or after the sponsor-defined reference time point defined by variable AGSTTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 39 | AGSTTPT | Start Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the reference point referred to by AGSTRTPT. Examples: "2003-12-15", "VISIT 1". |
| 40 | AGENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the end of the agent as being before or after the reference time point defined by variable AGENTPT. Identifies the end of the agent as being before or after the sponsor-defined reference time point defined by variable AGENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 41 | AGENTPT | End Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the reference point referred to by AGENRTPT. Examples: "2003-12-25", "VISIT 2". |

## CM (Interventions)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | CM | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | CMSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | CMGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | CMSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. Example: a number preprinted on the CRF as an explicit line identifier or record identifier defined in the sponsor's operational database. Example: line number on a concomitant medication page. |
| 7 | CMTRT | Reported Name of Drug, Med, or Therapy | Char | Topic | Req |  |  |  |  | Verbatim medication name that is either preprinted or collected on a CRF. |
| 8 | CMMODIFY | Modified Reported Name | Char | Synonym Qualifier | Perm |  |  |  |  | If CMTRT is modified to facilitate coding, then CMMODIFY will contain the modified text. |
| 9 | CMDECOD | Standardized Medication Name | Char | Synonym Qualifier | Perm |  |  |  |  | Standardized or dictionary-derived text description of CMTRT or CMMODIFY. Equivalent to the generic drug name in WHO Drug. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. If an intervention term does not have a decode value in the dictionary, then CMDECOD will be left blank. |
| 10 | CMCAT | Category for Medication | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of medications/treatment. Examples: "PRIOR", "CONCOMITANT", "ANTI-CANCER MEDICATION", "GENERAL CONMED". |
| 11 | CMSCAT | Subcategory for Medication | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of medications/treatment. Examples: "CHEMOTHERAPY", "HORMONAL THERAPY", "ALTERNATIVE THERAPY". |
| 12 | CMPRESP | CM Pre-specified | Char | Variable Qualifier | Perm | C66742 |  |  |  | Used to indicate whether ("Y"/null) information about the use of a specific medication was solicited on the CRF. |
| 13 | CMOCCUR | CM Occurrence | Char | Record Qualifier | Perm | C66742 |  |  |  | When the use of a specific medication is solicited. CMOCCUR is used to indicate whether ("Y"/"N") use of the medication occurred. Values are null for medications not specifically solicited. |
| 14 | CMSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question about the occurrence of a prespecified intervention was not answered. Should be null or have a value of "NOT DONE". |
| 15 | CMREASND | Reason Medication Not Collected | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with CMSTAT when value is "NOT DONE". |
| 16 | CMINDC | Indication | Char | Record Qualifier | Perm |  |  |  |  | Denotes why a medication was taken or administered. Examples: "NAUSEA", "HYPERTENSION". |
| 17 | CMCLAS | Medication Class | Char | Variable Qualifier | Perm |  |  |  |  | Drug class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, then follow Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit CMCLAS. |
| 18 | CMCLASCD | Medication Class Code | Char | Variable Qualifier | Perm |  |  |  |  | Class code corresponding to CMCLAS. Drug class. May be obtained from coding. When coding to a single class, populate with class code. If using a dictionary and coding to multiple classes, then follow Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit CMCLASCD. |
| 19 | CMDOSE | Dose per Administration | Num | Record Qualifier | Perm |  |  |  |  | Amount of CMTRT given. Not populated when CMDOSTXT is populated. |
| 20 | CMDOSTXT | Dose Description | Char | Record Qualifier | Perm |  |  |  |  | Dosing amounts or a range of dosing information collected in text form. Units may be stored in CMDOSU. Examples: "200-400", "15-20". Not populated when CMDOSE is populated. |
| 21 | CMDOSU | Dose Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Units for CMDOSE, CMDOSTOT, or CMDOSTXT. Examples: "ng", "mg", "mg/kg". |
| 22 | CMDOSFRM | Dose Form | Char | Variable Qualifier | Perm | C66726 |  |  |  | Dose form for CMTRT. Examples: "TABLET", "LOTION". |
| 23 | CMDOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier | Perm | C71113 |  |  |  | Usually expressed as the number of repeated administrations of CMDOSE within a specific time period. Examples: "BID" (twice daily), "Q12H" (every 12 hours). |
| 24 | CMDOSTOT | Total Daily Dose | Num | Record Qualifier | Perm |  |  |  |  | Total daily dose of CMTRT using the units in CMDOSU. Used when dosing is collected as total daily dose. Total dose over a period other than day could be recorded in a separate supplemental qualifier variable. |
| 25 | CMDOSRGM | Intended Dose Regimen | Char | Record Qualifier | Perm |  |  |  |  | Text description of the (intended) schedule or regimen for the Intervention. Example: "TWO WEEKS ON, TWO WEEKS OFF". |
| 26 | CMROUTE | Route of Administration | Char | Variable Qualifier | Perm | C66729 |  |  |  | Route of administration for the intervention. Examples: "ORAL", "INTRAVENOUS". |
| 27 | CMADJ | Reason for Dose Adjustment | Char | Record Qualifier | Perm |  |  |  |  | Describes reason or explanation of why a dose is adjusted. Examples: "ADVERSE EVENT", "INSUFFICIENT RESPONSE", "NON-MEDICAL REASON". |
| 28 | CMRSDISC | Reason the Intervention Was Discontinued | Char | Record Qualifier | Perm |  |  |  |  | When dosing of a treatment is recorded over multiple successive records, this variable is applicable only for the (chronologically) last record for the treatment. |
| 29 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the medication administration started. Null for medications that started before study participation. |
| 30 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the medication administration. Null for medications that started before study participation. |
| 31 | CMSTDTC | Start Date/Time of Medication | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Start date/time of the medication administration represented in ISO 8601 character format. |
| 32 | CMENDTC | End Date/Time of Medication | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | End date/time of the medication administration represented in ISO 8601 character format. |
| 33 | CMSTDY | Study Day of Start of Medication | Num | Timing | Perm |  |  |  |  | Study day of start of medication relative to the sponsor-defined RFSTDTC. |
| 34 | CMENDY | Study Day of End of Medication | Num | Timing | Perm |  |  |  |  | Study day of end of medication relative to the sponsor-defined RFSTDTC. |
| 35 | CMDUR | Duration | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration for a treatment episode. Used only if collected on the CRF and not derived from start and end date/times. |
| 36 | CMSTRF | Start Relative to Reference Period | Char | Timing | Perm | C66728 |  |  |  | Describes the start of the medication relative to sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR" was collected, this information may be translated into CMSTRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 37 | CMENRF | End Relative to Reference Period | Char | Timing | Perm | C66728 |  |  |  | Describes the end of the medication relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING, or "CONTINUING" was collected, this information may be translated into CMENRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 38 | CMSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the start of the medication as being before or after the sponsor-defined reference time point defined by variable CMSTTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 39 | CMSTTPT | Start Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by CMSTRTPT. Examples: "2003-12-15", "VISIT 1". |
| 40 | CMENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the end of the medication as being before or after the sponsor-defined reference time point defined by variable CMENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 41 | CMENTPT | End Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by CMENRTPT. Examples: "2003-12-25", "VISIT 2". |

## EC (Interventions)

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

## EX (Interventions)

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

## ML (Interventions)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | ML | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | MLSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | MLGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | MLSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. Examples: a number preprinted on the CRF as an explicit line identifier, record identifier defined in the sponsor's operational database. |
| 7 | MLTRT | Name of Meal | Char | Topic | Req |  |  |  |  | Verbatim food product name that is either preprinted or collected on a CRF. |
| 8 | MLCAT | Category for Meal | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of MLTRT values. |
| 9 | MLSCAT | Subcategory for Meal | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of MLCAT values. |
| 10 | MLPRESP | ML Pre-specified | Char | Variable Qualifier | Perm | C66742 |  |  |  | Used when a specific meal is prespecified on a CRF. Values should be "Y" or null. |
| 11 | MLOCCUR | ML Occurrence | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to record whether a prespecified meal occurred when information about the occurrence of a specific meal is solicited. |
| 12 | MLSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate when a question about the occurrence of a prespecified meal was not answered. Should be null or have a value of "NOT DONE". |
| 13 | MLREASND | Reason Meal Not Collected | Char | Record Qualifier | Perm |  |  |  |  | Describes the reason a response to a question about the occurrence of a meal was not collected. Used in conjunction with MLSTAT when value is "NOT DONE". |
| 14 | MLDOSE | Dose | Num | Record Qualifier | Perm |  |  |  |  | Amount of MLTRT consumed. Not populated when MLDOSTXT is populated. |
| 15 | MLDOSTXT | Dose Description | Char | Record Qualifier | Perm |  |  |  |  | Amount description of MLTRT consumed, collected in text form. Not populated when MLDOSE is populated. Examples: "<1 per day", "200-400". |
| 16 | MLDOSU | Dose Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Units for MLDOSE, MLDOSTOT, or MLDOSTXT. |
| 17 | MLDOSFRM | Dose Form | Char | Variable Qualifier | Perm | C66726 |  |  |  | Dosage form for MLTRT. Example: "BAR, CHEWABLE". |
| 18 | VISITNUM | Visit Number | Num | Timing | Perm |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 19 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 20 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 21 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the meal started. |
| 22 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the meal. |
| 23 | MLDTC | Date/Time of Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Collection date and time of the meal represented in ISO 8601 character format. |
| 24 | MLSTDTC | Start Date/Time of Meal | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Start date/time of the meal represented in ISO 8601 character format. |
| 25 | MLENDTC | End Date/Time of Meal | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | End date/time of the meal represented in ISO 8601 character format. |
| 26 | MLDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |  |  |  | Actual study day of the visit/collection expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 27 | MLSTDY | Study Day of Start of Meal | Num | Timing | Perm |  |  |  |  | Actual study day of start of the meal expressed in integer days relative to sponsor-defined RFSTDTC in Demographics. |
| 28 | MLENDY | Study Day of End of Meal | Num | Timing | Perm |  |  |  |  | Actual study day of end of the meal expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 29 | MLDUR | Duration of Meal | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration of the meal represented in ISO 8601 character format. Used only if collected on the CRF and not derived. |
| 30 | MLTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point. See MLTPTNUM and MLTPTREF. |
| 31 | MLTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numeric version of planned time point used in sorting. |
| 32 | MLELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned elapsed time (in ISO 8601) relative to the planned fixed reference (MLTPTREF). This variable is useful when there are repetitive measures. Not a clock time or a date/time variable. Represented as an ISO 8601 duration. |
| 33 | MLTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Description of the fixed reference point referred to by MLELTM, MLTPTNUM, and MLTPT. |
| 34 | MLRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by MLTPTREF in ISO 8601 character format. |
| 35 | MIDS | Disease Milestone Instance Name | Char | Timing | Perm |  |  |  |  | The name of a specific instance of a disease milestone type (MIDSTYPE) described in the Trial Disease Milestones dataset. This should be unique within a subject. Used only in conjunction with RELMIDS and MIDSDTC. |
| 36 | RELMIDS | Temporal Relation to Milestone Instance | Char | Timing | Perm |  |  |  |  | The temporal relationship of the observation to the disease milestone instance name in MIDS. Examples: "IMMEDIATELY BEFORE", "AT TIME OF", "AFTER". |
| 37 | MIDSDTC | Disease Milestone Instance Date/Time | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | The start date/time of the disease milestone instance name in MIDS, in ISO 8601 format. |

## PR (Interventions)

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

## SU (Interventions)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | SU | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SUSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | SUGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a block of related records in a single domain for a subject. |
| 6 | SUSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Tobacco & Alcohol Use CRF page. |
| 7 | SUTRT | Reported Name of Substance | Char | Topic | Req |  |  |  |  | Substance name. Examples: "CIGARETTES", "COFFEE". |
| 8 | SUMODIFY | Modified Substance Name | Char | Synonym Qualifier | Perm |  |  |  |  | If SUTRT is modified, then the modified text is placed here. |
| 9 | SUDECOD | Standardized Substance Name | Char | Synonym Qualifier | Perm |  |  |  |  | Standardized or dictionary-derived text description of SUTRT or SUMODIFY if the sponsor chooses to code the substance use. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. |
| 10 | SUCAT | Category for Substance Use | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of related records. Examples: "TOBACCO", "ALCOHOL", or "CAFFEINE". |
| 11 | SUSCAT | Subcategory for Substance Use | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of substance use. Examples: "CIGARS", "CIGARETTES", "BEER", "WINE". |
| 12 | SUPRESP | SU Pre-Specified | Char | Variable Qualifier | Perm | C66742 |  |  |  | Used to indicate whether ("Y"/null) information about the use of a specific substance was solicited on the CRF. |
| 13 | SUOCCUR | SU Occurrence | Char | Record Qualifier | Perm | C66742 |  |  |  | When the use of specific substances is solicited, SUOCCUR is used to indicate whether ("Y"/"N") a particular prespecified substance was used. Values are null for substances not specifically solicited. |
| 14 | SUSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | When the use of prespecified substances is solicited, the completion status indicates that there was no response to the question about the prespecified substance. When there is no prespecified list on the CRF, then the completion status indicates that substance use was not assessed for the subject. |
| 15 | SUREASND | Reason Substance Use Not Collected | Char | Record Qualifier | Perm |  |  |  |  | Describes the reason substance use was not collected. Used in conjunction with SUSTAT when value of SUSTAT is "NOT DONE". |
| 16 | SUCLAS | Substance Use Class | Char | Variable Qualifier | Perm |  |  |  |  | Substance use class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, then follow Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit SUCLAS. |
| 17 | SUCLASCD | Substance Use Class Code | Char | Variable Qualifier | Perm |  |  |  |  | Code corresponding to SUCLAS. May be obtained from coding. |
| 18 | SUDOSE | Substance Use Consumption | Num | Record Qualifier | Perm |  |  |  |  | Amount of SUTRT consumed. Not populated if SUDOSTXT is populated. |
| 19 | SUDOSTXT | Substance Use Consumption Text | Char | Record Qualifier | Perm |  |  |  |  | Substance use consumption amounts or a range of consumption information collected in text form. Not populated if SUDOSE is populated. |
| 20 | SUDOSU | Consumption Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Units for SUDOSE, SUDOSTOT, or SUDOSTXT. Examples: "oz", "CIGARETTE", "PACK", "g". |
| 21 | SUDOSFRM | Dose Form | Char | Variable Qualifier | Perm | C66726 |  |  |  | Dose form for SUTRT. Examples: "INJECTABLE", "LIQUID", "POWDER". |
| 22 | SUDOSFRQ | Use Frequency Per Interval | Char | Variable Qualifier | Perm | C71113 |  |  |  | Usually expressed as the number of repeated administrations of SUDOSE within a specific time period. Example: "Q24H" (every day). |
| 23 | SUDOSTOT | Total Daily Consumption | Num | Record Qualifier | Perm |  |  |  |  | Total daily use of SUTRT using the units in SUDOSU. Used when dosing is collected as total daily dose. If a sponsor needs to aggregate the data over a period other than daily, then the aggregated total could be recorded in a supplemental qualifier variable. |
| 24 | SUROUTE | Route of Administration | Char | Variable Qualifier | Perm | C66729 |  |  |  | Route of administration for SUTRT. Examples: "ORAL", "INTRAVENOUS". |
| 25 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the arm for the element in which the substance use started. Null for substances that started before study participation. |
| 26 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the start date/time of the substance use. Null for substances that started before study participation. |
| 27 | SUSTDTC | Start Date/Time of Substance Use | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Start date/time of the substance use represented in ISO 8601 character format. |
| 28 | SUENDTC | End Date/Time of Substance Use | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | End date/time of the substance use represented in ISO 8601 character format. |
| 29 | SUSTDY | Study Day of Start of Substance Use | Num | Timing | Perm |  |  |  |  | Study day of start of substance use relative to the sponsor-defined RFSTDTC. |
| 30 | SUENDY | Study Day of End of Substance Use | Num | Timing | Perm |  |  |  |  | Study day of end of substance use relative to the sponsor-defined RFSTDTC. |
| 31 | SUDUR | Duration of Substance Use | Char | Timing | Perm |  |  | ISO 8601 duration |  | Collected duration of substance use in ISO 8601 format. Used only if collected on the CRF and not derived from start and end date/times. |
| 32 | SUSTRF | Start Relative to Reference Period | Char | Timing | Perm | C66728 |  |  |  | Describes the start of the substance use relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR" was collected, this information may be translated into SUSTRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 33 | SUENRF | End Relative to Reference Period | Char | Timing | Perm | C66728 |  |  |  | Describes the end of the substance use with relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into SUENRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| 34 | SUSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the start of the substance as being before or after the reference time point defined by variable SUSTTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7 , Use of Relative Timing Variables. |
| 35 | SUSTTPT | Start Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the reference point referred to by SUSTRTPT. Examples: "2003-12-15", "VISIT 1". |
| 36 | SUENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |  |  |  | Identifies the end of the substance as being before or after the reference time point defined by variable SUENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7 , Use of Relative Timing Variables. |
| 37 | SUENTPT | End Reference Time Point | Char | Timing | Perm |  |  |  |  | Description or date/time in ISO 8601 character format of the reference point referred to by SUENRTPT. Examples: "2003-12-25", "VISIT 2". |

## RELREC (Relationship)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | RDOMAIN | Related Domain Abbreviation | Char | Identifier | Req | C66734 |  |  |  | Abbreviation for the domain of the parent record(s). |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Exp |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | IDVAR | Identifying Variable | Char | Identifier | Req |  |  |  |  | Name of the identifying variable in the general-observation-class dataset that identifies the related record(s). Examples: --SEQ, --GRPID. |
| 5 | IDVARVAL | Identifying Variable Value | Char | Identifier | Exp |  |  |  |  | Value of identifying variable described in IDVAR. If --SEQ is the variable being used to describe this record, then the value of --SEQ would be entered here. |
| 6 | RELTYPE | Relationship Type | Char | Record Qualifier | Exp | C78737 |  |  |  | Identifies the hierarchical level of the records in the relationship. Values should be either "ONE" or "MANY". Used only when identifying a relationship between datasets (as described in Section 8.3, Relating Datasets). |
| 7 | RELID | Relationship Identifier | Char | Record Qualifier | Req |  |  |  |  | Unique value within USUBJID that identifies the relationship. All records for the same USUBJID that have the same RELID are considered related/associated. RELID can be any value the sponsor chooses, and is only meaningful within the RELREC dataset to identify the related/associated domain records. |

## RELSPEC (Relationship)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 3 | REFID | Specimen ID | Char | Identifier | Req |  |  |  |  | Specimen identifier, unique within USUBJID. |
| 4 | SPEC | Specimen Type | Char | Variable Qualifier | Perm | C78734; C111114 |  |  |  | Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE", "SOFT TISSUE". |
| 5 | PARENT | Specimen Parent | Char | Identifier | Exp |  |  |  |  | Identifies the REFID of the parent of a specimen to support tracking its genealogy. |
| 6 | LEVEL | Specimen Level | Num | Variable Qualifier | Req |  |  |  |  | Identifies the generation number of the sample where the collected sample is considered the first generation. |

## RELSUB (Relationship)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | USUBJID | Unique Subject Identifier | Char | Identifier | Exp |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. Either USUBJID or POOLID must be populated. |
| 3 | POOLID | Pool Identifier | Char | Identifier | Perm |  |  |  |  | Identifier used to identify a pool of subjects. If POOLID is entered, POOLDEF records must exist for each subject in the pool and USUBJID must be null. Either USUBJID or POOLID must be populated. |
| 4 | RSUBJID | Related Subject or Pool Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to identify a related subject or pool of subjects. RSUBJID will be populated with either the USUBJID of the related subject or the POOLID of the related pool. |
| 5 | SREL | Subject Relationship | Char | Record Qualifier | Req | C100130 |  |  |  | Describes the relationship of the subject identified in USUBJID or the pool identified in POOLID to the subject or pool identified in RSUBJID. |

## SUPPQUAL (Relationship)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Study identifier of the parent record(s). |
| 2 | RDOMAIN | Related Domain Abbreviation | Char | Identifier | Req | C66734 |  |  |  | Two-character abbreviation for the domain of the parent record(s). |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. This is the value of USUBJID in the parent record(s). |
| 4 | IDVAR | Identifying Variable | Char | Identifier | Exp |  |  |  |  | Identifying variable in the dataset that identifies the related record(s). Examples: --SEQ, --GRPID. |
| 5 | IDVARVAL | Identifying Variable Value | Char | Identifier | Exp |  |  |  |  | Value of identifying variable of the parent record(s). |
| 6 | QNAM | Qualifier Variable Name | Char | Topic | Req |  |  |  |  | The short name of the qualifier variable, which is used as a column name in a domain view with data from the parent domain. The value in QNAM cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). QNAM cannot contain characters other than letters, numbers, or underscores. This will often be the column name in the sponsor's operational dataset. |
| 7 | QLABEL | Qualifier Variable Label | Char | Synonym Qualifier | Req |  |  |  |  | This is the long name or label associated with QNAM. The value in QLABEL cannot be longer than 40 characters. This will often be the column label in the sponsor's original dataset. |
| 8 | QVAL | Data Value | Char | Result Qualifier | Req |  |  |  |  | Result of, response to, or value associated with QNAM. A value for this column is required; no records can be in SUPP-- with a null value for QVAL. |
| 9 | QORIG | Origin | Char | Record Qualifier | Req |  |  |  |  | Because QVAL can represent a mixture of collected (on a CRF), derived, or assigned items, QORIG is used to indicate the origin of this data. Examples: "CRF", "Assigned", "Derived". See Section 4.1.8, Origin Metadata. |
| 10 | QEVAL | Evaluator | Char | Record Qualifier | Exp | C78735 |  |  |  | Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain objectively collected or derived data. Examples: "ADJUDICATION COMMITTEE", "STATISTICIAN", "DATABASE ADMINISTRATOR", "CLINICAL COORDINATOR". |

## CO (Special-Purpose)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | CO | Two-character abbreviation for the domain. |
| 3 | RDOMAIN | Related Domain Abbreviation | Char | Record Qualifier | Perm | C66734 |  |  |  | Two-character abbreviation for the domain of the parent record(s). Null for comments collected on a general comments or additional information CRF page. |
| 4 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 5 | COSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence Number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 6 | IDVAR | Identifying Variable | Char | Record Qualifier | Perm |  |  |  |  | Identifying variable in the parent dataset that identifies the record(s) to which the comment applies. Examples AESEQ or CMGRPID. Used only when individual comments are related to domain records. Null for comments collected on separate CRFs. |
| 7 | IDVARVAL | Identifying Variable Value | Char | Record Qualifier | Perm |  |  |  |  | Value of identifying variable of the parent record(s). Used only when individual comments are related to domain records. Null for comments collected on separate CRFs. |
| 8 | COREF | Comment Reference | Char | Record Qualifier | Perm |  |  |  |  | Sponsor-defined reference associated with the comment. May be the CRF page number (e.g., 650), or a module name (e.g., DEMOG), or a combination of information that identifies the reference (e.g. 650-VITALS-VISIT 2). |
| 9 | COVAL | Comment | Char | Topic | Req |  |  |  |  | The text of the comment. Text over 200 characters can be added to additional columns COVAL1-COVALn. See Assumption 3. |
| 10 | COEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |  |  |  | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Example: "INVESTIGATOR". |
| 11 | COEVALID | Evaluator Identifier | Char | Record Qualifier | Perm | C96777 |  |  |  | Used to distinguish multiple evaluators with the same role recorded in --EVAL. Examples: "RADIOLOGIST", "RADIOLOGIST 1", "RADIOLOGIST 2". |
| 12 | CODTC | Date/Time of Comment | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time of comment on dedicated comment form. Should be null if this is a child record of another domain or if comment date was not collected. |
| 13 | CODY | Study Day of Comment | Num | Timing | Perm |  |  |  |  | Study day of the comment, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. |

## DM (Special-Purpose)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | DM | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. This must be a unique value, and could be a compound identifier formed by concatenating STUDYID-SITEID-SUBJID. |
| 4 | SUBJID | Subject Identifier for the Study | Char | Topic | Req |  |  |  |  | Subject identifier, which must be unique within the study. Often the ID of the subject as recorded on a CRF. |
| 5 | RFSTDTC | Subject Reference Start Date/Time | Char | Record Qualifier | Exp |  |  | ISO 8601 datetime or interval |  | Reference start date/time for the subject in ISO 8601 character format. Usually equivalent to date/time when subject was first exposed to study treatment. See assumption 9 for additional detail on when RFSTDTC may be null. |
| 6 | RFENDTC | Subject Reference End Date/Time | Char | Record Qualifier | Exp |  |  | ISO 8601 datetime or interval |  | Reference end date/time for the subject in ISO 8601 character format. Usually equivalent to the date/time when subject was determined to have ended the trial, and often equivalent to date/time of last exposure to study treatment. Required for all randomized subjects; null for screen failures or unassigned subjects. |
| 7 | RFXSTDTC | Date/Time of First Study Treatment | Char | Record Qualifier | Exp |  |  | ISO 8601 datetime or interval |  | First date/time of exposure to any protocol-specified treatment or therapy, equal to the earliest value of EXSTDTC. |
| 8 | RFXENDTC | Date/Time of Last Study Treatment | Char | Record Qualifier | Exp |  |  | ISO 8601 datetime or interval |  | Last date/time of exposure to any protocol-specified treatment or therapy, equal to the latest value of EXENDTC (or the latest value of EXSTDTC if EXENDTC was not collected or is missing). |
| 9 | RFCSTDTC | Date/Time of First Challenge Agent Admin | Char | Record Qualifier | Perm |  |  | ISO 8601 datetime or interval |  | Used only when protocol specifies a challenge agent to induce a condition that the investigational treatment is intended to cure, mitigate, treat, or prevent. Equal to the earliest value of AGSTDTC for the challenge agent. |
| 10 | RFCENDTC | Date/Time of Last Challenge Agent Admin | Char | Record Qualifier | Perm |  |  | ISO 8601 datetime or interval |  | Used only when protocol specifies a challenge agent to induce a condition that the investigational treatment is intended to cure, mitigate, treat, or prevent. Equal to the latest value of AGENDTC for the challenge agent (or the latest value of AGSTDTC if AGENDTC was not collected or is missing). |
| 11 | RFICDTC | Date/Time of Informed Consent | Char | Record Qualifier | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of informed consent in ISO 8601 character format. This will be the same as the date of informed consent in the Disposition domain, if that protocol milestone is documented. Would be null only in studies not collecting the date of informed consent. |
| 12 | RFPENDTC | Date/Time of End of Participation | Char | Record Qualifier | Exp |  |  | ISO 8601 datetime or interval |  | Date/time when subject ended participation or follow-up in a trial, as defined in the protocol, in ISO 8601 character format. Should correspond to the last known date of contact. Examples include completion date, withdrawal date, last follow-up, date recorded for lost to follow up, and death date. |
| 13 | DTHDTC | Date/Time of Death | Char | Record Qualifier | Exp |  |  | ISO 8601 datetime or interval |  | Date/time of death for any subject who died, in ISO 8601 format. Should represent the date/time that is captured in the clinical-trial database. |
| 14 | DTHFL | Subject Death Flag | Char | Record Qualifier | Exp | C66742 |  |  |  | Indicates the subject died. Should be "Y" or null. Should be populated even when the death date is unknown. |
| 15 | SITEID | Study Site Identifier | Char | Record Qualifier | Req |  |  |  |  | Unique identifier for a site within a study. |
| 16 | INVID | Investigator Identifier | Char | Record Qualifier | Perm |  |  |  |  | An identifier to describe the Investigator for the study. May be used in addition to SITEID. Not needed if SITEID is equivalent to INVID. |
| 17 | INVNAM | Investigator Name | Char | Synonym Qualifier | Perm |  |  |  |  | Name of the investigator for a site. |
| 18 | BRTHDTC | Date/Time of Birth | Char | Record Qualifier | Perm |  |  | ISO 8601 datetime or interval |  | Date/time of birth of the subject. |
| 19 | AGE | Age | Num | Record Qualifier | Exp |  |  |  |  | Age expressed in AGEU. May be derived from RFSTDTC and BRTHDTC, but BRTHDTC may not be available in all cases (due to subject privacy concerns). |
| 20 | AGEU | Age Units | Char | Variable Qualifier | Exp | C66781 |  |  |  | Units associated with AGE. |
| 21 | SEX | Sex | Char | Record Qualifier | Req | C66731 |  |  |  | Sex of the subject. |
| 22 | RACE | Race | Char | Record Qualifier | Exp | C74457 |  |  |  | Race of the subject. Sponsors should refer to the FDA guidance2 regarding the collection of race. See assumption below regarding RACE. |
| 23 | ETHNIC | Ethnicity | Char | Record Qualifier | Perm | C66790 |  |  |  | The ethnicity of the subject. Sponsors should refer to the FDA guidance1 regarding the collection of ethnicity. |
| 24 | ARMCD | Planned Arm Code | Char | Record Qualifier | Exp |  |  |  |  | ARMCD is limited to 20 characters. It is not subject to the character restrictions that apply to TESTCD. The maximum length of ARMCD is longer than for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20. If the subject was not assigned to a trial arm, ARMCD is null and ARMNRS is populated. \n With the exception of studies which use multistage arm assignments, must be a value of ARMCD in the Trial Arms dataset. |
| 25 | ARM | Description of Planned Arm | Char | Synonym Qualifier | Exp |  |  |  |  | Name of the arm to which the subject was assigned. If the subject was not assigned to an arm, ARM is null and ARMNRS is populated. \n With the exception of studies which use multistage arm assignments, must be a value of ARM in the Trial Arms dataset. |
| 26 | ACTARMCD | Actual Arm Code | Char | Record Qualifier | Exp |  |  |  |  | Code of actual arm. ACTARMCD is limited to 20 characters. It is not subject to the character restrictions that apply to TESTCD. The maximum length of ACTARMCD is longer than for other short variables to accommodate the kind of values that are likely to be needed for crossover trials. \n With the exception of studies which use multistage arm assignments, must be a value of ARMCD in the Trial Arms dataset. \n If the subject was not assigned to an arm or followed a course not described by any planned arm, ACTARMCD is null and ARMNRS is populated. |
| 27 | ACTARM | Description of Actual Arm | Char | Synonym Qualifier | Exp |  |  |  |  | Description of actual arm. \n With the exception of studies which use multistage arm assignments, must be a value of ARM in the Trial Arms dataset. \n If the subject was not assigned to an arm or followed a course not described by any planned arm, ACTARM is null and ARMNRS is populated. |
| 28 | ARMNRS | Reason Arm and/or Actual Arm is Null | Char | Record Qualifier | Exp | C142179 |  |  |  | A coded reason that arm variables (ARM and ARMCD) and/or actual arm variables (ACTARM and ACTARMCD) are null. Examples: "SCREEN FAILURE", "NOT ASSIGNED", "ASSIGNED, NOT TREATED", "UNPLANNED TREATMENT". It is assumed that if the arm and actual arm variables are null, the same reason applies to both arm and actual arm. |
| 29 | ACTARMUD | Description of Unplanned Actual Arm | Char | Record Qualifier | Exp |  |  |  |  | A description of actual treatment for a subject who did not receive treatment described in a planned trial arm. |
| 30 | COUNTRY | Country | Char | Record Qualifier | Req |  |  |  |  | Country of the investigational site in which the subject participated in the trial. \n \n Generally represented using ISO 3166-1 Alpha-3. Note that regulatory agency specific requirements (e.g., US FDA) may require other terminologies; in such cases, follow regulatory requirements. |
| 31 | DMDTC | Date/Time of Collection | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time of demographic data collection. |
| 32 | DMDY | Study Day of Collection | Num | Timing | Perm |  |  |  |  | Study day of collection measured as integer days. |

## SE (Special-Purpose)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | SE | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SESEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness of subject records within a domain. Should be assigned to be consistent chronological order. |
| 5 | ETCD | Element Code | Char | Topic | Req |  |  |  |  | 1. ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name. \n 2. If an encountered element differs from the planned element to the point that it is considered a new element, then use "UNPLAN" as the value for ETCD to represent this element. |
| 6 | ELEMENT | Description of Element | Char | Synonym Qualifier | Perm |  |  |  |  | The name of the element. If ETCD has a value of "UNPLAN", then ELEMENT should be null. |
| 7 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |  |  |  | Number that gives the planned order of the element within the subject's assigned trial arm. |
| 8 | EPOCH | Epoch | Char | Timing | Perm | C99079 |  |  |  | Epoch associated with the element in the planned sequence of elements for the arm to which the subject was assigned. |
| 9 | SESTDTC | Start Date/Time of Element | Char | Timing | Req |  |  | ISO 8601 datetime or interval |  | Start date/time for an element for each subject. |
| 10 | SEENDTC | End Date/Time of Element | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | End date/time for an element for each subject. |
| 11 | SESTDY | Study Day of Start of Element | Num | Timing | Perm |  |  |  |  | Study day of start of element relative to the sponsor-defined RFSTDTC. |
| 12 | SEENDY | Study Day of End of Element | Num | Timing | Perm |  |  |  |  | Study day of end of element relative to the sponsor-defined RFSTDTC. |
| 13 | SEUPDES | Description of Unplanned Element | Char | Synonym Qualifier | Perm |  |  |  |  | Description of what happened to the subject during an unplanned element. Used only if ETCD has the value of "UNPLAN". |

## SM (Special-Purpose)

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

## SV (Special-Purpose)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | SV | Two-character abbreviation for the domain most relevant to the observation. The domain abbreviation is also used as a prefix for variables to ensure uniqueness when datasets are merged. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | VISITNUM | Visit Number | Num | Topic | Req |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 5 | VISIT | Visit Name | Char | Synonym Qualifier | Perm |  |  |  |  | Protocol-defined description of a clinical encounter. |
| 6 | SVPRESP | Pre-specified | Char | Variable Qualifier | Exp | C66742 |  |  |  | Used to indicate whether the visit was planned (i.e., visits specified in the TV domain). Value is "Y" for planned visits, null for unplanned visits. |
| 7 | SVOCCUR | Occurrence | Char | Record Qualifier | Exp | C66742 |  |  |  | Used to record whether a planned visit occurred. The value is null for unplanned visits. |
| 8 | SVREASOC | Reason for Occur Value | Char | Record Qualifier | Perm |  |  |  |  | The reason for the value in SVOCCUR. If SVOCCUR="N", SVREASOC is the reason the visit did not occur. |
| 9 | SVCNTMOD | Contact Mode | Char | Record Qualifier | Perm | C171445 |  |  |  | The way in which the visit was conducted. Examples: "IN PERSON", "TELEPHONE CALL", "IVRS". |
| 10 | SVEPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicates whether the visit was changed due to an epidemic or pandemic. |
| 11 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 12 | SVSTDTC | Start Date/Time of Observation | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Start date/time of an observation represented in IS0 8601 character format. |
| 13 | SVENDTC | End Date/Time of Observation | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | End date/time of the observation represented in IS0 8601 character format. |
| 14 | SVSTDY | Study Day of Start of Observation | Num | Timing | Perm |  |  |  |  | Actual study day of start of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 15 | SVENDY | Study Day of End of Observation | Num | Timing | Perm |  |  |  |  | Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 16 | SVUPDES | Description of Unplanned Visit | Char | Record Qualifier | Perm |  |  |  |  | Description of what happened to the subject during an unplanned visit. Only populated for unplanned visits. |

## OI (Study Reference)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | OI | Two-character abbreviation for the domain. |
| 3 | NHOID | Non-host Organism Identifier | Char | Identifier | Req |  |  |  |  | Sponsor-defined identifier for a non-host organism. NHOID should be populated with an intuitive name based on the identity of the organism as reported by the lab. It must be unique for each unique organism as defined by the specific values of the organism's entire known taxonomy described by pairs of OIPARMCD and OIVAL . |
| 4 | OISEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to given to ensure uniqueness within a parameter within an organism (NHOID) within dataset. |
| 5 | OIPARMCD | Non-host Organism ID Element Short Name | Char | Topic | Req | C179591 |  |  |  | Short name of the taxon being described. Examples: "GROUP", "GENTYP", "SUBTYP". |
| 6 | OIPARM | Non-host Organism ID Element Name | Char | Synonym Qualifier | Req | C179590 |  |  |  | Name of the taxon being described. Examples: "Group", "Genotype", "Subtype". |
| 7 | OIVAL | Non-host Organism ID Element Value | Char | Result Qualifier | Req |  |  |  |  | Value for the taxon in OIPARMCD/OIPARM for the organism identified by NHOID. |

## TA (Trial Design)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TA | Two-character abbreviation for the domain. |
| 3 | ARMCD | Planned Arm Code | Char | Topic | Req |  |  |  |  | ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than that for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20. |
| 4 | ARM | Description of Planned Arm | Char | Synonym Qualifier | Req |  |  |  |  | Name given to an arm or treatment group. |
| 5 | TAETORD | Planned Order of Element within Arm | Num | Timing | Req |  |  |  |  | Number that gives the order of the element within the arm. |
| 6 | ETCD | Element Code | Char | Record Qualifier | Req |  |  |  |  | ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name. |
| 7 | ELEMENT | Description of Element | Char | Synonym Qualifier | Perm |  |  |  |  | The name of the element. The same element may occur more than once within an arm. |
| 8 | TABRANCH | Branch | Char | Rule | Exp |  |  |  |  | Condition subject met, at a "branch" in the trial design at the end of this element, to be included in this arm (e.g., "Randomization to DRUG X"). |
| 9 | TATRANS | Transition Rule | Char | Rule | Exp |  |  |  |  | If the trial design allows a subject to transition to an element other than the next element in sequence, then the conditions for transitioning to those other elements, and the alternative element sequences, are specified in this rule (e.g., "Responders go to washout"). |
| 10 | EPOCH | Epoch | Char | Timing | Req | C99079 |  |  |  | Name of the trial epoch with which this element of the arm is associated. |

## TD (Trial Design)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TD | Two-character abbreviation for the domain. |
| 3 | TDORDER | Sequence of Planned Assessment Schedule | Num | Timing | Req |  |  |  |  | A number given to ensure ordinal sequencing of the planned assessment schedules within a trial. |
| 4 | TDANCVAR | Anchor Variable Name | Char | Timing | Req |  |  |  |  | A reference to the date variable name that provides the start point from which the planned disease assessment schedule is measured. This must be a referenced from the ADaM ADSL dataset (e.g., "ANCH1DT"). Note: TDANCVAR will contain the name of a reference date variable. |
| 5 | TDSTOFF | Offset from the Anchor | Char | Timing | Req |  |  | ISO 8601 duration |  | A fixed offset from the date provided by the variable referenced in TDANCVAR. This is used when the timing of planned cycles does not start on the exact day referenced in the variable indicated in TDANCVAR. The value of this variable will be either zero or a positive value and will be represented in ISO 8601 character format. |
| 6 | TDTGTPAI | Planned Assessment Interval | Char | Timing | Req |  |  | ISO 8601 duration |  | The planned interval between disease assessments represented in ISO 8601 character format. |
| 7 | TDMINPAI | Planned Assessment Interval Minimum | Char | Timing | Req |  |  | ISO 8601 duration |  | The lower limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format. |
| 8 | TDMAXPAI | Planned Assessment Interval Maximum | Char | Timing | Req |  |  | ISO 8601 duration |  | The upper limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format. |
| 9 | TDNUMRPT | Maximum Number of Actual Assessments | Num | Record Qualifier | Req |  |  |  |  | This variable must represent the maximum number of actual assessments for the analysis that this disease assessment schedule describes. In a trial where the maximum number of assessments is not defined explicitly in the protocol (e.g., assessments occur until death), TDNUMRPT should represent the maximum number of disease assessments that support the efficacy analysis encountered by any subject across the trial at that point in time. |

## TE (Trial Design)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TE | Two-character abbreviation for the domain. |
| 3 | ETCD | Element Code | Char | Topic | Req |  |  |  |  | ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name. |
| 4 | ELEMENT | Description of Element | Char | Synonym Qualifier | Req |  |  |  |  | The name of the element. |
| 5 | TESTRL | Rule for Start of Element | Char | Rule | Req |  |  |  |  | Describes condition for beginning element. |
| 6 | TEENRL | Rule for End of Element | Char | Rule | Perm |  |  |  |  | Describes condition for ending element. Either TEENRL or TEDUR must be present for each element. |
| 7 | TEDUR | Planned Duration of Element | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned duration of element in ISO 8601 format. Used when the rule for ending the element is applied after a fixed duration. |

## TI (Trial Design)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TI | Two-character abbreviation for the domain. |
| 3 | IETESTCD | Incl/Excl Criterion Short Name | Char | Topic | Req |  |  |  |  | Short name IETEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). IETESTCD cannot contain characters other than letters, numbers, or underscores. The prefix "IE" is used to ensure consistency with the IE domain. |
| 4 | IETEST | Inclusion/Exclusion Criterion | Char | Synonym Qualifier | Req |  |  |  |  | Full text of the inclusion or exclusion criterion. The prefix "IE" is used to ensure consistency with the IE domain. |
| 5 | IECAT | Inclusion/Exclusion Category | Char | Grouping Qualifier | Req | C66797 |  |  |  | Used for categorization of the inclusion or exclusion criteria. |
| 6 | IESCAT | Inclusion/Exclusion Subcategory | Char | Grouping Qualifier | Perm |  |  |  |  | A further categorization of the exception criterion. Can be used to distinguish criteria for a sub-study or to categorize as major or minor exceptions. Examples: "MAJOR", "MINOR". |
| 7 | TIRL | Inclusion/Exclusion Criterion Rule | Char | Rule | Perm |  |  |  |  | Rule that expresses the criterion in computer-executable form. See Assumption 4. |
| 8 | TIVERS | Protocol Criteria Versions | Char | Record Qualifier | Perm |  |  |  |  | The number of this version of the Inclusion/Exclusion criteria. May be omitted if there is only 1 version. |

## TM (Trial Design)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TM | Two-character abbreviation for the domain, which must be TM. |
| 3 | MIDSTYPE | Disease Milestone Type | Char | Topic | Req |  |  |  |  | The type of disease milestone. Example: "HYPOGLYCEMIC EVENT". |
| 4 | TMDEF | Disease Milestone Definition | Char | Variable Qualifier | Req |  |  |  |  | Definition of the disease milestone. |
| 5 | TMRPT | Disease Milestone Repetition Indicator | Char | Record Qualifier | Req | C66742 |  |  |  | Indicates whether this is a disease milestone that can occur only once ("N") or a type of disease milestone that can occur multiple times ("Y"). |

## TS (Trial Design)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TS | Two-character abbreviation for the domain. |
| 3 | TSSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number given to ensure uniqueness within a parameter. Allows inclusion of multiple records for the same TSPARMCD. |
| 4 | TSGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to tie together a group of related records. |
| 5 | TSPARMCD | Trial Summary Parameter Short Name | Char | Topic | Req | C66738 |  |  |  | TSPARMCD (the companion to TSPARM) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that TSPARMCD will need to serve as variable names. Examples: "AGEMIN", "AGEMAX". |
| 6 | TSPARM | Trial Summary Parameter | Char | Synonym Qualifier | Req | C67152 |  |  |  | Term for the trial summary parameter. The value in TSPARM cannot be longer than 40 characters. Examples: "Planned Minimum Age of Subjects", "Planned Maximum Age of Subjects". |
| 7 | TSVAL | Parameter Value | Char | Result Qualifier | Exp |  |  |  |  | Value of TSPARM. Example: "ASTHMA" when TSPARM value is "Trial Indication". TSVAL can only be null when TSVALNF is populated. Text over 200 characters can be added to additional columns TSVAL1-TSVALn. See Assumption 8. |
| 8 | TSVALNF | Parameter Value Null Flavor | Char | Result Qualifier | Perm |  |  | ISO 21090 NullFlavor |  | Null flavor for the value of TSPARM, to be populated only if TSVAL is null. |
| 9 | TSVALCD | Parameter Value Code | Char | Result Qualifier | Exp |  |  |  |  | This is the code of the term in TSVAL. For example, "6CW7F3G59X" is the code for gabapentin; "C49488" is the code for Y. The length of this variable can be longer than 8 to accommodate the length of the external terminology. |
| 10 | TSVCDREF | Name of the Reference Terminology | Char | Result Qualifier | Exp | C66788 |  |  |  | The name of the reference terminology from which TSVALCD is taken. For example; CDISC CT, SNOMED, ISO 8601. |
| 11 | TSVCDVER | Version of the Reference Terminology | Char | Result Qualifier | Exp |  |  |  |  | The version number of the reference terminology, if applicable. |

## TV (Trial Design)

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TV | Two-character abbreviation for the domain. |
| 3 | VISITNUM | Visit Number | Num | Topic | Req |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 4 | VISIT | Visit Name | Char | Synonym Qualifier | Req |  |  |  |  | Description of clinical encounter. This is often defined in the protocol. Used in addition to VISITNUM and/or VISITDY as a text description of the clinical encounter. |
| 5 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Due to its sequential nature, used for sorting. |
| 6 | ARMCD | Planned Arm Code | Char | Record Qualifier | Exp |  |  |  |  | 1. ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20. \n 2. If the timing of visits for a trial does not depend on which arm a subject is in, then ARMCD should be null. |
| 7 | ARM | Description of Planned Arm | Char | Synonym Qualifier | Perm |  |  |  |  | 1. Name given to an arm or treatment group. \n 2. If the timing of visits for a trial does not depend on which arm a subject is in, then Arm should be left blank. |
| 8 | TVSTRL | Visit Start Rule | Char | Rule | Req |  |  |  |  | Rule describing when the visit starts, in relation to the sequence of elements. |
| 9 | TVENRL | Visit End Rule | Char | Rule | Perm |  |  |  |  | Rule describing when the visit ends, in relation to the sequence of elements. |
