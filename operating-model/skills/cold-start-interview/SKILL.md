---
name: cold-start-interview
description: >
  This skill should be used when the user runs
  "/operating-model:cold-start-interview" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  operating-model plugin," or wants to redo setup after the structure,
  decision rights, or reward mechanics change materially. Writes the shared
  org profile and the operating-model practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "operating-model practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Cold-Start Interview — operating-model

## When to use

Org design leads configuring structure fit, decision rights, matrix rules, span/layers, and reward mechanics — explicit invocation only.

## What this skill does not do

- **Does not run org design analysis** — writes profiles only.
- **Does not auto-write without confirmation.**
- **Does not modify other plugins' profiles.**

## Preconditions

Per `../../references/cold-start-framework.md` — detect setup, offer quick/full.

## Provisional mode

Quick mode: structure-fit priority and reward mechanism must be recorded or flagged for `diagnose-structure-fit` and `align-rewards-and-incentives`.

## Trust spine

Structured-aggregation bands; explicit confirmation before write; rewards captured as actual measurement/pay, not values doc.

## Shared framework

Read and follow `../../references/cold-start-framework.md` with `operating-model` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/operating-model/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied:

1. **Full mode:** current org chart and RACI documentation as seed.
2. **Structure fit** — what structure optimizes for (efficiency, innovation, customer intimacy, coordination).
3. **Decision-rights gaps** — contested or unclear ownership decisions.
4. **Matrix relationships** — dual reporting and tie-breaker rules.
5. **Span and layers** — typical team sizes, layer count.
6. **Rewards and incentives** — how people are actually measured and paid; re-ask if sanitized.
7. **Write profiles** following `../../CLAUDE.md`.
8. **Confirm and summarize.**

## Living profile

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills.

## Output format

Summary of org + plugin changes; defaults used; files written on confirmation.

## Worked example

**Input:** `--quick`, matrix product/geo, no documented tie-breakers, functional bonuses, 6 layers.

**Summary excerpt:** Structure optimizes customer intimacy; matrix tie-breakers flagged unknown; reward mechanism functional P&L — note for `align-rewards-and-incentives`.

## Quality checks before delivering

- [ ] Structure-fit priority recorded
- [ ] Reward mechanism captured (not values-only)
- [ ] Matrix/tie-breaker status recorded
- [ ] Confirmation before write

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `diagnose-structure-fit` or `design-decision-rights`.
