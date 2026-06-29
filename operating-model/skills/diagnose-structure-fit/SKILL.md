---
name: diagnose-structure-fit
description: >
  This skill should be used when the user asks "is our structure right for
  our strategy," "should we reorganize," "why does coordination feel so
  slow," or needs the current or proposed structure tested against the
  actual coordination need the strategy requires.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "operating-model practice"
  review_cadence: "quarterly"
  work_shape: "hypothesis-driven-analysis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Diagnose Structure Fit

## When to use

Test current/proposed structure against coordination needs the strategy requires — no universally "best" org chart.

## What this skill does not do

- **Does not align rewards** — route to `/operating-model:align-rewards-and-incentives`.
- **Does not design RACI** — route to `/operating-model:design-decision-rights`.
- **Does not recommend full redesign by default** — targeted fixes only.

## Preconditions

| Input | If missing |
|---|---|
| Strategic priority / coordination need | Ask what structure should optimize for |
| Current or proposed structure by area | Ask user to describe or provide org chart |
| Practice profile | Proceed with labeled assumptions |

## Provisional mode

Without area breakdown: assess at highest level available; flag `[review]` on incomplete area coverage.

## Trust spine

- **Confidence bands** (`hypothesis-driven-analysis`):
  - **High:** Coordination needs stated per area; fit/mismatch specific; blank-page test complete.
  - **Medium:** Some areas inferred; mismatches flagged with hypotheses.
  - **Low:** Strategy priority unstated — halt.
- **Failure modes:**
  - **Strategic advice vs. support:** Recommendations are options; leadership owns reorg decision.
  - **Client confidentiality:** Structure politics sensitive — CONFIDENTIAL header.
  - **Accountability gap:** Blank-page test names political drivers when present `[review]`.
  - **Analytical Rigor:** MECE area coverage; mismatches falsifiable.
  - **Incentive Gaming:** N/A — structure focus.
- **Escalation triggers:** Structure driven by personalities not work — name directly.

## Workflow

1. **Read practice profile** for structure optimization goal.
2. **State coordination need precisely** by area — cross-functional speed, expertise depth, local responsiveness, central control.
3. **Test structure against need per area** — name specific mismatches.
4. **Run blank-page test** — designed fresh around work, or legacy of titles/politics?
5. **Recommend targeted changes** where fit breaks down.
6. **MECE check** before output: areas in scope covered.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
STRATEGIC PRIORITY: [what the structure should optimize for]

AREA: [function/business line] — Coordination need: [...]
  Current structure: [...] — Fit: [match / mismatch — specifics]

[repeat per area]

BLANK-PAGE TEST: [yes/no — if no, what's driving current shape]

RECOMMENDED CHANGES: [targeted, by area]
```

## Worked example

**Input:** Strategy needs fast cross-functional product decisions; strict functional hierarchy with no integrator.

**Expected output (excerpt):**

```
AREA: Product delivery — Coordination need: fast cross-functional decisions
  Current structure: strict functional silos — Fit: mismatch — no integrating mechanism [review]
BLANK-PAGE TEST: no — structure mirrors current VP titles [review]
RECOMMENDED CHANGES: Add product integrator role or cross-functional squad layer for delivery area only
```

## Quality checks before delivering

- [ ] Coordination need stated per area
- [ ] Mismatches specific, not vague
- [ ] Blank-page test completed
- [ ] Changes targeted, not blanket redesign
- [ ] MECE area coverage

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `align-rewards-and-incentives`, `design-decision-rights`, or exec workshop.
