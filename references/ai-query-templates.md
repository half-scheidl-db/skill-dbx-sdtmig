# ai_query Templates for SDTM Clinical Data

Ready-to-use Databricks SQL examples using `ai_query()` for clinical data tasks against SDTM structures.

---

## 1. MedDRA Classification

Map free-text adverse event terms (AETERM) to MedDRA Preferred Terms and System Organ Classes.

```sql
SELECT
  usubjid,
  aeterm,
  ai_query(
    'databricks-meta-llama-3-3-70b-instruct',
    CONCAT(
      'You are a medical coding specialist. Classify this adverse event term into MedDRA terminology. ',
      'Return ONLY a JSON object with these fields: ',
      '{"preferred_term": "...", "system_organ_class": "...", "llt": "..."}. ',
      'Use standard MedDRA preferred terms. Do not explain.\n\n',
      'Adverse event verbatim term: ', aeterm
    )
  ) AS meddra_json
FROM clinical_data.study_abc123.ae
WHERE aedecod IS NULL OR aebodsys IS NULL
```

**Input:** Rows from the AE domain where dictionary coding is incomplete.

**Output:** JSON string with `preferred_term` (maps to AEDECOD), `system_organ_class` (maps to AEBODSYS), and `llt` (lowest level term).

**Notes:**
- Parse the JSON output with `from_json()` or `get_json_object()` to extract fields
- Always validate results against the actual MedDRA dictionary before submission use
- Consider batching with `LIMIT` for large datasets to manage cost
- Model choice: use a larger model (70B+) for medical terminology accuracy

---

## 2. EPOCH Validation

Check that visit dates and assigned epochs are temporally consistent.

```sql
WITH epoch_checks AS (
  SELECT
    sv.usubjid,
    sv.visit,
    sv.visitnum,
    sv.epoch,
    sv.svstdtc,
    dm.rfstdtc,
    ai_query(
      'databricks-meta-llama-3-3-70b-instruct',
      CONCAT(
        'You are a clinical data reviewer checking SDTM epoch assignments. ',
        'In a typical clinical trial, epochs occur in this order: SCREENING, RUN-IN, TREATMENT, FOLLOW-UP. ',
        'The treatment reference start date is: ', COALESCE(dm.rfstdtc, 'unknown'), '. ',
        'A subject visit "', sv.visit, '" (visit number ', CAST(sv.visitnum AS STRING), ') ',
        'occurred on ', COALESCE(sv.svstdtc, 'unknown date'), ' ',
        'and is assigned to epoch "', sv.epoch, '". ',
        'Is this epoch assignment plausible? ',
        'Respond with JSON: {"valid": true/false, "reason": "brief explanation"}'
      )
    ) AS validation_result
  FROM clinical_data.study_abc123.sv sv
  LEFT JOIN clinical_data.study_abc123.dm dm ON sv.usubjid = dm.usubjid
  WHERE sv.epoch IS NOT NULL
)
SELECT *
FROM epoch_checks
WHERE get_json_object(validation_result, '$.valid') = 'false'
```

**Input:** Subject visits (SV) with epoch assignments, joined with Demographics (DM) for treatment start date.

**Output:** Rows where the LLM flags the epoch assignment as implausible, with reasoning.

**Notes:**
- This is a screening tool for data managers, not a definitive validation
- False positives are expected for complex study designs (crossover, adaptive)
- Filter to specific subjects or visits with `WHERE` to reduce cost

---

## 3. Synthetic Record Generation

Generate SDTM-compliant test records for a specified domain.

```sql
SELECT
  ai_query(
    'databricks-meta-llama-3-3-70b-instruct',
    CONCAT(
      'Generate 10 realistic SDTM Adverse Events (AE) domain records for a Phase III oncology trial. ',
      'Study ID: "ONCO-2024-001". Subject IDs: "ONCO-2024-001-001" through "ONCO-2024-001-005" (2 events each). ',
      '\n\nRequired variables per SDTMIG v3.4:\n',
      '- STUDYID (String): study identifier\n',
      '- DOMAIN (String): "AE"\n',
      '- USUBJID (String): unique subject ID\n',
      '- AESEQ (Int): sequence number, unique per subject\n',
      '- AETERM (String): verbatim adverse event term\n',
      '- AEDECOD (String): MedDRA Preferred Term\n',
      '- AEBODSYS (String): MedDRA System Organ Class\n',
      '- AESEV (String): MILD | MODERATE | SEVERE\n',
      '- AESER (String): Y | N\n',
      '- AEREL (String): NOT RELATED | POSSIBLY RELATED | RELATED\n',
      '- AEACN (String): DOSE NOT CHANGED | DOSE REDUCED | DRUG INTERRUPTED | DRUG WITHDRAWN\n',
      '- AEOUT (String): RECOVERED/RESOLVED | RECOVERING/RESOLVING | NOT RECOVERED/NOT RESOLVED | FATAL\n',
      '- AESTDTC (String): start date in ISO 8601 (2024-01-xx to 2024-06-xx range)\n',
      '- AEENDTC (String): end date in ISO 8601 (after start, within 30 days)\n',
      '\nReturn ONLY a JSON array of objects. Use clinically realistic oncology adverse events ',
      '(e.g., neutropenia, fatigue, nausea, peripheral neuropathy, anemia). ',
      'Ensure AESEQ is unique per USUBJID. Do not include explanatory text.'
    )
  ) AS synthetic_ae_json
```

**Post-processing:** Parse the JSON array into a DataFrame:

```python
from pyspark.sql import functions as F
from pyspark.sql.types import ArrayType, StructType, StructField, StringType, IntegerType

ae_schema = ArrayType(StructType([
    StructField("STUDYID", StringType()),
    StructField("DOMAIN", StringType()),
    StructField("USUBJID", StringType()),
    StructField("AESEQ", IntegerType()),
    StructField("AETERM", StringType()),
    StructField("AEDECOD", StringType()),
    StructField("AEBODSYS", StringType()),
    StructField("AESEV", StringType()),
    StructField("AESER", StringType()),
    StructField("AEREL", StringType()),
    StructField("AEACN", StringType()),
    StructField("AEOUT", StringType()),
    StructField("AESTDTC", StringType()),
    StructField("AEENDTC", StringType()),
]))

df_synthetic = (
    spark.sql("SELECT synthetic_ae_json FROM ...")
    .withColumn("parsed", F.from_json(F.col("synthetic_ae_json"), ae_schema))
    .select(F.explode("parsed").alias("record"))
    .select("record.*")
)
```

**Notes:**
- Include the variable spec in the prompt to ensure controlled terminology compliance
- Validate generated records against SDTM Core requirements before use
- Useful for testing pipelines, DQ rules, and downstream analytics without real patient data

---

## 4. Narrative Extraction

Extract structured SDTM fields from unstructured clinical narrative text.

```sql
SELECT
  note_id,
  patient_id,
  narrative_text,
  ai_query(
    'databricks-meta-llama-3-3-70b-instruct',
    CONCAT(
      'You are a clinical data abstraction specialist. Extract SDTM Adverse Event (AE) domain fields ',
      'from this clinical narrative. If a field cannot be determined, use null.\n\n',
      'Extract these SDTM AE variables:\n',
      '- AETERM: verbatim adverse event term as described\n',
      '- AEDECOD: MedDRA Preferred Term (your best coding)\n',
      '- AEBODSYS: MedDRA System Organ Class\n',
      '- AESEV: MILD | MODERATE | SEVERE (if mentioned)\n',
      '- AESER: Y | N (serious if: death, life-threatening, hospitalization, disability, congenital anomaly)\n',
      '- AEREL: NOT RELATED | POSSIBLY RELATED | RELATED (if causality mentioned)\n',
      '- AEACN: action taken with study drug (if mentioned)\n',
      '- AEOUT: outcome (if mentioned)\n',
      '- AESTDTC: start date in ISO 8601 (if mentioned)\n',
      '- AEENDTC: end date in ISO 8601 (if mentioned)\n',
      '\nReturn a JSON array of objects (one per adverse event found). If multiple events in one narrative, extract each separately.\n\n',
      'Clinical narrative:\n', narrative_text
    )
  ) AS extracted_events
FROM clinical_data.study_abc123.raw_clinical_notes
WHERE narrative_text IS NOT NULL
```

**Input:** Unstructured clinical notes or narratives (e.g., from an EHR integration or manual case reports).

**Output:** JSON array of extracted AE records, one per adverse event found in the narrative.

**Notes:**
- Multiple AEs can appear in a single narrative — the prompt handles this
- Extraction results require clinical review before use in regulatory submissions
- Consider adding few-shot examples to the prompt for domain-specific terminology
- Works well combined with template #1 (MedDRA classification) for a two-pass approach

---

## Best Practices

### Prompt Engineering for Clinical Data

1. **Specify controlled terminology** — include valid values (e.g., "MILD | MODERATE | SEVERE") in the prompt so the model constrains output to SDTM-compliant terms
2. **Request structured output** — always ask for JSON to enable downstream parsing with `from_json()` / `get_json_object()`
3. **Include domain context** — reference the specific SDTM domain and version for accuracy
4. **Set role context** — prefix prompts with a role ("You are a medical coding specialist") for better domain adherence

### Operational Considerations

- **Batch processing:** Use `LIMIT` and windowing for large tables to manage cost and latency
- **Validation layer:** Always validate ai_query outputs against controlled terminology before writing to curated tables
- **Human review:** LLM outputs for clinical data should be reviewed by domain experts before regulatory use
- **Determinism:** Set temperature to 0 (if supported) for consistent coding results
- **Audit trail:** Store both the raw LLM output and the final validated value for traceability

### Cost Management

```sql
-- Process in batches of 100 to control spend
SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (ORDER BY usubjid, aeseq) as rn
  FROM clinical_data.study_abc123.ae
  WHERE aedecod IS NULL
)
WHERE rn BETWEEN 1 AND 100
```
