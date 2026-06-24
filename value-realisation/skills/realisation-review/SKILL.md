---
name: realisation-review
description: >
  This skill should be used when the user asks to "run our benefits
  realisation review," "how did we do against the original business
  case," "post-implementation review," or needs a portfolio-level
  planned-vs-actual comparison at the end of a realisation window, with
  an explicit check on whether estimates were systematically optimistic.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "value-realisation practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Realisation Review

## When to use

End-of-window planned-vs-actual portfolio review — optimism-bias calibration across initiatives.

## What this skill does not do

- **Does not re-litigate LAPSED reasons** — carry forward from `benefits-recovery`.
- **Does not blend benefit types** in one headline cash figure.

## Preconditions

| Input | If missing |
|---|---|
| Full register + tracking history | Ask |
| Prior realisation reviews (optional) | Skip optimism-bias cross-review |

## Provisional mode

Single-initiative review without portfolio history — note optimism-bias check limited.

## Trust spine

Narrative-synthesis BLUF; root-cause cluster diagnosis; calibration discount for future cases.

## Workflow

1. **Read the practice profile** (`../../CLAUDE.md`), the full benefits register, the complete tracking history, and any `benefits-recovery` decisions for benefits in the window under review.

2. **Score each benefit**: REALISED IN FULL / PARTIALLY REALISED (state the percentage) / NOT REALISED / LAPSED (carry forward the specific reason recorded in `benefits-recovery`, don't re-litigate it here).

3. **Roll up to portfolio level — total planned value vs. total realised value, split by type.** Report cash-releasing, cash-releasable, and non-cash/qualitative separately; don't blend them into one headline figure. If any cash-releasable benefit was treated as guaranteed cash anywhere in the original case or subsequent reporting, call that out explicitly here — it's a common and material distortion in how a portfolio's "savings" get represented upward.

4. **Run the optimism-bias check.** If prior `realisation-review` runs exist for other initiatives, compare this initiative's realisation rate to the pattern across those reviews. A single underperforming initiative may just be that initiative's story; a consistent realisation rate well below 100% across multiple independent reviews is a finding about how this organization's business cases get sized, and should be named as such rather than absorbed case-by-case. If a pattern emerges, state a suggested calibration discount for future business case estimates and flag it as a direct input to `transformation:business-case` or `corporate-strategy:evaluate-strategic-option`.

5. **Diagnose what should change about how benefits get planned, specifically — not a generic "do better" conclusion.** If `benefits-recovery`'s root-cause classifications across this portfolio cluster on NOT EMBEDDED, the gap is in adoption planning, not estimation, and the fix belongs in how business changes get resourced, not in how numbers get forecast. If they cluster on THEORY PROBLEM, the gap is in how causal assumptions get tested before a case is approved — say which one it actually was, since the two point to entirely different fixes.

6. **Output a BLUF-structured PIR** suitable as direct input to `consulting:exec-memo` or `deck-outline` for a steering-committee version, if that plugin is installed.

## Output format

```
RECOMMENDATION: [one to two sentences — overall verdict on this initiative's value delivery]

PORTFOLIO ROLL-UP:
| Benefit type | Planned | Realised | % |
|---|---|---|---|
| Cash-releasing | ... | ... | ... |
| Cash-releasable | ... | ... | ... |
| Non-cash/qualitative | ... | ... | ... |

CASH-RELEASABLE-AS-CASH FLAGS: [list, or "none"]

PER-BENEFIT SCORES:
  [name]: [REALISED IN FULL | PARTIALLY REALISED — X% | NOT REALISED | LAPSED — reason: ...]
  [repeat]

OPTIMISM-BIAS CHECK: [no prior reviews to compare] or
  [pattern across N reviews: average realisation rate X%; suggested calibration
   discount for future cases: ...]

ROOT-CAUSE CLUSTER (from benefits-recovery, this portfolio): [dominant cause(s) — what
  this implies should change in HOW benefits get planned next time]
```

## Worked example

**Input:** 60% realisation; three prior reviews averaged 55%.

**Expected output:** OPTIMISM-BIAS CHECK: pattern across 4 reviews; suggested calibration discount for future cases [review].

## Quality checks before delivering

- [ ] Types reported separately in roll-up
- [ ] Optimism-bias check run when history exists
- [ ] Root-cause cluster named with planning implication
- [ ] BLUF recommendation first

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `transformation:business-case` calibration, `consulting:exec-memo`, or steering PIR.
