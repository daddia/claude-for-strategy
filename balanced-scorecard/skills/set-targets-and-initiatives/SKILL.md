---
name: set-targets-and-initiatives
description: >
  This skill should be used when the user asks to "set targets for the
  scorecard," "what initiatives support this objective," or needs each
  measure given a target and each objective checked against whether a real
  program of work is actually driving it.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "balanced-scorecard practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Set Targets and Initiatives

## When to use

For strategy office or program leads completing the classic BSC four-column structure: Objective, Measure, Target, Initiative. The Initiative column is where most scorecards fail — this skill checks both directions (objective without initiative, initiative without objective).

## What this skill does not do

- **Does not select measures** — requires `select-measures` output.
- **Does not build or revise the strategy map** — reads objectives from `build-strategy-map`.
- **Does not invent baselines** — unknown current values → route to measurement first.
- **Does not duplicate transformation roadmaps** — references `transformation` items when installed.

## Preconditions

| Input | If missing |
|---|---|
| Measures per objective from `select-measures` | Halt — route to `select-measures` |
| Current values for targets (or explicit unknown) | Flag `BASELINE NEEDED`; do not guess |
| Practice profile scoring convention | Use profile or tag `[PROVISIONAL]` |

## Provisional mode

When current values unknown or initiative portfolio incomplete:

- Set targets only where baseline exists; others flagged `BASELINE NEEDED`.
- Flag objectives with targets but no initiative as **NONE — no engine behind this target**.
- Reverse check runs only when user provides initiative portfolio.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Every measure has current→target where baseline known; every objective has ≥1 named initiative or explicit NONE flag; reverse check complete if portfolio provided.
  - **Medium:** Some baselines missing; initiative names generic but flagged.
  - **Low:** Scaffold only — measures missing or majority targets invented without data.
- **Tag vocabulary:** `[verify]`, `[review]`, `BASELINE NEEDED`, `NONE — flagged`.
- **Failure modes:**
  - **Strategic advice vs. support:** Surfaces unmapped initiatives and overload flags; strategist decides descoping — does not cancel programs unilaterally.
  - **Client confidentiality:** Targets and initiative names may be sensitive — CONFIDENTIAL header when appropriate.
  - **Accountability gap:** NONE flags and reverse-check unmapped list prevent wishes-with-numbers passing as strategy.
  - **Analytical Rigor:** N/A — linkage completeness, not MECE analysis.
  - **Incentive Gaming:** N/A — no status scoring here.
- **Escalation triggers:**
  - Objective with target, no initiative → explicit NONE flag; do not silently omit Initiative column.
  - Initiative with no mapped objective → list in REVERSE CHECK for descoping consideration.
  - Many initiatives on one objective → INITIATIVE OVERLOAD flag; suggest split objective or merge initiatives.
  - Generic initiative text ("improve CX") → flag insufficient specificity.

## Workflow

1. **Read the practice profile** for scoring/status convention.

2. **Set current value and target for each measure** from `select-measures`. Unknown current → `BASELINE NEEDED`, route to measurement.

3. **For every objective, require at least one named strategic initiative** — specific enough to tell whether it's happening. Target but no initiative → flag **NONE — no engine behind this target**.

4. **Reverse check** (if initiative portfolio provided): every initiative maps to a strategic objective? Unmapped → list for descoping.

5. **Flag initiative overload** per objective — broad objective or redundant initiatives; name which.

6. **Cross-check `transformation` roadmap** if installed — reference existing roadmap items; don't duplicate definitions.

7. **Completeness check:** no invented baselines; every NONE and unmapped item explicit in output.

## Output format

```
OBJECTIVE: [text]
  Measure: [name] — Current: [value | BASELINE NEEDED] → Target: [value]
  Initiative(s): [name(s)] or [NONE — flagged: no engine behind this target]

[repeat per objective]

REVERSE CHECK (if initiative portfolio provided):
  Unmapped initiatives (no strategic objective traced): [...]

INITIATIVE OVERLOAD FLAGS: [objectives with many initiatives — broad objective or
  redundant initiatives, specify which]
```

## Worked example

**Input:** Customer objective "Improve onboarding NPS." Measure: Onboarding NPS, current unknown, target 50. User names initiative "Redesign onboarding flow (Q2)."

**Expected output (excerpt):**

```
OBJECTIVE: Improve onboarding NPS
  Measure: Onboarding NPS — Current: BASELINE NEEDED → Target: 50
  Initiative(s): Redesign onboarding flow (Q2)

INITIATIVE OVERLOAD FLAGS: none
```

**Input variant:** Same objective, target 50, no initiative named.

```
  Initiative(s): NONE — flagged: no engine behind this target
```

## Quality checks before delivering

- [ ] Every measure has current→target or BASELINE NEEDED
- [ ] Every objective has initiative(s) or explicit NONE flag
- [ ] Reverse check run when portfolio provided
- [ ] Overload flags applied
- [ ] Transformation references used instead of duplicate definitions
- [ ] No invented baseline values

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Natural next branches: measurement/baseline capture, `/balanced-scorecard:review-and-validate` at period end, or descoping unmapped initiatives.
