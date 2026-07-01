---
name: milestone-tracker
description: >
  This skill should be used when the user asks to "where are we against
  plan," "check milestone status," "what's on the critical path," or
  provides a milestone plan and actuals that need a critical-path status
  check with slippage flagged.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "pmo practice"
  review_cadence: "quarterly"
  work_shape: "governance-tracking"
  permission_tier: advisory
  output_class: "tracking-update"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Milestone Tracker

## When to use

Critical-path milestone status with slippage against profile tolerance — knock-on effects, not flat date lists.

## What this skill does not do

- **Does not invent progress** — ask for plan and actuals.
- **Does not escalate non-critical float slips** — distinguish timeline threats from noise.

## Preconditions

| Input | If missing |
|---|---|
| Milestone plan | Ask — halt if absent |
| Current actuals/forecast | Ask — don't infer |
| Slippage tolerance (profile) | Default with `[PROVISIONAL]` |

## Provisional mode

Partial actuals: assess available milestones; flag incomplete coverage.

## Trust spine

- **Confidence bands** (`governance-tracking`):
  - **High:** Critical path identified; slippage classified; knock-on effects stated.
  - **Medium:** Some forecasts uncertain — tagged `[review]`.
  - **Low:** Plan missing — halt.
- **Failure modes:**
  - **Incentive Gaming:** N/A — schedule focus.
- **Escalation triggers:** Critical-path slip beyond tolerance — overall end date at risk.

## Workflow

1. Read profile for plan location and slippage tolerance.
2. Get plan and actuals.
3. Identify critical path vs float.
4. Classify each critical milestone: on track / at risk / slipped.
5. State knock-on effects for at-risk/slipped items.
6. Note non-critical items briefly without escalation.
7. Gaming-pattern check before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
CRITICAL PATH STATUS:
[Milestone] — Planned: [date] | Actual/Forecast: [date] | Status: [...]
  Knock-on effect: [...]

NON-CRITICAL (float available): [...]
OVERALL END DATE: [on track | at risk | slipped] — [why]
```

## Worked example

**Input:** Integration milestone 2 weeks late on critical path; QA milestone 1 week late with float.

**Expected output:** Integration slipped with end-date knock-on; QA noted non-critical only.

## Quality checks before delivering

- [ ] Critical path distinguished from float
- [ ] Tolerance from profile applied
- [ ] Knock-on effects for critical slips
- [ ] No invented actuals

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/pmo:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `status-report`, `raid-log` entry, or recovery plan.
