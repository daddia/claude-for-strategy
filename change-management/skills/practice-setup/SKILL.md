---
name: practice-setup
description: >
  This skill should be used when the user runs
  "/change-management:practice-setup" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  change-management plugin," "teach Claude our OCM approach," or
  wants to redo setup after the change methodology, sponsor model, or
  comms approval path changes materially. Writes the shared org profile
  and the change-management practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "change-management practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Practice Setup — change-management

## When to use

Run before other change-management skills produce tailored output. Explicit invocation only.

## What this skill does not do

- **Does not run change analysis** — writes profiles only.
- **Does not auto-write without confirmation.**

## Preconditions

Per `../../references/practice-setup-framework.md` — detect setup, offer quick/full.

## Provisional mode

Quick mode: change methodology, sponsor visibility definition, and comms approval path must be explicit, not silent defaults.

## Trust spine

Structured-aggregation bands; explicit confirmation before write; readiness RAG and sponsor definitions captured concretely.

## Shared framework

Read `../../references/practice-setup-framework.md` with `change-management` as plugin name.

**Org:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin:** `~/.claude/plugins/config/claude-for-strategy/change-management/CLAUDE.md`

## Plugin-specific interview

1. Full mode: existing stakeholder map, comms plan, or readiness assessment as seed.
2. Change methodology — ADKAR, Kotter, house framework, or hybrid; change network model.
3. Sponsor engagement — what "visible/available/active" means; cadence and checkpoints.
4. Comms ownership — who drafts, approves, and sends; approval path before external distribution.
5. Readiness gates — dimensions checked before go-live; people-side RAG if used.
6. Resistance taxonomy — how the practice labels loss, competence, habit, and political blockers.
7. Write profiles — precise sponsor and readiness definitions.
8. Confirm and summarize.

## Living profile

Auto-apply this skill only after confirmation; other skills use propose profile update.

## Output format

Summary of org + plugin changes; files written on confirmation.

## Worked example

**Input:** `--quick`, Prosci ADKAR hybrid, sponsor = monthly town hall + weekly email, comms via central team with program lead draft.

**Summary excerpt:** Sponsor visibility = town hall + weekly note; comms approval = central comms sign-off; readiness dimensions = leadership alignment + training complete.

## Quality checks before delivering

- [ ] Change methodology recorded
- [ ] Sponsor visibility definition concrete
- [ ] Comms approval path captured
- [ ] Confirmation before write

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `stakeholder-impact-map` or `change-readiness-assessment`.
