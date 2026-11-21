# OI — Non-host Organism Identifiers

**Class:** Study Reference  
**Structure:** One record per taxon per non-host organism

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | OI | Two-character abbreviation for the domain. |
| 3 | NHOID | Non-host Organism Identifier | Char | Identifier | Req |  |  |  |  | Sponsor-defined identifier for a non-host organism. NHOID should be populated with an intuitive name based on the identity of the organism as reported by the lab. It must be unique for each unique organism as defined by the specific values of the organism's entire known taxonomy described by pairs of OIPARMCD and OIVAL . |
| 4 | OISEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to given to ensure uniqueness within a parameter within an organism (NHOID) within dataset. |
| 5 | OIPARMCD | Non-host Organism ID Element Short Name | Char | Topic | Req | C179591 |  |  |  | Short name of the taxon being described. Examples: "GROUP", "GENTYP", "SUBTYP". |
| 6 | OIPARM | Non-host Organism ID Element Name | Char | Synonym Qualifier | Req | C179590 |  |  |  | Name of the taxon being described. Examples: "Group", "Genotype", "Subtype". |
| 7 | OIVAL | Non-host Organism ID Element Value | Char | Result Qualifier | Req |  |  |  |  | Value for the taxon in OIPARMCD/OIPARM for the organism identified by NHOID. |
