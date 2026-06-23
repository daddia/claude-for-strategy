---
name: score-and-retro
description: >
  This skill should be used when the user asks to "score this cycle's
  OKRs," "run our OKR retro," "grade these key results," or needs
  end-of-cycle scoring plus a keep/kill/revise recommendation for each
  objective heading into the next cycle.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Score and Retro

The core failure mode this catches: grading the numbers and calling it done, without checking whether hitting the numbers actually served the objective. A KR scored 1.0 doesn't always mean the objective was achieved, and a KR scored 0.4 doesn't always mean it failed in any way that matters — those divergences are the most important output of a retro, not a footnote.

## Trust spine

```
INCENTIVE GAMING: Guards against grade inflation and sandbagging normalization —
  treating KR scores as sufficient without checking objective served, defaulting
  to keep-as-is, or ignoring cross-team patterns of trivial aspirational hits.
  Sandbagging detection: name when multiple teams score ~1.0 on aspirational KRs
  in the same direction; flag KR/objective divergences rather than averaging
  them away; keep-as-is is the least common recommendation, not the default.
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent an input — flag what's needed instead.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

Full rules: repo-root `references/trust-conventions.md`.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for the scoring formula and commit/aspirational handling.

2. **Score each KR** using the formula set in `set-targets`. State the score plainly.

3. **Roll up to objective level, but don't just average.** For each objective, ask explicitly: given how the KRs scored, was the objective actually achieved in spirit? Two specific divergences to look for and name if found:
   - **KRs scored well, objective wasn't really served** — the KRs turned out to be a weak proxy after all (a `write-key-results` miss surfacing late), or the result was achieved in a way that didn't matter (e.g. hit a growth number through a one-off channel that won't repeat).
   - **KRs missed numerically, objective was substantially advanced anyway** — sometimes the target was miscalibrated (`set-targets` overreach) rather than the work falling short; don't let a missed number erase real progress if that's what actually happened.

4. **For each objective, recommend keep / kill / revise / promote-to-commit** for next cycle, with the one-line reason. "Keep as-is" should be the least common recommendation, not the default — a cycle that changes nothing usually means the retro wasn't honest.

5. **If multiple teams' retros are being reviewed together**, look for cross-team patterns: a shared external cause behind several misses (worth naming once rather than re-litigating per team), or a sandbagging pattern across multiple teams' aspirational KRs in the same direction.

## Output format

```
OBJECTIVE: [text]

KR scores:
  [KR text]: [score] ([commit | aspirational])
  [KR text]: [score] (...)

OBJECTIVE-LEVEL CALL: [achieved / partially achieved / not achieved] — [one line, may
  diverge from a simple score average; explain if so]

NEXT CYCLE: [keep | kill | revise | promote-to-commit] — [why]

[repeat per objective]

CROSS-TEAM PATTERNS (if applicable): [shared causes, shared sandbagging, etc.]
```
