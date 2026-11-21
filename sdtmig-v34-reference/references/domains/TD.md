# TD — Trial Disease Assessments

**Class:** Trial Design  
**Structure:** One record per planned constant assessment period

| Variable Order | Variable Name | Variable Label | Type | Role | Core | CDISC CT Codelist Code(s) | Codelist Submission Value(s) | Described Value Domain(s) | Value List | CDISC Notes |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |  |  |  | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req |  |  |  | TD | Two-character abbreviation for the domain. |
| 3 | TDORDER | Sequence of Planned Assessment Schedule | Num | Timing | Req |  |  |  |  | A number given to ensure ordinal sequencing of the planned assessment schedules within a trial. |
| 4 | TDANCVAR | Anchor Variable Name | Char | Timing | Req |  |  |  |  | A reference to the date variable name that provides the start point from which the planned disease assessment schedule is measured. This must be a referenced from the ADaM ADSL dataset (e.g., "ANCH1DT"). Note: TDANCVAR will contain the name of a reference date variable. |
| 5 | TDSTOFF | Offset from the Anchor | Char | Timing | Req |  |  | ISO 8601 duration |  | A fixed offset from the date provided by the variable referenced in TDANCVAR. This is used when the timing of planned cycles does not start on the exact day referenced in the variable indicated in TDANCVAR. The value of this variable will be either zero or a positive value and will be represented in ISO 8601 character format. |
| 6 | TDTGTPAI | Planned Assessment Interval | Char | Timing | Req |  |  | ISO 8601 duration |  | The planned interval between disease assessments represented in ISO 8601 character format. |
| 7 | TDMINPAI | Planned Assessment Interval Minimum | Char | Timing | Req |  |  | ISO 8601 duration |  | The lower limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format. |
| 8 | TDMAXPAI | Planned Assessment Interval Maximum | Char | Timing | Req |  |  | ISO 8601 duration |  | The upper limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format. |
| 9 | TDNUMRPT | Maximum Number of Actual Assessments | Num | Record Qualifier | Req |  |  |  |  | This variable must represent the maximum number of actual assessments for the analysis that this disease assessment schedule describes. In a trial where the maximum number of assessments is not defined explicitly in the protocol (e.g., assessments occur until death), TDNUMRPT should represent the maximum number of disease assessments that support the efficacy analysis encountered by any subject across the trial at that point in time. |
