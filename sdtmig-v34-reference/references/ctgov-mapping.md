# ClinicalTrials.gov (API v2) → study spec → SDTM

Record: `GET https://clinicaltrials.gov/api/v2/studies/<NCT>`. Implemented in `scripts/ctgov_to_spec.py`.

## Protocol section

| CT.gov field | Spec field | SDTM target |
|---|---|---|
| `identificationModule.nctId` | `study.source_nct` | TS REGID |
| `identificationModule.officialTitle` | `study.title` | TS TITLE (prefixed `[SYNTHETIC]`) |
| — | `study.studyid` = `SYN-<NCT>` | STUDYID everywhere (never the real ID) |
| `designModule.phases` | `study.phase` | TS TPHASE (`PHASE III TRIAL`, …) |
| `designModule.designInfo.allocation` | `study.randomized` | TS RANDOM |
| `designModule.designInfo.maskingInfo.masking` | `study.blinding` | TS TBLIND |
| `designModule.designInfo.interventionModel` | `study.intervention_model` | TS INTMODEL |
| `designModule.enrollmentInfo.count` | `generation.n_randomized` | TS PLANSUB; DM row count |
| `statusModule.startDateStruct` | `study.study_start` | TS SSTDTC; earliest RFICDTC |
| `statusModule.primaryCompletionDateStruct` | `study.data_cutoff` | TS DCUTDTC; latest date anywhere |
| `conditionsModule.conditions` | `study.conditions`, `medical_history` | TS TDIGRP; MH primary diagnosis; oncology detection → RS |
| `armsInterventionsModule.armGroups` | `arms[]` (`armcd` A, B, …) | TA, TE, DM ARM/ARMCD |
| `armsInterventionsModule.interventions` + arm descriptions | `arms[].interventions` (dose/route/frequency parsed) | EX, TS TRT / COMPTRT |
| `eligibilityModule.minimumAge / maximumAge / sex` | `population.age_min/max`, `population.sex` | DM AGE/SEX, TS AGEMIN/AGEMAX/SEXPOP |
| `eligibilityModule.eligibilityCriteria` (bullets) | `eligibility[]` | TI; IE for screen failures (IETEST ≤ 200 chars) |
| `outcomesModule.*.timeFrame` ("Week 12") | `visits.scheduled` days | TV, SV |
| `contactsLocationsModule.locations[].country` | `sites[]` (ISO 3166 alpha-3, site count) | DM SITEID, COUNTRY |

## Results section (only if `hasResults`; this is what makes data realistic)

| CT.gov field | Spec field | Effect |
|---|---|---|
| `participantFlowModule` STARTED per group | `arms[].ratio` | Exact randomization ratio (permuted blocks) |
| `participantFlowModule.dropWithdraws` | `disposition.study_withdrawal`, `death`, `ongoing_at_cutoff` | DS reasons and rates per arm |
| `baselineCharacteristicsModule` age / sex / race / ethnicity / region | `population.*`, `sites[].weight` | DM distributions (NIH/OMB → CDISC CT) |
| `adverseEventsModule.eventGroups[].deathsNumAffected` | `disposition.death` | DTHFL rate per arm |
| `adverseEventsModule.otherEvents / seriousEvents` | `adverse_events.terms[]` (incidence, serious_fraction per arm) | AE AEDECOD/AEBODSYS (registry MedDRA terms), AESER |

## Not in ClinicalTrials.gov (defaults, listed under `review:`)

- **Schedule of activities**: visits, windows, which assessments at which visit. Biggest gap.
- **Treatment discontinuation reasons**: the registry reports study withdrawal only.
- **Screen-failure rate**, enrollment curve, site-level enrolment.
- **Dosing detail**: titration, loading and weight-based doses, split infusions.
- **Lab panel and reference ranges** (generator default panel), ECG and vital-sign parameters.
- **Efficacy measurements**: endpoint values, tumour measurements, questionnaires.

A protocol, ideally ICH M11 structured or CDISC USDM, fills most of these gaps. Map its SoA to `visits`, its interventions to `arms[].interventions`, and its endpoints to findings domains.
