---
name: write-key-results
description: >
  This skill should be used when the user asks to "write key results for
  this objective," "are these good KRs," "turn this into KRs," or provides
  candidate key results that need to be checked for whether they measure an
  outcome or just confirm a deliverable shipped.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "okr practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Write Key Results

## When to use

When KRs need the outcome test — measurable change in an indicator, not confirmation a deliverable shipped.

## What this skill does not do

- **Does not draft objectives** — route to `/okr:draft-objectives`.
- **Does not set targets** — route to `/okr:set-targets` after baselines known.
- **Does not instrument metrics** — route unknown baselines to `/okr:instrument-metrics`.

## Preconditions

| Input | If missing |
|---|---|
| Objective the KR set serves | Ask — every check depends on it |
| Candidate KRs (or request to draft) | Ask user to provide or draft from objective |

## Provisional mode

Without baseline data: flag **Baseline status: unknown** per KR; do not imply targets are ready.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Outcome-shaped KRs, vanity risks named, set collectively sufficient.
  - **Medium:** Some output-shaped flags with reframes.
  - **Low:** Majority deliverable-shaped — set not ready for targets.
- **Failure modes:**
  - **Strategic advice vs. support:** Verdicts diagnostic; strategist owns final KRs.
  - **Client confidentiality:** KRs may be pre-release — CONFIDENTIAL header.
  - **Accountability gap:** Deliverables relocated to tasks, not silently kept as KRs.
  - **Analytical Rigor:** Set-level sufficiency check — hitting all KRs proves objective?
  - **Incentive Gaming:** Vanity-metric and sandbagging-by-proxy checks — easy-to-hit numbers that don't prove objective.
- **Escalation triggers:** Set insufficient even if every KR passes individually — name gap.

## Workflow

1. **Get the objective** — explicit, not implied.
2. **Outcome test** per KR — deliverable language ("ship," "launch") → reframe to outcome.
3. **Vanity-metric check** — would unrelated improvement fool readers?
4. **Baseline check** — unknown → flag for `instrument-metrics`.
5. **Set sufficiency** — would hitting all KRs prove the objective?
6. **Completeness check** before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
LOAD-BEARING ASSUMPTIONS: [if any]
OBJECTIVE: [text]

KR 1: [text]
  Verdict: [PASS | FLAG — output-shaped | FLAG — vanity metric risk]
  Baseline status: [known | unknown — flag for instrument-metrics]

[repeat per KR]

SET-LEVEL CHECK: [would hitting all KRs prove the objective? any gap?]
```

## Worked example

**Input:** Objective "Improve enterprise retention." KR "Ship onboarding v2."

**Expected output (excerpt):**

```
KR 1: Ship onboarding v2
  Verdict: FLAG — output-shaped; suggested outcome: 90-day logo retention ≥ 92%
  Baseline status: unknown — flag for instrument-metrics

SET-LEVEL CHECK: insufficient — single output KR doesn't prove retention objective
```

## Quality checks before delivering

- [ ] Objective explicit at top
- [ ] Outcome test on every KR
- [ ] Vanity-metric check run
- [ ] Baseline status per KR
- [ ] Set-level sufficiency assessed
- [ ] Figures source-tagged or omitted

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `instrument-metrics`, `set-targets`, or revise flagged KRs.
