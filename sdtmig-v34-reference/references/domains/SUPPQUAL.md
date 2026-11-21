# SUPPQUAL — Supplemental Qualifiers for [domain name]

**Class:** Relationship  
**Structure:** One record per supplemental qualifier per related parent domain record(s)

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
