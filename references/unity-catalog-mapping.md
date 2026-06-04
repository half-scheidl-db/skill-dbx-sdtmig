# SDTM to Unity Catalog Mapping Guide

How to represent SDTMIG v3.4 metadata using Databricks Unity Catalog constructs.

---

## Type Mapping

| SDTM Type | Variable Pattern | Unity Catalog Type | Notes |
|-----------|-----------------|-------------------|-------|
| Char | General text | `STRING` | Default for all Char variables |
| Num | `--SEQ`, `--DY` | `INT` | Sequence numbers and study days |
| Num | General numeric | `DOUBLE` | Lab results, vital signs measurements |
| Char | `--DTC` (dates) | `STRING` | ISO 8601 partial dates cannot use DATE type |
| Char | `--DUR` (durations) | `STRING` | ISO 8601 duration format (Char in SDTMIG, e.g., "PT2H30M") |

### Why --DTC stays STRING

SDTM dates use ISO 8601 with permitted partial representations (e.g., `2024-03`, `2024`, `2024-01-15T08:30`). Spark's `DATE` and `TIMESTAMP` types reject incomplete values. Keep them as `STRING` and parse to `DATE`/`TIMESTAMP` only in downstream silver/gold layers where imputation rules apply.

---

## Role Mapping → Column Tags

| SDTM Role | UC Tag | Purpose |
|-----------|--------|---------|
| Identifier | `sdtm_role:identifier` | Subject/record keys |
| Topic | `sdtm_role:topic` | The focus of the observation |
| Qualifier | `sdtm_role:qualifier` | Additional context about the topic |
| Timing | `sdtm_role:timing` | When the observation occurred |
| Record Qualifier | `sdtm_role:record_qualifier` | Qualifies the entire record |
| Synonym Qualifier | `sdtm_role:synonym_qualifier` | Alternative names |
| Variable Qualifier | `sdtm_role:variable_qualifier` | Qualifies a specific variable |
| Rule | `sdtm_role:rule` | Algorithmic or rule-based |

```sql
ALTER TABLE clinical_data.study_abc123.ae
  ALTER COLUMN usubjid SET TAGS ('sdtm_role' = 'identifier');
ALTER TABLE clinical_data.study_abc123.ae
  ALTER COLUMN aeterm SET TAGS ('sdtm_role' = 'topic');
ALTER TABLE clinical_data.study_abc123.ae
  ALTER COLUMN aesev SET TAGS ('sdtm_role' = 'qualifier');
ALTER TABLE clinical_data.study_abc123.ae
  ALTER COLUMN aestdtc SET TAGS ('sdtm_role' = 'timing');
```

---

## Core Mapping → Constraints and Expectations

| SDTM Core | Unity Catalog Constraint | DLT Expectation | Behavior |
|-----------|-------------------------|-----------------|----------|
| Req | `NOT NULL` | `@dlt.expect_or_drop` | Row rejected if missing |
| Exp | Nullable (no constraint) | `@dlt.expect` | Row flagged, not dropped |
| Perm | Nullable (no constraint) | None | No validation |

```sql
-- Apply NOT NULL for Core=Req variables
ALTER TABLE clinical_data.study_abc123.ae
  ALTER COLUMN studyid SET NOT NULL;
ALTER TABLE clinical_data.study_abc123.ae
  ALTER COLUMN usubjid SET NOT NULL;
ALTER TABLE clinical_data.study_abc123.ae
  ALTER COLUMN aeseq SET NOT NULL;
ALTER TABLE clinical_data.study_abc123.ae
  ALTER COLUMN aeterm SET NOT NULL;
```

---

## Naming Conventions

| Level | Convention | Example |
|-------|-----------|---------|
| Catalog | Organization or program level | `clinical_data` |
| Schema | One per study | `study_abc123` |
| Table | Lowercase domain name | `ae`, `dm`, `lb`, `vs` |
| Column | Lowercase variable name | `usubjid`, `aeterm`, `aestdtc` |

### Alternative schema strategies

| Strategy | When to use |
|----------|-------------|
| `study_{id}` | Single-study analysis, simple navigation |
| `{study_id}_{submission}` | Multiple submissions per study |
| `sdtm` + `adam` schemas | Separate raw SDTM from analysis datasets |

---

## Table-Level Metadata

```sql
CREATE TABLE clinical_data.study_abc123.dm (
  ...
)
COMMENT 'Demographics — One record per subject'
TBLPROPERTIES (
  'sdtm.class'     = 'Special-Purpose',
  'sdtm.structure' = 'One record per subject',
  'sdtm.version'   = '3.4',
  'sdtm.domain'    = 'DM'
);
```

| Property | Source | Purpose |
|----------|--------|---------|
| `COMMENT` | Dataset Label from SDTMIG | Human-readable description |
| `sdtm.class` | Class column from workbook | Filter domains by class |
| `sdtm.structure` | Structure column from workbook | Documents record grain |
| `sdtm.version` | IG version | Traceability |
| `sdtm.domain` | Dataset Name | Programmatic lookup |

---

## Column-Level Metadata

```sql
ALTER TABLE clinical_data.study_abc123.dm
  ALTER COLUMN usubjid COMMENT 'Identifier used to uniquely identify a subject across all studies.';

ALTER TABLE clinical_data.study_abc123.dm
  ALTER COLUMN usubjid SET TAGS (
    'sdtm_role' = 'identifier',
    'sdtm_core' = 'req',
    'sdtm_codelist' = ''
  );

ALTER TABLE clinical_data.study_abc123.dm
  ALTER COLUMN sex COMMENT 'Sex of the subject.';

ALTER TABLE clinical_data.study_abc123.dm
  ALTER COLUMN sex SET TAGS (
    'sdtm_role' = 'record_qualifier',
    'sdtm_core' = 'req',
    'sdtm_codelist' = 'C66731'
  );
```

---

## Complete Example: DM Domain

```sql
CREATE TABLE IF NOT EXISTS clinical_data.study_abc123.dm (
  studyid     STRING    NOT NULL  COMMENT 'Unique identifier for a study.',
  domain      STRING    NOT NULL  COMMENT 'Two-character abbreviation for the domain.',
  usubjid     STRING    NOT NULL  COMMENT 'Identifier used to uniquely identify a subject across all studies.',
  subjid      STRING    NOT NULL  COMMENT 'Subject identifier unique within a study.',
  rfstdtc     STRING              COMMENT 'Subject reference start date/time (ISO 8601). May be null for screen failures.',
  rfendtc     STRING              COMMENT 'Subject reference end date/time (ISO 8601).',
  siteid      STRING    NOT NULL  COMMENT 'Unique identifier for a site within a study.',
  brthdtc     STRING              COMMENT 'Date/time of birth (ISO 8601).',
  age         DOUBLE              COMMENT 'Age at reference start date.',
  ageu        STRING              COMMENT 'Units for AGE: YEARS, MONTHS, WEEKS, DAYS, HOURS.',
  sex         STRING    NOT NULL  COMMENT 'Sex of the subject.',
  race        STRING              COMMENT 'Race of the subject.',
  ethnic      STRING              COMMENT 'Ethnicity of the subject.',
  armcd       STRING              COMMENT 'Short name for planned arm.',
  arm         STRING              COMMENT 'Description of planned arm.',
  actarmcd    STRING              COMMENT 'Short name for actual arm.',
  actarm      STRING              COMMENT 'Description of actual arm.',
  country     STRING    NOT NULL  COMMENT 'Country (ISO 3166 three-letter code).',
  dmdtc       STRING              COMMENT 'Date/time of collection (ISO 8601).',
  dmdy        INT                 COMMENT 'Study day of collection.'
)
COMMENT 'Demographics — One record per subject'
TBLPROPERTIES (
  'sdtm.class'     = 'Special-Purpose',
  'sdtm.structure' = 'One record per subject',
  'sdtm.version'   = '3.4',
  'sdtm.domain'    = 'DM'
);
```

---

## Discovery Queries

Find all SDTM tables in a catalog:

```sql
SELECT table_schema, table_name, comment
FROM clinical_data.information_schema.tables
WHERE table_schema LIKE 'study_%'
ORDER BY table_schema, table_name;
```

Find all required (Core=Req) columns for a domain:

```sql
SELECT column_name, comment
FROM clinical_data.information_schema.columns
WHERE table_schema = 'study_abc123'
  AND table_name = 'ae'
  AND is_nullable = 'NO';
```

Find columns by SDTM role tag:

```sql
SELECT table_name, column_name, tag_value
FROM clinical_data.information_schema.column_tags
WHERE tag_name = 'sdtm_role'
  AND tag_value = 'identifier';
```
