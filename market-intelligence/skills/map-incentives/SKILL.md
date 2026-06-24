---
name: map-incentives
description: >
  This skill should be used when the user asks to "map the incentives
  here," "why is this player behaving this way," "predict how X will
  react," or has a strategic situation where a player's actual incentive
  structure — not their stated motivation — needs to be reasoned through.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "market-intelligence practice"
  review_cadence: "quarterly"
  work_shape: "hypothesis-driven-analysis"
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Map Incentives

## When to use

When behavior must be predicted from actual reward/penalty structures — internal stakeholders, competitors, channels, regulators — not stated motivations.

## What this skill does not do

- **Does not fix misaligned incentives** — route structural fixes to `/operating-model:align-rewards-and-incentives`.
- **Does not forecast competitive retaliation** — route to `/market-intelligence:forecast-competitive-response` once maps exist.
- **Does not accept vague motivations** — insists on measurable incentive structures.

## Preconditions

| Input | If missing |
|---|---|
| Situation and relevant players named | Ask once to scope |
| Incentive data (comp plan, KPIs, evaluation criteria) | Proceed with `[PROVISIONAL]` — flag predictions `[review]`; ask user for specifics |

## Provisional mode

Without comp/KPI detail: state predictions as hypotheses from partial data; tag every player **Actual incentive structure: incomplete — [review]**.

## Trust spine

- **Confidence bands** (`hypothesis-driven-analysis`):
  - **High:** Specific incentive structures cited; behavior predictions falsifiable; divergence analysis complete.
  - **Medium:** Some structures inferred; divergences flagged openly.
  - **Low:** Stated-motivation-only input — refuse to validate as incentive map.
- **Failure modes:**
  - **Strategic advice vs. support:** Predictions are hypotheses for strategist validation, not behavioral verdicts.
  - **Client confidentiality:** Comp structures may be sensitive — CONFIDENTIAL header.
  - **Accountability gap:** Divergence flags force engagement with misalignment, not silent acceptance.
  - **Analytical Rigor:** MECE player coverage; incentive-before-stated-motivation discipline enforced.
  - **Incentive Gaming:** Names when players may game stated metrics — flag pattern explicitly.
- **Escalation triggers:** Internal misalignment threatens stated strategy — name as fixable problem, route to operating-model.

## Workflow

1. **Name every player** relevant to the situation.
2. **For each player, state actual incentive structure** — measured, paid, evaluated, by whom, what timeframe. Reject "wants success" as substitute.
3. **Predict behavior from incentive structure alone** — before checking stated motivation.
4. **Compare to stated motivation.** Divergence = incentive prediction trusted.
5. **Flag misaligned incentives** as named fixable problems.
6. **MECE check** before output: all relevant players covered.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
PLAYER: [name/role]
  Stated motivation: [what they'd say drives them]
  Actual incentive structure: [how they're measured/paid/evaluated, by whom, what timeframe]
  Predicted behavior FROM INCENTIVE: [...]
  Predicted behavior FROM STATED MOTIVATION: [...]
  Divergence: [none] or [significant — incentive prediction should be trusted over stated motivation]

[repeat per player]

MISALIGNED INCENTIVE FLAGS: [any internal player whose incentive works against the
  stated strategy — name it as a fixable problem]
```

## Worked example

**Input:** Premium positioning push; enterprise sales team paid on quarterly new-logo ARR only.

**Expected output (excerpt):**

```
CONFIDENCE: defensible recommendation
PLAYER: Enterprise AE team
  Stated motivation: Win strategic accounts aligned with premium brand
  Actual incentive structure: 100% variable on quarterly new-logo ARR; no retention component
  Predicted behavior FROM INCENTIVE: Discount to close before quarter-end; prioritize volume over margin
  Predicted behavior FROM STATED MOTIVATION: Hold price, walk from bad-fit deals
  Divergence: significant — incentive prediction should be trusted

MISALIGNED INCENTIVE FLAGS: Sales comp undermines premium positioning — fixable via operating-model align-rewards-and-incentives [review]
```

## Quality checks before delivering

- [ ] Every relevant player covered
- [ ] Incentive structures specific (not stated motivation disguised)
- [ ] Prediction-from-incentive stated before comparison
- [ ] Misalignments named as fixable problems
- [ ] Output does not read as concluded org redesign

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `forecast-competitive-response`, `test-positioning`, or `operating-model:align-rewards-and-incentives`.
