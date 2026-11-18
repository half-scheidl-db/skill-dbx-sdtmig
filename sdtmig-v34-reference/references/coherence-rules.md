# Coherence rules for synthetic SDTM

Implemented in `scripts/validate_sdtm.py` (rule IDs match). ERROR = the dataset contradicts itself or the standard. WARN = plausible but worth checking. The validator works on any SDTM folder (CSV/parquet), not just generated data.

## Structure (C01–C05)
| ID | Rule |
|---|---|
| C01 | Every Core=Req variable from `variables.csv` is present |
| C02 | Req variables are never null |
| C03 | Core=Exp variables exist as columns (may be null) — WARN |
| C04 | `--SEQ` unique within USUBJID in each domain |
| C05 | DM has exactly one record per subject |

## Referential integrity (C10–C14)
| ID | Rule |
|---|---|
| C10 | Every USUBJID in every domain exists in DM |
| C11 | DM ARMCD / ACTARMCD exist in TA |
| C12 | ARMNRS is populated exactly when ACTARMCD is null (screen failure, assigned not treated) |
| C13 | Scheduled SV VISITNUMs exist in TV |
| C14 | Findings (VS, LB, EG, RS, IE) USUBJID+VISITNUM exist in SV |

## Timeline (C20–C30)
| ID | Rule |
|---|---|
| C20 | All event/finding/exposure dates fall between RFICDTC and RFPENDTC |
| C21 | Nothing is dated after DTHDTC |
| C22 | RFICDTC ≤ RFSTDTC ≤ RFXENDTC ≤ RFPENDTC |
| C23 | RFXSTDTC = first EXSTDTC and RFXENDTC = last EXENDTC |
| C24 | Subjects with ARMNRS (not treated) have no EX |
| C25 | EXENDTC ≥ EXSTDTC |
| C26 | SE elements are contiguous (SEENDTC = next SESTDTC) |
| C27 | The first element starts at RFICDTC |
| C28 | SE ETCD exists in TE |
| C29 | EPOCH on AE/LB/VS/EX/DS equals the SE element in effect on that date |
| C30 | `--DY` is derived from RFSTDTC with no day 0 |

## Disposition, death and AE ↔ EX (C40–C52)
| ID | Rule |
|---|---|
| C40 | At most one end-of-study (DSSCAT=STUDY PARTICIPATION) record per subject |
| C41 | DTHFL=Y ⇔ DTHDTC populated ⇔ DS DEATH record |
| C42 | Screen failures have DS SCREEN FAILURE and no ARMCD |
| C43 | Screen failures have at least one IE record (the criterion not met) — WARN |
| C44 | Subjects whose participation ended before the cutoff have an end-of-study record |
| C45 | Nothing after the data cutoff (TS DCUTDTC) |
| C46 | AEOUT=FATAL ⇒ AESDTH=Y, DTHFL=Y and AEENDTC = DTHDTC |
| C47 | AEENDTC ≥ AESTDTC |
| C48 | AEs without an end date aren't RECOVERED |
| C49 | No dosing after an AE with AEACN=DRUG WITHDRAWN |
| C50 | AEs starting after the end-of-treatment decision have no dose action |
| C51 | End-of-treatment reason ADVERSE EVENT ⇔ an AE with AEACN=DRUG WITHDRAWN on that date |
| C52 | End-of-treatment DS date ≥ RFXENDTC |

## Findings (C60–C64)
| ID | Rule |
|---|---|
| C60 | LBNRIND agrees with LBSTRESN vs LBSTNRLO/LBSTNRHI |
| C61 | `--LOBXFL` at most once per subject and test |
| C62 | The `--LOBXFL` record is on or before first dose |
| C63 | Lab-defined AEs (neutropenia, anaemia, ALT increased, …) have a matching abnormal lab during the AE — WARN |
| C64 | Treatment stopped for PROGRESSIVE DISEASE ⇔ an RS assessment of PD exists |

## Terminology and design (C70–C72)
| ID | Rule |
|---|---|
| C70 | SEX, RACE, ETHNIC, AESEV, AESER, AEOUT, AEACN, NY flags and EPOCH use values from `codelists-common.csv` |
| C71 | DM AGE within TS AGEMIN/AGEMAX |
| C72 | Participation length within TS LENGTH (+14 days visit-window slack), for fixed-duration trials |

## Adding a rule

When a user or reviewer spots an incoherence, add a rule here **and** in `validate_sdtm.py` before fixing the generator. That way the fix is proven and protected against regressions.
