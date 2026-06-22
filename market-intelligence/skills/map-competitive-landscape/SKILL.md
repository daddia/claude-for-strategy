---
name: map-competitive-landscape
description: >
  This skill should be used when the user asks to "map the competitive
  landscape," "who are our real competitors," "find white space in this
  market," or needs competitors grouped by actual strategic logic rather
  than by surface product category.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Map Competitive Landscape

The failure this catches: grouping competitors by what's visible and discussed internally (the loud incumbent already fighting you for the same deals) rather than by actual strategic logic — cost structure, target segment, channel, business model. The quiet player in an adjacent group, structurally capable of moving into your space, is the one usually missed.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for the market definition and known competitor set.

2. **Group competitors into strategic groups** by actual strategic logic — same cost structure, same target segment, same channel, same business model — not by product category labels. Two competitors selling the "same" product through fundamentally different cost structures or channels belong in different groups; they compete differently and will respond to moves differently.

3. **Identify mobility barriers between groups** — what would it actually take for a player in one group to move into another (capital, channel access, brand repositioning, regulatory)? Rate each barrier realistically: a "high" barrier that's actually just inertia is a false sense of safety.

4. **Identify white space** — a position no group currently occupies — and ask the harder question directly: is it unoccupied because nobody's spotted it, or because it's structurally unattractive or undefendable (low margin, easily copied, regulatory exposure)? Don't present white space as automatically attractive; state which explanation looks more likely and why.

5. **Flag the under-the-radar competitor explicitly** — scan the adjacent groups for any player with a low mobility barrier into your group, regardless of how much internal attention they currently get. This is usually the most useful single output of the exercise and the easiest thing to skip.

## Output format

```
STRATEGIC GROUP: [name — defined by cost structure/segment/channel/model]
  Members: [...]

[repeat per group]

MOBILITY BARRIERS:
[Group A] → [Group B]: [barrier, realistic rating: high/medium/low]

WHITE SPACE: [position] — Unoccupied because: [nobody's spotted it / structurally
  unattractive — explain which]

UNDER-THE-RADAR THREAT: [player, group, low-barrier path into your space, even if not
  currently visible as a competitor]
```
