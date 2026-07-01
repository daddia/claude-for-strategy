---
name: score-and-retro
description: >
  This skill should be used when the user asks to "score this cycle's
  OKRs," "run our OKR retro," "grade these key results," or needs
  end-of-cycle scoring plus a keep/kill/revise recommendation for each
  objective heading into the next cycle.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "okr practice"
  review_cadence: "quarterly"
  work_shape: "governance-tracking"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Score and Retro

## When to use

End-of-cycle scoring plus keep/kill/revise — checking whether hitting numbers served the objective, not just grading KRs.

## What this skill does not do

- **Does not set next-cycle targets** — route to `/okr:set-targets`.
- **Does not invent actuals** — `INPUT NEEDED` when missing.
- **Does not default objective call to KR average** unless profile explicitly requires it.

## Preconditions

| Input | If missing |
|---|---|
| Baseline, target, actual per KR | Score `INPUT NEEDED` — do not guess |
| Org + OKR practice profiles | Use default scoring doctrine; tag `[PROVISIONAL — configure profile]` |
| Commit/aspirational labels per KR | Ask; do not infer from score |

## Provisional mode

`[PROVISIONAL — configure profile for org-calibrated scoring]` when profiles missing; default formula applies.

## Trust spine

- **Confidence bands** (`governance-tracking`):
  - **High:** Every KR scored with shown arithmetic; objective calls with divergence checks; sandbagging named if present.
  - **Medium:** Some `INPUT NEEDED`; provisional profile scoring.
  - **Low:** Actuals missing for majority of KRs — halt retro conclusions.
- **Failure modes:**
  - **Strategic advice vs. support:** Keep/kill/revise are recommendations; calibration session owns final calls.
  - **Client confidentiality:** Scores may be sensitive — CONFIDENTIAL header.
  - **Accountability gap:** KR/objective divergences flagged, not averaged away.
  - **Analytical Rigor:** N/A — governance shape.
  - **Incentive Gaming:** Guards grade inflation and sandbagging normalization — 1.0 on aspirational or consistent ~1.0 across teams named as pattern.
- **Escalation triggers:** Widespread sandbagging pattern — flag for calibration, not praise.

## Scoring doctrine (inline)

Apply formula from practice profile. If none set, use defaults below.

### Default formula — increase-is-better KRs

```
score = (actual − baseline) ÷ (target − baseline)
```

Cap at **1.0** unless profile allows overachievement. Below baseline → **0.0**.

### Decrease-is-better KRs

```
score = (baseline − actual) ÷ (baseline − target)
```

### Binary / milestone KRs

| Outcome | Score |
|---|---|
| Fully achieved | 1.0 |
| Partially achieved | 0.5–0.7 per profile; default 0.5 |
| Not achieved | 0.0 |

### Commit vs aspirational at scoring time

| Type | How to read the score |
|---|---|
| **Commit** | 0.7–1.0 = delivered. Below 0.7 = miss worth explaining. |
| **Aspirational** | 0.6–0.7 = healthy stretch `[unverified — common OKR convention]`. 1.0 = overperformance or sandbag — check calibration. |

## Workflow

### Step 1: Load profiles

Read `org-profile.md` and `okr/CLAUDE.md` before scoring.

### Step 2: Score each KR

State baseline, target, actual, formula, score, commit/aspirational label. Show arithmetic.

### Step 3: Roll up to objective — do not average

Use decision tree: Achieved | Partially achieved | Not achieved. Mandatory divergence checks:
1. KRs scored well, objective wasn't served.
2. KRs missed, objective substantially advanced.

### Step 4: Next-cycle recommendation per objective

keep | kill | revise | promote-to-commit — "keep" should be least common.

### Step 5: Cross-team patterns

Shared external causes, sandbagging, systematic proxy failure.

### Step 6: Gaming-pattern check before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
SCORING FORMULA: [from profile, or default]

OBJECTIVE: [text]
KR scores:
  [KR text]: [score] ([commit | aspirational]) — baseline [x] → target [y], actual [z]

OBJECTIVE-LEVEL CALL: [achieved | partially achieved | not achieved] — [one line]

DIVERGENCE FLAG: [none | KRs hit / objective missed | KRs missed / objective advanced]

NEXT CYCLE: [keep | kill | revise | promote-to-commit] — [why]

[repeat per objective]

CROSS-TEAM PATTERNS (if applicable): [...]
CALIBRATION NOTES: [...]
```

## Worked example

**Input:** Objective "Win mid-market." KR "ARR $10M" scored 1.0 via one-off deal; KR "Logo retention 90%" scored 0.4.

**Expected output (excerpt):**

```
OBJECTIVE-LEVEL CALL: partially achieved — revenue spike not repeatable
DIVERGENCE FLAG: KRs hit / objective missed — ARR via one-off doesn't prove mid-market win [review]
NEXT CYCLE: revise — replace ARR KR with retention-led measures
```

## Quality checks before delivering

- [ ] Profile loaded or `[PROVISIONAL]` tagged
- [ ] Every KR has formula and arithmetic or `INPUT NEEDED`
- [ ] Objective calls do not default to KR averages
- [ ] Divergence types checked per objective
- [ ] "Keep" justified, not assumed
- [ ] Sandbagging signals named if present
- [ ] Gaming-pattern check run

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/okr/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/okr:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `set-targets` for revised KRs, calibration session, or `draft-objectives` for kill/revise.
