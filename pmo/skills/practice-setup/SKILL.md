---
name: practice-setup
description: >
  This skill should be used when the user runs
  "/pmo:practice-setup" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  pmo plugin," "teach Claude our governance cadence," or
  wants to redo that setup after the governance structure or reporting
  format changes materially. Writes the shared org profile and the pmo
  practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "pmo practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Practice Setup — pmo

## When to use

Run before `raid-log`, `status-report`, `steering-pack`, `milestone-tracker`, or `decision-log` produce tailored output. Explicit invocation only.

## What this skill does not do

- **Does not run governance tasks** — writes profiles only.
- **Does not auto-write without confirmation.**

## Preconditions

Per `../../references/practice-setup-framework.md` — detect setup, offer quick/full.

## Provisional mode

Quick mode: RAG thresholds and RAID distinctions must be explicit, not silent defaults.

## Trust spine

Structured-aggregation bands; explicit confirmation before write; concrete RAG/RAID definitions captured.

## Shared framework

Read `../../references/practice-setup-framework.md` with `pmo` as plugin name.

**Org:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin:** `~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md`

## Plugin-specific interview

1. Full mode: existing status report, RAID, or steering pack.
2. Governance structure — steering cadence, escalation thresholds, RAID definitions.
3. Status reporting — audiences, RAG thresholds, cadence.
4. Milestone tracking — plan location, slippage tolerance.
5. Decision log — format and storage.
6. Write profiles — precise RAG/RAID distinctions.
7. Confirm and summarize.

## Living profile

Auto-apply this skill only after confirmation; other skills use propose profile update.

## Output format

Summary of org + plugin changes; files written on confirmation.

## Worked example

**Input:** `--quick`, weekly sponsor report, Red = missed critical milestone, RAID in Jira.

**Summary excerpt:** RAG thresholds recorded; escalation = program schedule impact; milestone source Jira.

## Quality checks before delivering

- [ ] RAG thresholds concrete
- [ ] RAID category definitions captured
- [ ] Confirmation before write

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `status-report` or `raid-log`.
