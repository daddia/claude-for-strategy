---
name: review-and-validate
description: >
  This skill should be used when the user asks to "review the scorecard,"
  "how are we tracking against the strategy map," "run our quarterly BSC
  review," or needs measures scored against targets AND the strategy map's
  causal links tested against what actually happened — the distinctively
  BSC discipline that separates a failed initiative from a failed theory.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Review and Validate

Scoring the measures and calling it a review misses the actual point of a balanced scorecard. The distinctive move — the one OKR retros have no real equivalent for — is testing whether the causal links from `build-strategy-map` held up in the data. When a leading measure improved but the downstream lagging measure didn't follow as the map predicted, that's evidence the *strategy's theory* may be wrong, not necessarily evidence anyone executed poorly. Conflating those two diagnoses is the single most common way a scorecard review wastes its own most valuable signal.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for scoring/status convention and the strategy map's current causal links.

2. **Score each measure** against its target — current period, status (per the profile's convention), trend versus prior period.

3. **For every causal link in the strategy map, test it against this period's data**, classified as:
   - **CONFIRMED** — the leading measure moved as expected, and the downstream measure it's hypothesized to drive moved in the predicted direction within a plausible lag.
   - **NOT YET OBSERVABLE** — too little time has passed since the leading measure moved to expect the downstream effect yet; don't force a verdict prematurely.
   - **CONTRADICTED** — the leading measure moved as expected, enough time has passed, and the downstream measure did *not* move as predicted.

4. **For every CONTRADICTED link, run the execution-vs-theory split** — this is the step that matters most:
   - **Execution problem**: the initiative behind the leading measure wasn't actually run, or wasn't run as designed. The leading measure's own movement may even be misleading if it moved for reasons unrelated to the initiative. Fix: re-commit to executing, or revise the initiative — the strategy map itself may still be sound.
   - **Theory problem**: the initiative ran as designed, the leading measure moved as intended, and the hypothesized downstream effect still didn't materialize. This means the causal mechanism stated in the map was wrong. Fix: this requires revisiting `build-strategy-map`, not just trying harder at the same initiative — say this explicitly, even though it's the less comfortable conclusion to deliver.
   - Don't default to "execution problem" because it's the easier conversation — if the evidence points to a theory problem, say so.

5. **Roll up to an overall verdict** per perspective and flag whether enough CONTRADICTED-and-theory-problem links have accumulated to warrant pulling forward the annual map-refresh cadence rather than waiting for its scheduled date.

## Output format

```
MEASURE STATUS:
[Objective] — [Measure]: [current] vs [target] — [status] — Trend: [...]

[repeat per measure]

CAUSAL LINK VALIDATION:
[Lower objective] → [Upper objective]: [CONFIRMED | NOT YET OBSERVABLE | CONTRADICTED]
  [If CONTRADICTED:] Diagnosis: [execution problem | theory problem] — [evidence for the
    diagnosis, not just the assertion]
  [If theory problem:] Recommend revisiting build-strategy-map for this link.

[repeat per causal link]

OVERALL: [verdict] — [whether accumulated theory problems warrant an early map refresh]
```
