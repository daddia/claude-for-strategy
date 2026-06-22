---
name: exec-memo
description: >
  This skill should be used when the user asks to "write an exec memo,"
  "BLUF this," "turn this into a one-pager," or needs a narrative or raw
  notes condensed into a conclusion-first executive memo.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Exec Memo

Produce a BLUF-structured executive memo: bottom line first, then the MECE reasons, then the ask (if any), then supporting detail for readers who want to go deeper. Full convention in `../../references/bluf-conventions.md`.

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

Full rules: `../../references/trust-conventions.md`.

## Process

1. **Read the practice profile** (`~/.claude/plugins/config/claude-for-strategy/consulting/CLAUDE.md`) for default memo length and audience.

2. **Get or build the narrative.** If a `narrative-builder` output exists, the governing thought becomes the bottom line and the key line becomes the "why" section directly. If working from raw notes, do this compression inline rather than requiring a separate step first — a memo is allowed to be a lighter-weight pyramid than a full deck.

3. **Write the bottom line** — 1-2 sentences, the answer or recommendation, not the topic. This goes first, full stop, even before any framing sentence about context.

4. **Write the "why"** — 2-4 MECE points, each a sentence or short paragraph, not a wall of evidence. Apply the so-what test: cut anything that doesn't directly support the bottom line.

5. **Write the ask, if there is one** — what decision, resource, or sign-off is actually needed. Make it impossible to miss; don't bury it in a closing paragraph.

6. **Write supporting detail last** — background, methodology, caveats. This section is genuinely optional reading; nothing essential to the bottom line should live only here.

7. **Check length against the practice profile's default.** If it specifies one page, hold to it — cut detail, don't shrink the bottom line or the why.

## Output format

```
[BOTTOM LINE — 1-2 sentences]

WHY:
1. [point]
2. [point]
3. [point]

ASK: [what's needed, from whom, by when — omit if none]

DETAIL:
[background, methodology, caveats]
```
