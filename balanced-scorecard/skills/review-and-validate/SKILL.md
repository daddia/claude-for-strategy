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
  version: "0.3.0"
  owner: "balanced-scorecard practice"
  review_cadence: "quarterly"
  work_shape: "governance-tracking"
  permission_tier: advisory
  output_class: "tracking-update"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Review and Validate

## When to use

For strategy office, FP&A, or scorecard owners running periodic BSC reviews. Scoring measures alone misses the point — this skill tests whether causal links from `build-strategy-map` held in the data, separating execution failure from theory failure.

## What this skill does not do

- **Does not build or revise the strategy map** — recommends `build-strategy-map` revisit when theory problems are diagnosed; does not rewrite mechanisms inline.
- **Does not set targets or select measures** — reads existing scorecard artifacts only.
- **Does not invent actuals** — missing data → `INPUT NEEDED` / structured first pass.
- **Does not replace OKR retros** — BSC causal-link testing is distinct from quarterly KR scoring.

## Preconditions

| Input | If missing |
|---|---|
| Live strategy map (profile location) | Halt — produce structured first pass with `INPUT NEEDED` |
| Current-period measure actuals vs targets | List gaps; do not invent values or causal verdicts |
| Practice profile scoring convention | Use default RAG with `[PROVISIONAL]` tag |

## Provisional mode

When map or period data is incomplete:

- Label **CONFIDENCE: structured first pass**.
- Score only measures with data; mark links **NOT TESTABLE THIS PERIOD** where leading data absent.
- Do not assign CONTRADICTED without evidence.

## Trust spine

- **Confidence bands** (`governance-tracking`):
  - **High:** Data current and instrumented; every measure scored; every link tested with lag rules applied.
  - **Medium:** Partially current data or `[PROVISIONAL]` scoring convention; some links NOT YET OBSERVABLE.
  - **Low:** Stale or missing actuals — flag explicitly; no causal verdicts presented as fact.
- **Tag vocabulary:** `[verify]`, `[review]`, `[PROVISIONAL]`, `[unverified — planning convention]` on default lag windows.
- **Failure modes:**
  - **Strategic advice vs. support:** Diagnoses execution vs theory with evidence; recommends map revisit — strategist decides whether to refresh.
  - **Client confidentiality:** Review may contain proprietary performance data — CONFIDENTIAL header; destination check.
  - **Accountability gap:** CONTRADICTED links require execution-vs-theory split with evidence — not a single RAG rollup that hides theory failure.
  - **Analytical Rigor:** N/A — governance review, not MECE decomposition.
  - **Incentive Gaming:** Guards against **RAG-washing** (green leading measures while lagging outcomes flat) and **execution-default bias** (blaming teams when theory is contradicted). Requires explicit theory-problem call when conditions met; early map refresh trigger prevents deferring uncomfortable map revisions.
- **Escalation triggers:**
  - Two+ theory-problem links or one on load-bearing top link → recommend early map refresh.
  - Measure definition changed mid-period → flag execution diagnosis unreliable.
  - Mixed evidence on CONTRADICTED link → **inconclusive**; name data needed next period.
  - External confound on leading measure → execution problem or NOT TESTABLE; do not confirm theory.

## Workflow

### Step 1: Load artifacts

Read:

- `~/.claude/plugins/config/claude-for-strategy/balanced-scorecard/CLAUDE.md` — scoring/status convention, lag assumptions
- The **live strategy map** at the profile location
- Current-period measure actuals vs targets

### Step 2: Score each measure

For each measure: current value, target, status per profile convention, trend vs prior period.

| Status (default RAG if profile unset) | Rule |
|---|---|
| **Green** | ≥ 95% of target (increase-is-better) or ≤ 105% (decrease-is-better) |
| **Amber** | 80–94% of target (or equivalent band) |
| **Red** | Below amber threshold |

Use the profile's convention if it differs. Tag `[PROVISIONAL]` if using defaults.

### Step 3: Causal link test (core discipline)

For **every upward causal link** in the strategy map, run against period data:

```
1. Did the LEADING measure move as predicted?
   → No: NOT TESTABLE THIS PERIOD
   → Yes: continue

2. Has enough lag elapsed?
   → No: NOT YET OBSERVABLE
   → Yes: continue

3. Did the LAGGING measure move as predicted?
   → Yes: CONFIRMED
   → No: CONTRADICTED
```

**Default lag windows** (profile overrides when set) `[unverified — planning convention]`:

| Link direction | Typical lag |
|---|---|
| Learning & Growth → Internal Process | 1–2 periods |
| Internal Process → Customer | 1 period |
| Customer → Financial / Mission | 1–2 periods |

Do not force **CONTRADICTED** inside the lag window.

### Step 4: Execution vs theory split (every CONTRADICTED link)

Do not default to "execution problem" because it's the easier conversation.

**Execution problem** — when any of: initiative unfunded/unstaffed; delivered differently than designed; leading move from external confound; measure definition changed; artifact not real improvement.

**Theory problem** — only when all hold: initiative ran as designed; leading move attributable to initiative; adequate lag elapsed; downstream still did not move as mechanism predicted.

**Fix for theory problem:** Revisit `build-strategy-map` for this link — state explicitly.

If mixed → **inconclusive**; name data for next period.

### Step 5: Roll up and escalation

Per perspective: measure status + link counts (CONFIRMED / CONTRADICTED / NOT YET OBSERVABLE).

**Early map refresh trigger:** Two+ theory-problem links, or one on load-bearing top link → recommend pulling forward annual map refresh.

### Step 6: Gaming-pattern check

Before output: confirm no perspective shows all-green measures while top-level lagging outcomes are red without a CONTRADICTED or theory-problem flag on the relevant links.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
REVIEW PERIOD: [period]
SCORING CONVENTION: [from profile or default RAG]

MEASURE STATUS:
| Objective | Measure | Current | Target | Status | Trend |
|---|---|---|---|---|---|
| ... | ... | ... | ... | G/A/R | ... |

CAUSAL LINK VALIDATION:
[Lower objective] → [Upper objective]
  Mechanism (from map): [quoted or summarized]
  Leading measure: [moved as predicted | did not move | N/A]
  Lag elapsed: [yes | no — testable after [period]]
  Downstream measure: [moved as predicted | did not move | N/A]
  Verdict: [CONFIRMED | NOT YET OBSERVABLE | CONTRADICTED | NOT TESTABLE THIS PERIOD]
  [If CONTRADICTED:]
    Diagnosis: [execution problem | theory problem | inconclusive]
    Evidence: [specific — not assertion]
    Recommended fix: [re-execute initiative | revisit build-strategy-map | gather [data] next period]

PERSPECTIVE ROLLUP:
| Perspective | Measure summary | Link summary |
|---|---|---|
| ... | ... | ... |

OVERALL: [verdict] — [whether theory problems warrant early map refresh]
```

## Worked example

**Input:** Q1 review. Map link: "Onboarding NPS → Grow ARR" with mechanism "NPS lift reduces churn." NPS improved 32→45 (green); ARR growth flat (amber). Initiative ran on schedule; 2-period lag elapsed for Customer→Financial.

**Expected output (excerpt):**

```
CAUSAL LINK VALIDATION:
Improve onboarding NPS → Grow ARR 25%
  Mechanism: NPS lift reduces churn, improving net retention
  Leading measure: moved as predicted
  Lag elapsed: yes
  Downstream measure: did not move as predicted
  Verdict: CONTRADICTED
    Diagnosis: theory problem
    Evidence: onboarding delivered per plan; NPS gain attributable; ARR flat after lag window
    Recommended fix: revisit build-strategy-map — churn may be driven by factors other than onboarding NPS
```

## Quality checks before delivering

- [ ] Every measure scored with status and trend
- [ ] Every map causal link tested (not just measures scored)
- [ ] Lag windows applied — NOT YET OBSERVABLE where appropriate
- [ ] CONTRADICTED links get execution-vs-theory split with evidence
- [ ] Theory problems recommend map revisit, not "try harder"
- [ ] Early refresh flagged if threshold met
- [ ] RAG-washing pattern checked before output

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/balanced-scorecard/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/balanced-scorecard:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Offer dashboard when measure table exceeds ~10 rows. Natural next branches: early `build-strategy-map` refresh, initiative re-commitment, or gather data for inconclusive links.
