---
name: test-positioning
description: >
  This skill should be used when the user asks to "test our positioning,"
  "are we differentiated," "is this a real strategy or just a slogan," or
  has a positioning statement that needs the trade-off discipline applied —
  what are you choosing not to do.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "market-intelligence practice"
  review_cadence: "quarterly"
  work_shape: "option-evaluation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Test Positioning

## When to use

When a positioning claim needs trade-off discipline — what you're choosing not to do — before treating it as strategy.

## What this skill does not do

- **Does not write positioning from scratch** — tests an existing claim; cold-start captures baseline.
- **Does not map competitors** — route to `/market-intelligence:map-competitive-landscape`.
- **Does not validate marketing slogans without trade-offs** — flags aspiration vs. strategic choice.

## Preconditions

| Input | If missing |
|---|---|
| Positioning statement (profile or user) | Ask user to state claim |
| Practice profile | Proceed from user input |
| `map-incentives` output (optional) | Skip incentive coherence check; note gap |

## Provisional mode

No trade-off named by user: output **TRADE-OFF: NONE FOUND** and stop short of validating as real strategic choice.

## Trust spine

- **Confidence bands** (`option-evaluation`):
  - **High:** Trade-off explicit, stuck-in-the-middle check passed, alienation assessed, incentive coherence checked.
  - **Medium:** Trade-off named but alienation acceptance unclear — `[review]`.
  - **Low:** No trade-off — positioning flagged as aspiration only.
- **Failure modes:**
  - **Strategic advice vs. support:** Surfaces trade-offs and failures; does not declare positioning "good" or "bad."
  - **Client confidentiality:** Positioning may be pre-release — CONFIDENTIAL header.
  - **Accountability gap:** "Who this alienates" forces deliberate acceptance question.
  - **Analytical Rigor:** Stuck-in-the-middle pattern named directly when present.
  - **Incentive Gaming:** Checks whether internal incentives undermine stated position.
- **Escalation triggers:** Stuck-in-the-middle with no structural mechanism — flag as blocking for strategy credibility.

## Workflow

1. **Read the practice profile** for current positioning.
2. **State the positioning as claimed**, plainly.
3. **Demand the trade-off** — segment, use case, or feature set walked away from. If none: flag explicitly.
4. **Check stuck-in-the-middle** — cost leadership + differentiation without credible mechanism.
5. **Stress-test who this alienates** — deliberate and accepted, or unexamined side-effect?
6. **Check incentive coherence** against `map-incentives` if available.
7. **Validate** before output: trade-off discipline applied; no false validation of slogans.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
POSITIONING AS CLAIMED: [statement]

TRADE-OFF: [named explicitly] or [NONE FOUND — flag: not yet a real strategic choice]

STUCK-IN-THE-MIDDLE CHECK: [pass] or [flag — claiming cost leadership and differentiation
  with no credible mechanism for both]

WHO THIS ALIENATES: [segment/use case] — Deliberate and accepted? [yes/no — if no, flag
  as the more important finding]

INCENTIVE COHERENCE (if map-incentives available): [supports / undermines the stated position]
```

## Worked example

**Input:** "Best workflow automation for everyone — enterprise power at mid-market price."

**Expected output (excerpt):**

```
CONFIDENCE: structured first pass
POSITIONING AS CLAIMED: Best workflow automation for everyone — enterprise power at mid-market price

TRADE-OFF: NONE FOUND — flag: not yet a real strategic choice

STUCK-IN-THE-MIDDLE CHECK: flag — claiming cost leadership and differentiation with no credible mechanism for both [review]

WHO THIS ALIENATES: none stated — Deliberate and accepted? no — unexamined; real position must alienate someone [review]

INCENTIVE COHERENCE: not assessed — run map-incentives
```

## Quality checks before delivering

- [ ] Trade-off demanded and recorded or NONE FOUND flagged
- [ ] Stuck-in-the-middle check run
- [ ] Alienation assessed with deliberate-acceptance question
- [ ] Incentive coherence checked if data available
- [ ] Output does not validate positioning without trade-off

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: refine positioning, run `map-incentives`, or `map-competitive-landscape`.
