---
name: research-deep
description: Execute the approved structured research outline item-by-item using parallel web research, evidence triangulation, customs/product matching, supplier checks and strict uncertainty handling.
---

# Shen Heng Research — Deep Phase

## Trigger
`/research-deep`

## Workflow
1. Locate the active `<topic_slug>/outline.yaml` and `fields.yaml`.
2. Read `items` and execution settings.
3. Check `results/` for completed item JSON files and resume without duplicating completed work.
4. Research items in batches. Each item is an independent research unit.
5. For each item, use multiple query formulations and multiple source types appropriate to the topic.
6. Triangulate material facts whenever practical. Resolve conflicting numbers by recording source, year, methodology and reason for selecting one figure.
7. For company research, verify that the company identity and address match across sources before accepting a supplier/importer/contact relationship.
8. For customs research, distinguish importer-reported data, exporter mirror data and secondary databases.
9. For trade measures, verify effective dates, product scope, country scope, duty basis and whether the user's product is actually covered.
10. Mark unresolved values `[uncertain]` and add their field names to the JSON `uncertain` array.
11. Save one JSON per item under `results/`.
12. Validate field coverage before treating an item as complete.

## Research agent
Use the repository's `agents-codex/web-researcher.toml` configuration for the independent web-research worker. For steel/customs tasks, route through `agents-codex/web-search-modules/steel-trade.md`.

## Shen Heng prioritization
For market development research, prioritize evidence that answers: Can Shen Heng sell this product into this market, who is buying it, who supplies it now, what products/specifications are involved, and what regulatory or price barriers could prevent a deal?

## Required quality controls
- No fabricated values or contacts.
- No unsupported supplier/importer relationships.
- No duplicate companies when a prior list is available.
- Current/recent data should be preferred, but older complete data may be used when newer importer data is unavailable; state the year.
- Do not silently combine different HS codes into one market figure.
- Do not infer product demand solely from a generic steel company description.
- Preserve source URLs and source names for every important factual block.

## Output schema
Each item JSON should follow `fields.yaml`, use English field values for machine-readable output, and include:
```json
{"uncertain": []}
```
where unresolved fields are explicitly listed.

## Validation
After generating each result, run:
```bash
python .agents/skills/research-deep/scripts/validate_json.py -f <topic_slug>/fields.yaml -j <topic_slug>/results/<item>.json
```
Only treat the item as complete when validation passes.

## Resume behavior
A valid completed JSON should be skipped on subsequent runs unless the user requests refresh/recheck. If a file exists but fails validation or contains material uncertainty requiring recheck, research it again.

## Final status
Report completed items, failed items, uncertain items, and the results directory.
