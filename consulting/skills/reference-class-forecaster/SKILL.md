---
name: reference-class-forecaster
description: >
  This skill should be used when the user asks to "forecast this project
  using reference class," "apply outside-view to this estimate," "calibrate
  optimism bias on this business case," or has cost, duration, or benefit
  estimates that need Flyvbjerg-style outside-view benchmarking and HM
  Treasury Green Book optimism-bias uplift before approval.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "consulting practice"
  review_cadence: "quarterly"
  work_shape: "hypothesis-driven-analysis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Reference Class Forecaster

## When to use

Calibrate cost, duration, and benefit estimates using the **outside view** before inside-view narrative wins the room — capital projects, transformation programs, product launches, and M&A integration timelines.

Pairs naturally with `/transformation:business-case`, `/corporate-strategy:evaluate-strategic-option`, and `/value-realisation:realisation-review` calibration loops.

## What this skill does not do

- **Does not replace sponsor judgment** — produces adjusted ranges and explicit bias flags; strategist decides funding.
- **Does not invent a reference class** — asks for comparables or uses sourced benchmarks; gaps tagged `INPUT NEEDED`.
- **Does not approve spend** — output is decision support with `[review]` on every adjusted headline number.

## Preconditions

| Input | If missing |
|---|---|
| Inside-view estimate (cost, duration, benefit, or all three) | Ask — cannot forecast without a claim to calibrate |
| Project type and scale band | Ask or infer from context; label assumption |
| Comparable reference class (optional) | Build from user examples + tagged public benchmarks |

## Provisional mode

When no org-specific track record exists in profiles, use published reference-class medians (Flyvbjerg infrastructure/program data, sector benchmarks) tagged `[model knowledge — verify]` and confidence **structured first pass**.

## Trust spine

- **Confidence bands** (`hypothesis-driven-analysis`):
  - **High:** ≥3 independent comparables in class; uplift applied with cited Green Book or org policy.
  - **Medium:** 1–2 comparables or mixed quality; uplift stated with rationale.
  - **Low:** Class named but thin evidence — directional adjustment only.
- **Analytical Rigor (mandatory):** Inside vs outside view shown side by side; uplift arithmetic explicit.
- **Accountability gap:** Adjusted range presented; inside-view retained for contrast — strategist picks which to fund against.
- Per `../../references/trust-conventions.md` for sourcing, `[verify]`, and GATE before board finals.

## Assumption audit

| Assumption | Status | If wrong, what breaks |
|---|---|---|
| Reference class is comparable (scale, sector, delivery model) | [confirmed / partial / weak] | Outside view misapplied |
| Inside-view estimate completeness | [full / partial / headline only] | Wrong dimension calibrated |
| Org optimism-bias policy | [profile / Green Book default / user override] | Uplift % disputed |
| Benefit vs cost/duration focus | [stated / inferred] | Wrong metric adjusted |

## Red flags

**Non-negotiable** calibration rules:

- **MUST NOT** present a single-point inside-view forecast as defensible without an outside-view row — narrative planning causes systematic underestimation of cost and duration (Flyvbjerg).
- **Do not proceed** to High confidence without naming the reference class explicitly — unnamed classes cause apples-to-oranges calibration.
- **Hard stop:** applying zero uplift when inside view is below class median on benefits or above on cost/duration without written rationale — that is optimism bias unchecked.
- **MUST NOT** blend cost, duration, and benefit adjustments into one opaque haircut — show each dimension.

## Outside-view step

This skill's core workflow **is** the outside view (Flyvbjerg) plus **optimism-bias uplift** (HM Treasury Green Book):

1. **Name the inside view** — restate the sponsor's estimate for cost, duration, and/or benefits exactly as given.
2. **Define the reference class** — 3+ comparable delivered projects/programs where outcomes are documented; tag each source.
3. **Extract class statistics** — median and P80 cost overrun, duration slip, and benefit realisation for the class (Flyvbjerg outside-view method).
4. **Apply Green Book optimism-bias uplift** — where inside view is more optimistic than class median on benefits or more pessimistic than median on risk, apply an explicit percentage uplift to costs/duration or haircut to benefits per Green Book guidance ("demonstrated, systematic tendency" for appraisers to be overly optimistic); state the % and policy basis.
5. **Produce adjusted range** — low / central / high with inside view retained for contrast.

**Always show inside and outside views side by side** because decision-makers anchor on the first number they see — presenting only the inside view tends to cause approval at an uncorrected optimistic estimate.

## Workflow

**Before step 1:** Read and apply `../../references/trust-conventions.md` — source-tagging, `[verify]` on model-only numbers, load-bearing assumptions at top, numbers provenance, confidence labeling, and board-ready gate.

1. Confirm project type, scale, and which dimensions to calibrate (cost, duration, benefit).
2. Run **Assumption audit**; halt on missing inside-view estimate.
3. Assemble reference class — user comparables first, then tagged public benchmarks.
4. Compute class medians and spread; document sources.
5. Apply **Green Book optimism-bias uplift** per dimension with explicit %.
6. Flag where inside view sits vs class (optimistic / aligned / conservative).
7. Run **Red flags** self-check before output.
8. GATE before board/exec final per trust spine.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
REFERENCE CLASS: [name — comparables listed with sources]

INSIDE VIEW (sponsor estimate):
| Dimension | Value | Source |
|---|---|---|
| Cost | ... | ... |
| Duration | ... | ... |
| Benefits | ... | ... |

OUTSIDE VIEW (class statistics — Flyvbjerg):
| Dimension | Class median | Class P80 / realisation rate | Source |
|---|---|---|---|

GREEN BOOK OPTIMISM-BIAS UPLIFT APPLIED:
| Dimension | Uplift % | Rationale |
|---|---|---|

ADJUSTED FORECAST RANGE:
| Dimension | Low | Central | High | vs inside view |
|---|---|---|---|---|

LOAD-BEARING ASSUMPTIONS:
- ...

CALIBRATION VERDICT: [inside view optimistic / aligned / conservative] — [review] on funding recommendation
EVIDENCE GAPS: [...]
```

## Worked example

**Input:** Platform rollout — inside view: $4M, 9 months, $6M annual benefits.

**Expected output (excerpt):**

```
REFERENCE CLASS: Mid-market SaaS core-system replacements (n=4) [model knowledge — verify]
OUTSIDE VIEW: median cost +28%, duration +35%, benefit realisation 62% at 12 months
GREEN BOOK OPTIMISM-BIAS UPLIFT APPLIED: cost +20%, duration +25%, benefits -30% vs plan
ADJUSTED FORECAST RANGE: cost $4.8–5.2M; duration 11–13 months; benefits $3.8–4.2M annual [review]
```

## Quality checks before delivering

- [ ] Inside and outside views both present
- [ ] Reference class named with ≥1 comparable or gap flagged
- [ ] Green Book uplift % explicit per dimension
- [ ] No single-point defensible forecast without range
- [ ] Flyvbjerg outside-view and Green Book cited in methodology line

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Natural next: `/transformation:business-case` with adjusted inputs, `/consulting:exec-memo` for IC brief, or profile update for org calibration discount.
