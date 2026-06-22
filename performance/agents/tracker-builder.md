---
name: tracker-builder
description: >
  Tracker Builder — builds an actual `.xlsx` metrics tracker with a Daily Log
  tab wired to a Summary tab via live formulas, replicating your existing
  pattern rather than a generic template.
skills:
  - tracker-builder
---

# Tracker Builder

Build a real spreadsheet tracker: a daily/periodic log tab feeding a summary tab via `AVERAGEIFS`/`SUMIFS`-style formulas, matching the wiring pattern recorded in your practice profile. Reads the profile first — if a tracker already exists, this agent extends or replicates that exact structure, not a redesign. Flags any metric where the raw Daily Log input isn't yet specified rather than inventing plausible-looking columns.

**Command:** `/performance:tracker-builder`

Provide the metric list (from KPI Tree Builder or your own), then invoke this agent or run the command directly.
