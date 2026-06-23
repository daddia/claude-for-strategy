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
  version: "0.2.0"
---

# Review and Validate

Scoring the measures and calling it a review misses the actual point of a balanced scorecard. The distinctive move — the one OKR retros have no real equivalent for — is testing whether the causal links from `build-strategy-map` held up in the data. When a leading measure improved but the downstream lagging measure didn't follow as the map predicted, that's evidence the *strategy's theory* may be wrong, not necessarily evidence anyone executed poorly. Conflating those two diagnoses is the single most common way a scorecard review wastes its own most valuable signal.

## Precondition: load artifacts

Read:

- `~/.claude/plugins/config/claude-for-strategy/balanced-scorecard/CLAUDE.md` — scoring/status convention (RAG, numeric, % to target), typical lag assumptions
- The **live strategy map** at the location recorded in the profile (perspectives, objectives, mechanism statements, causal links)
- Current-period measure actuals vs targets

If the map or period data is missing, produce a **structured first pass** with `INPUT NEEDED` — do not invent measure values or causal verdicts.

## Process

### Step 1: Score each measure

For each measure: current value, target, status per profile convention, trend vs prior period.

| Status (default RAG if profile unset) | Rule |
|---|---|
| **Green** | ≥ 95% of target (increase-is-better) or ≤ 105% (decrease-is-better) |
| **Amber** | 80–94% of target (or equivalent band) |
| **Red** | Below amber threshold |

Use the profile's convention if it differs. Tag `[PROVISIONAL]` if using defaults.

### Step 2: Causal link test (the core discipline)

For **every upward causal link** in the strategy map (lower objective → upper objective, with stated mechanism), run this test against period data:

**Link verdict decision tree:**

```
1. Did the LEADING (lower-perspective) measure move in the direction
   the map predicted this period?
   → No: NOT TESTABLE THIS PERIOD (leading side didn't move — link idle)
   → Yes: continue

2. Has enough time passed for the downstream effect to plausibly appear?
   → No: NOT YET OBSERVABLE
   → Yes: continue

3. Did the LAGGING (upper-perspective) measure move in the predicted direction?
   → Yes: CONFIRMED
   → No: CONTRADICTED
```

**Default lag windows** (use profile overrides when set) `[unverified — planning convention]`:

| Link direction | Typical lag |
|---|---|
| Learning & Growth → Internal Process | 1–2 periods |
| Internal Process → Customer | 1 period |
| Customer → Financial / Mission | 1–2 periods |

Do not force **CONTRADICTED** inside the lag window — use **NOT YET OBSERVABLE** and state when the link becomes testable.

### Step 3: Execution vs theory split (for every CONTRADICTED link)

This is the step that matters most. Do not default to "execution problem" because it's the easier conversation.

**Execution problem** — assign when **any** of these is true:

| Evidence | Example |
|---|---|
| Initiative behind the leading measure wasn't funded or staffed | Budget cut mid-quarter |
| Initiative delivered differently than designed | Training rolled out to 20% of cohort |
| Leading measure moved for an **external** reason unrelated to the initiative | Market tailwind inflated NPS |
| Measure definition or collection method changed mid-period | Survey instrument swapped |
| Leading measure improvement is artifact, not real | Sample size too small |

**Fix:** Re-commit to execution or revise the initiative. The strategy map may still be sound.

**Theory problem** — assign only when **all** of these are true:

| Condition | Must hold |
|---|---|
| Initiative ran as designed | Evidence of delivery, not intent |
| Leading measure movement is attributable to the initiative | Not external confound |
| Adequate lag has elapsed | Per lag table above |
| Downstream measure still did not move as the mechanism predicted | Despite 1–3 |

**Fix:** Revisit `build-strategy-map` for this link — the stated mechanism was wrong. Say this explicitly even when uncomfortable. Trying harder at the same initiative will not fix a wrong theory.

If evidence is mixed, state **inconclusive** and what data would resolve it next period — do not guess.

### Step 4: Roll up and escalation

Per perspective: summarize measure status and how many links are CONFIRMED / CONTRADICTED / NOT YET OBSERVABLE.

**Early map refresh trigger:** If **two or more** CONTRADICTED links are diagnosed as **theory problems** in the same review — or one theory problem on a load-bearing top-perspective link — recommend pulling forward the annual map refresh rather than waiting for its scheduled date.

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
    Recommended fix: [re-execute initiative | revisit build-strategy-map for this link | gather [data] next period]

[repeat per causal link]

PERSPECTIVE ROLLUP:
| Perspective | Measure summary | Link summary |
|---|---|---|
| ... | ... | ... |

OVERALL: [verdict] — [whether theory problems warrant early map refresh]
```

## Quality checks before delivering

- [ ] Every measure scored with status and trend
- [ ] Every map causal link tested (not just measures scored)
- [ ] Lag windows applied — NOT YET OBSERVABLE used where appropriate
- [ ] CONTRADICTED links get execution-vs-theory split with evidence
- [ ] Theory problems explicitly recommend map revisit, not "try harder"
- [ ] Early refresh flagged if threshold met
