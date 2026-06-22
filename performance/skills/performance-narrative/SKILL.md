---
name: performance-narrative
description: >
  This skill should be used when the user asks to "turn these numbers into a
  narrative," "write up our performance for the board," or provides metrics
  or tracker results that need to become a readable, BLUF-structured
  narrative rather than a table of numbers.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Performance Narrative

Turn metrics/results into a BLUF-structured narrative for the audience recorded in the practice profile. Apply the BLUF convention: bottom line first, then why, then what's needed, then detail.

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

1. **Read the practice profile** (`~/.claude/plugins/config/claude-for-strategy/performance/CLAUDE.md`) for audience and reporting cadence.

2. **Identify the headline** before writing anything else — across all the metrics provided, what's the one thing the audience most needs to know this period? Not every metric that moved; the one that matters most given the audience and what they'd act on.

3. **Write the bottom line first** — the headline finding, one to two sentences, stated as a conclusion ("Conversion is down 8% this month, driven almost entirely by the mid-tier price change") not a topic ("Here's our conversion performance this month").

4. **Group supporting metrics into 2-4 MECE points** that explain the headline — not a metric-by-metric walkthrough of everything that moved. Apply the so-what test: a metric that moved but doesn't change the picture for the audience belongs in an appendix, not the main narrative.

5. **State what's needed, if anything** — a decision, an investment, awareness only. Make this explicit rather than letting the reader infer it.

6. **Put the full metric detail last**, as supporting reference — this is where every number that moved gets its due, for the reader who wants it, without competing with the headline for attention.

## Output format

```
HEADLINE: [bottom line — the one thing that matters most this period]

WHY:
1. [supporting point]
2. [supporting point]

WHAT'S NEEDED: [decision/investment/awareness-only — be explicit]

FULL DETAIL:
[metric-by-metric breakdown, all movements, for reference]
```
