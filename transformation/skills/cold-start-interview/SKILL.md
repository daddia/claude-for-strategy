---
name: cold-start-interview
description: >
  This skill should be used when the user runs
  "/transformation:cold-start-interview" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  transformation plugin," "teach Claude our platform context," or
  wants to redo that setup after the transformation program or platform
  context changes materially. Writes the shared org profile and the
  transformation practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "transformation practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Cold-Start Interview — transformation

## When to use

Run before transformation skills produce tailored output. Explicit invocation only.

## What this skill does not do

- **Does not build roadmaps or business cases** — writes profiles only.
- **Does not auto-write without confirmation.**

## Preconditions

Per `../../references/cold-start-framework.md` — detect setup, offer quick/full.

## Provisional mode

Unanswered items marked "no strong preference — will use generic defaults" for downstream skills.

## Trust spine

Structured-aggregation bands; explicit confirmation before write.

## Shared framework

Read `../../references/cold-start-framework.md` with `transformation` as plugin name.

**Org:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin:** `~/.claude/plugins/config/claude-for-strategy/transformation/CLAUDE.md`

## Plugin-specific interview

1. Quick vs full — full reviews prior roadmap/architecture/TOM.
2. Operating model — delivery, release, funding, governance, platform vocabulary, horizons.
3. Framework preferences — roadmap tracks, maturity framework, EA principles.
4. Definitions — maturity scale, transformation metrics, tech constraints, business-case thresholds.
5. Review gates — discovery exit, steering, investment, release.
6. Role context — leading, advising, reporting.
7. Write profiles; mark unanswered defaults.
8. Confirm and summarize.

## Living profile

Auto-apply this skill only after confirmation.

## Output format

Summary of org + plugin changes; files written on confirmation.

## Worked example

**Input:** `--quick`, dual-track delivery, Now/Next/Later horizons, 1–5 maturity scale.

**Summary excerpt:** Roadmap track model recorded; business-case threshold >$500K; EA principles pending full mode.

## Quality checks before delivering

- [ ] Delivery model and horizons recorded
- [ ] Maturity framework named
- [ ] Confirmation before write

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `roadmap-builder` or `business-case`.
