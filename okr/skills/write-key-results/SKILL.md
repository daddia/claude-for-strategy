---
name: write-key-results
description: >
  This skill should be used when the user asks to "write key results for
  this objective," "are these good KRs," "turn this into KRs," or provides
  candidate key results that need to be checked for whether they measure an
  outcome or just confirm a deliverable shipped.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Write Key Results

The core failure mode: a key result that measures whether work got *done* rather than whether it *worked*. "Ship the new onboarding flow" is an output — it can be 100% true and the objective can still have failed completely. The skill's job is forcing every KR to be a measurable change in a leading or lagging indicator, with the deliverable demoted to a supporting initiative if it shows up at all.

## Process

1. **Get the objective this KR set serves** — every check below depends on having it explicit, not implied.

2. **For each candidate KR, run the outcome test**: if this number moves the stated amount, does that prove the objective happened, or does it just prove some work got done? Deliverable-shaped language ("launch," "complete," "deliver," "ship") is the tell — when you see it, ask what the deliverable was *for*, and write the KR as that outcome instead. Relocate the original deliverable to a supporting initiative or task list, not a KR.

3. **Run the vanity-metric check.** A KR can be a genuine outcome metric and still be the wrong one — chosen because it's easy to measure or easy to move, not because it actually correlates with the objective. Ask explicitly: if this metric improved for reasons unrelated to the objective (a one-off promotion, a seasonal effect, a measurement change), would anyone be fooled into thinking the objective was served? If yes, it's too loosely coupled — either tighten the metric or pair it with a second KR that catches the gap.

4. **Check the baseline exists.** A KR with no real current value to measure from isn't ready — flag it for `instrument-metrics` rather than letting a target get set against an unknown starting point (see `set-targets`, which depends on this).

5. **Check the set is collectively sufficient.** 2-5 KRs per objective is the usual range. More importantly: if every KR in the set were hit, would the objective genuinely be achieved, or is there an obvious gap a skeptical reader would spot? Name the gap if one exists rather than letting the set look complete by count alone.

## Output format

```
OBJECTIVE: [text]

KR 1: [text]
  Verdict: [PASS — measurable outcome, plausibly causal to objective]
          or [FLAG — output-shaped; this measures work done, not impact; suggested
              outcome reframe: ...; original phrasing relocated to a supporting task]
          or [FLAG — vanity metric risk: could move for unrelated reasons; consider
              pairing with: ...]
  Baseline status: [known / unknown — flag for instrument-metrics]

[repeat per KR]

SET-LEVEL CHECK: [would hitting all KRs genuinely prove the objective? any gap?]
```
