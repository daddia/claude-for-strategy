---
name: workplan-builder
description: >
  This skill should be used when the user asks to "turn this into a workplan,"
  "build a hypothesis-driven workplan," "who's doing what on this analysis,"
  or has a hypothesis tree (from this plugin or elsewhere) that needs owners,
  timelines, and data sources attached.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "consulting practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Workplan Builder

## When to use

Translate hypothesis tree into executable workplan with owners, timelines, data sources, pre-stated so-whats.

## What this skill does not do

- **Does not build hypothesis tree** — route to `hypothesis-tree` if missing.
- **Does not assign owners without confirmation** — flag TBD.
- **Does not invent data sources** — flag unknown.

## Preconditions

| Input | If missing |
|---|---|
| Hypothesis tree | Ask to run `hypothesis-tree` or supply structure |
| Owner/timeline constraints | Ask; no arbitrary day counts |

## Provisional mode

Missing owners/timelines: table with TBD flags; no silent placeholders.

## Trust spine

- **Confidence bands** (`structured-aggregation`): High = all rows complete; Medium = some TBD; Low = tree missing branches.
- **Escalation:** Disproportionate effort vs so-what → flag revisit tree.

## Workflow

1. Get hypothesis tree.
2. Per sub-hypothesis: analysis method, data source, owner, timeline, expected so-what (from tree).
3. Sanity-check effort vs payoff.
4. Output table; flag incomplete rows.

## Output format

| Hypothesis | Analysis | Data source | Owner | Timeline | Expected so-what |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

Flags: effort/payoff mismatches; missing owner/timeline/source.

## Worked example

**Input:** Tree branch "elasticity >15% in mid-tier."

**Row:** Cohort price-volume analysis | billing warehouse | TBD owner | before steering 3/15 | if true, supports revert recommendation.

## Quality checks before delivering

- [ ] So-what carried from tree pre-analysis
- [ ] No invented sources or owners
- [ ] Effort flags applied

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: drop into tracker or steering deck.
