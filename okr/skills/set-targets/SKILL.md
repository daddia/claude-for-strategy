---
name: set-targets
description: >
  This skill should be used when the user asks to "set targets for these
  KRs," "what should our target be," "calibrate this OKR," or has key
  results that need a baseline, target, commit/aspirational label, and
  scoring formula attached.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "okr practice"
  review_cadence: "quarterly"
  work_shape: "governance-tracking"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Set Targets

## When to use

Attach baseline, target, commit/aspirational label, and scoring formula — same number means opposite things without commitment level.

## What this skill does not do

- **Does not instrument metrics** — route unknown baselines to `/okr:instrument-metrics` first.
- **Does not write KRs** — route to `/okr:write-key-results`.
- **Does not score the cycle** — route to `/okr:score-and-retro`.

## Preconditions

| Input | If missing |
|---|---|
| KRs with known baselines | Halt — route to `instrument-metrics` |
| Practice profile (philosophy, formula) | Default linear interpolation; tag `[PROVISIONAL]` |
| Explicit commit/aspirational label per KR | Ask — do not infer from number |

## Provisional mode

Without seed history: set-level sandbagging check limited to trivial-target flags on current set.

## Trust spine

- **Confidence bands** (`governance-tracking`):
  - **High:** Every KR has type, baseline, target, formula, calibration flag.
  - **Medium:** Some calibration flags on commit/aspirational mismatch.
  - **Low:** Baselines unknown — halt, route to instrument-metrics.
- **Failure modes:**
  - **Strategic advice vs. support:** Targets are draft for calibration approval.
  - **Client confidentiality:** Targets may be pre-approval — CONFIDENTIAL header.
  - **Accountability gap:** Sandbagging patterns named, not praised.
  - **Analytical Rigor:** N/A — governance shape.
  - **Incentive Gaming:** Guards sandbagging — trivial aspirational targets and commit labels on stretch goals flagged.
- **Escalation triggers:** Consistent ~1.0 history in seed data — name sandbagging pattern for calibration.

## Workflow

1. **Read practice profile** for philosophy and scoring formula.
2. **Get explicit commit/aspirational label** per KR — don't infer.
3. **Set baseline and target** — halt if baseline unknown.
4. **State scoring formula** alongside each KR.
5. **Calibration check:** commits realistic? aspirational genuinely stretch? history of ~1.0?
6. **Gaming-pattern check** before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
LOAD-BEARING ASSUMPTIONS: [if any]

KR: [text]
  Type: [commit | aspirational]
  Baseline: [value] → Target: [value]
  Scoring formula: [from profile]
  Calibration flag: [none | trivial aspirational | unrealistic commit | baseline unknown]

[repeat per KR]

SET-LEVEL PATTERN CHECK: [sandbagging or overreach history if seed data exists]
```

## Worked example

**Input:** Aspirational KR "NPS 50." Baseline 38. Target 40 (2pt lift).

**Expected output (excerpt):**

```
KR: NPS 50
  Type: aspirational
  Baseline: 38 → Target: 40
  Scoring formula: linear interpolation
  Calibration flag: target looks trivial for an aspirational KR [review]
```

## Quality checks before delivering

- [ ] Commit/aspirational explicit per KR
- [ ] Baselines known or routed to instrument-metrics
- [ ] Formula stated per KR
- [ ] Calibration flags applied
- [ ] Sandbagging pattern named if history supports it
- [ ] Gaming-pattern check run

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: calibration approval, `check-in` cadence, or revise targets.
