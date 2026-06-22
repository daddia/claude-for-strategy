---
name: tech-strategy-brief
description: >
  This skill should be used when the user asks to "write a decision brief for
  this platform choice," "brief this architecture decision," or needs a
  technology strategy decision (platform, vendor, build-vs-buy, architecture
  pattern) framed as options with a recommendation.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Tech Strategy Brief

Produce a BLUF-structured decision brief for a technology strategy call — options, recommendation, risks, stated conclusion-first. Apply the BLUF convention: bottom line first, then the MECE reasons, then the ask, then supporting detail.

## Trust spine

```
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent an input — flag what's needed instead.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

## Process

1. **Read the practice profile** (`~/.claude/plugins/config/claude-for-strategy/transformation/CLAUDE.md`) for platform vocabulary and risk posture.

2. **State the decision being made**, precisely — not "should we improve our architecture" but the actual specific choice (e.g. "should Identity be a shared platform service or remain per-product").

3. **Lay out the options** — including the implicit "do nothing / stay as-is" option, which is often skipped but is always one of the real choices.

4. **For each option, give**: what it requires, what it costs (not just dollars — also time, org disruption, lock-in), and the main risk.

5. **State the recommendation first**, before the options detail — this is a BLUF document, the reader should know the answer in the first two sentences.

6. **Give the reasoning as 2-4 MECE points**, not a narrative walk-through of the analysis process.

7. **State the ask explicitly** — sign-off, budget, a specific decision needed by a specific date.

8. **Flag what would change the recommendation** — what new information or changed constraint would flip the call. This is a hypothesis-driven habit worth carrying into decision briefs: state the conditions under which you'd be wrong.

## Output format

```
RECOMMENDATION: [one to two sentences — the answer, stated first]

WHY:
1. [point]
2. [point]
3. [point]

ASK: [decision/budget/sign-off needed, by when]

OPTIONS CONSIDERED:
| Option | Requires | Cost (time/$/disruption) | Main risk |
|---|---|---|---|
| [Recommended option] | ... | ... | ... |
| [Alternative] | ... | ... | ... |
| Do nothing | ... | ... | ... |

WHAT WOULD CHANGE THIS CALL: [conditions that would flip the recommendation]
```
