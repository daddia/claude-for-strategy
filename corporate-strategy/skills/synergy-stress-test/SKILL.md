---
name: synergy-stress-test
description: >
  This skill should be used when the user asks to "stress-test these
  synergies," "is this deal's synergy case realistic," or has a deal or
  partnership's projected synergies that need cost/revenue separation,
  evidence checks, and a base-rate haircut.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Synergy Stress Test

The base-rate problem this skill exists to apply: cost synergies are reasonably reliable to project and capture; revenue synergies are notoriously overestimated and underdelivered, almost across the board, because they depend on customer and market behavior the acquirer doesn't control. Most synergy cases blend the two into one number, which lets an unreliable revenue estimate borrow credibility from a reliable cost estimate. This skill won't let that happen.

## Process

1. **Separate every claimed synergy into cost or revenue.** No blended line items — if a claimed synergy is genuinely mixed, split it into its cost and revenue components.

2. **For each cost synergy, check the evidence**: is this a specific, named action (consolidating a named facility, eliminating a named duplicate function) with an identified owner, or a generic percentage applied to a cost base ("10% G&A savings")? Generic percentage-of-base claims get flagged as weaker evidence even within the cost category.

3. **For each revenue synergy, check the evidence even harder**: what specifically drives this (cross-sell to a named customer base, pricing power from reduced competition, channel access)? Demand a mechanism, not an assertion — "we expect cross-sell uplift" with no stated mechanism is the weakest possible form of this claim.

4. **Apply a haircut by category**, stated explicitly rather than silently: cost synergies with strong evidence get a light haircut; cost synergies with weak evidence and all revenue synergies get a heavier one, reflecting the base-rate pattern that revenue synergies are achieved at a much lower rate than projected industry-wide.

5. **Check for double-counting** — the same saving or revenue gain claimed under two different line items (a common way synergy cases inflate without anyone intending to mislead).

6. **Recompute the deal economics with the haircut applied**, and state plainly whether the case still clears the bar at the haircut-adjusted number — if it only works at the optimistic number, say so directly.

## Output format

```
COST SYNERGIES:
[Item] — Evidence: [specific/named or generic] — Haircut: [%] — Adjusted value: [...]

REVENUE SYNERGIES:
[Item] — Mechanism stated: [yes/no — if no, flag as weakest form] — Haircut: [%] — Adjusted value: [...]

DOUBLE-COUNTING FLAGS: [any]

TOTAL SYNERGY VALUE: As-claimed: [value] → Haircut-adjusted: [value]
DOES THE CASE STILL CLEAR AT THE ADJUSTED NUMBER: [yes/no]
```
