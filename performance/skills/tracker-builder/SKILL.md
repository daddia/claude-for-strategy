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
  version: "0.1.0"
---

# Tracker Builder

Build an actual spreadsheet tracker: a daily/periodic log tab feeding a summary tab via formulas, replicating the user's existing pattern rather than a generic template. This skill produces a real `.xlsx` file — when the spreadsheet itself needs to be created or edited, read `/mnt/skills/public/xlsx/SKILL.md` first for the correct build approach in this environment, then apply the structure below.

## Process

1. **Read the practice profile** (`~/.claude/plugins/config/claude-for-strategy/performance/CLAUDE.md`) for the existing tracker structure — summary sheet columns, the daily log mechanism, and the metric taxonomy/category codes. If a tracker already exists, this skill's job is to extend or replicate that exact pattern, not redesign it.

2. **Confirm the metric list** for this specific tracker — which metrics, under which category codes, with what refresh cadence.

3. **Design the Daily Log tab**: one row per period (day, typically), one column per raw input needed to calculate each tracked metric. Keep raw inputs separate from calculated metrics — the log captures inputs, the summary sheet calculates.

4. **Design the summary sheet**: one row (or section) per metric, with movement columns (period-over-period or against-target change) calculated from the Daily Log via `AVERAGEIFS`/`SUMIFS`-style formulas keyed on date ranges — matching whatever the practice profile records as the existing wiring pattern. If no existing pattern is recorded, default to: a movement column per metric showing current-period value, prior-period value, and absolute/percentage change, each computed via `AVERAGEIFS`/`SUMIFS` against the Daily Log's date column.

5. **Build the actual file** using the xlsx skill's guidance — formulas should be live formulas in the output file, not static computed values, so the tracker keeps working as new daily log rows are added.

6. **Document the formula logic** in a short notes section or tab in the output — what each summary column's formula references, so the tracker is maintainable without re-deriving the logic from scratch.

7. **Flag any metric where the raw input needed for the Daily Log isn't yet specified** — don't invent a plausible-looking input column; ask what the actual source field is.

## Output

A `.xlsx` file with at minimum: a Daily Log tab and a Summary tab with live formulas wired between them, following the structure above. Confirm the file location with the user (this environment's outputs directory) once built.
