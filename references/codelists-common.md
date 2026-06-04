# Common CDISC Controlled Terminology for SDTM

The most frequently used codelists in SDTMIG v3.4 submissions. Values are CDISC Controlled Terminology submission values.

---

## SEX (C66731)

Sex of the subject.

| Submission Value | Definition |
|---|---|
| F | Female |
| M | Male |
| U | Unknown |
| UNDIFFERENTIATED | Undifferentiated |

---

## RACE (C74457)

Race of the subject.

| Submission Value | Definition |
|---|---|
| AMERICAN INDIAN OR ALASKA NATIVE | A person having origins in any of the original peoples of North and South America |
| ASIAN | A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian subcontinent |
| BLACK OR AFRICAN AMERICAN | A person having origins in any of the black racial groups of Africa |
| NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER | A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands |
| WHITE | A person having origins in any of the original peoples of Europe, the Middle East, or North Africa |
| MULTIPLE | More than one race reported |
| NOT REPORTED | Not reported |
| UNKNOWN | Unknown |
| OTHER | Other |

---

## ETHNIC (C66790)

Ethnicity of the subject.

| Submission Value | Definition |
|---|---|
| HISPANIC OR LATINO | A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin |
| NOT HISPANIC OR LATINO | A person not of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin |
| NOT REPORTED | Not reported |
| UNKNOWN | Unknown |

---

## NY (C66742)

Yes/No response (no null allowed).

| Submission Value | Definition |
|---|---|
| N | No |
| Y | Yes |

---

## NYNULL (C66742 variant)

Yes/No response (null allowed for not assessed).

| Submission Value | Definition |
|---|---|
| N | No |
| Y | Yes |
| *(null)* | Not assessed or not applicable |

---

## EPOCH (C99079)

Trial epoch — a period of time in the planned conduct of a study.

| Submission Value | Definition |
|---|---|
| SCREENING | Period for assessing eligibility |
| RUN-IN | Period between screening and treatment for washout or stabilization |
| TREATMENT | Period during which treatment is administered |
| FOLLOW-UP | Period after treatment for observing outcomes |
| NOT APPLICABLE | Not applicable |

---

## ACN (C66767)

Action taken with study treatment.

| Submission Value | Definition |
|---|---|
| DOSE NOT CHANGED | Dose of study treatment was not changed |
| DOSE REDUCED | Dose of study treatment was reduced |
| DOSE INCREASED | Dose of study treatment was increased |
| DRUG INTERRUPTED | Study treatment was temporarily interrupted |
| DRUG WITHDRAWN | Study treatment was permanently discontinued |
| NOT APPLICABLE | Not applicable (e.g., event not related to treatment) |
| UNKNOWN | Unknown action taken |

---

## AEOUT (C66768)

Outcome of the adverse event.

| Submission Value | Definition |
|---|---|
| FATAL | Subject died |
| NOT RECOVERED/NOT RESOLVED | Adverse event has not resolved at time of last observation |
| RECOVERED/RESOLVED | Adverse event has completely resolved |
| RECOVERED/RESOLVED WITH SEQUELAE | Adverse event resolved with lasting effects |
| RECOVERING/RESOLVING | Adverse event is improving but not yet resolved |
| UNKNOWN | Outcome is unknown |

---

## AESEV (C66769)

Severity or intensity of the adverse event.

| Submission Value | Definition |
|---|---|
| MILD | Awareness of sign or symptom but easily tolerated |
| MODERATE | Discomfort enough to cause interference with usual activity |
| SEVERE | Incapacitating with inability to perform usual activities |

---

## AEREL (C66756)

Causality — relationship of adverse event to study treatment.

| Submission Value | Definition |
|---|---|
| NOT RELATED | No reasonable possibility of causal relationship |
| UNLIKELY RELATED | Doubtful causal relationship |
| POSSIBLY RELATED | Causal relationship cannot be ruled out |
| PROBABLY RELATED | Likely causal relationship |
| RELATED | Definite causal relationship |

---

## POSITION (C71148)

Position of the subject during measurement.

| Submission Value | Definition |
|---|---|
| SITTING | Seated position |
| STANDING | Upright position |
| SUPINE | Lying face up |
| PRONE | Lying face down |
| SEMI-RECUMBENT | Partially reclined |
| TRENDELENBURG | Supine with feet elevated above head |
| REVERSE TRENDELENBURG | Supine with head elevated above feet |

---

## LAT (C99073)

Laterality qualifier.

| Submission Value | Definition |
|---|---|
| LEFT | Left side |
| RIGHT | Right side |
| BILATERAL | Both sides |

---

## DIR (C99074)

Directionality — anatomical direction qualifier.

| Submission Value | Definition |
|---|---|
| ANTERIOR | Front |
| POSTERIOR | Back |
| DORSAL | Back surface |
| LATERAL | Side |
| MEDIAL | Toward midline |
| PROXIMAL | Closer to trunk |
| DISTAL | Further from trunk |
| UPPER | Above |
| LOWER | Below |

---

## VSTESTCD (C66741)

Vital signs test short names (used for VSTESTCD variable).

| Submission Value (VSTESTCD) | VSTEST (Full Name, codelist C67153) | Typical Unit |
|---|---|---|
| HEIGHT | Height | cm |
| WEIGHT | Weight | kg |
| BMI | BMI | kg/m2 |
| SYSBP | Systolic Blood Pressure | mmHg |
| DIABP | Diastolic Blood Pressure | mmHg |
| HR | Heart Rate | beats/min |
| TEMP | Temperature | C |
| RESP | Respiratory Rate | breaths/min |
| PULSE | Pulse Rate | beats/min |
| MAP | Mean Arterial Pressure | mmHg |

---

## LBTEST (selected common lab tests)

| Submission Value (LBTESTCD) | LBTEST (Full Name) | Typical Unit | Category |
|---|---|---|---|
| ALB | Albumin | g/L | Chemistry |
| ALP | Alkaline Phosphatase | U/L | Chemistry |
| ALT | Alanine Aminotransferase | U/L | Chemistry |
| AST | Aspartate Aminotransferase | U/L | Chemistry |
| BILI | Bilirubin | umol/L | Chemistry |
| BUN | Blood Urea Nitrogen | mmol/L | Chemistry |
| CREAT | Creatinine | umol/L | Chemistry |
| GLUC | Glucose | mmol/L | Chemistry |
| HBA1C | Hemoglobin A1C | % | Chemistry |
| K | Potassium | mmol/L | Chemistry |
| NA | Sodium | mmol/L | Chemistry |
| CHOL | Cholesterol | mmol/L | Chemistry |
| HGB | Hemoglobin | g/L | Hematology |
| HCT | Hematocrit | fraction | Hematology |
| WBC | Leukocytes | 10^9/L | Hematology |
| PLAT | Platelets | 10^9/L | Hematology |
| RBC | Erythrocytes | 10^12/L | Hematology |
| NEUT | Neutrophils | 10^9/L | Hematology |
| LYMPH | Lymphocytes | 10^9/L | Hematology |

---

## Common Units (C71620)

| Unit | Used For |
|---|---|
| kg | Weight |
| cm | Height |
| kg/m2 | BMI |
| mmHg | Blood pressure |
| beats/min | Heart rate, pulse |
| breaths/min | Respiratory rate |
| C | Temperature |
| g/L | Albumin, hemoglobin |
| U/L | Liver enzymes (ALT, AST, ALP) |
| umol/L | Bilirubin, creatinine |
| mmol/L | Electrolytes, glucose, cholesterol |
| 10^9/L | WBC, platelets, neutrophils |
| 10^12/L | RBC |
| mg | Dose amount |
| mg/dL | US lab units (glucose, creatinine) |
| % | HbA1c, hematocrit (alternate) |
