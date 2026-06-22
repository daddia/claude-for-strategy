---
name: set-targets-and-initiatives
description: >
  This skill should be used when the user asks to "set targets for the
  scorecard," "what initiatives support this objective," or needs each
  measure given a target and each objective checked against whether a real
  program of work is actually driving it.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Set Targets and Initiatives

The classic BSC four-column structure is Objective, Measure, Target, Initiative — and the Initiative column is where most scorecards quietly fail. An objective with a target but no named initiative is a wish with a number attached; an initiative with no objective behind it is busywork that happens to be funded. This skill checks both directions, not just the target-setting.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for scoring/status convention.

2. **Set current value and target for each measure** from `select-measures`. Where the current value is unknown, route to measurement first rather than guessing a baseline.

3. **For every objective, require at least one named strategic initiative** — an actual program of work, with enough specificity to tell whether it's happening (not "improve customer experience" as its own initiative, but "redesign the onboarding flow" as the initiative meant to move the Customer-perspective objective). If an objective has a target but no initiative, flag it explicitly: this objective currently has no engine behind it.

4. **Check the reverse direction** if the user provides an existing initiative portfolio: for every initiative, does it map to a specific strategic objective on the map? An initiative with no objective it's meant to serve is a candidate for descoping — it's consuming resourcing that isn't traceable to the strategy, regardless of how locally reasonable it seems. This is the check that catches strategy/execution drift before it compounds across a planning cycle.

5. **Flag initiative overload per objective** — many initiatives mapped to one objective usually means either the objective is too broad or the initiatives are genuinely redundant; name which.

6. **Cross-check against `transformation`'s roadmap, if relevant and installed** — an Internal Process or Technology-flavored objective's initiative is often literally a transformation roadmap item; don't duplicate the initiative definition, reference it.

## Output format

```
OBJECTIVE: [text]
  Measure: [name] — Current: [value] → Target: [value]
  Initiative(s): [name(s)] or [NONE — flagged: no engine behind this target]

[repeat per objective]

REVERSE CHECK (if initiative portfolio provided):
  Unmapped initiatives (no strategic objective traced): [...]

INITIATIVE OVERLOAD FLAGS: [objectives with many initiatives — broad objective or
  redundant initiatives, specify which]
```
