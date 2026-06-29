---
name: practice-setup
description: >
  This skill should be used when the user runs
  "/market-intelligence:practice-setup" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  market-intelligence plugin," or wants to redo setup after the market
  definition, positioning, or competitor set changes materially. Writes the
  shared org profile and the market-intelligence practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "market-intelligence practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Practice Setup — market-intelligence

## When to use

Competitive strategy leads, CI analysts, product strategy partners — configure market definition, positioning, signal monitoring, and incentive context. Explicit invocation only.

## What this skill does not do

- **Does not run competitive analysis** — writes profiles only; route to `/market-intelligence:map-competitive-landscape` or `/market-intelligence:test-positioning`.
- **Does not auto-write without confirmation.**
- **Does not modify other plugins' profiles.**

## Preconditions

Per `../../references/practice-setup-framework.md` — detect existing setup, offer quick/full.

## Provisional mode

Quick mode: essentials only; market definition and competitor set must be recorded or flagged as required for `map-competitive-landscape` and `test-positioning`.

## Trust spine

Structured-aggregation bands; explicit confirmation before write; competitor claims and market figures tagged in seed review, never invented.

## Shared framework

Read and follow `../../references/practice-setup-framework.md` with `market-intelligence` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/market-intelligence/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied (sector may already be in org profile):

1. **Full mode:** include a recent competitive landscape deck or win/loss analysis.
2. **Market definition** — who you actually compete with vs. what a skeptical outsider would list. Push on narrow answers.
3. **Positioning** — current claim and what's deliberately ruled out. Flag if no trade-off is named.
4. **Incentive context** — internal and external incentive structures with specifics for `map-incentives`.
5. **Signal monitoring** — what counts as a meaningful signal and preferred scan cadence.
6. **Write profiles** following `../../CLAUDE.md`.
7. **Confirm and summarize.**

## Living profile

**Profile paths:** org `org-profile.md`; plugin `market-intelligence/CLAUDE.md` under `~/.claude/plugins/config/claude-for-strategy/`.

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills — org facts to org profile; market/positioning/signal facts to plugin profile.

## Output format

Summary of org + plugin changes; defaults used; files written on confirmation.

## Worked example

**Input:** `--quick`, B2B SaaS CI lead, five named competitors, positioning "mid-market workflow automation — not enterprise suite," weekly signal scan, no trade-off on geography yet.

**Summary excerpt:** Competitor set recorded with strategic groups; positioning claim captured; geography trade-off flagged `[review]` for `test-positioning`; signal taxonomy defaults to pricing/product/partnership.

## Quality checks before delivering

- [ ] Market definition and competitor set recorded or explicit gap flagged
- [ ] Positioning trade-off captured or flagged for follow-up
- [ ] Confirmation before write
- [ ] Framework startup rules followed

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `map-competitive-landscape` or `map-incentives`.
