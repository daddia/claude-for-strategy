---
name: practice-setup
description: >
  This skill should be used when the user runs
  "/value-realisation:practice-setup", asks to "set up the
  value-realisation plugin," "teach Claude how we track benefits," or
  wants to redo that setup after the benefits framework, governance
  model, or realisation cadence changes materially.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "value-realisation practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Practice Setup — value-realisation

## When to use

Run before benefits skills produce tailored output. Baseline-discipline answer matters — get honest answer before anything else.

## What this skill does not do

- **Does not map or track benefits** — writes profile only.
- **Does not auto-write without confirmation.**
- **Does not replace propose profile update** — other skills must show diffs and ask before profile changes.

## Preconditions

Offer quick vs full; read org profile via shared framework when applicable.

## Provisional mode

Unanswered items → "no strong preference — will flag baselines and attribution conservatively by default."

## Trust spine

Structured-aggregation bands; explicit confirmation; baseline discipline recorded honestly.

## Shared framework

Read `../../references/practice-setup-framework.md` with `value-realisation` as plugin name where org layer needed.

**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/value-realisation/CLAUDE.md`

## Plugin-specific interview

1. Benefits framework and taxonomy.
2. Governance — benefit owner vs delivery PM; escalation; decision log home.
3. Baseline discipline — before vs after go-live (push for honest answer).
4. Attribution convention.
5. Cadence — realisation window, tracking, review triggers.
6. Cross-plugin: transformation/corporate-strategy installed?
7. Seed documents (full mode).
8. Write profile per `../../CLAUDE.md` template into the config path above.
9. Confirm and summarize.

**Propose profile update:** all other skills — org facts to org profile; benefits framework, baseline discipline, and cadence facts to plugin profile.

## Output format

Summary of profile changes; files written on confirmation.

## Worked example

**Input:** Baselines usually reconstructed after go-live; judgment-based attribution; quarterly tracking.

**Summary excerpt:** Baseline discipline recorded as post-go-live; downstream skills will flag RETROFITTED BASELINE conservatively.

## Quality checks before delivering

- [ ] Baseline discipline honest (not rounded up)
- [ ] Benefit owner vs PM distinction captured
- [ ] Confirmation before write

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `benefits-map` or `benefits-register`.
