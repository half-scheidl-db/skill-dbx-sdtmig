# TE — Trial Elements

**Class:** Trial Design  
**Structure:** One record per planned Element

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TE | Two-character abbreviation for the domain. |
| 3 | ETCD | Element Code | Char | Topic | Req |  |  |  |  | ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name. |
| 4 | ELEMENT | Description of Element | Char | Synonym Qualifier | Req |  |  |  |  | The name of the element. |
| 5 | TESTRL | Rule for Start of Element | Char | Rule | Req |  |  |  |  | Describes condition for beginning element. |
| 6 | TEENRL | Rule for End of Element | Char | Rule | Perm |  |  |  |  | Describes condition for ending element. Either TEENRL or TEDUR must be present for each element. |
| 7 | TEDUR | Planned Duration of Element | Char | Timing | Perm |  |  | ISO 8601 duration |  | Planned duration of element in ISO 8601 format. Used when the rule for ending the element is applied after a fixed duration. |
