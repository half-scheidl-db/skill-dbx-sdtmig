# CO — Comments

**Class:** Special-Purpose  
**Structure:** One record per comment per subject

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
