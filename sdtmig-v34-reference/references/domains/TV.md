# TV — Trial Visits

**Class:** Trial Design  
**Structure:** One record per planned Visit per Arm

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
