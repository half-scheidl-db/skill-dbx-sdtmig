# DA — Product Accountability

**Class:** Findings  
**Structure:** One record per product accountability finding per subject

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
