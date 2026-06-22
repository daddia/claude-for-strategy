---
name: metrics-glossary
description: >
  This skill should be used when the user asks to "document our metric
  definitions," "build a metrics glossary," "what does this metric actually
  mean," or needs a single source-of-truth reference for how each tracked
  metric is defined, sourced, and owned.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Metrics Glossary

Produce a single source-of-truth glossary entry per metric: name, exact formula, data source, owner, refresh cadence. The point is precision — two different people should be able to read an entry and calculate the same number independently.

## Process

1. **Read the practice profile** (`~/.claude/plugins/config/claude-for-strategy/performance/CLAUDE.md`) for existing category codes and known metrics.

2. **For each metric, capture**:
   - **Name** and **category code** (if applicable).
   - **Exact formula** — not a description ("conversion rate") but the literal calculation ("completed signups ÷ unique visitors to signup page, same period, excluding bot traffic per the standard filter").
   - **Data source** — the actual system/sheet/table the inputs come from.
   - **Owner** — who's accountable for the number being right.
   - **Refresh cadence** — how often it updates.
   - **Known caveats** — anything that would make two people calculate it differently if not stated (timezone handling, what counts as "active," exclusions).

3. **Flag ambiguous formulas explicitly** — if the user describes a metric in a way that admits multiple calculation methods, ask which one rather than picking one silently. This is the most common source of "the dashboard says X but the report says Y" problems later.

4. **Check for near-duplicate metrics** — two entries that sound different but calculate almost the same thing under different names; flag for consolidation.

## Output format

```
METRIC: [name] [category code]
  Formula: [exact calculation]
  Source: [system/sheet/table]
  Owner: [name/role]
  Refresh: [cadence]
  Caveats: [anything that affects reproducibility]

[repeat per metric]

AMBIGUITY FLAGS: [metrics where the formula needs clarification]
NEAR-DUPLICATE FLAGS: [metrics that may be the same thing under different names]
```
