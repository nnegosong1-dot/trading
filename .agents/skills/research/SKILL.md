---
name: research
description: Start a structured preliminary research project for Shen Heng Steel. Build a research outline and field schema before deep research, with customs-data, product-fit, supplier, customer and trade-measure dimensions when relevant.
---

# Shen Heng Research — Preliminary Phase

## Trigger
`/research <topic>`

## Purpose
Create a reproducible research project before deep searching. The project must define research objects, fields, evidence standards, and execution settings.

## Workflow
1. Parse the user's topic and identify the business decision the research must support.
2. Build an initial item list and field framework from model knowledge.
3. Supplement the framework with live web research when the topic is current, market-related, company-related, customs-related, regulatory, or otherwise time-sensitive.
4. Merge relevant Shen Heng reference rules from `../shenheng-deep-research/references/`.
5. Create `<topic_slug>/outline.yaml` and `<topic_slug>/fields.yaml`.
6. Show the proposed scope and ask for confirmation only when a material scope decision remains. Do not block useful work on optional details.

## Shen Heng default research dimensions
When applicable, include:
- Market size and import trend
- HS code / product mapping
- Import value and quantity
- China share and major supplying countries
- Product-level demand for HRC, CRC, GI/GL, PPGI/PPGL, GI/PPGI strip, angle, channel, UPN/UPE, IPE/IPEAA, H beam, flat bar and wire rod
- Anti-dumping, safeguard, tariff and other trade measures
- Major importers / distributors / stockists / traders
- Current suppliers and origin countries
- Company website evidence of steel demand
- Contact information and procurement contacts
- Duplicate screening
- Commercial attractiveness for Shen Heng

## Evidence rules
- Never invent a company, importer, supplier, contact, trade flow, HS code, tariff, price or quantity.
- Separate confirmed facts, reasonable inference and unresolved uncertainty.
- Prefer customs/statistical sources and official government sources for trade figures and measures.
- Prefer official company websites and verified company profiles for identity/contact information.
- Record data year and publication/update date.
- Do not treat a mirror/export record as equivalent to importer-reported customs data without labeling it.

## Output
```text
<topic_slug>/
  outline.yaml
  fields.yaml
  results/
```

The outline should contain `topic`, `items`, and `execution.batch_size`, `execution.items_per_agent`, and `execution.output_dir`. Fields should define categories, descriptions, detail levels, and an `uncertain` mechanism.

## Follow-up
- `/research-add-items`
- `/research-add-fields`
- `/research-deep`
- `/research-report`
