---
name: select-measures
description: >
  This skill should be used when the user asks to "select measures for
  these objectives," "what should we measure for this," or needs each
  strategy-map objective assigned 1-3 measures with an explicit lead/lag
  classification and a check on the overall measure portfolio.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Select Measures

The discipline most scorecards skip: classifying every measure as leading (predicts future performance, available in time to act) or lagging (confirms past performance, too late to change this period's outcome) — and then checking that the *mix* makes sense per perspective, not just that each objective has a number attached.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for the target total measure count (default ~20-25 across the whole scorecard) and whether `performance` is installed.

2. **For each strategy-map objective, propose 1-3 measures.** More than 3 per objective is almost always a sign the objective itself is too broad — flag rather than just listing every plausible metric.

3. **Classify every measure explicitly as leading or lagging.** A leading measure should give enough warning to act before the period closes; a lagging measure confirms the result after the fact. Be honest about borderline cases rather than calling everything "leading" because that sounds more proactive.

4. **Check the lead/lag mix per perspective against what the perspective's causal role implies**: the top perspective (Financial/Mission) is necessarily mostly lagging — you find out at period end whether the theory worked. Learning & Growth and Internal Process should be majority leading — if they're not, the org has no early warning system and won't know there's a problem until the lagging top-perspective numbers confirm it, too late to react. Flag any perspective whose mix doesn't fit its causal role.

5. **Check total measure count against the practice profile's ceiling.** A scorecard with 60 measures isn't more rigorous than one with 20 — it's diluted past the point where anyone can hold the whole picture in mind. If over the ceiling, identify the weakest candidates for removal (measures with no clear decision attached to them, or duplicating another measure's signal) rather than just flagging the overage.

6. **If `performance` is installed**, hand off the formal metric definition (exact formula, source, owner, refresh cadence) to `performance:metrics-glossary` — this skill only owns the objective-to-measure mapping and the lead/lag classification, same seam pattern as `okr:instrument-metrics`.

## Output format

```
OBJECTIVE: [text] — Perspective: [name]
  Measure: [name] — [Leading | Lagging] — [if performance installed: "defined in
    performance:metrics-glossary"; else: formula/source/owner/cadence inline]
  Measure: ... (max 3)

[repeat per objective]

LEAD/LAG MIX CHECK:
  [Perspective]: [N leading, N lagging] — [fits causal role / flag: needs more leading
    indicators, this perspective has no early warning]

TOTAL MEASURE COUNT: [N] vs. ceiling [N] — [within / over; if over, removal candidates: ...]
```
