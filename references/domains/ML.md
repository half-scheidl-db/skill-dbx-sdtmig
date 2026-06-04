# ML — Meal Data

**Class:** Interventions  
**Structure:** One record per food product occurrence or constant intake interval per subject

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
