---
name: so-what-sharpener
description: >
  This skill should be used when the user asks "what's the so-what here,"
  "sharpen this insight," "this is just facts, what does it mean," or
  provides a list of observations or data points that need to be turned into
  insight statements.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# So-What Sharpener

Turn raw observations into sharpened insight statements by forcing the observation → implication → insight chain explicitly, one point at a time. This is the smallest unit of the Minto discipline (see `../../references/minto-pyramid.md`) — useful standalone when the user has a pile of facts and needs to know what they actually mean before building a full narrative around them.

## Process

For each observation or data point provided:

1. **State the observation as given** — the raw fact, unchanged.
2. **State the implication** — what does this fact suggest, on its own? This is still fairly literal (e.g. "revenue per user dropped 12% in the mid-tier" → "mid-tier users are spending less").
3. **State the insight** — what does this mean for the decision at hand? This is the so-what that actually matters to the reader (e.g. "the mid-tier price increase priced out exactly the segment it was meant to monetize better — the pricing change should be reconsidered, not just monitored").

Run this chain explicitly for every point — don't skip straight from observation to insight, since the implication step is usually where the laziest version of the insight gets caught and corrected.

4. **Flag observations that don't earn an insight.** Some facts are just facts — true, but not load-bearing for any decision. Say so rather than manufacturing a forced insight to make every point look productive.

5. **Group sharpened insights** if there are several, checking for overlap or redundancy — two insights that are really the same point stated twice should be merged.

## Output format

```
Observation: [raw fact]
  → Implication: [what it suggests]
  → Insight: [what it means for the decision]

Observation: [raw fact]
  → Implication: ...
  → Insight: ...

No insight earned: [observations that are true but not decision-relevant, with why]
```
