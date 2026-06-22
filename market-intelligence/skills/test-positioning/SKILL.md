---
name: test-positioning
description: >
  This skill should be used when the user asks to "test our positioning,"
  "are we differentiated," "is this a real strategy or just a slogan," or
  has a positioning statement that needs the trade-off discipline applied —
  what are you choosing not to do.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Test Positioning

A real position requires choosing not to do something. A positioning statement with no stated trade-off is usually marketing language, not strategy — this skill forces the trade-off out into the open and checks for the specific failure of trying to be everything at once.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for current positioning.

2. **State the positioning as claimed**, plainly.

3. **Demand the trade-off.** Ask directly: what customer segment, use case, or feature set are you deliberately walking away from to hold this position? If none can be named, say so explicitly — this is evidence the positioning isn't yet a real strategic choice, just an aspiration, and the skill should stop short of validating it as one.

4. **Check for "stuck in the middle"** — claiming both cost leadership and meaningful differentiation simultaneously, without a credible structural mechanism for achieving both (most attempts to be "the best of both" end up neither cheap enough nor differentiated enough to win on either axis). If this pattern shows up, name it directly rather than softening it into "broad appeal."

5. **Stress-test who this alienates.** A real position alienates someone — ask who, specifically, and whether that's an acceptable, deliberate cost the org has actually agreed to, or an unexamined side-effect nobody's confronted. If it's the latter, that's the more useful finding than the positioning statement itself.

6. **Check coherence against `map-incentives` output, if available** — does the org's actual internal incentive structure support this position, or does it (per the sales-volume-vs-premium-positioning example) quietly undermine it day to day?

## Output format

```
POSITIONING AS CLAIMED: [statement]

TRADE-OFF: [named explicitly] or [NONE FOUND — flag: not yet a real strategic choice]

STUCK-IN-THE-MIDDLE CHECK: [pass] or [flag — claiming cost leadership and differentiation
  with no credible mechanism for both]

WHO THIS ALIENATES: [segment/use case] — Deliberate and accepted? [yes/no — if no, flag
  as the more important finding]

INCENTIVE COHERENCE (if map-incentives available): [supports / undermines the stated position]
```
