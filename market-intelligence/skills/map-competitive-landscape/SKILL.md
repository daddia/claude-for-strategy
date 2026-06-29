---
name: map-competitive-landscape
description: >
  This skill should be used when the user asks to "map the competitive
  landscape," "who are our real competitors," "find white space in this
  market," or needs competitors grouped by actual strategic logic rather
  than by surface product category.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "market-intelligence practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Map Competitive Landscape

## When to use

CI and product strategy practitioners grouping competitors by strategic logic — cost structure, segment, channel, model — not surface product labels.

## What this skill does not do

- **Does not forecast responses** — route to `/market-intelligence:forecast-competitive-response`.
- **Does not test positioning** — route to `/market-intelligence:test-positioning`.
- **Does not invent market share data** — tag figures `[verify]` or omit.

## Preconditions

| Input | If missing |
|---|---|
| Market definition (practice profile or user) | Ask; do not assume category from product name alone |
| Named competitors or candidate set | Ask user to name players; flag `[review]` if list may be incomplete |
| Practice profile | Proceed from user input; label assumptions |

## Provisional mode

Thin competitor list: output groups with explicit **UNDER-THE-RADAR THREAT: unknown — competitor set incomplete** flag; do not present white space as validated.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** MECE groups, mobility barriers rated with evidence, white space hypothesis stated with structural rationale.
  - **Medium:** Groups solid, some barrier ratings `[review]`, under-the-radar scan attempted.
  - **Low:** Incomplete competitor set or category-only grouping — scaffold only.
- **Failure modes:**
  - **Strategic advice vs. support:** Surfaces groups and threats; does not recommend which position to take.
  - **Client confidentiality:** Competitor intelligence sensitive — CONFIDENTIAL header per plugin `CLAUDE.md`.
  - **Accountability gap:** White space labeled attractive vs. structurally unattractive — strategist validates.
  - **Analytical Rigor:** Groups MECE by strategic logic; mobility barriers falsifiable.
  - **Incentive Gaming:** N/A for this shape.
- **Escalation triggers:** User insists on category-only grouping — explain failure mode, proceed only if acknowledged.

## Workflow

1. **Read the practice profile** — `~/.claude/plugins/config/claude-for-strategy/org-profile.md` and `~/.claude/plugins/config/claude-for-strategy/market-intelligence/CLAUDE.md` — for market definition and known competitor set.
2. **Group competitors into strategic groups** by cost structure, target segment, channel, business model — not product category labels.
3. **Identify mobility barriers between groups** — capital, channel, brand, regulatory; rate realistically (inertia ≠ high barrier).
4. **Identify white space** — ask: unoccupied because unseen or structurally unattractive? State which explanation is more likely.
5. **Flag under-the-radar competitor** — adjacent group player with low mobility barrier into your space.
6. **Completeness check** before output: every named competitor placed; market figures source-tagged.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
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

## Worked example

**Input:** Workflow automation market. User names Incumbent A (enterprise suite), Challenger B (mid-market SaaS), Adjacent C (RPA vendor expanding).

**Expected output (excerpt):**

```
CONFIDENCE: structured first pass
STRATEGIC GROUP: Enterprise integrated suite
  Members: Incumbent A

STRATEGIC GROUP: Mid-market point solution
  Members: Challenger B

MOBILITY BARRIERS:
Mid-market → Enterprise: high (implementation services, brand trust)

WHITE SPACE: Vertical-specific compliance workflows — Unoccupied because: structurally unattractive (small TAM per vertical) [verify]

UNDER-THE-RADAR THREAT: Adjacent C — RPA/automation group — low-barrier path via workflow module launch into mid-market [review]
```

## Quality checks before delivering

- [ ] Groups defined by strategic logic, not category labels only
- [ ] Every named competitor placed in a group
- [ ] White space includes structural attractiveness assessment
- [ ] Under-the-radar threat explicitly named or gap flagged
- [ ] Market figures source-tagged or omitted

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `forecast-competitive-response`, `test-positioning`, or `map-incentives` on key players.
