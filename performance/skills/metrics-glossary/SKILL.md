---
name: metrics-glossary
description: >
  This skill should be used when the user asks to "document our metric
  definitions," "build a metrics glossary," "what does this metric actually
  mean," or needs a single source-of-truth reference for how each tracked
  metric is defined, sourced, and owned.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "performance practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Metrics Glossary

## When to use

Single source-of-truth glossary — exact formula, source, owner, cadence — so two people calculate the same number.

## What this skill does not do

- **Does not build KPI trees** — route to `/performance:kpi-tree-builder`.
- **Does not pick ambiguous formulas silently** — flags for clarification.
- **Does not duplicate OKR instrumentation** — `okr:instrument-metrics` defers here when performance installed.

## Preconditions

| Input | If missing |
|---|---|
| Metrics to document | Ask user to list |
| Performance practice profile | Proceed; flag `[PROVISIONAL]` on category codes |

## Provisional mode

Ambiguous formulas: **AMBIGUITY FLAGS** — do not finalize entry until clarified.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Every metric has exact formula, source, owner, cadence, caveats.
  - **Medium:** Some ambiguities or near-duplicates flagged.
  - **Low:** Formulas described not calculated — halt until literal formula provided.
- **Failure modes:**
  - **Strategic advice vs. support:** Glossary is draft for metric governance approval.
  - **Client confidentiality:** Definitions may expose internal systems — CONFIDENTIAL header.
  - **Accountability gap:** Owner named per metric.
  - **Analytical Rigor:** Completeness check; near-duplicate consolidation flagged.
  - **Incentive Gaming:** N/A — definition focus.
- **Escalation triggers:** Two metrics calculating same thing under different names — flag consolidation.

## Workflow

1. **Read practice profile** for category codes and known metrics.
2. **Per metric:** name, code, exact formula, source, owner, refresh, caveats.
3. **Flag ambiguous formulas** — ask, don't pick silently.
4. **Check near-duplicates** for consolidation.
5. **Completeness check** before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
METRIC: [name] [category code]
  Formula: [exact calculation]
  Source: [system/sheet/table]
  Owner: [name/role]
  Refresh: [cadence]
  Caveats: [...]

AMBIGUITY FLAGS: [...]
NEAR-DUPLICATE FLAGS: [...]
```

## Worked example

**Input:** "Conversion rate" — user says "signups divided by visitors."

**Expected output (excerpt):**

```
METRIC: Conversion rate [B3]
  Formula: AMBIGUITY FLAG — admits multiple methods (unique visitors vs sessions; signup completion definition) [review]
```

## Quality checks before delivering

- [ ] Literal formulas, not descriptions
- [ ] Ambiguities flagged not silently resolved
- [ ] Near-duplicates checked
- [ ] Owner and source per metric
- [ ] Every metric in scope covered

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: governance approval, `tracker-builder` wiring, or `okr:instrument-metrics` handoff.
