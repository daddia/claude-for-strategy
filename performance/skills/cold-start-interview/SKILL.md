---
name: cold-start-interview
description: >
  This skill should be used when the user runs
  "/performance:cold-start-interview" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  performance plugin," "teach Claude our KPI structure," or wants
  to redo that setup after the metric taxonomy or tracker structure changes
  materially. Writes the shared org profile and the performance practice
  profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "performance practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Cold-Start Interview — performance

## When to use

Run before `tracker-builder`, `kpi-tree-builder`, `metrics-glossary`, or `performance-narrative` produce tailored output. Explicit invocation only.

## What this skill does not do

- **Does not build trackers or KPI trees** — writes profiles only.
- **Does not auto-write without confirmation.**
- **Does not modify other plugins' profiles.**

## Preconditions

Per `../../references/cold-start-framework.md` — detect setup, offer quick/full.

## Provisional mode

Quick mode: KPI taxonomy and tracker structure must be recorded or flagged for `tracker-builder`.

## Trust spine

Structured-aggregation bands; explicit confirmation before write; tracker structure captured precisely.

## Shared framework

Read and follow `../../references/cold-start-framework.md` with `performance` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/performance/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied:

1. **Full mode:** review existing tracker if one exists.
2. **KPI taxonomy** — North Star metric(s); category codes and meanings.
3. **Tracker structure** — tool, summary columns, daily/period log mechanism, refresh cadence.
4. **Reporting** — narrative audience and cadence.
5. **Write profiles** — precise on tracker structure; note if none exists.
6. **Confirm and summarize.**

## Living profile

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills.

## Output format

Summary of org + plugin changes; defaults used; files written on confirmation.

## Worked example

**Input:** `--quick`, North Star = net revenue retention, B2/B3 category codes, Google Sheets Daily Log + SUMIFS summary, weekly rollup.

**Summary excerpt:** North Star NRR; tracker pattern Daily Log → Summary via SUMIFS; no existing tracker gaps flagged for `tracker-builder`.

## Quality checks before delivering

- [ ] North Star and taxonomy recorded
- [ ] Tracker structure precise or explicit gap noted
- [ ] Confirmation before write

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `kpi-tree-builder` or `tracker-builder`.
