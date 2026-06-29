---
name: cold-start-interview
description: >
  This skill should be used when the user runs
  "/corporate-strategy:cold-start-interview" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  corporate-strategy plugin," or wants to redo setup after the portfolio,
  growth ambition, or capital allocation process changes materially. Writes
  the shared org profile and the corporate-strategy practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "corporate-strategy practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Cold-Start Interview — corporate-strategy

## When to use

CSO, portfolio managers, corp dev — configure portfolio, growth, and capital allocation conventions. Explicit invocation only.

## What this skill does not do

- **Does not run portfolio analysis** — writes profiles only.
- **Does not auto-write without confirmation.**
- **Does not modify other plugins' profiles.**

## Preconditions

Per `../../references/cold-start-framework.md` — detect setup, offer quick/full.

## Provisional mode

Quick mode: essentials only; growth target must be recorded or flagged as required for `assess-growth-vectors`.

## Trust spine

Structured-aggregation bands; explicit confirmation before write; M&A track record captured for synergy calibration.

## Shared framework

Read `../../references/cold-start-framework.md` with `corporate-strategy` as plugin name.

**Org:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin:** `~/.claude/plugins/config/claude-for-strategy/corporate-strategy/CLAUDE.md`

## Plugin-specific interview

1. Full mode: recent portfolio review or growth deck.
2. Portfolio — units and priority ranking.
3. Growth ambition — rate, horizon, source (never blank).
4. Capital allocation — decision rhythm, stickiness.
5. Risk posture and track record — M&A, entries, exits.
6. Write profiles per templates.
7. Confirm and summarize.

## Living profile

Auto-apply this skill only after confirmation; other skills use propose profile update.

## Output format

Summary of org + plugin changes; defaults used; files written on confirmation.

## Worked example

**Input:** `--quick`, three BUs, 8% growth target board-set, annual capital cycle, conservative M&A track record.

**Summary excerpt:** Growth target 8%/3yr `[board]`; allocation stickiness ~2 quarters; synergy haircut defaults from past deals.

## Quality checks before delivering

- [ ] Growth target recorded or explicit gap flagged
- [ ] Confirmation before write
- [ ] Framework startup rules followed

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `assess-growth-vectors` or `allocate-resources`.
