---
name: forecast-competitive-response
description: >
  This skill should be used when the user asks "how will competitors
  react to this," "will this move invite retaliation," "war-game this
  decision," or has a planned strategic move that needs competitor
  response forecasted from their actual incentive structure, not generic
  assumption.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "market-intelligence practice"
  review_cadence: "quarterly"
  work_shape: "hypothesis-driven-analysis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Forecast Competitive Response

## When to use

CI analysts and strategy leads war-gaming a planned move — ground predictions in competitor incentive structures, not generic "they'll probably react."

## What this skill does not do

- **Does not build incentive maps from scratch** — route to `/market-intelligence:map-incentives` if structures are unknown.
- **Does not map the landscape** — use `/market-intelligence:map-competitive-landscape` for strategic groups.
- **Does not recommend whether to proceed** — surfaces retaliation scenarios; strategist decides.

## Preconditions

| Input | If missing |
|---|---|
| Planned move stated precisely | Ask once to narrow scope, scale, timing |
| Competitor set or strategic groups | Halt — route to `map-competitive-landscape` or ask user to name competitors |
| Incentive structures per competitor | Proceed with `[PROVISIONAL]` — flag predictions as low confidence; route to `map-incentives` |

## Provisional mode

Without incentive maps: label **CONFIDENCE: structured first pass**; tag every retaliation prediction `[review]`; do not present generic industry assumptions as grounded forecasts.

## Trust spine

- **Confidence bands** (`hypothesis-driven-analysis`):
  - **High:** Move precise, incentive maps available, visibility/threat classified per competitor with falsifiable retaliation hypotheses.
  - **Medium:** Some incentive gaps; predictions stated as hypotheses with explicit assumptions.
  - **Low:** No incentive data — scenario sketch only, not a forecast.
- **Failure modes:**
  - **Strategic advice vs. support:** "Plan survives predicted response" is a test result, not a go/no-go; strategist owns the decision.
  - **Client confidentiality:** Competitor intelligence may be sensitive — CONFIDENTIAL header per plugin `CLAUDE.md`.
  - **Accountability gap:** Each retaliation hypothesis tagged `[review]` where incentive grounding is thin.
  - **Analytical Rigor:** MECE competitor coverage; falsifiable retaliation levers named, not "they'll react."
  - **Incentive Gaming:** N/A — external competitor focus.
- **Escalation triggers:** Move threatens multiple core-position competitors simultaneously; plan only works in no-response case — flag explicitly.

## Workflow

1. **State the planned move precisely.**
2. **For each relevant competitor** (use `map-competitive-landscape` strategic groups if available), get or build incentive structure (`map-incentives`) and assess: does this move threaten something they'd defend hard?
3. **Classify visibility and threat level** per competitor: visible + threatens core = retaliation likely; quiet + low priority = unlikely; in-between cases reasoned explicitly.
4. **For every "retaliation likely" competitor, state the plausible response** — specific lever (price, copycat feature, channel, PR) grounded in incentive structure and capability.
5. **Stress-test the plan** against predicted response: does the move still make sense if retaliation happens? If only works in no-response case, say so directly.
6. **MECE/falsifiability check** before output: every named competitor covered; each retaliation hypothesis states what would falsify it.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
PLANNED MOVE: [precise statement]

[Competitor] — Strategic group: [...] — Threatens their priority: [yes/no, which priority]
  Visibility: [visible/quiet] — Retaliation likelihood: [likely/unlikely/uncertain]
  If likely: Predicted response: [specific lever, grounded in their incentive structure]

[repeat per competitor]

PLAN SURVIVES PREDICTED RESPONSE: [yes/no] — [if no, what changes]
```

## Worked example

**Input:** SaaS vendor plans 30% price cut on mid-market tier. Competitor A (same segment, volume-incented sales) and B (enterprise-focused, different group).

**Expected output (excerpt):**

```
CONFIDENCE: structured first pass
PLANNED MOVE: 30% price cut on mid-market tier, effective Q3

Competitor A — Strategic group: mid-market workflow — Threatens their priority: yes (core ARR segment)
  Visibility: visible — Retaliation likelihood: likely
  If likely: Predicted response: matching discount on comparable tier within 60 days [review]

Competitor B — Strategic group: enterprise suite — Threatens their priority: no
  Visibility: visible — Retaliation likelihood: unlikely

PLAN SURVIVES PREDICTED RESPONSE: uncertain — plan assumes net win rate gain; if A matches, margin impact may erase volume benefit [review]
```

## Quality checks before delivering

- [ ] Planned move stated with scope, scale, timing
- [ ] Every relevant competitor covered (MECE)
- [ ] Retaliation predictions grounded in incentive structure or flagged `[review]`
- [ ] Plan-survival test answered honestly
- [ ] Output does not read as concluded go/no-go

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: revise move, run `map-incentives` for thin competitors, or escalate to corp strategy.
