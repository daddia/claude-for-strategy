---
name: map-incentives
description: >
  This skill should be used when the user asks to "map the incentives
  here," "why is this player behaving this way," "predict how X will
  react," or has a strategic situation where a player's actual incentive
  structure — not their stated motivation — needs to be reasoned through.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Map Incentives

"Show me the incentive and I'll show you the outcome." This skill applies that discipline literally: for any player relevant to a strategic situation, map what they're actually rewarded or penalized for — not what they say motivates them — and predict behavior from that, then check whether the prediction matches what stated motivation alone would have implied.

## Process

1. **Name every player relevant to the situation** — internal stakeholders, competitors, customer segments, channel partners, regulators, whoever's behavior actually matters to the outcome.

2. **For each player, state the actual incentive structure**, as specifically as possible: how are they measured, paid, evaluated, or otherwise rewarded/penalized — by whom, on what timeframe. "Wants the deal to succeed" is a stated motivation; "is paid a bonus tied to this quarter's volume, not retention" is an incentive structure. Insist on the second kind.

3. **Predict behavior from the incentive structure alone**, independent of any stated motivation or stated strategy. State this prediction explicitly before checking it against anything else.

4. **Compare to the stated motivation or stated strategy.** If they match, the situation is straightforward. If they diverge — flag this as the more important and more reliable signal. A sales team incented purely on volume will discount aggressively regardless of a company-wide stated commitment to premium positioning; the incentive wins, almost always, and predicting otherwise because of the stated strategy is the actual mistake to avoid.

5. **Flag misaligned incentives as a named problem**, not just an observation — if an internal player's incentive structure works against the stated strategic direction, that's a fixable problem (see `operating-model:align-rewards-and-incentives` if the fix is structural) rather than just a fact to note and move past.

## Output format

```
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
