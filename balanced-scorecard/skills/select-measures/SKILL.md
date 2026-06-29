---
name: select-measures
description: >
  This skill should be used when the user asks to "select measures for
  these objectives," "what should we measure for this," or needs each
  strategy-map objective assigned 1-3 measures with an explicit lead/lag
  classification and a check on the overall measure portfolio.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
  owner: "balanced-scorecard practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Select Measures

## When to use

For strategy office or FP&A practitioners assigning measures to strategy-map objectives. The discipline most scorecards skip: explicit lead/lag classification per measure and a portfolio mix check per perspective — not just attaching a number to each objective.

## What this skill does not do

- **Does not build the strategy map** — requires `build-strategy-map` objectives as input.
- **Does not set targets or initiatives** — route to `/balanced-scorecard:set-targets-and-initiatives`.
- **Does not own formal metric definitions when `performance` is installed** — hands off to `/performance:metrics-glossary` (same seam as `okr:instrument-metrics`).
- **Does not validate causal mechanisms empirically** — that's `/balanced-scorecard:review-and-validate`.

## Preconditions

| Input | If missing |
|---|---|
| Strategy map with objectives per perspective | Halt — route to `build-strategy-map` |
| Practice profile measure-count ceiling | Use default ~20–25; tag `[PROVISIONAL]` |
| Perspective causal roles (from map / define-perspectives) | Read profile; flag `[review]` if top perspective unclear |

## Provisional mode

When objectives exist but measure data sources are unknown:

- Propose measures with formula/source as `TBD — [verify]` inline (when `performance` not installed).
- Label borderline lead/lag cases honestly; do not call everything leading.
- Flag over-3-measures-per-objective as objective-too-broad, not measure sprawl.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Every objective has 1–3 measures, lead/lag classified, mix check per perspective, total within ceiling.
  - **Medium:** Mostly complete; some sources TBD or borderline classifications flagged.
  - **Low:** Scaffold only — missing map input or majority measures without classification.
- **Tag vocabulary:** `[verify]`, `[review]`, `[PROVISIONAL]` on defaults.
- **Failure modes:**
  - **Strategic advice vs. support:** Proposes measure candidates; strategist selects and removes — removal candidates listed, not silently dropped.
  - **Client confidentiality:** Measure definitions may expose operational detail — CONFIDENTIAL header when appropriate.
  - **Accountability gap:** LEAD/LAG MIX CHECK and over-ceiling removal candidates force portfolio judgment; no hidden dilution.
  - **Analytical Rigor:** N/A — classification and completeness, not MECE decomposition.
  - **Incentive Gaming:** N/A — no scoring or status reporting here.
- **Escalation triggers:**
  - More than 3 measures proposed for one objective → flag objective too broad; suggest split in `build-strategy-map`.
  - Top perspective majority leading → flag misaligned with causal role (lagging confirmation expected).
  - L&G or Internal Process majority lagging → flag no early-warning system.
  - Total count over ceiling → name removal candidates with rationale.

## Workflow

1. **Read the practice profile** for target total measure count (default ~20–25) and whether `performance` is installed.

2. **For each strategy-map objective, propose 1–3 measures.** More than 3 → flag objective too broad.

3. **Classify every measure as leading or lagging.** Be honest about borderline cases.

4. **Check lead/lag mix per perspective** against causal role: top perspective mostly lagging; L&G and Internal Process majority leading. Flag misfits.

5. **Check total measure count** against ceiling. If over, identify weakest removal candidates (no clear decision attached, duplicate signal).

6. **If `performance` is installed**, hand off formal metric definition to `performance:metrics-glossary` — this skill owns objective-to-measure mapping and lead/lag only.

7. **Completeness check:** every proposed measure has classification and source/formula path before output.

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

## Worked example

**Input:** Customer perspective objective "Improve onboarding NPS." Ceiling 22 measures; 18 already assigned elsewhere.

**Expected output (excerpt):**

```
OBJECTIVE: Improve onboarding NPS — Perspective: Customer
  Measure: Onboarding NPS (post-day-14 survey) — Leading — formula: avg score 0–100, source: Qualtrics, weekly
  Measure: 90-day logo churn rate — Lagging — defined in performance:metrics-glossary

LEAD/LAG MIX CHECK:
  Customer: 2 leading, 3 lagging — fits causal role

TOTAL MEASURE COUNT: 20 vs. ceiling 22 — within
```

## Quality checks before delivering

- [ ] Every objective has 1–3 measures with lead/lag classification
- [ ] No objective silently given 4+ measures without broad-objective flag
- [ ] Mix check run per perspective
- [ ] Total count vs ceiling with removal candidates if over
- [ ] Performance seam noted when installed
- [ ] Output does not read as final approved scorecard

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Natural next branches: `/balanced-scorecard:set-targets-and-initiatives`, `/performance:metrics-glossary` for formal definitions, or `/balanced-scorecard:review-and-validate` once actuals exist.
