---
name: performance-narrative
description: >
  This skill should be used when the user asks to "turn these numbers into a
  narrative," "write up our performance for the board," or provides metrics
  or tracker results that need to become a readable, BLUF-structured
  narrative rather than a table of numbers.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "performance practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Performance Narrative

## When to use

Turn metrics/tracker results into BLUF narrative for the audience in the practice profile — bottom line first, not metric-by-metric walkthrough.

## What this skill does not do

- **Does not invent actuals** — flag missing numbers `[verify]`.
- **Does not build trackers** — route to `/performance:tracker-builder`.
- **Does not replace finance sign-off** — board numbers need finance validation per profile gates.

## Preconditions

| Input | If missing |
|---|---|
| Metrics or tracker results | Ask user to provide |
| Practice profile (audience, cadence) | Use org default audiences; tag `[PROVISIONAL]` |
| Headline-worthy context | Ask what audience will act on |

## Provisional mode

Without audience in profile: default to sponsor/exec; tag `[PROVISIONAL]`; apply quiet mode for external-facing per plugin `CLAUDE.md`.

## Trust spine

- **Confidence bands** (`narrative-synthesis`):
  - **High:** BLUF headline, 2–4 MECE supporting points, explicit what's-needed, sourced figures.
  - **Medium:** Some unsourced movements tagged `[verify]`.
  - **Low:** Numbers missing for headline claim — halt or narrow scope.
- **Failure modes:**
  - **Strategic advice vs. support:** Narrative surfaces findings; audience decides action.
  - **Client confidentiality:** Board/sponsor content — CONFIDENTIAL header; quiet mode for external.
  - **Accountability gap:** What's-needed stated explicitly, not inferred.
  - **Analytical Rigor:** MECE supporting points; so-what test on each metric.
  - **Incentive Gaming:** N/A — narrative shape.
- **Escalation triggers:** Headline depends on unverified figure — tag before BLUF.

## Workflow

1. **Read practice profile** for audience and cadence.
2. **Identify headline** — one thing audience must know this period.
3. **Write bottom line first** — conclusion not topic.
4. **Group supporting metrics** into 2–4 MECE points; so-what test.
5. **State what's needed** — decision, investment, awareness.
6. **Full metric detail last** as reference appendix.
7. **MECE/falsifiability check** before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
HEADLINE: [bottom line]

WHY:
1. [supporting point]
2. [supporting point]

WHAT'S NEEDED: [decision/investment/awareness-only]

FULL DETAIL:
[metric-by-metric breakdown for reference]
```

## Worked example

**Input:** Conversion down 8%; mid-tier price change; board audience.

**Expected output (excerpt):**

```
HEADLINE: Conversion fell 8% this month, driven almost entirely by the mid-tier price change [sourced: tracker].
WHAT'S NEEDED: Decision whether to revert price test or accept conversion hit for margin gain [review]
```

## Quality checks before delivering

- [ ] BLUF headline is conclusion not topic
- [ ] Supporting points MECE; trivial movers in appendix
- [ ] What's-needed explicit
- [ ] Figures source-tagged
- [ ] Quiet mode for external-facing deliverables

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: finance validation, deeper dive on flagged metric, or exec decision on what's-needed.
