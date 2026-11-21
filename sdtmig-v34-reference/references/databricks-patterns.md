# Databricks Code Patterns for SDTM

Reusable PySpark and SQL templates for working with SDTM data on Databricks.

---

## 1. Create an SDTM Domain Table in Unity Catalog

```sql
CREATE TABLE IF NOT EXISTS clinical_data.study_abc123.ae (
  studyid       STRING    NOT NULL COMMENT 'Unique identifier for a study.',
  domain        STRING    NOT NULL COMMENT 'Two-character abbreviation for the domain.',
  usubjid       STRING    NOT NULL COMMENT 'Identifier used to uniquely identify a subject across all studies.',
  aeseq         INT       NOT NULL COMMENT 'Sequence number to ensure uniqueness within domain.',
  aegrpid       STRING             COMMENT 'Used to tie together a block of related records.',
  aerefid       STRING             COMMENT 'Internal or external identifier such as a serial number on an SAE form.',
  aespid        STRING             COMMENT 'Sponsor-defined identifier.',
  aeterm        STRING    NOT NULL COMMENT 'Verbatim name of the event.',
  aedecod       STRING    NOT NULL COMMENT 'Dictionary-derived term (MedDRA Preferred Term).',
  aebodsys      STRING             COMMENT 'Body system or organ class (MedDRA SOC).',
  aecat         STRING             COMMENT 'Category for the adverse event.',
  aesev         STRING             COMMENT 'Severity or intensity: MILD, MODERATE, SEVERE.',
  aeser         STRING             COMMENT 'Serious event flag: Y or N.',
  aeacn         STRING             COMMENT 'Action taken with study treatment.',
  aerel         STRING             COMMENT 'Causality: relationship to study treatment.',
  aeout         STRING             COMMENT 'Outcome of the adverse event.',
  aestdtc       STRING             COMMENT 'Start date/time (ISO 8601).',
  aeendtc       STRING             COMMENT 'End date/time (ISO 8601).',
  aedy          INT                COMMENT 'Study day of start of event.'
)
COMMENT 'Adverse Events — One record per adverse event per subject'
TBLPROPERTIES (
  'sdtm.class'     = 'Events',
  'sdtm.structure' = 'One record per adverse event per subject',
  'sdtm.version'   = '3.4'
);
```

---

## 2. Lakeflow Declarative Pipeline (medallion) for SDTM ETL

Uses the current `pyspark.pipelines` API (`dp`). Older `import dlt` code still runs, but don't use it for new code.

```python
from pyspark import pipelines as dp
from pyspark.sql import functions as F

RAW = "/Volumes/clinical_data/raw/study_abc123/ae/"   # one folder per domain

# --- Bronze: incremental raw ingestion with Auto Loader ---

@dp.table(name="ae_bronze", comment="Raw adverse events as delivered (CSV extracts)")
def ae_bronze():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", True)
        .load(RAW)
        .withColumn("_source_file", F.col("_metadata.file_path"))
    )


# --- Silver: SDTM-conformed and validated ---

@dp.table(name="ae_silver", comment="SDTM-conformed adverse events")
@dp.expect_or_drop("valid_studyid", "studyid IS NOT NULL")
@dp.expect_or_drop("valid_usubjid", "usubjid IS NOT NULL")
@dp.expect_or_drop("valid_aeseq", "aeseq IS NOT NULL")
@dp.expect_or_drop("valid_aeterm", "aeterm IS NOT NULL")
@dp.expect("valid_severity", "aesev IN ('MILD', 'MODERATE', 'SEVERE') OR aesev IS NULL")
@dp.expect("valid_serious", "aeser IN ('Y', 'N') OR aeser IS NULL")
def ae_silver():
    return (
        spark.readStream.table("ae_bronze")
        .withColumn("domain", F.lit("AE"))
        .withColumn("aeseq", F.col("aeseq").cast("int"))
        .withColumn("aedy", F.col("aedy").cast("int"))
        .select(
            "studyid", "domain", "usubjid", "aeseq",
            "aegrpid", "aerefid", "aespid",
            "aeterm", "aedecod", "aebodsys", "aecat",
            "aesev", "aeser", "aeacn", "aerel", "aeout",
            "aestdtc", "aeendtc", "aedy"
        )
    )


# --- Gold: analysis-ready (ADaM-style) ---

@dp.materialized_view(name="adae", comment="Analysis dataset for adverse events (ADaM ADAE-like)")
def adae():
    dm = spark.read.table("dm_silver")
    ae = spark.read.table("ae_silver")
    return (
        ae.join(dm.select("usubjid", "arm", "rfstdtc"), on="usubjid", how="left")
        .withColumn("astdt", F.to_date(F.substring("aestdtc", 1, 10)))
        .withColumn("aendt", F.to_date(F.substring("aeendtc", 1, 10)))
        .withColumn("trtemfl", F.when(F.col("astdt") >= F.to_date(F.substring("rfstdtc", 1, 10)), "Y"))
    )
```

> ISO 8601 `--DTC` values can be partial (`2024-03`) or carry a time (`2024-03-05T10:30`). Take the date part before casting, and decide explicitly how to impute partial dates.

---

## 3. Data Quality Expectations from SDTM Core

Derive the Core=Req rules from the workbook metadata (`references/variables.csv`, uploaded next to the pipeline code or to a Volume) so they never drift from the standard:

```python
import csv
from pyspark import pipelines as dp

VARIABLES_CSV = "/Volumes/clinical_data/reference/sdtmig/variables.csv"

def required_vars(domain: str) -> list[str]:
    with open(VARIABLES_CSV, newline="") as f:
        return [r["Variable Name"].lower() for r in csv.DictReader(f)
                if r["Dataset Name"] == domain.upper() and r["Core"] == "Req"]

def build_expectations(domain: str) -> dict:
    """Core=Req -> NOT NULL expectations. Exp/Perm are not null-checked."""
    return {f"req_{v}": f"{v} IS NOT NULL" for v in required_vars(domain)}


@dp.table(name="lb_silver")
@dp.expect_all_or_drop(build_expectations("LB"))
def lb_silver():
    return spark.readStream.table("lb_bronze").select(...)
```

`Req` = must be present and non-null. `Exp` = column must exist, nulls allowed. `Perm` = include when collected. Use `expect` (warn) rather than `expect_or_drop` if dropped rows would hide data-quality problems from data managers.

---

## 4. Ingest SAS XPT Files into Delta

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Using the sas7bdat/xport format via spark-sas7bdat or pandas
import pandas as pd

def ingest_xpt_to_delta(xpt_path: str, catalog: str, schema: str, domain: str):
    """Read a SAS XPT transport file and write to Unity Catalog as Delta."""
    pdf = pd.read_sas(xpt_path, format="xport", encoding="utf-8")

    # Lowercase all column names to match SDTM convention in UC
    pdf.columns = [c.lower() for c in pdf.columns]

    df = spark.createDataFrame(pdf)
    df.write.mode("overwrite").saveAsTable(f"{catalog}.{schema}.{domain}")

# Example usage
ingest_xpt_to_delta(
    xpt_path="/Volumes/clinical_data/raw/study_abc123/ae.xpt",
    catalog="clinical_data",
    schema="study_abc123",
    domain="ae"
)
```

---

## 5. Synthetic SDTM Data Generation with PySpark

```python
from pyspark.sql import SparkSession, Row
from pyspark.sql import functions as F
import random
from datetime import date, timedelta

spark = SparkSession.builder.getOrCreate()

def generate_sdtm_ae(study_id: str, n_subjects: int = 10, max_events: int = 5):
    """Generate synthetic SDTM AE domain records."""
    
    TERMS = [
        ("Headache", "Headache", "Nervous system disorders"),
        ("Nausea", "Nausea", "Gastrointestinal disorders"),
        ("Fatigue", "Fatigue", "General disorders and administration site conditions"),
        ("Dizziness", "Dizziness", "Nervous system disorders"),
        ("Rash", "Rash", "Skin and subcutaneous tissue disorders"),
        ("Arthralgia", "Arthralgia", "Musculoskeletal and connective tissue disorders"),
    ]
    SEVERITY = ["MILD", "MODERATE", "SEVERE"]
    OUTCOME = ["RECOVERED/RESOLVED", "RECOVERING/RESOLVING", "NOT RECOVERED/NOT RESOLVED"]
    ACTION = ["DOSE NOT CHANGED", "DOSE REDUCED", "DRUG INTERRUPTED", "DRUG WITHDRAWN"]

    rows = []
    for subj_num in range(1, n_subjects + 1):
        usubjid = f"{study_id}-{subj_num:03d}"
        n_events = random.randint(1, max_events)
        base_date = date(2024, 1, 1) + timedelta(days=random.randint(0, 60))

        for seq in range(1, n_events + 1):
            term, decod, bodsys = random.choice(TERMS)
            start = base_date + timedelta(days=random.randint(0, 90))
            end = start + timedelta(days=random.randint(1, 30))
            rows.append(Row(
                studyid=study_id,
                domain="AE",
                usubjid=usubjid,
                aeseq=seq,
                aeterm=term,
                aedecod=decod,
                aebodsys=bodsys,
                aesev=random.choice(SEVERITY),
                aeser=random.choice(["Y", "N"]),
                aerel=random.choice(["NOT RELATED", "POSSIBLY RELATED", "RELATED"]),
                aeacn=random.choice(ACTION),
                aeout=random.choice(OUTCOME),
                aestdtc=start.isoformat(),
                aeendtc=end.isoformat(),
            ))

    return spark.createDataFrame(rows)

# Generate and write
df_ae = generate_sdtm_ae("ABC-001", n_subjects=50, max_events=5)
df_ae.write.mode("overwrite").saveAsTable("clinical_data.study_abc001.ae")
```

---

## 6. Volume-Based File Organization

Recommended Volumes layout for clinical trial data:

```
/Volumes/clinical_data/
├── raw/
│   └── study_abc123/
│       ├── ae.xpt
│       ├── dm.xpt
│       ├── lb.xpt
│       └── ...
├── define/
│   └── study_abc123/
│       └── define.xml
└── submissions/
    └── study_abc123/
        └── m5/
            └── datasets/
                ├── ae.xpt
                └── ...
```
