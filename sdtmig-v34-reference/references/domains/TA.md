# TA — Trial Arms

**Class:** Trial Design  
**Structure:** One record per planned Element per Arm

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
