---
name: assess-growth-vectors
description: >
  This skill should be used when the user asks to "assess our growth
  options," "where should our growth come from," "build a growth strategy,"
  or has a portfolio of growth initiatives that need to be checked against
  a real growth target — not just sorted into categories.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
  owner: "corporate-strategy practice"
  review_cadence: "quarterly"
  work_shape: "hypothesis-driven-analysis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Assess Growth Vectors

## When to use

For strategy leads testing whether a portfolio of growth initiatives can realistically hit a stated target — arithmetic most growth plans skip.

## What this skill does not do

- **Does not run without a growth target** — halt and ask.
- **Does not take optimistic upside at face value** — applies category success-rate priors.
- **Does not approve mix shifts** — names options; strategist decides.
- **Does not invent initiative upside** — user-provided or `INPUT NEEDED`.

## Preconditions

| Input | If missing |
|---|---|
| Growth target (rate, horizon) | Halt — skill meaningless without target |
| Initiative list with stated upside | Ask; partial OK with gaps flagged |
| Practice profile | Read or `[PROVISIONAL]` |

## Provisional mode

No profile: state success-rate priors explicitly as `[PROVISIONAL — argue in room]`; all upside figures user-sourced.

## Trust spine

- **Analytical Rigor (mandatory):** Category classification honest; priors visible; gap arithmetic explicit.
- **Confidence bands** (`hypothesis-driven-analysis`): High = triangulated priors; Low = assumption-driven — label load-bearing assumptions.
- **Escalation:** Mislabeled adjacent (actually transformational) → push back; gap softened → forbidden.

## Workflow

1. Read practice profile for growth target and portfolio context.
2. Categorize each initiative: core / adjacent / transformational — classify honestly.
3. Apply stated success-rate prior per category (visible, arguable).
4. Realistic contribution = stated upside × prior; sum portfolio.
5. State growth gap: sum vs target in plain terms.
6. If gap: name options (more initiatives, lower target, mix shift, extend horizon).

## Output format

```
GROWTH TARGET: [rate] over [horizon]

INITIATIVES:
[Initiative] — [Core | Adjacent | Transformational] — Stated upside: [value] —
  Success-rate prior: [X%] — Realistic contribution: [value]

TOTAL REALISTIC CONTRIBUTION: [sum] vs TARGET: [value] — GAP: [amount | none]

IF GAP EXISTS — OPTIONS:
1. [...]
```

## Worked example

**Input:** Target +$100M over 3 years. Three initiatives: core +$40M (prior 80%), adjacent +$80M (prior 40%), transformational +$120M (prior 15%).

**Excerpt:** Realistic sum $32M+$32M+$18M=$82M; GAP $18M. Options include shift mix toward core or extend horizon `[review]`.

## Quality checks before delivering

- [ ] Target confirmed
- [ ] Priors stated per category
- [ ] Gap not softened
- [ ] Options named if gap exists
- [ ] No invented upside figures

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `allocate-resources` for bet funding, or add initiatives.
