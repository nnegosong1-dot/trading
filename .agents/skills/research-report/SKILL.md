---
name: research-report
description: Convert completed Shen Heng research JSON results into a concise, evidence-based Markdown report, preserving source traceability and excluding unresolved values from headline conclusions.
---

# Shen Heng Research — Report Phase

## Trigger
`/research-report`

## Workflow
1. Locate `<topic_slug>/outline.yaml`, `fields.yaml`, and `results/`.
2. Load all valid result JSON files.
3. Extract useful summary metrics for the table of contents.
4. Generate a Markdown report covering all defined fields and relevant extra fields.
5. Exclude fields marked `[uncertain]`, fields listed in `uncertain`, and empty values from headline conclusions.
6. Keep source attribution close to the factual claim.
7. For Shen Heng market research, add a decision-oriented section: priority, product fit, buyer/importer fit, supplier landscape, trade barriers, and recommended next action.
8. Save `<topic_slug>/report.md` and, when needed, `<topic_slug>/generate_report.py`.

## Formatting rules
- Support flat and nested JSON.
- Map English/Chinese category names bidirectionally.
- Format lists of dictionaries compactly.
- Break long text for readability.
- Put unclassified extra fields under `Other Info`.
- Never turn an uncertain value into a factual headline.

## Shen Heng report structure
1. Executive Summary
2. Research Scope & Data Years
3. Market / Product Findings
4. Importer & Buyer Findings
5. Supplier / Origin Findings
6. Trade Measures & Commercial Risks
7. Priority Ranking
8. Company-level Detail
9. Sources & Evidence Notes
10. Recommended Next Actions

## Output
`<topic_slug>/report.md`
