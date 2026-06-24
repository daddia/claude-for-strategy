---
name: tracker-builder
description: >
  This skill should be used when the user asks to "build me a metrics
  tracker," "wire up a daily log to the summary sheet," "create a
  performance tracker spreadsheet," or needs an actual spreadsheet built
  that replicates a Daily Log / summary-sheet pattern with formulas wired
  between tabs.
allowed-tools: Read, Grep, Glob, Write, Bash
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "performance practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Tracker Builder

## When to use

Build actual `.xlsx` tracker — Daily Log tab feeding Summary via live formulas — replicating practice profile pattern, not generic template.

## What this skill does not do

- **Does not define metrics** — route to `/performance:metrics-glossary` or `/performance:kpi-tree-builder` first.
- **Does not invent raw input columns** — ask for actual source fields.
- **Does not redesign existing tracker** — extends/replicates profile pattern.

## Preconditions

| Input | If missing |
|---|---|
| Performance practice profile (tracker structure) | Ask; default Daily Log + SUMIFS summary with `[PROVISIONAL]` |
| Metric list for this tracker | Ask which metrics and category codes |
| xlsx build guidance | Read `/mnt/skills/public/xlsx/SKILL.md` before building |

## Provisional mode

No existing pattern in profile: default Daily Log + Summary with AVERAGEIFS/SUMIFS movement columns; document formula logic tab.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Live formulas wired; raw inputs separate from calculated; formula doc included.
  - **Medium:** Some raw inputs `INPUT NEEDED` flagged in notes.
  - **Low:** Metric list undefined — halt build.
- **Failure modes:**
  - **Strategic advice vs. support:** Tracker is draft structure for owner validation.
  - **Client confidentiality:** Tracker may contain proprietary metrics — CONFIDENTIAL header on docs.
  - **Accountability gap:** Formula logic documented for maintainability.
  - **Analytical Rigor:** Completeness — every summary metric traces to log inputs.
  - **Incentive Gaming:** N/A — build focus.
- **Escalation triggers:** Raw input unspecified — flag, don't invent column.

## Workflow

1. **Read practice profile** for existing tracker structure.
2. **Confirm metric list** and category codes.
3. **Design Daily Log** — one row per period, columns for raw inputs only.
4. **Design Summary** — movement columns via AVERAGEIFS/SUMIFS per profile pattern.
5. **Build `.xlsx`** with live formulas per xlsx skill guidance.
6. **Document formula logic** in notes tab or section.
7. **Flag unspecified raw inputs** — don't invent.
8. **Completeness check** before delivery.

## Output format

Deliverable: `.xlsx` with Daily Log + Summary tabs (minimum), formula documentation, file path confirmed with user.

```
TRACKER LOCATION: [path]
METRICS INCLUDED: [list]
FORMULA PATTERN: [AVERAGEIFS/SUMIFS/etc.]
INPUT GAPS: [raw inputs not yet specified]
```

## Worked example

**Input:** Three B2 metrics; profile shows SUMIFS on date column; weekly periods.

**Expected output:** `.xlsx` with Daily Log date column + three raw input columns; Summary rows with current/prior/change via SUMIFS; notes tab listing formula references.

## Quality checks before delivering

- [ ] Formulas live, not static values
- [ ] Raw inputs separate from calculated metrics
- [ ] Pattern matches profile or documented default
- [ ] Formula logic documented
- [ ] Unspecified inputs flagged not invented

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: populate Daily Log, `performance-narrative` once data exists, or `metrics-glossary` for new metrics.
