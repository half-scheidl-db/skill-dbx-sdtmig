# SE — Subject Elements

**Class:** Special-Purpose  
**Structure:** One record per actual Element per subject

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
