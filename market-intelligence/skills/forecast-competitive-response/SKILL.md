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
  version: "0.1.0"
---

# Forecast Competitive Response

The discipline: ground the prediction in the competitor's actual incentive structure (from `map-incentives`), not a generic "they'll probably react." And apply a simple but often-skipped game-theoretic filter: a move that's quiet and outside a competitor's priority area is unlikely to draw a response regardless of how good it looks on paper; a move that's visible and threatens a competitor's core position almost always draws one, and the plan needs to survive that, not just the no-response case.

## Process

1. **State the planned move precisely.**

2. **For each relevant competitor** (use `map-competitive-landscape`'s strategic groups if available), get or build their incentive structure (`map-incentives`) and assess: does this move threaten something this competitor's incentive structure makes them likely to defend hard (their core revenue, their highest-margin segment, their CEO's stated priority), or does it land somewhere they're structurally unlikely to prioritize a response to?

3. **Classify visibility and threat level** for each competitor: visible + threatens core = retaliation likely; quiet + threatens nothing they prioritize = retaliation unlikely; the in-between cases (visible but low threat, or quiet but high threat if discovered) get reasoned through explicitly rather than defaulted into one bucket.

4. **For every "retaliation likely" competitor, state the plausible response** — not just "they'll react," but the specific lever they'd actually pull given their incentive structure and capability (price, a copycat feature, a channel move, an aggressive PR response).

5. **Stress-test the plan against the predicted response**: does the move still make sense if the most likely retaliation happens? If the plan only works in the no-response case, say so directly — that's the same discipline as `corporate-strategy:evaluate-strategic-option`'s downside sizing, applied to competitive dynamics specifically.

## Output format

```
PLANNED MOVE: [precise statement]

[Competitor] — Strategic group: [...] — Threatens their priority: [yes/no, which priority]
  Visibility: [visible/quiet] — Retaliation likelihood: [likely/unlikely/uncertain]
  If likely: Predicted response: [specific lever, grounded in their incentive structure]

[repeat per competitor]

PLAN SURVIVES PREDICTED RESPONSE: [yes/no] — [if no, what changes]
```
