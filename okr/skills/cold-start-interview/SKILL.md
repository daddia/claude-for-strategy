---
name: cold-start-interview
description: >
  This skill should be used when the user runs "/okr:cold-start-interview"
  (with optional --quick, --full, --redo, --check-integrations, or --resume),
  asks to "set up the okr plugin," "teach Claude our OKR process," or wants
  to redo that setup after the cadence, scoring approach, or cascade
  structure changes materially. Writes the shared org profile and the okr
  practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "okr practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Cold-Start Interview — okr

## When to use

OKR cycle owners configuring philosophy, scoring, cadence, and cascade — explicit invocation only. Philosophy question matters more here than most plugins.

## What this skill does not do

- **Does not draft OKRs** — writes profiles only.
- **Does not auto-write without confirmation.**
- **Does not modify other plugins' profiles.**

## Preconditions

Per `../../references/cold-start-framework.md` — detect setup, offer quick/full.

## Provisional mode

Quick mode: philosophy and scoring must be explicit choices, not silent defaults; gaps flagged for `set-targets` and `score-and-retro`.

## Trust spine

Structured-aggregation bands; explicit confirmation before write; commit vs aspirational philosophy recorded.

## Shared framework

Read and follow `../../references/cold-start-framework.md` with `okr` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/okr/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied (planning cadence may already be in org profile):

1. **Full mode:** include a prior cycle's OKR set — objectives, KRs, targets, scores.
2. **Philosophy** — commit-only vs mixed; sandbagging/overreach history.
3. **Scoring** — scale and formula (default linear interpolation baseline→target).
4. **Cadence** — cycle length, check-in frequency, retro timing (`check-in-nudge` agent).
5. **Cascade structure** — levels and ceilings on objectives/KRs per level.
6. **Cross-plugin:** whether `performance` is installed (metric handoff to `instrument-metrics`).
7. **Write profiles** — Philosophy and Scoring must not be silent defaults.
8. **Confirm and summarize.**

## Living profile

**Profile paths:** org `org-profile.md`; plugin `okr/CLAUDE.md` under `~/.claude/plugins/config/claude-for-strategy/`.

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills — org facts to org profile; OKR facts to plugin profile.

## Output format

Summary of org + plugin changes; defaults used; files written on confirmation.

## Worked example

**Input:** `--quick`, quarterly cycle, mixed commit/aspirational, linear scoring, 3 objectives max, performance plugin installed.

**Summary excerpt:** Philosophy mixed; aspirational band 0.6–0.7; check-in biweekly; cascade company→team; performance handoff enabled for `instrument-metrics`.

## Quality checks before delivering

- [ ] Philosophy and scoring explicitly recorded (not silent defaults)
- [ ] Cascade levels and ceilings captured
- [ ] Confirmation before write
- [ ] Framework startup rules followed

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `draft-objectives` or `cascade`.
