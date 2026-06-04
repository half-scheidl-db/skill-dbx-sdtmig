# TS — Trial Summary

**Class:** Trial Design  
**Structure:** One record per trial summary parameter value

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
