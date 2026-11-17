-- SDTM metric views (Unity Catalog, YAML v1.1) — 8 views over SDTMIG v3.4 domain tables.
--
-- Placeholders (replace before running, or use scripts/deploy_metric_views.py):
--   {{SDTM_SCHEMA}}    catalog.schema holding the SDTM tables (ae, cm, dm, ds, lb, ts, tv, vs)
--   {{TARGET_SCHEMA}}  catalog.schema where the metric views are created
--
-- Requirements: Databricks Runtime 17.3+ / current serverless or SQL warehouse (semantic metadata).
-- Tables may pool several studies (rows identified by STUDYID); slice with the study_id dimension.
--
-- Source columns used beyond SDTM Req/Exp variables (Permissible; may be all-null):
--   CM.CMCLAS, LB.LBSTAT, LB.LBTPT, VS.VSCAT, VS.VSSTAT, VS.VSDRVFL, VS.VSTPT, TS.TSGRPID, TV.ARM
--
-- Changes vs. the original sdtm_modeling.metric_views export (2026-11-17):
--   * Sources parameterised; hard-coded STUDYID IN (...) filters removed.
--   * PARAM (an ADaM variable) is derived as "<--TEST> (<--STRESU>)"; the PARAM LIKE '%(%' filters were removed.
--   * --BLFL -> --LOBXFL (SDTMIG 3.4 last-observation-before-exposure flag) for LB and VS baseline logic.
--   * VS baseline_subject_count uses the baseline flag instead of VISIT = 'Baseline'.
--   * AE/CM study days use the SDTM --STDY/--ENDY variables (no day 0) instead of DATEDIFF(...)+1.
--   * DS completion/discontinuation rates no longer multiply by 100 (the percentage format already does);
--     added disposition_subcategory (DSSCAT) to separate study-treatment vs study-participation dispositions.
--   * DM treatment_time is inclusive (last - first dose + 1).
--   * AE: added ae_toxicity_grade (AETOXGR; oncology studies use CTCAE grade instead of AESEV).
--   * TS indication falls back to TDIGRP when INDIC is absent.
--   * TS/TV: removed table_fetched_timestamp (pipeline audit column, not SDTM).
--   * Fixed copy-paste comments and the AE outcome / race metadata.
--   * CM conmed_per_subject = records per subject (as originally documented; was distinct meds / subjects).
--   * TS intervention lists all TRT values (was MAX of one); TV visits_list orders by VISITNUM (VISITDY is null
--     for event-driven visits such as end of treatment).
--   * Column lists with duplicated COMMENTs dropped from CREATE VIEW; comments live in the YAML (single source).

-- ======================================================================
-- adverse_event_metrics_view
-- ======================================================================
CREATE OR REPLACE VIEW {{TARGET_SCHEMA}}.adverse_event_metrics_view
COMMENT 'Contains adverse event data combined with demography and subject disposition details collected in a clinical study'
WITH METRICS
LANGUAGE YAML
AS
$$
version: 1.1

source: {{SDTM_SCHEMA}}.ae

joins:
  - name: dm
    source: {{SDTM_SCHEMA}}.dm
    using:
      - USUBJID

comment: Contains adverse event data combined with demography and subject disposition
  details collected in a clinical study

dimensions:
  - name: study_id
    expr: source.STUDYID
    comment: The unique identifier of the study in which the data was collected
    display_name: Study ID
    synonyms:
      - study identifier
      - research id
      - clinical study id
      - trial id

  - name: subject_id
    expr: source.USUBJID
    comment: The unique identifier for the subject
    display_name: Subject ID
    synonyms:
      - participant id
      - patient id
      - subject identifier
      - study subject id

  - name: ae_term_reported
    expr: source.AETERM
    comment: Verbatim name of the event as reported by the investigator
    display_name: Reported Term
    synonyms:
      - adverse event term
      - reported event name
      - investigator reported term
      - event description

  - name: ae_start_date
    expr: source.AESTDTC
    comment: Start date or time of the adverse event represented in ISO 8601 character format
    display_name: Start Date
    synonyms:
      - adverse event start date
      - event start date
      - AE start date
      - adverse event onset

  - name: ae_sequence_number
    expr: source.AESEQ
    comment: Sequence number given to ensure uniqueness of the record within a domain. May be any valid number.
    display_name: Sequence Number
    synonyms:
      - sequence number
      - record sequence
      - unique sequence
      - domain sequence

  - name: ae_domain
    expr: source.DOMAIN
    comment: Two-character abbreviation for the domain, which indicates the type of data contained in the dataset
    display_name: Domain
    synonyms:
      - domain code
      - domain abbreviation
      - domain short name
      - domain ID

  - name: ae_id
    expr: "CONCAT(source.USUBJID, '-', source.AESEQ)"
    comment: Unique identifier created by combining the subject id with the AE sequence number
    display_name: AE ID
    synonyms:
      - ae identifier

  - name: ae_pt
    expr: source.AEDECOD
    comment: Dictionary-derived text description of AETERM or AEMODIFY. Equivalent to the Preferred Term (PT in MedDRA).
    display_name: Preferred Term
    synonyms:
      - preferred term
      - ae preferred term
      - adverse event term
      - meddra preferred term
      - coded term for adverse event

  - name: ae_soc
    expr: source.AEBODSYS
    comment: "Dictionary derived. Body system or organ class used by the sponsor from the coding dictionary (e.g., MedDRA).
      When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses
      and summary tables, which may not necessarily be the primary SOC."
    display_name: Body System or Organ Class
    synonyms:
      - body system
      - organ class
      - system organ class
      - medical dictionary category

  - name: ae_severity
    expr: source.AESEV
    comment: The severity or intensity of the event ("MILD", "MODERATE", "SEVERE"). Often null in oncology studies, which use ae_toxicity_grade.
    display_name: Severity
    synonyms:
      - event severity
      - severity level
      - intensity
      - adverse event severity

  - name: ae_toxicity_grade
    expr: source.AETOXGR
    comment: Toxicity grade of the event (e.g. NCI CTCAE grade 1-5). Used instead of severity in oncology studies.
    display_name: Toxicity Grade
    synonyms:
      - CTCAE grade
      - AE grade
      - toxicity grade
      - grade

  - name: ae_seriousness
    expr: source.AESER
    comment: Is this a serious event. Valid values are "Y" and "N".
    display_name: Seriousness
    synonyms:
      - event criticality
      - serious event indicator

  - name: ae_relationship
    expr: source.AEREL
    comment: "Records the investigator's opinion as to the causality of the event to the treatment. ICH does not establish
      any required or recommended terms for non-device relatedness. ICH E2A and E2B examples include terms such as
      NOT RELATED, UNLIKELY RELATED, POSSIBLY RELATED, RELATED."
    display_name: Relationship or Causality
    synonyms:
      - causality
      - event relationship
      - treatment relatedness
      - causal relationship

  - name: ae_outcome
    expr: source.AEOUT
    comment: "Outcome of the event (CDISC CT OUT): RECOVERED/RESOLVED, RECOVERING/RESOLVING, NOT RECOVERED/NOT RESOLVED,
      RECOVERED/RESOLVED WITH SEQUELAE, FATAL, UNKNOWN."
    display_name: Outcome

  - name: ae_death
    expr: source.AESDTH
    comment: Did the serious event result in death. Valid values are "Y" and "N".
    display_name: Results in Death
    synonyms:
      - death outcome
      - fatality indicator
      - resulted in death
      - mortality flag

  - name: ae_hospitalization
    expr: source.AESHOSP
    comment: Did the serious event require or prolong hospitalization. Valid values are "Y" and "N".
    display_name: Hospitalization

  - name: ae_end_date
    expr: source.AEENDTC
    comment: End date/time of the adverse event represented in ISO 8601 character format.
    display_name: End Date
    synonyms:
      - adverse event end date
      - event end date
      - AE end datetime
      - adverse event completion date

  - name: ae_onset_day
    expr: source.AESTDY
    comment: "Study day of start of adverse event (AESTDY) relative to RFSTDTC, usually the first exposure to study
      treatment. Day 1 is the reference date; the day before is -1 (there is no day 0)."
    display_name: Onset Day
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
      hide_group_separator: false
      abbreviation: none
    synonyms:
      - adverse event onset day
      - AE start day
      - event onset day
      - study day of AE
      - start day of event

  - name: ae_end_day
    expr: source.AEENDY
    comment: Study day of end of event (AEENDY) relative to RFSTDTC. There is no day 0.
    display_name: End Day
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
      hide_group_separator: false
      abbreviation: none
    synonyms:
      - event end day
      - study day of event stop
      - study day of event resolution

  - name: ae_duration
    expr: |-
      CASE WHEN source.AEENDTC IS NOT NULL AND source.AESTDTC IS NOT NULL THEN DATEDIFF(source.AEENDTC, source.AESTDTC) + 1
      ELSE NULL END
    comment: Duration of adverse event in days. Only calculated if both the start and the end date for the adverse event is available.
    display_name: Duration
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
      hide_group_separator: false
      abbreviation: none
    synonyms:
      - event duration
      - AE duration
      - adverse event duration

  - name: ae_action_taken
    expr: source.AEACN
    comment: "Describes changes to the study treatment as a result of the event, e.g. DRUG WITHDRAWN, DOSE REDUCED,
      DOSE INCREASED, DOSE NOT CHANGED, DRUG INTERRUPTED, UNKNOWN, NOT APPLICABLE."
    display_name: Action Taken
    synonyms:
      - adverse event action
      - treatment change related to adverse event
      - study treatment adjustment due to event
      - AE action

  - name: death_flag
    expr: dm.DTHFL
    comment: Indicates the subject died. Should be "Y" or null. Should be populated even when the death date is unknown.
    display_name: Death Flag
    synonyms:
      - subject has died
      - deceased

  - name: site_id
    expr: dm.SITEID
    comment: Unique identifier for an investigational site within a study.
    display_name: Site ID
    synonyms:
      - site identifier
      - investigational site ID
      - study site
      - clinical site

  - name: Age
    expr: dm.AGE
    comment: Age expressed in AGEU.
    display_name: Age
    synonyms:
      - patient age
      - subject age
      - participant age

  - name: age_unit
    expr: dm.AGEU
    comment: The unit used for age, normally years
    display_name: Age Unit

  - name: Sex
    expr: dm.SEX
    comment: Sex of the subject.
    display_name: Sex
    synonyms:
      - gender
      - sex category
      - biological sex

  - name: Race
    expr: dm.RACE
    comment: Race of the subject.
    display_name: Race
    synonyms:
      - racial category
      - race classification

  - name: arm_planned
    expr: dm.ARM
    comment: Name of the arm to which the subject was assigned. If the subject was not assigned to an arm, ARM is null and ARMNRS is populated.
    display_name: Planned Arm
    synonyms:
      - planned treatment arm
      - planned study arm
      - assigned arm
      - clinical study arm

  - name: arm_actual
    expr: dm.ACTARM
    comment: Name of the actual treatment arm.
    display_name: Actual Arm
    synonyms:
      - actual treatment arm
      - actual study arm

  - name: Country
    expr: dm.COUNTRY
    comment: Country of the investigational site (ISO 3166-1 alpha-3).
    display_name: Country
    synonyms:
      - country code
      - site country
      - location country
      - ISO country

measures:
  - name: record_count
    expr: COUNT(*)
    comment: Represents the total number of rows in the dataset. Use this measure to count all records.
    display_name: Count

  - name: event_count
    expr: COUNT(DISTINCT ae_id)
    comment: Count number of adverse events
    display_name: Events

  - name: ae_subject_count
    expr: COUNT(DISTINCT source.USUBJID)
    comment: Counts number of subjects with one or more events
    display_name: Subjects
$$;

-- ======================================================================
-- concomitant_medications_metrics_view
-- ======================================================================
CREATE OR REPLACE VIEW {{TARGET_SCHEMA}}.concomitant_medications_metrics_view
COMMENT 'Metric view for Concomitant Medications (CM) domain. Provides measures and dimensions for analyzing medication usage, other than the investigated treatments, across subjects enrolled in the study.'
WITH METRICS
LANGUAGE YAML
AS
$$
version: 1.1

source: {{SDTM_SCHEMA}}.cm

joins:
  - name: dm
    source: {{SDTM_SCHEMA}}.dm
    using:
      - USUBJID

comment: "Metric view for Concomitant Medications (CM) domain. Provides measures and dimensions for analyzing medication
  usage, other than the investigated treatments, across subjects enrolled in the study."

dimensions:
  - name: study_id
    expr: source.STUDYID
    comment: Unique identifier for the clinical study
    display_name: Study ID

  - name: subject_id
    expr: source.USUBJID
    comment: Unique identifier for each subject in the study
    display_name: Subject ID
    synonyms:
      - patient
      - subject
      - participant

  - name: conmed_name
    expr: source.CMTRT
    comment: Verbatim name of the concomitant medication as reported
    display_name: Reported Medication Name
    synonyms:
      - drug name
      - concomitant treatment
      - concomitant medication

  - name: standardized_conmed_name
    expr: source.CMDECOD
    comment: "Standardized or dictionary-derived text description of CMTRT or CMMODIFY. Equivalent to the generic drug
      name in WHO Drug. If an intervention term does not have a standardised value in the dictionary, the field is blank."
    display_name: Standardized Medication Name
    synonyms:
      - decoded name
      - WHO drug name

  - name: conmed_class
    expr: source.CMCLAS
    comment: Therapeutic class of the concomitant medication
    display_name: Medication Class
    synonyms:
      - drug class
      - therapeutic class

  - name: conmed_dose
    expr: source.CMDOSE
    comment: Dose per administration
    display_name: Dose

  - name: conmed_dose_unit
    expr: source.CMDOSU
    comment: Units for the dose per administration
    display_name: Dose Unit

  - name: conmed_start_date
    expr: source.CMSTDTC
    comment: Start date/time of the concomitant medication
    display_name: ConMed Start Date

  - name: conmed_end_date
    expr: source.CMENDTC
    comment: End date/time of the concomitant medication
    display_name: ConMed End Date

  - name: conmed_start_day
    expr: source.CMSTDY
    comment: Study day of start of the concomitant medication (CMSTDY, no day 0; negative = before first dose)
    display_name: ConMed Start Day

  - name: conmed_end_day
    expr: source.CMENDY
    comment: Study day of the end of the concomitant medication (CMENDY, no day 0)
    display_name: ConMed End Day

  - name: conmed_duration
    expr: |-
      CASE WHEN source.CMSTDTC IS NOT NULL AND source.CMENDTC IS NOT NULL THEN DATEDIFF(source.CMENDTC, source.CMSTDTC) + 1
      ELSE NULL END
    comment: The calculated total duration in days the subject has taken the concomitant medication
    display_name: ConMed Duration

  - name: domain
    expr: source.DOMAIN
    comment: SDTM domain abbreviation (CM). Indicates the type of data contained in the dataset.
    display_name: Domain

  - name: site_id
    expr: dm.SITEID
    comment: Unique identifier for an investigational site within a study.
    display_name: Site ID
    synonyms:
      - site identifier
      - investigational site ID
      - study site
      - clinical site

  - name: Age
    expr: dm.AGE
    comment: Age expressed in AGEU.
    display_name: Age
    synonyms:
      - patient age
      - subject age
      - participant age

  - name: age_unit
    expr: dm.AGEU
    comment: The unit used for age, normally years
    display_name: Age Unit

  - name: Sex
    expr: dm.SEX
    comment: Sex of the subject.
    display_name: Sex
    synonyms:
      - gender
      - sex category
      - biological sex

  - name: Race
    expr: dm.RACE
    comment: Race of the subject.
    display_name: Race
    synonyms:
      - racial category
      - race classification

  - name: arm_planned
    expr: dm.ARM
    comment: Name of the arm to which the subject was assigned. If the subject was not assigned to an arm, ARM is null and ARMNRS is populated.
    display_name: Planned Arm
    synonyms:
      - planned treatment arm
      - planned study arm
      - assigned arm
      - clinical study arm

  - name: arm_actual
    expr: dm.ACTARM
    comment: Name of the actual treatment arm.
    display_name: Actual Arm
    synonyms:
      - actual treatment arm
      - actual study arm

  - name: Country
    expr: dm.COUNTRY
    comment: Country of the investigational site (ISO 3166-1 alpha-3).
    display_name: Country
    synonyms:
      - country code
      - site country
      - location country
      - ISO country

measures:
  - name: total_conmed_records
    expr: COUNT(*)
    comment: Total number of concomitant medication records
    display_name: Total Medication Records
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - medication record count
      - number of medication records

  - name: cm_subject_count
    expr: COUNT(DISTINCT source.USUBJID)
    comment: Number of distinct subjects with concomitant medications
    display_name: Subjects
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - patient count
      - participant count
      - subject count
      - number of patients
      - number of subjects
      - number of participants

  - name: unique_reported_conmed_count
    expr: COUNT(DISTINCT source.CMTRT)
    comment: Number of distinct concomitant medications as reported
    display_name: Unique Reported Medications
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - distinct reported drugs
      - count of reported medications

  - name: unique_conmed_count
    expr: COUNT(DISTINCT source.CMDECOD)
    comment: "Number of distinct concomitant medications based on the standardised (WHO Drug) coded term; excludes
      reported medications that have not been coded"
    display_name: Unique Medications
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - distinct coded drugs
      - coded medication count
      - drug count

  - name: unique_medication_classes
    expr: COUNT(DISTINCT source.CMCLAS)
    comment: Number of distinct therapeutic medication classes
    display_name: Medication Classes
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - drug class count
      - number of drug classes

  - name: avg_conmed_dose
    expr: AVG(source.CMDOSE)
    comment: Average medication dose across all records (only meaningful within one medication and unit)
    display_name: Average Dose
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - mean dose

  - name: total_conmed_dose
    expr: SUM(source.CMDOSE)
    comment: Sum of all medication doses (only meaningful within one medication and unit)
    display_name: Total Dose
    format:
      type: number
      decimal_places:
        type: exact
        places: 2

  - name: avg_conmed_duration
    expr: AVG(conmed_duration)
    comment: Average duration of medication treatment in days (records with both start and end date)
    display_name: Average Treatment Duration (Days)
    format:
      type: number
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - mean duration
      - avg duration

  - name: conmed_per_subject
    expr: MEASURE(total_conmed_records) / MEASURE(cm_subject_count)
    comment: Average number of concomitant medication records per subject with medications
    display_name: Medications Per Subject
    format:
      type: number
      decimal_places:
        type: exact
        places: 1
$$;

-- ======================================================================
-- demographics_metrics_view
-- ======================================================================
CREATE OR REPLACE VIEW {{TARGET_SCHEMA}}.demographics_metrics_view
COMMENT 'Contains subject-level demography data (one record per subject, DM domain) including treatment arms and exposure dates collected in a clinical study'
WITH METRICS
LANGUAGE YAML
AS
$$
version: 1.1

source: {{SDTM_SCHEMA}}.dm

comment: Contains subject-level demography data (one record per subject, DM domain) including treatment arms and
  exposure dates collected in a clinical study

dimensions:
  - name: study_id
    expr: STUDYID
    comment: Unique identifier for the study
    display_name: Study ID
    synonyms:
      - study
      - study identifier
      - trial
      - trial id

  - name: subject_id
    expr: USUBJID
    comment: Unique identifier for the subject
    display_name: Subject ID
    synonyms:
      - subject
      - subject identifier
      - patient
      - participant

  - name: site_id
    expr: SITEID
    comment: Identifier for the site within the study
    display_name: Site ID
    synonyms:
      - site
      - site identifier

  - name: age
    expr: AGE
    comment: Age of the subject
    display_name: Age
    format:
      type: number
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - subject age

  - name: sex
    expr: SEX
    comment: Sex of the subject
    display_name: Sex
    synonyms:
      - gender

  - name: race
    expr: RACE
    comment: Race of the subject
    display_name: Race
    synonyms:
      - racial category

  - name: arm_planned
    expr: ARM
    comment: Treatment arm to which the subject was assigned (null for screen failures; see ARMNRS)
    display_name: Planned Arm
    synonyms:
      - planned treatment arm
      - planned treatment group
      - assigned treatment

  - name: arm_actual
    expr: ACTARM
    comment: Name of the actual treatment arm.
    display_name: Actual Arm
    synonyms:
      - actual treatment arm
      - actual study arm

  - name: country
    expr: COUNTRY
    comment: Country of site at which the subject was enrolled
    display_name: Country
    synonyms:
      - country of site

  - name: treatment_time
    expr: "DATEDIFF(RFXENDTC, RFXSTDTC) + 1"
    comment: Treatment time in days from first dosing day to last dosing day, inclusive (null if never dosed)
    display_name: Treatment Time (days)
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - treatment duration

measures:
  - name: subject_count
    expr: COUNT(DISTINCT USUBJID)
    comment: Number of unique subjects
    display_name: Subjects
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - number of subjects
      - subject total

  - name: age_average
    expr: AVG(AGE)
    comment: Average age of subjects
    display_name: Average Age
    format:
      type: number
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - mean age

  - name: age_min
    expr: MIN(AGE)
    comment: Minimum age of subjects
    display_name: Min Age
    format:
      type: number
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - lowest age

  - name: age_max
    expr: MAX(AGE)
    comment: Maximum age of subjects
    display_name: Max Age
    format:
      type: number
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - highest age

  - name: age_sd
    expr: STDDEV(AGE)
    comment: Standard deviation for age of subjects
    display_name: SD Age
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - age deviation

  - name: age_sem
    expr: STDDEV(AGE) / SQRT(COUNT(AGE))
    comment: Standard error of mean for age of subjects
    display_name: SEM Age
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - age standard error

  - name: subject_count_sex
    expr: COUNT(DISTINCT USUBJID)
    window:
      - order: sex
        semiadditive: last
        range: all
    comment: Total number of unique subjects across all sexes (denominator for percentages by sex)
    display_name: Total Count by Sex
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - total number of subjects by sex
      - subject count by sex

  - name: subject_count_race
    expr: COUNT(DISTINCT USUBJID)
    window:
      - order: race
        semiadditive: last
        range: all
    comment: Total number of unique subjects across all races (denominator for percentages by race)
    display_name: Total Count by Race
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - total number of subjects by race
      - subject count by race

  - name: subject_percentage_sex
    expr: "MEASURE(`subject_count`)/NULLIF(MEASURE(`subject_count_sex`), 0)"
    comment: Percentage of subjects by sex
    display_name: Percentage by Sex
    format:
      type: percentage
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - percent of subjects by sex
      - subject percentage by sex
      - subject proportion by sex

  - name: subject_percentage_race
    expr: "MEASURE(`subject_count`)/NULLIF(MEASURE(`subject_count_race`), 0)"
    comment: Percentage of subjects by race
    display_name: Percentage by Race
    format:
      type: percentage
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - percent of subjects by race
      - subject percentage by race
      - subject proportion by race

  - name: subject_count_arm
    expr: COUNT(DISTINCT USUBJID)
    window:
      - order: arm_actual
        semiadditive: last
        range: all
    comment: Total number of unique subjects across all actual arms (denominator for percentages by arm)
    display_name: Total Count by Arm
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - total number of subjects by treatment
      - all subjects by treatment

  - name: subject_percentage_arm
    expr: "MEASURE(`subject_count`)/NULLIF(MEASURE(`subject_count_arm`), 0)"
    comment: Percentage of subjects by arm
    display_name: Percentage by Arm
    format:
      type: percentage
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - percent of subjects by treatment
      - subject percentage by treatment
      - subject proportion by treatment

  - name: treatment_time_total
    expr: "NULLIF(SUM(`treatment_time`)/365.25, 0)"
    comment: Total treatment exposure in patient-years
    display_name: Total On-treatment (PYE)
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - patient years of exposure
      - total exposure
      - total treatment time

  - name: subject_list
    expr: ARRAY_AGG(DISTINCT USUBJID)
    comment: List of subjects in the group
    display_name: Subject List
$$;

-- ======================================================================
-- disposition_metrics_view
-- ======================================================================
CREATE OR REPLACE VIEW {{TARGET_SCHEMA}}.disposition_metrics_view
COMMENT 'CDISC SDTM DS (Disposition) domain metric view. Tracks subject disposition events including protocol milestones such as informed consent, randomization, treatment completion, and study discontinuation.'
WITH METRICS
LANGUAGE YAML
AS
$$
version: 1.1

source: {{SDTM_SCHEMA}}.ds

joins:
  - name: dm
    source: {{SDTM_SCHEMA}}.dm
    using:
      - USUBJID

comment: "CDISC SDTM DS (Disposition) domain metric view. Tracks subject disposition events including protocol
  milestones such as informed consent, randomization, treatment completion, and study discontinuation. Filter
  disposition_subcategory to separate end-of-treatment from end-of-study dispositions before reading rates. Rates use
  subjects WITH a record in the current slice as denominator; subjects still ongoing at the data cutoff have no
  end-of-study record, so use demographics_metrics_view subject counts for rates over all randomized subjects."

dimensions:
  - name: study_id
    expr: source.STUDYID
    comment: Unique identifier for the clinical study or trial. Corresponds to SDTM variable STUDYID.
    display_name: Study ID
    synonyms:
      - study identifier
      - protocol number
      - trial id
      - clinical study id

  - name: domain
    expr: source.DOMAIN
    comment: Two-character abbreviation for the SDTM domain. For disposition records this is always 'DS'.
    display_name: Domain Abbreviation
    synonyms:
      - domain abbreviation
      - domain code
      - sdtm domain

  - name: unique_subject_id
    expr: source.USUBJID
    comment: Unique subject identifier across all studies. Corresponds to SDTM variable USUBJID.
    display_name: Subject ID
    synonyms:
      - subject id
      - patient id
      - participant id
      - usubjid
      - subject identifier

  - name: disposition_sequence
    expr: source.DSSEQ
    comment: Sequence number used to ensure uniqueness of disposition records within a subject (DSSEQ).
    display_name: Disposition Sequence Number
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - sequence number
      - dsseq
      - record sequence

  - name: reported_disposition_term
    expr: source.DSTERM
    comment: Verbatim or reported term for the disposition event (DSTERM).
    display_name: Reported Disposition Term
    synonyms:
      - reported term
      - dsterm
      - verbatim disposition
      - disposition description

  - name: standardized_disposition_term
    expr: source.DSDECOD
    comment: "Controlled terminology for the disposition event, e.g. COMPLETED, ADVERSE EVENT, WITHDRAWAL BY SUBJECT,
      PHYSICIAN DECISION, PROGRESSIVE DISEASE, DEATH, SCREEN FAILURE (DSDECOD)."
    display_name: Standardized Disposition Term
    synonyms:
      - decoded term
      - dsdecod
      - disposition decode
      - disposition outcome
      - disposition reason

  - name: disposition_category
    expr: source.DSCAT
    comment: Category of the disposition event (PROTOCOL MILESTONE, DISPOSITION EVENT, OTHER EVENT) (DSCAT).
    display_name: Disposition Category
    synonyms:
      - category
      - dscat
      - event category
      - disposition event category
      - milestone category

  - name: disposition_subcategory
    expr: source.DSSCAT
    comment: "Sponsor-defined subcategory of the disposition event, e.g. STUDY TREATMENT (end of treatment) or
      STUDY PARTICIPATION (end of study) (DSSCAT). Filter on this before reading completion/discontinuation rates."
    display_name: Disposition Subcategory
    synonyms:
      - dsscat
      - disposition level
      - end of treatment or end of study
      - epoch of disposition

  - name: disposition_start_datetime
    expr: source.DSSTDTC
    comment: Start date/time of the disposition event in ISO 8601 character format (DSSTDTC).
    display_name: Disposition Start Date/Time
    synonyms:
      - start date
      - dsstdtc
      - disposition date
      - event date
      - event start date

  - name: site_id
    expr: dm.SITEID
    comment: Unique identifier for an investigational site within a study.
    display_name: Site ID
    synonyms:
      - site identifier
      - investigational site ID
      - study site
      - clinical site

  - name: Age
    expr: dm.AGE
    comment: Age expressed in AGEU.
    display_name: Age
    synonyms:
      - patient age
      - subject age
      - participant age

  - name: age_unit
    expr: dm.AGEU
    comment: The unit used for age, normally years
    display_name: Age Unit

  - name: Sex
    expr: dm.SEX
    comment: Sex of the subject.
    display_name: Sex
    synonyms:
      - gender
      - sex category
      - biological sex

  - name: Race
    expr: dm.RACE
    comment: Race of the subject.
    display_name: Race
    synonyms:
      - racial category
      - race classification

  - name: arm_planned
    expr: dm.ARM
    comment: Name of the arm to which the subject was assigned. If the subject was not assigned to an arm, ARM is null and ARMNRS is populated.
    display_name: Planned Arm
    synonyms:
      - planned treatment arm
      - planned study arm
      - assigned arm
      - clinical study arm

  - name: arm_actual
    expr: dm.ACTARM
    comment: Name of the actual treatment arm.
    display_name: Actual Arm
    synonyms:
      - actual treatment arm
      - actual study arm

  - name: Country
    expr: dm.COUNTRY
    comment: Country of the investigational site (ISO 3166-1 alpha-3).
    display_name: Country
    synonyms:
      - country code
      - site country
      - location country
      - ISO country

measures:
  - name: total_records
    expr: COUNT(*)
    comment: Total number of disposition records. Each record represents one disposition event for a subject.
    display_name: Total Disposition Records
    synonyms:
      - record count
      - row count
      - number of records
      - total rows

  - name: total_subjects
    expr: COUNT(DISTINCT source.USUBJID)
    comment: Total number of unique subjects with at least one disposition record.
    display_name: Subjects
    synonyms:
      - unique subjects
      - subject count
      - patient count
      - number of patients
      - number of subjects

  - name: total_distinct_disposition_events
    expr: COUNT(DISTINCT source.DSDECOD)
    comment: Total number of distinct standardized disposition terms observed.
    display_name: Distinct Disposition Events
    synonyms:
      - unique disposition terms
      - distinct events
      - number of event types

  - name: total_distinct_categories
    expr: COUNT(DISTINCT source.DSCAT)
    comment: Total number of distinct disposition categories observed.
    display_name: Distinct Disposition Categories
    synonyms:
      - unique categories
      - category count
      - number of categories

  - name: completed_subject_count
    expr: |-
      COUNT(DISTINCT CASE
        WHEN source.DSDECOD = 'COMPLETED' THEN source.USUBJID
      END)
    comment: Number of unique subjects with a disposition record DSDECOD = COMPLETED.
    display_name: Completed Subjects
    synonyms:
      - completers
      - subjects completed
      - number completed
      - completed patients

  - name: discontinued_subject_count
    expr: |-
      COUNT(DISTINCT CASE
        WHEN source.DSDECOD != 'COMPLETED'
          AND source.DSCAT = 'DISPOSITION EVENT'
        THEN source.USUBJID
      END)
    comment: "Number of unique subjects with a disposition event whose standardized term is not COMPLETED (includes
      screen failures). Filter disposition_subcategory to count treatment vs study discontinuation separately."
    display_name: Discontinued Subjects
    synonyms:
      - dropouts
      - subjects discontinued
      - number discontinued
      - early terminations
      - withdrawn subjects

  - name: completion_rate
    expr: MEASURE(completed_subject_count) / MEASURE(total_subjects)
    comment: Share of unique subjects who completed out of all subjects with disposition records.
    display_name: Completion Rate
    format:
      type: percentage
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - completion percentage
      - percent completed
      - study completion rate
      - retention rate

  - name: discontinuation_rate
    expr: MEASURE(discontinued_subject_count) / MEASURE(total_subjects)
    comment: Share of unique subjects who discontinued. Complementary to the completion rate within one disposition_subcategory.
    display_name: Discontinuation Rate
    format:
      type: percentage
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - dropout rate
      - attrition rate
      - percent discontinued
      - withdrawal rate

  - name: avg_disposition_events_per_subject
    expr: COUNT(*) / COUNT(DISTINCT source.USUBJID)
    comment: Average number of disposition records per subject.
    display_name: Avg Events per Subject
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - events per patient
      - average dispositions per subject
      - mean events per subject
$$;

-- ======================================================================
-- laboratory_test_results_metrics_view
-- ======================================================================
CREATE OR REPLACE VIEW {{TARGET_SCHEMA}}.laboratory_test_results_metrics_view
COMMENT 'Metric view for the CDISC SDTM LB (Laboratory Test Results) domain. Provides standardized measures and dimensions for laboratory data analysis including result statistics, reference range comparisons, and abnormality counts.'
WITH METRICS
LANGUAGE YAML
AS
$$
version: 1.1

source: {{SDTM_SCHEMA}}.lb

joins:
  - name: dm
    source: {{SDTM_SCHEMA}}.dm
    using:
      - USUBJID

comment: "Metric view for the CDISC SDTM LB (Laboratory Test Results) domain. Provides standardized measures and
  dimensions for laboratory data analysis including result statistics, reference range comparisons, and abnormality
  counts. Statistics on results are only meaningful within one parameter."

dimensions:
  - name: study_id
    expr: source.STUDYID
    comment: Unique identifier for the clinical study (STUDYID)
    display_name: Study ID
    synonyms:
      - studyid
      - protocol number
      - study identifier
      - trial id

  - name: subject_id
    expr: source.USUBJID
    comment: Unique subject identifier across all studies (USUBJID)
    display_name: Subject ID
    synonyms:
      - usubjid
      - patient id
      - subject
      - participant id

  - name: test_name
    expr: source.LBTEST
    comment: Name of the lab test (LBTEST, max 40 characters), e.g. "Alanine Aminotransferase".
    display_name: Test Name
    synonyms:
      - lbtest
      - test name
      - lab test
      - analyte name

  - name: parameter
    expr: "CONCAT(source.LBTEST, COALESCE(CONCAT(' (', source.LBSTRESU, ')'), ''))"
    comment: Descriptive label for the lab parameter including test and standard units, derived as LBTEST (LBSTRESU).
    display_name: Parameter
    synonyms:
      - param
      - parameter
      - lab parameter description

  - name: lab_category
    expr: source.LBCAT
    comment: Category of related records, e.g. "HEMATOLOGY", "URINALYSIS", "CHEMISTRY".
    display_name: Category
    synonyms:
      - lbcat
      - test category
      - lab panel
      - specimen category

  - name: specimen_type
    expr: source.LBSPEC
    comment: Type of specimen used for a measurement, e.g. "SERUM", "PLASMA", "URINE".
    display_name: Specimen Type
    synonyms:
      - lbspec
      - sample type
      - specimen
      - material type

  - name: standard_result
    expr: source.LBSTRESN
    comment: The numeric lab result in standard units (LBSTRESN)
    display_name: Result
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - result
      - lab value
      - lbstresn

  - name: standard_units
    expr: source.LBSTRESU
    comment: Standard units used for the numeric result (LBSTRESU)
    display_name: Standard Units
    synonyms:
      - lbstresu
      - std units
      - result units

  - name: original_units
    expr: source.LBORRESU
    comment: Original units in which the lab result was reported (LBORRESU)
    display_name: Original Units
    synonyms:
      - lborresu
      - orig units
      - reported units

  - name: reference_range_indicator
    expr: source.LBNRIND
    comment: "Where the value falls with respect to the reference range, e.g. NORMAL, ABNORMAL, HIGH, LOW (LBNRIND).
      Not an indicator of clinical significance."
    display_name: Reference Range Indicator
    synonyms:
      - lbnrind
      - normal range indicator
      - abnormality flag
      - range flag

  - name: baseline_flag
    expr: source.LBLOBXFL
    comment: "Last observation before exposure flag (LBLOBXFL, SDTMIG 3.4 replacement for LBBLFL). Y or null.
      The authoritative baseline for statistical analysis is in ADaM."
    display_name: Baseline Flag
    synonyms:
      - lblobxfl
      - lbblfl
      - baseline indicator
      - is baseline

  - name: completion_status
    expr: source.LBSTAT
    comment: Used to indicate exam not done (LBSTAT). Null if a result exists.
    display_name: Lab Not Done
    synonyms:
      - lbstat
      - test status
      - done status

  - name: visit_name
    expr: source.VISIT
    comment: Protocol-defined description of clinical encounter (VISIT).
    display_name: Visit Name
    synonyms:
      - visit
      - visit label
      - clinic visit
      - encounter

  - name: visit_number
    expr: source.VISITNUM
    comment: Clinical encounter number. Numeric version of VISIT, used for sorting (VISITNUM)
    display_name: Visit Number
    format:
      type: number
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - visitnum
      - visit num
      - visit sequence

  - name: planned_study_day
    expr: source.VISITDY
    comment: Planned study day of the visit relative to RFSTDTC (VISITDY).
    display_name: Planned Study Day of Visit
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - visitdy
      - study day
      - planned day
      - protocol day

  - name: collection_date
    expr: source.LBDTC
    comment: Date/time of specimen collection in ISO 8601 format (LBDTC)
    display_name: Collection Date/Time
    synonyms:
      - lbdtc
      - specimen date
      - collection datetime
      - lab date

  - name: planned_time_point
    expr: source.LBTPT
    comment: Planned time point name for the specimen collection, e.g. Pre-dose, 1 Hour Post-dose (LBTPT).
    display_name: Planned Time Point
    synonyms:
      - lbtpt
      - time point
      - scheduled time point
      - sampling time

  - name: site_id
    expr: dm.SITEID
    comment: Unique identifier for an investigational site within a study.
    display_name: Site ID
    synonyms:
      - site identifier
      - investigational site ID
      - study site
      - clinical site

  - name: Age
    expr: dm.AGE
    comment: Age expressed in AGEU.
    display_name: Age
    synonyms:
      - patient age
      - subject age
      - participant age

  - name: age_unit
    expr: dm.AGEU
    comment: The unit used for age, normally years
    display_name: Age Unit

  - name: Sex
    expr: dm.SEX
    comment: Sex of the subject.
    display_name: Sex
    synonyms:
      - gender
      - sex category
      - biological sex

  - name: Race
    expr: dm.RACE
    comment: Race of the subject.
    display_name: Race
    synonyms:
      - racial category
      - race classification

  - name: arm_planned
    expr: dm.ARM
    comment: Name of the arm to which the subject was assigned. If the subject was not assigned to an arm, ARM is null and ARMNRS is populated.
    display_name: Planned Arm
    synonyms:
      - planned treatment arm
      - planned study arm
      - assigned arm
      - clinical study arm

  - name: arm_actual
    expr: dm.ACTARM
    comment: Name of the actual treatment arm.
    display_name: Actual Arm
    synonyms:
      - actual treatment arm
      - actual study arm

  - name: Country
    expr: dm.COUNTRY
    comment: Country of the investigational site (ISO 3166-1 alpha-3).
    display_name: Country
    synonyms:
      - country code
      - site country
      - location country
      - ISO country

measures:
  - name: record_count
    expr: COUNT(*)
    comment: Total number of lab result records
    display_name: Record Count
    synonyms:
      - total records
      - number of records
      - observation count
      - row count

  - name: subject_count
    expr: COUNT(DISTINCT source.USUBJID)
    comment: Number of unique subjects with lab results
    display_name: Subjects
    synonyms:
      - number of subjects
      - patient count
      - unique subjects
      - participant count

  - name: test_count
    expr: COUNT(DISTINCT source.LBTESTCD)
    comment: Number of distinct lab tests performed
    display_name: Distinct Test Count
    synonyms:
      - number of tests
      - unique tests
      - analyte count

  - name: mean_standard_result
    expr: AVG(source.LBSTRESN)
    comment: Mean of the numeric lab result in standard units (LBSTRESN)
    display_name: Mean Result
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - average result
      - mean lab value
      - avg lbstresn

  - name: min_standard_result
    expr: MIN(source.LBSTRESN)
    comment: Minimum numeric lab result in standard units (LBSTRESN)
    display_name: Min Result
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - minimum result
      - lowest value
      - min lab value

  - name: max_standard_result
    expr: MAX(source.LBSTRESN)
    comment: Maximum numeric lab result in standard units (LBSTRESN)
    display_name: Max Result
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - maximum result
      - highest value
      - max lab value

  - name: sum_standard_result
    expr: SUM(source.LBSTRESN)
    comment: Sum of all numeric lab results in standard units (LBSTRESN)
    display_name: Sum Result
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - total result
      - sum lab values
      - sum lbstresn

  - name: stddev_standard_result
    expr: STDDEV(source.LBSTRESN)
    comment: Standard deviation of the numeric lab result in standard units (LBSTRESN)
    display_name: Std Dev Result
    format:
      type: number
      decimal_places:
        type: exact
        places: 4
    synonyms:
      - standard deviation
      - result variability
      - sd result

  - name: mean_lower_ref_range
    expr: AVG(source.LBSTNRLO)
    comment: Mean of the lower limit of the reference range in standard units (LBSTNRLO). Only relevant within one parameter.
    display_name: Mean Lower Reference Range
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - average lower limit
      - mean lbstnrlo
      - lower normal range

  - name: mean_upper_ref_range
    expr: AVG(source.LBSTNRHI)
    comment: Mean of the upper limit of the reference range in standard units (LBSTNRHI). Only relevant within one parameter.
    display_name: Mean Upper Reference Range
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - average upper limit
      - mean lbstnrhi
      - upper normal range

  - name: abnormal_high_count
    expr: COUNT(*) FILTER (WHERE reference_range_indicator = 'HIGH')
    comment: Count of lab results flagged as above the upper reference range limit
    display_name: Abnormal High Count
    synonyms:
      - high results
      - above normal count
      - elevated count

  - name: abnormal_low_count
    expr: COUNT(*) FILTER (WHERE reference_range_indicator = 'LOW')
    comment: Count of lab results flagged as below the lower reference range limit
    display_name: Abnormal Low Count
    synonyms:
      - low results
      - below normal count
      - decreased count

  - name: abnormal_count
    expr: COUNT(*) FILTER (WHERE reference_range_indicator = 'LOW' OR reference_range_indicator = 'HIGH')
    comment: Count of lab results flagged as below or above the reference range (LOW or HIGH)
    display_name: Abnormal Count
    synonyms:
      - outside normal range results
      - below or above normal range results
      - abnormal count

  - name: normal_count
    expr: COUNT(*) FILTER (WHERE reference_range_indicator = 'NORMAL')
    comment: Count of lab results within the normal reference range
    display_name: Normal Count
    synonyms:
      - in range count
      - within normal limits
      - normal results

  - name: abnormal_percentage
    expr: (MEASURE(abnormal_count)) / (MEASURE(abnormal_count) + MEASURE(normal_count))
    comment: Share of lab results outside the normal reference range (HIGH or LOW) among results with a range indicator
    display_name: Abnormal Percentage
    format:
      type: percentage
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - pct abnormal
      - out of range percentage
      - abnormality rate

  - name: baseline_record_count
    expr: COUNT(*) FILTER (WHERE baseline_flag = 'Y')
    comment: Count of lab records flagged as baseline (last observation before exposure)
    display_name: Baseline Record Count
    synonyms:
      - baseline count
      - number of baselines
      - baseline observations
$$;

-- ======================================================================
-- trial_summary_metric_view
-- ======================================================================
CREATE OR REPLACE VIEW {{TARGET_SCHEMA}}.trial_summary_metric_view
COMMENT 'Trial Summary (TS) metric view based on the SDTM model. Contains trial-level summary parameters describing key characteristics of a clinical study.'
WITH METRICS
LANGUAGE YAML
AS
$$
version: 1.1

source: {{SDTM_SCHEMA}}.ts

comment: Trial Summary (TS) metric view based on the SDTM model. Contains trial-level summary parameters describing
  key characteristics of a clinical study. Group by study_id to get one row per study.

dimensions:
  - name: study_id
    expr: source.STUDYID
    comment: Unique identifier for the clinical study
    display_name: Study ID
    synonyms:
      - study identifier
      - protocol number
      - clinical trial id
      - protocol id

  - name: domain
    expr: source.DOMAIN
    comment: Two-character abbreviation for the SDTM domain (TS)
    display_name: Domain Abbreviation
    synonyms:
      - domain code
      - dataset name
      - domain id

  - name: sequence_number
    expr: source.TSSEQ
    comment: Sequence number to ensure uniqueness of records within a parameter
    display_name: Sequence Number
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - seq number
      - record sequence
      - tsseq

  - name: group_id
    expr: source.TSGRPID
    comment: Identifier used to group related trial summary parameter records
    display_name: Group ID
    synonyms:
      - group identifier
      - grouping id
      - parameter group

  - name: parameter_short_name
    expr: source.TSPARMCD
    comment: Short name of the trial summary parameter as defined by CDISC controlled terminology
    display_name: Parameter Short Name
    synonyms:
      - parameter code
      - tsparmcd
      - cdisc parameter code
      - parameter short name

  - name: parameter
    expr: source.TSPARM
    comment: Full descriptive name of the trial summary parameter
    display_name: Parameter
    synonyms:
      - parameter name
      - trial parameter
      - parameter label
      - parameter description

  - name: parameter_value
    expr: source.TSVAL
    comment: Value of the trial summary parameter
    display_name: Value
    synonyms:
      - value
      - trial summary value
      - parameter result
      - tsval

measures:
  - name: record_count
    expr: COUNT(*)
    comment: Total number of trial summary parameter records
    display_name: Record Count
    synonyms:
      - row count
      - number of records
      - total records
      - observation count

  - name: parameter_count
    expr: COUNT(DISTINCT source.TSPARMCD)
    comment: Number of distinct trial summary parameters reported
    display_name: Distinct Parameter Count
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - unique parameters
      - number of parameters
      - parameter count

  - name: study_count
    expr: COUNT(DISTINCT source.STUDYID)
    comment: Number of distinct clinical studies in the dataset
    display_name: Distinct Study Count
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - unique studies
      - number of studies
      - study count
      - trial count

  - name: countries_list
    expr: "CONCAT_WS(', ', COLLECT_SET(CASE WHEN source.TSPARMCD = 'FCNTRY' THEN source.TSVAL END))"
    comment: Comma-separated list of distinct countries (TSPARMCD FCNTRY) for each study
    display_name: Countries
    synonyms:
      - country list
      - study countries
      - trial countries
      - country names

  - name: data_cut_off
    expr: |-
      CONCAT_WS(': ',
        MAX(CASE WHEN source.TSPARMCD = 'DCUTDESC' THEN source.TSVAL END),
        MAX(CASE WHEN source.TSPARMCD = 'DCUTDTC' THEN source.TSVAL END))
    comment: Concatenation of the Data Cutoff Description and Data Cutoff Date for the study
    display_name: Data Cut-off
    synonyms:
      - cutoff info
      - data cutoff description and date
      - cutoff date
      - dcutoff

  - name: age_range
    expr: |-
      CONCAT_WS(' - ',
        MAX(CASE WHEN source.TSPARMCD = 'AGEMIN' THEN source.TSVAL END),
        MAX(CASE WHEN source.TSPARMCD = 'AGEMAX' THEN source.TSVAL END))
    comment: Concatenation of the minimum and maximum planned age of subjects (ISO 8601 durations, e.g. P18Y)
    display_name: Age Range
    synonyms:
      - min max age
      - age limits
      - subject age range
      - planned age range

  - name: study_period
    expr: |-
      CONCAT_WS(' to ',
        MAX(CASE WHEN source.TSPARMCD = 'SSTDTC' THEN source.TSVAL END),
        MAX(CASE WHEN source.TSPARMCD = 'SENDTC' THEN source.TSVAL END))
    comment: Concatenation of the study start date (SSTDTC) and study end date (SENDTC)
    display_name: Study Period
    synonyms:
      - trial period
      - study duration
      - trial duration

  - name: sex
    expr: INITCAP(MAX(CASE WHEN source.TSPARMCD = 'SEXPOP' THEN source.TSVAL END))
    comment: Sex of participants in the study (SEXPOP)
    display_name: Sex
    synonyms:
      - sex population
      - gender
      - subject sex
      - sexpop

  - name: indication
    expr: |-
      INITCAP(COALESCE(
        MAX(CASE WHEN source.TSPARMCD = 'INDIC' THEN source.TSVAL END),
        MAX(CASE WHEN source.TSPARMCD = 'TDIGRP' THEN source.TSVAL END)))
    comment: Indication investigated in the study (INDIC, falling back to diagnosis group TDIGRP)
    display_name: Indication
    synonyms:
      - disease or disorder

  - name: type
    expr: INITCAP(MAX(CASE WHEN source.TSPARMCD = 'STYPE' THEN source.TSVAL END))
    comment: The type of the study, i.e., interventional or observational (STYPE)
    display_name: Type
    synonyms:
      - study type
      - trial type

  - name: title
    expr: MAX(CASE WHEN source.TSPARMCD = 'TITLE' THEN source.TSVAL END)
    comment: The title of the study (TITLE)
    display_name: Study Title
    synonyms:
      - protocol title
      - trial title

  - name: intervention
    expr: "CONCAT_WS(', ', COLLECT_SET(CASE WHEN source.TSPARMCD = 'TRT' THEN INITCAP(source.TSVAL) END))"
    comment: Investigational therapy or treatment(s) in the study (TRT)
    display_name: Intervention
    synonyms:
      - study intervention
      - study therapy
      - study drug

  - name: arms
    expr: MAX(CASE WHEN source.TSPARMCD = 'NARMS' THEN source.TSVAL END)
    comment: Number of treatment arms in the study (NARMS)
    display_name: Arms
    synonyms:
      - treatment groups
      - treatment arms

  - name: subjects_screened
    expr: MAX(CASE WHEN source.TSPARMCD = 'ACTSUB' AND source.TSGRPID = 'SCREENED' THEN source.TSVAL END)
    comment: Total number of subjects screened (sponsor convention ACTSUB with TSGRPID = SCREENED)
    display_name: Screened
    synonyms:
      - patients screened
      - screened
      - participants screened

  - name: subjects_treated
    expr: MAX(CASE WHEN source.TSPARMCD = 'ACTSUB' AND source.TSGRPID = 'TREATED' THEN source.TSVAL END)
    comment: Total number of subjects treated (sponsor convention ACTSUB with TSGRPID = TREATED)
    display_name: Treated
    synonyms:
      - patients treated
      - treated
      - participants treated

  - name: subjects_completing
    expr: MAX(CASE WHEN source.TSPARMCD = 'ACTSUB' AND source.TSGRPID = 'COMPLETED' THEN source.TSVAL END)
    comment: Total number of subjects completing (sponsor convention ACTSUB with TSGRPID = COMPLETED)
    display_name: Completing
    synonyms:
      - patients completing
      - completes
      - participants completing

  - name: phase
    expr: MAX(CASE WHEN source.TSPARMCD = 'TPHASE' THEN source.TSVAL END)
    comment: The clinical phase of the study (TPHASE)
    display_name: Phase
    synonyms:
      - study phase
      - trial phase
$$;

-- ======================================================================
-- trial_visit_metric_view
-- ======================================================================
CREATE OR REPLACE VIEW {{TARGET_SCHEMA}}.trial_visit_metric_view
COMMENT 'Trial Visits (TV) metric view based on the SDTM model. Defines the planned visits and their attributes for each arm in a clinical study, as described in the SDTM Implementation Guide.'
WITH METRICS
LANGUAGE YAML
AS
$$
version: 1.1

source: {{SDTM_SCHEMA}}.tv

comment: "Trial Visits (TV) metric view based on the SDTM model. Defines the planned visits and their attributes for
  each arm in a clinical study, as described in the SDTM Implementation Guide. Null ARMCD means the visit applies to all arms."

dimensions:
  - name: study_id
    expr: source.STUDYID
    comment: Unique identifier for a study, assigned by the sponsor
    display_name: Study ID
    synonyms:
      - study identifier
      - protocol number
      - clinical trial id
      - protocol id

  - name: domain_abbreviation
    expr: source.DOMAIN
    comment: Two-character abbreviation for the domain name (TV)
    display_name: Domain Abbreviation
    synonyms:
      - domain code
      - dataset name
      - domain id

  - name: visit_number
    expr: source.VISITNUM
    comment: Clinical encounter number that serves as a numeric key for ordering visits within a study
    display_name: Visit Number
    format:
      type: number
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - visitnum
      - visit sequence
      - encounter number
      - visit order

  - name: visit_name
    expr: source.VISIT
    comment: Protocol-defined description of a clinical encounter, as specified in the study protocol
    display_name: Visit Name
    synonyms:
      - visit label
      - visit description
      - clinical encounter
      - protocol visit

  - name: planned_study_day_of_visit
    expr: source.VISITDY
    comment: Planned study day of the visit, relative to the study reference start date (null for event-driven visits such as end of treatment)
    display_name: Planned Study Day of Visit
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - visit day
      - study day
      - planned day
      - visitdy

  - name: planned_arm_code
    expr: source.ARMCD
    comment: Short code for the planned arm (null when the visit applies to all arms)
    display_name: Planned Arm Code
    synonyms:
      - arm code
      - armcd
      - treatment code
      - group code

  - name: description_of_planned_arm
    expr: source.ARM
    comment: Full descriptive name of the planned arm (null when the visit applies to all arms)
    display_name: Description of Planned Arm
    synonyms:
      - arm name
      - arm description
      - treatment arm
      - treatment group

measures:
  - name: visit_count
    expr: COUNT(*)
    comment: Total number of planned visit records in the trial visits domain
    display_name: Visit Count
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - number of visits
      - total visits
      - record count
      - visit records

  - name: distinct_visit_count
    expr: COUNT(DISTINCT source.VISIT)
    comment: Number of distinct planned visits across all arms
    display_name: Distinct Visit Count
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - unique visits
      - number of unique visits
      - distinct visits

  - name: arm_count
    expr: COUNT(DISTINCT source.ARMCD)
    comment: Number of distinct planned treatment arms with arm-specific visits
    display_name: Distinct Arm Count
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - number of arms
      - treatment arm count
      - unique arms
      - group count

  - name: study_count
    expr: COUNT(DISTINCT source.STUDYID)
    comment: Number of distinct clinical studies in the dataset
    display_name: Distinct Study Count
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - unique studies
      - number of studies
      - trial count

  - name: visits_list
    expr: "ARRAY_JOIN(TRANSFORM(SORT_ARRAY(COLLECT_SET(STRUCT(source.VISITNUM, source.VISIT))), x -> x.VISIT), ', ')"
    comment: Comma-separated list of distinct visits ordered by visit number
    display_name: Visits List (Ordered by Visit Number)
    synonyms:
      - visit schedule
      - ordered visits
      - visit list
      - planned visit sequence

  - name: max_study_day
    expr: MAX(source.VISITDY)
    comment: The latest planned study day across all visits, indicating the planned study duration in days
    display_name: Max Planned Study Day
    format:
      type: number
      decimal_places:
        type: exact
        places: 0
    synonyms:
      - last visit day
      - study duration days
      - latest planned day
      - max visit day
$$;

-- ======================================================================
-- vital_signs_metrics_view
-- ======================================================================
CREATE OR REPLACE VIEW {{TARGET_SCHEMA}}.vital_signs_metrics_view
COMMENT 'Vital Signs (VS) metric view based on CDISC SDTM specification. Provides standardized dimensions and measures for analysis of vital signs observations including blood pressure, heart rate, temperature, weight, and height.'
WITH METRICS
LANGUAGE YAML
AS
$$
version: 1.1

source: |-
  SELECT *,
    CONCAT(VSTEST, COALESCE(CONCAT(' (', VSSTRESU, ')'), '')) AS PARAM,
    VSSTRESN - LAG(VSSTRESN) OVER (
      PARTITION BY USUBJID, VSTESTCD
      ORDER BY VISITNUM
    ) AS CFPV
  FROM {{SDTM_SCHEMA}}.vs

joins:
  - name: dm
    source: {{SDTM_SCHEMA}}.dm
    using:
      - USUBJID

comment: "Vital Signs (VS) metric view based on CDISC SDTM specification. Provides standardized dimensions and measures
  for analysis of vital signs observations including blood pressure, heart rate, temperature, weight, and height.
  Statistics on results are only meaningful within one parameter."

dimensions:
  - name: study_id
    expr: source.STUDYID
    comment: Unique identifier for the clinical study (STUDYID)
    display_name: Study ID
    synonyms:
      - study
      - protocol
      - trial id
      - clinical study

  - name: subject_id
    expr: source.USUBJID
    comment: Unique subject identifier across all studies (USUBJID)
    display_name: Subject ID
    synonyms:
      - subject
      - patient
      - participant
      - usubjid

  - name: domain
    expr: source.DOMAIN
    comment: Two-character SDTM domain abbreviation, expected value VS (DOMAIN)
    display_name: Domain Abbreviation
    synonyms:
      - domain code
      - sdtm domain

  - name: sequence_number
    expr: source.VSSEQ
    comment: Sequence number to ensure uniqueness of records within a subject (VSSEQ)
    display_name: Sequence Number
    synonyms:
      - vsseq
      - record sequence

  - name: test_code
    expr: source.VSTESTCD
    comment: Short name of the vital signs test, e.g. SYSBP, DIABP, PULSE, TEMP, WEIGHT, HEIGHT (VSTESTCD)
    display_name: Test Code
    synonyms:
      - test code
      - vstestcd
      - vs test code
      - parameter code

  - name: test_name
    expr: source.VSTEST
    comment: Name of the vital signs test performed (VSTEST)
    display_name: Test Name
    synonyms:
      - test name
      - vstest
      - vital sign
      - measurement type

  - name: parameter
    expr: source.PARAM
    comment: Descriptive text for the vital signs parameter including standard units, derived as VSTEST (VSSTRESU)
    display_name: Parameter Description
    synonyms:
      - param
      - parameter name
      - test description
      - analysis parameter

  - name: category
    expr: source.VSCAT
    comment: Category for vital signs, used to group related tests (VSCAT)
    display_name: Category
    synonyms:
      - category
      - vscat
      - test category
      - vs category

  - name: subject_position
    expr: source.VSPOS
    comment: Position of the subject during the measurement, e.g. STANDING, SITTING, SUPINE (VSPOS)
    display_name: Subject Position
    synonyms:
      - position
      - vspos
      - body position
      - measurement position

  - name: original_result
    expr: source.VSORRES
    comment: Result or finding as originally collected in original units (VSORRES)
    display_name: Original Result
    synonyms:
      - vsorres
      - raw result
      - original finding
      - collected result

  - name: original_units
    expr: source.VSORRESU
    comment: Units of the original result (VSORRESU)
    display_name: Original Units
    synonyms:
      - vsorresu
      - raw units
      - collected units

  - name: standard_character_result
    expr: source.VSSTRESC
    comment: Character result in standardized format (VSSTRESC)
    display_name: Standardized Character Result
    synonyms:
      - vsstresc
      - standardized result
      - character result

  - name: standard_units
    expr: source.VSSTRESU
    comment: Units for the standardized numeric result, e.g. mmHg, beats/min, C, kg, cm (VSSTRESU)
    display_name: Standard Units
    synonyms:
      - vsstresu
      - std units
      - standardized units

  - name: completion_status
    expr: source.VSSTAT
    comment: Completion status of the measurement, e.g. NOT DONE (VSSTAT)
    display_name: Completion Status
    synonyms:
      - vsstat
      - status
      - done status
      - collection status

  - name: baseline_flag
    expr: source.VSLOBXFL
    comment: Last observation before exposure flag, Y if baseline (VSLOBXFL, SDTMIG 3.4 replacement for VSBLFL)
    display_name: Baseline Flag
    synonyms:
      - vslobxfl
      - vsblfl
      - baseline
      - baseline indicator
      - is baseline

  - name: derived_flag
    expr: source.VSDRVFL
    comment: Indicator for whether the result is derived, Y if derived (VSDRVFL)
    display_name: Derived Flag
    synonyms:
      - vsdrvfl
      - derived
      - derived indicator
      - is derived

  - name: visit_number
    expr: source.VISITNUM
    comment: Clinical encounter number used for sorting visits in chronological order (VISITNUM)
    display_name: Visit Number
    format:
      type: number
      decimal_places:
        type: exact
        places: 1
    synonyms:
      - visitnum
      - visit num
      - encounter number

  - name: visit_name
    expr: source.VISIT
    comment: Protocol-defined description of the clinical encounter, e.g. SCREENING, WEEK 4 (VISIT)
    display_name: Visit Name
    synonyms:
      - visit
      - visit label
      - encounter
      - clinic visit

  - name: planned_study_day
    expr: source.VISITDY
    comment: Planned study day of the visit relative to the reference start date (VISITDY)
    display_name: Planned Study Day
    synonyms:
      - visitdy
      - study day
      - planned day
      - protocol day

  - name: measurement_datetime
    expr: source.VSDTC
    comment: Date and time of the vital signs measurement in ISO 8601 format (VSDTC)
    display_name: Date/Time of Measurement
    synonyms:
      - vsdtc
      - measurement date
      - collection date
      - observation date

  - name: planned_time_point
    expr: source.VSTPT
    comment: Planned time point name for the measurement, e.g. AFTER LYING DOWN FOR 5 MINUTES (VSTPT)
    display_name: Planned Time Point
    synonyms:
      - vstpt
      - time point
      - scheduled time point
      - assessment time point

  - name: site_id
    expr: dm.SITEID
    comment: Unique identifier for an investigational site within a study.
    display_name: Site ID
    synonyms:
      - site identifier
      - investigational site ID
      - study site
      - clinical site

  - name: Age
    expr: dm.AGE
    comment: Age expressed in AGEU.
    display_name: Age
    synonyms:
      - patient age
      - subject age
      - participant age

  - name: age_unit
    expr: dm.AGEU
    comment: The unit used for age, normally years
    display_name: Age Unit

  - name: Sex
    expr: dm.SEX
    comment: Sex of the subject.
    display_name: Sex
    synonyms:
      - gender
      - sex category
      - biological sex

  - name: Race
    expr: dm.RACE
    comment: Race of the subject.
    display_name: Race
    synonyms:
      - racial category
      - race classification

  - name: arm_planned
    expr: dm.ARM
    comment: Name of the arm to which the subject was assigned. If the subject was not assigned to an arm, ARM is null and ARMNRS is populated.
    display_name: Planned Arm
    synonyms:
      - planned treatment arm
      - planned study arm
      - assigned arm
      - clinical study arm

  - name: arm_actual
    expr: dm.ACTARM
    comment: Name of the actual treatment arm.
    display_name: Actual Arm
    synonyms:
      - actual treatment arm
      - actual study arm

  - name: Country
    expr: dm.COUNTRY
    comment: Country of the investigational site (ISO 3166-1 alpha-3).
    display_name: Country
    synonyms:
      - country code
      - site country
      - location country
      - ISO country

  - name: standard_result
    expr: source.VSSTRESN
    comment: The numeric results in standard units (VSSTRESN)
    display_name: Result
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - result
      - value
      - vsstresn

  - name: standard_result_change
    expr: source.CFPV
    comment: The change from the previous visit for the same subject and test
    display_name: Change
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - delta
      - change from previous

measures:
  - name: observation_count
    expr: COUNT(*)
    comment: Total count of vital signs observation records
    display_name: Assessments
    synonyms:
      - record count
      - total observations
      - number of records
      - vs count

  - name: subject_count
    expr: COUNT(DISTINCT source.USUBJID)
    comment: Count of unique subjects with vital signs data
    display_name: Subjects
    synonyms:
      - patient count
      - number of patients
      - unique subjects
      - participant count

  - name: visit_count
    expr: COUNT(DISTINCT source.VISIT)
    comment: Count of distinct clinical visits with vital signs observations
    display_name: Visits
    synonyms:
      - number of visits
      - unique visits
      - distinct visits

  - name: mean_standard_result
    expr: AVG(source.VSSTRESN)
    comment: Arithmetic mean of numeric results in standard units (VSSTRESN)
    display_name: Mean Result
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - average result
      - mean value
      - avg vsstresn
      - mean vital sign

  - name: median_standard_result
    expr: PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY source.VSSTRESN)
    comment: Median (50th percentile) of numeric results in standard units (VSSTRESN)
    display_name: Median Result
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - median value
      - p50
      - 50th percentile
      - median vital sign

  - name: min_standard_result
    expr: MIN(source.VSSTRESN)
    comment: Minimum numeric result in standard units (VSSTRESN)
    display_name: Minimum Result (Standard Units)
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - minimum value
      - min value
      - lowest result
      - min vital sign

  - name: max_standard_result
    expr: MAX(source.VSSTRESN)
    comment: Maximum numeric result in standard units (VSSTRESN)
    display_name: Maximum Result (Standard Units)
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - maximum value
      - max value
      - highest result
      - max vital sign

  - name: stddev_standard_result
    expr: STDDEV(source.VSSTRESN)
    comment: Standard deviation of numeric results in standard units (VSSTRESN)
    display_name: Standard Deviation (Standard Units)
    format:
      type: number
      decimal_places:
        type: exact
        places: 3
    synonyms:
      - std dev
      - standard deviation
      - result variability
      - sd

  - name: baseline_mean_result
    expr: (AVG(source.VSSTRESN) FILTER (WHERE source.VSLOBXFL = 'Y'))
    comment: Mean of numeric results at baseline (VSLOBXFL = Y) in standard units
    display_name: Baseline Mean Result
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - baseline average
      - mean at baseline
      - baseline value

  - name: baseline_subject_count
    expr: COUNT(DISTINCT source.USUBJID) FILTER (WHERE source.VSLOBXFL = 'Y')
    comment: Number of unique subjects with baseline vital signs observations (VSLOBXFL = Y)
    display_name: Baseline Subject Count
    synonyms:
      - subjects at baseline
      - baseline patients
      - baseline participants

  - name: not_done_count
    expr: COUNT(*) FILTER (WHERE source.VSSTAT = 'NOT DONE')
    comment: Count of vital signs observations marked as NOT DONE
    display_name: Not Done Count
    synonyms:
      - missing observations
      - incomplete records
      - not performed count

  - name: change_from_baseline
    expr: MEASURE(mean_standard_result) - MEASURE(baseline_mean_result)
    window:
      - order: visit_number
        semiadditive: first
        range: all
    comment: "Mean result minus baseline mean result across subjects (a difference of group means, not a per-subject
      change; subjects missing at later visits bias it)"
    display_name: Change from Baseline
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - CFB
      - delta baseline
      - baseline change
      - mean change from baseline

  - name: baseline_mean_across_visits
    expr: AVG(source.VSSTRESN) FILTER (WHERE source.VSLOBXFL = 'Y')
    window:
      - order: visit_number
        semiadditive: first
        range: cumulative
    comment: Baseline mean result made available at every visit level via a window, so it can be subtracted at each visit.
    display_name: Baseline Mean (All Visits)
    format:
      type: number
      decimal_places:
        type: exact
        places: 2

  - name: change_from_baseline_by_visit
    expr: MEASURE(mean_standard_result) - MEASURE(baseline_mean_across_visits)
    comment: "Change from baseline at each visit: visit mean result minus the baseline mean (difference of group means).
      Use with visit_name or visit_number."
    display_name: Change from Baseline (by Visit)
    format:
      type: number
      decimal_places:
        type: exact
        places: 2
    synonyms:
      - CFB by visit
      - visit change from baseline
      - delta from baseline per visit
      - per-visit change
$$;
