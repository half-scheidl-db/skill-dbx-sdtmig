# SDTMIG v3.4 skill for Databricks

An [Agent Skill](https://agentskills.io) that gives coding agents, such as Genie Code, Genie Code CLI and Claude Code, a fast reference to **CDISC SDTMIG v3.4 metadata**: datasets, variables, roles, core status and common controlled terminology. It also includes a CDISC Therapeutic Area User Guide index and SDTM-specific Databricks patterns for Unity Catalog tables, Lakeflow pipelines and `ai_query`.

## Repository layout

```
skill-dbx-sdtmig/                 ← register this folder as a skills folder
├── sdtmig-v34-reference/         ← the skill (folder name == skill name)
│   ├── SKILL.md
│   ├── references/
│   │   ├── datasets.md / .csv
│   │   ├── domains/{DOMAIN}.md   ← one file per domain (63)
│   │   ├── variables.csv         ← machine-readable, for code only (~430 KB)
│   │   ├── codelists-common.md / .csv
│   │   ├── workbook-readme.md
│   │   ├── cdisc_therapeutic_areas.md
│   │   ├── databricks-patterns.md
│   │   ├── ai-query-templates.md
│   │   ├── synthetic-study-generation.md  ← workflow: NCT ID -> spec -> SDTM -> validation
│   │   ├── ctgov-mapping.md
│   │   └── coherence-rules.md
│   ├── assets/study-spec-template.yaml
│   ├── assets/metric-views/sdtm_metric_views.sql  ← 8 UC metric views (AE CM DM DS LB TS TV VS)
│   └── scripts/
│       ├── ctgov_to_spec.py      ← ClinicalTrials.gov record -> reviewed study spec
│       ├── generate_sdtm.py      ← spec -> coherent fictional SDTM (CSV/parquet/UC)
│       ├── validate_sdtm.py      ← 55 cross-domain coherence rules
│       └── deploy_metric_views.py ← render + create the metric views
└── source/                       ← original workbook + raw extract (not loaded by agents)
```

The skill lives in a subfolder, so the repo root can be registered directly as a skills folder.

## Install

**Genie Code (workspace)**
1. Add this repo as a Databricks Git folder, e.g. `/Users/<you>/skill-dbx-sdtmig`.
2. In the Genie Code pane open **Settings → skills**, enter the Git folder path and click **Add folder**. Register the repo root, not `sdtmig-v34-reference/`.
3. Start a new chat. The skill loads automatically for SDTM questions, or you can `@sdtmig-v34-reference` it.

Alternatively, copy `sdtmig-v34-reference/` into `Workspace/.assistant/skills/` (workspace skill) or `/Users/<you>/.assistant/skills/` (user skill).

**Genie Code CLI**: copy or symlink `sdtmig-v34-reference/` into `~/.genie/skills/`, or into `.agents/skills/` of a project repo.

**Claude Code**: copy or symlink `sdtmig-v34-reference/` into `~/.claude/skills/` or `.claude/skills/`.

## Synthetic SDTM in three commands

```bash
cd sdtmig-v34-reference/scripts
python ctgov_to_spec.py NCT04487080 --out-dir ../../study      # draft spec; review the `review:` list
python generate_sdtm.py ../../study/NCT04487080_spec.yaml --out ../../study/sdtm
python validate_sdtm.py ../../study/sdtm                       # 0 errors expected
```

Requires `pandas`, `numpy` and `pyyaml`. Output is fictional by design (`SYN-` STUDYID, `[SYNTHETIC]` title).

## Scope and limitations

- Workbook **metadata only**, not the SDTMIG prose (assumptions, examples).
- SDTMIG v3.4 only; SEND, ADaM, CDASH and other IG versions are out of scope.
- The TAUG file is an index; full TAUGs are available from CDISC.
- `ai_query` outputs (e.g. MedDRA suggestions) are aids for humans, not coded submission values.

## Source and licensing

The metadata is derived from the CDISC SDTMIG v3.4 metadata workbook (`source/SDTMIG_v3.4.xlsx`). CDISC standards are subject to the [CDISC IP policy and terms of use](https://www.cdisc.org/). Confirm that redistributing the workbook and derived metadata is permitted before sharing this repository publicly.
