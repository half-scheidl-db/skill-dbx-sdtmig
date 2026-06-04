# GF — Genomics Findings

**Class:** Findings  
**Structure:** One record per finding per observation per biospecimen per subject

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | GF | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |  |  |  | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier for a device. |
| 5 | NHOID | Non-Host Organism Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears. |
| 6 | GFSEQ | Sequence Number | Num | Identifier | Req |  |  |  |  | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| 7 | GFGRPID | Group ID | Char | Identifier | Perm |  |  |  |  | Used to link together a block of related records within a subject in a domain. |
| 8 | GFREFID | Reference ID | Char | Identifier | Exp |  |  |  |  | A unique identifier for the assayed genetic specimen. |
| 9 | GFSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |  |  |  | Sponsor-defined identifier. |
| 10 | GFLNKID | Link ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| 11 | GFLNKGRP | Link Group ID | Char | Identifier | Perm |  |  |  |  | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| 12 | GFTESTCD | Short Name of Genomic Measurement | Char | Topic | Req | C181178 |  |  |  | Short name of the measurement, test, or examination described in GFTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in GFTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). GFTESTCD cannot contain characters other than letters, numbers, or underscores. |
| 13 | GFTEST | Name of Genomic Measurement | Char | Synonym Qualifier | Req | C181179 |  |  |  | Long name for GFTESTCD. The value in GFTEST cannot be longer than 40 characters. |
| 14 | GFTSTDTL | Measurement, Test, or Examination Detail | Char | Variable Qualifier | Perm | C181180 |  |  |  | Description of a reportable qualifying the assessment in GFTESTCD and GFTEST. |
| 15 | GFCAT | Category for Genomic Finding | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a category of topic-variable values. |
| 16 | GFSCAT | Subcategory for Genomic Finding | Char | Grouping Qualifier | Perm |  |  |  |  | Used to define a further categorization of GFCAT values. |
| 17 | GFORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |  |  |  | Result of the measurement or finding as originally received or collected. |
| 18 | GFORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Unit for GFORRES. |
| 19 | GFORREF | Reference Result in Original Units | Char | Variable Qualifier | Perm |  |  |  |  | Reference value for the result or finding as originally received or collected. GFORREF uses the same units as GFORRES, if applicable. |
| 20 | GFSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |  |  |  | Contains the result value for all findings, copied or derived from GFORRES, in a standard format or in standard units. GFSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in GFSTRESN. |
| 21 | GFSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |  |  |  | Used for continuous or numeric results or findings in standard format; copied in numeric format from GFSTRESC. GFSTRESN should store all numeric test results or findings. |
| 22 | GFSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |  |  |  | Standardized units used for GFSTRESC, GFSTRESN, GFSTREFC, and GFSTREFN. |
| 23 | GFSTREFC | Reference Result in Standard Format | Char | Variable Qualifier | Perm |  |  |  |  | Reference value for the result or finding copied or derived from GFORREF in a standard format. |
| 24 | GFSTREFN | Numeric Reference Result in Std Units | Num | Variable Qualifier | Perm |  |  |  |  | Reference value for continuous or numeric results or findings in standard format or in standard units. GFSTREFN uses the same units as GFSTRESN, if applicable. |
| 25 | GFRESCAT | Result Category | Char | Variable Qualifier | Perm |  |  |  |  | Used to categorize the result of a finding. |
| 26 | GFINHERT | Inheritability | Char | Variable Qualifier | Perm | C181177 |  |  |  | Identifies whether the variation can be passed to the next generation. |
| 27 | GFGENREF | Genome Reference | Char | Variable Qualifier | Perm |  |  |  |  | An identifier for the genome reference used to generate the reported result. For example, Genome Reference Consortium Human Build 38 patch release 13 may be represented as "GRCh38.p13". |
| 28 | GFCHROM | Chromosome Identifier | Char | Variable Qualifier | Perm |  |  |  |  | The designation (name or number) of the chromosome or contig on which the variant or other feature appears (e.g., "17"; "X"). |
| 29 | GFSYM | Genomic Symbol | Char | Variable Qualifier | Perm |  |  |  |  | A published symbol for the portion of the genome serving as a locus for the experiment/test. |
| 30 | GFSYMTYP | Genomic Symbol Type | Char | Variable Qualifier | Perm | C181176 |  |  |  | A description of the type of genomic entity that is represented by the published symbol in GFSYM. |
| 31 | GFGENLOC | Genetic Location | Char | Variable Qualifier | Perm |  |  |  |  | Specifies the location within a sequence for the observed value in GFORRES. |
| 32 | GFGENSR | Genetic Sub-Region | Char | Variable Qualifier | Perm |  |  |  |  | The portion of the locus in which the variation was found. Examples: "Exon 15", "Kinase domain". |
| 33 | GFSEQID | Sequence Identifier \n | Char | Variable Qualifier | Perm |  |  |  |  | A unique identifier for the sequence used as the reference to identify the genetic variation in the result. Examples: "NM_001234", "ENSG00000182533", "ENST00000343849.2". |
| 34 | GFPVRID | Published Variant Identifier | Char | Variable Qualifier | Perm |  |  |  |  | A unique identifier for the variation that has been publicly characterized in an external database. Examples: "rs2231142", "COSM41596". |
| 35 | GFCOPYID | Copy Identifier | Char | Variable Qualifier | Perm |  |  |  |  | An arbitrary identifier used to differentiate between copies of a genetic target of interest present on homologous chromosomes. |
| 36 | GFSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |  |  |  | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| 37 | GFREASND | Reason Test Not Done | Char | Record Qualifier | Perm |  |  |  |  | Reason not done. Used in conjunction with GFSTAT when value is "NOT DONE". |
| 38 | GFXFN | External File Path | Char | Record Qualifier | Perm |  |  |  |  | The filename and/or path to external data not stored in the same format and possibly not the same location as the other data for a study. |
| 39 | GFNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |  |  |  | Name or identifier of the vendor that provided the test result. When more than 1 vendor is involved in the generation of the result, additional vendors should be represented as supplemental qualifiers. |
| 40 | GFSPEC | Specimen Material Type | Char | Record Qualifier | Perm | C111114 |  |  |  | Identifies the type of genetic material used for the measurement. |
| 41 | GFMETHOD | Method of Test or Examination | Char | Record Qualifier | Exp | C85492 |  |  |  | The test method by which the examination is performed by the wet lab in order to yield the result reported in the dataset. |
| 42 | GFRUNID | Run ID | Char | Record Qualifier | Perm |  |  |  |  | A unique identifier for a particular run of a test performed by the wet lab on a particular batch of samples. This identifier can be used to distinguish between records for the same test performed at different times. |
| 43 | GFANMETH | Analysis Method | Char | Record Qualifier | Perm | C181181 |  |  |  | The method of secondary processing performed by the dry lab to yield the result reported in the dataset. |
| 44 | GFBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Indicator used to identify a baseline value. Should be "Y" or null. |
| 45 | GFDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |  |  |  | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| 46 | GFLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Perm |  |  |  |  | Indicates the lower limit of quantitation for an assay. Units will be those used for GFSTRESU. |
| 47 | GFREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |  |  |  | The instance number of a test that is repeated within a given timeframe for the same test performed by the wet lab. |
| 48 | VISITNUM | Visit Number | Num | Timing | Exp |  |  |  |  | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 49 | VISIT | Visit Name | Char | Timing | Perm |  |  |  |  | Protocol-defined description of clinical encounter. |
| 50 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |  |  |  | Planned study day of VISIT. Should be an integer. |
| 51 | GFDTC | Date/Time of Specimen Collection | Char | Timing | Exp |  |  | ISO 8601 datetime or interval |  | Date and time of specimen collection. |
| 52 | GFDY | Study Day of Specimen Collection | Num | Timing | Perm |  |  |  |  | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 53 | GFTPT | Planned Time Point Name | Char | Timing | Perm |  |  |  |  | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See GFTPTNUM and GFTPTREF. |
| 54 | GFTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |  |  |  | Numerical version of GFTPT used in sorting. |
| 55 | GFELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm |  |  | ISO 8601 duration |  | Elapsed time relative to a planned fixed reference (GFTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration. |
| 56 | GFTPTREF | Time Point Reference | Char | Timing | Perm |  |  |  |  | Name of the fixed reference point referred to by GFELTM, GFTPTNUM, and GFTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| 57 | GFRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm |  |  | ISO 8601 datetime or interval |  | Date/time for a fixed reference time point defined by GFTPTREF. |
