---
name: score-and-retro
description: >
  This skill should be used when the user asks to "score this cycle's
  OKRs," "run our OKR retro," "grade these key results," or needs
  end-of-cycle scoring plus a keep/kill/revise recommendation for each
  objective heading into the next cycle.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
---

# Score and Retro

The core failure mode this catches: grading the numbers and calling it done, without checking whether hitting the numbers actually served the objective. A KR scored 1.0 doesn't always mean the objective was achieved, and a KR scored 0.4 doesn't always mean it failed in any way that matters — those divergences are the most important output of a retro, not a footnote.

## Trust spine

```
INCENTIVE GAMING: Guards against grade inflation and sandbagging normalization —
  treating KR scores as sufficient without checking objective served, defaulting
  to keep-as-is, or ignoring cross-team patterns of trivial aspirational hits.
  Sandbagging detection: name when multiple teams score ~1.0 on aspirational KRs
  in the same direction; flag KR/objective divergences rather than averaging
  them away; keep-as-is is the least common recommendation, not the default.
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent an input — flag what's needed instead.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

## Precondition: load profiles

**Before scoring, read both:**

- `~/.claude/plugins/config/claude-for-strategy/org-profile.md` — calibration norms, public vs internal OKR policy
- `~/.claude/plugins/config/claude-for-strategy/okr/CLAUDE.md` — scoring formula, commit/aspirational philosophy, expected aspirational band, sandbagging history in seed data

If either file is missing or still has template placeholders, use the **default scoring doctrine** below and tag output `[PROVISIONAL — configure profile for org-calibrated scoring]`.

## Scoring doctrine (inline)

Apply the formula recorded in the practice profile. If none is set, use this default:

### Default formula — increase-is-better KRs

```
score = (actual − baseline) ÷ (target − baseline)
```

Cap at **1.0** unless the profile explicitly allows overachievement above 1.0. If `actual` is below `baseline`, score is **0.0** (do not extrapolate negative scores unless the profile says otherwise).

### Decrease-is-better KRs (cost, churn, defects)

```
score = (baseline − actual) ÷ (baseline − target)
```

Same cap rules. If baseline or target is missing, score is **`INPUT NEEDED`** — do not guess.

### Binary / milestone KRs

| Outcome | Score |
|---|---|
| Fully achieved | 1.0 |
| Partially achieved (profile or user defines partial) | 0.5–0.7 per profile; default 0.5 |
| Not achieved | 0.0 |

### Commit vs aspirational at scoring time

| Type | How to read the score |
|---|---|
| **Commit** | 0.7–1.0 = delivered as promised. Below 0.7 = a miss worth explaining — not automatically a failure of the objective, but a miss on this KR. Scoring 1.0 on a commit is **expected**, not exceptional — don't treat it as retro "success" by itself. |
| **Aspirational** | 0.6–0.7 = healthy stretch zone `[unverified — common OKR convention]`. Below 0.4 may still be valuable progress if the objective was substantially advanced anyway (see objective rollup). **1.0 on aspirational** = either genuine overperformance or a sandbagged target — check calibration from `set-targets`. |

### Sandbagging signals (name if present)

- Multiple aspirational KRs scored **≥ 0.95** in the same cycle across a team
- Historical seed data shows **consistent ~1.0** on most KRs across prior cycles
- Targets were set trivially above baseline at cycle start (flagged in `set-targets`)

Do not normalize sandbagging away — name the pattern and let it inform next-cycle recommendations.

## Process

### Step 1: Score each KR

For each KR, state: baseline, target, actual, formula used, computed score, commit/aspirational label. Show the arithmetic in one line when inputs exist — scoring should not be reverse-engineered later.

### Step 2: Roll up to objective level — do not average

For each objective, assign an **objective-level call** using this decision tree (KR scores inform but do not mechanically determine the call):

| Objective-level call | When to use |
|---|---|
| **Achieved** | The outcome the objective described actually happened — even if some KRs missed numerically |
| **Partially achieved** | Material progress but the full outcome wasn't reached; or mixed KR results that net to meaningful but incomplete delivery |
| **Not achieved** | The objective's outcome did not materialize in any way that matters |

**Mandatory divergence checks** — name explicitly if either applies:

1. **KRs scored well, objective wasn't really served** — weak proxy KRs (a `write-key-results` miss surfacing late), or the number was hit in a way that doesn't repeat or doesn't matter (one-off channel, pulled-forward revenue, scope cut that left the underlying outcome unchanged).
2. **KRs missed numerically, objective was substantially advanced anyway** — target miscalibration from `set-targets` overreach, or the KR was a poor measure of what actually moved; don't let a missed number erase real progress.

A simple KR average is **not** the objective-level call unless the user explicitly uses average-as-rollup in their profile.

### Step 3: Next-cycle recommendation per objective

| Recommendation | When to use | Not when |
|---|---|---|
| **keep** | Objective still right; KRs and targets were well-calibrated; execution gap was the issue, not strategy | Objective was wrong but numbers looked fine |
| **kill** | Objective no longer a strategic priority, or retro proved the objective itself was misguided | One bad quarter on a still-valid multi-year objective |
| **revise** | Objective direction right but KRs, targets, or wording need rework | Objective itself is obsolete |
| **promote-to-commit** | An aspirational KR was consistently hit or nearly hit — ready to formalize as a commit next cycle | First cycle on a genuinely stretch target that scored 0.7 |

**"Keep as-is" should be the least common recommendation**, not the default. A cycle that changes nothing usually means the retro wasn't honest.

### Step 4: Cross-team patterns (if multiple teams)

- **Shared external cause** behind several misses — name once at portfolio level rather than re-litigating per team
- **Sandbagging pattern** — multiple teams' aspirational KRs all scoring ~1.0 in the same direction
- **Systematic proxy failure** — same KR type (e.g. all vanity pipeline metrics) scoring well while objectives aren't served

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
SCORING FORMULA: [from profile, or default as stated above]

OBJECTIVE: [text]

KR scores:
  [KR text]: [score] ([commit | aspirational]) — baseline [x] → target [y], actual [z]
  [KR text]: [score] (...)

OBJECTIVE-LEVEL CALL: [achieved | partially achieved | not achieved] — [one line; explain
  if this diverges from KR scores]

DIVERGENCE FLAG: [none | KRs hit / objective missed | KRs missed / objective advanced] —
  [evidence]

NEXT CYCLE: [keep | kill | revise | promote-to-commit] — [why per rubric above]

[repeat per objective]

CROSS-TEAM PATTERNS (if applicable): [shared causes, sandbagging, proxy failures]

CALIBRATION NOTES: [any sandbagging signals, targets to revisit via set-targets]
```

## Quality checks before delivering

- [ ] Profile loaded (or `[PROVISIONAL]` tagged)
- [ ] Every KR has stated formula and arithmetic (or `INPUT NEEDED`)
- [ ] Objective-level calls do not default to KR averages
- [ ] Both divergence types explicitly checked per objective
- [ ] "Keep" is justified, not assumed
- [ ] Sandbagging signals named if present
