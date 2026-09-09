---
name: research-add-items
description: Expand an existing Shen Heng research project's item list with additional relevant companies, markets, products or competitors without duplicating existing items.
---

# Add Research Items

## Trigger
`/research-add-items <what to add>`

## Workflow
1. Locate the active `<topic_slug>/outline.yaml`.
2. Read all existing items.
3. Search for missing objects relevant to the research decision.
4. Deduplicate by normalized company/entity name and known aliases.
5. Add only evidence-supported items; mark newly proposed items with rationale.
6. Update `outline.yaml` while preserving existing execution settings.
7. Report what was added and what was rejected as duplicate or weakly relevant.

## Shen Heng rules
For customer development, prefer distributors, stockists, traders, agents, terminals and processing factories with demonstrable steel demand. Do not add manufacturers merely because they are large steel companies unless the research explicitly targets manufacturers.
