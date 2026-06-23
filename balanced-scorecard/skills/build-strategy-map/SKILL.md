---
name: build-strategy-map
description: >
  This skill should be used when the user asks to "build our strategy map,"
  "draft objectives for the scorecard," "what's our causal chain," or has
  candidate objectives that need an explicit causal mechanism linking each
  one to the perspective above it — the actual intellectual core of a
  balanced scorecard, not just objectives sorted into four boxes.
work_shape: structured-aggregation
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
---

# Build Strategy Map

A strategy map without stated mechanisms is just four lists with arrows drawn out of habit. The discipline this skill enforces: every objective must state, in causal language, *why* achieving it would produce the effect claimed in the perspective above — "if we achieve X, we expect Y because [mechanism]," not just an arrow pointing upward.

## Trust spine

```
ANALYTICAL RIGOR: Every upward link requires a stated mechanism ("because …") or
  is tagged UNVALIDATED — do not supply plausible-sounding causal prose on the
  user's behalf. Orphan objectives, unfunded mandates, and redundant objectives
  within a perspective are listed explicitly in the output block, not hidden
  behind clean-looking arrows.
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent an input — flag what's needed instead.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

## Precondition: perspective order

Get the perspective order from `define-perspectives` output or the practice profile. If neither exists, route to `define-perspectives` first — a map without an agreed causal top is building on sand.

## Causal mechanism doctrine (inline)

Every objective below the top perspective must link upward with a **mechanism statement**:

```
Achieving [this objective] is expected to drive [objective above] because [mechanism].
```

### Mechanism quality rubric

Grade every mechanism before accepting it:

| Quality | Test | Action |
|---|---|---|
| **Strong** | Names actor or process, intermediate effect, and why it reaches the parent objective; falsifiable in `review-and-validate` | Accept |
| **Weak** | Logical connection but vague or unmeasurable ("improve culture," "drive excellence") | Accept with flag — hard to test later |
| **Invalid** | Tautology, correlation asserted as causation, or "related to" with no chain | Reject — require rewrite or tag **UNVALIDATED** |
| **Missing** | User cannot state a mechanism | Tag **UNVALIDATED — no mechanism stated**; do not invent plausible prose |

**Examples:**

| Invalid / weak | Strong |
|---|---|
| "More revenue drives financial results" (tautology) | "Reducing churn from 8% to 5% retains $Xm ARR, directly improving operating margin" |
| "Better customer experience improves customer perspective" (vague) | "NPS improvement from onboarding redesign increases referral rate, growing new-logo revenue" |
| "Learning objective supports growth" (no chain) | "Certifying 200 sellers on new platform cuts demo-to-close time by 2 weeks, raising win rate" |

If the user can't state a mechanism, **do not supply one on their behalf** — flag **UNVALIDATED** and carry to `review-and-validate` for empirical test.

## Process

### Step 1: Draft objectives

**2–4 objectives per perspective.** Draft top-down or bottom-up — either works — but test every link in the **upward** direction: if this objective is achieved, does it plausibly cause the effect claimed above?

### Step 2: Require mechanism on every upward link

Apply the rubric above. Every link gets Mechanism: [statement] or [UNVALIDATED — reason].

### Step 3: Structural integrity checks

| Check | Definition | If found |
|---|---|---|
| **Orphan objective** | Lower-perspective objective with no stated upward link | Ask what it's for; add mechanism or remove from map |
| **Unfunded mandate** | Top-perspective objective with nothing beneath plausibly driving it | Flag as wish, not strategy — add supporting objectives or demote |
| **Over-stuffing** | More than ~4 objectives in one perspective | Suggest merge or demote extras to initiatives (`set-targets-and-initiatives`) |
| **Redundancy** | Two objectives in same perspective that are the same thing in different words | Merge |

### Step 4: Persist the map

Write to the location in the practice profile (`~~whiteboard`, doc path, or plugin `data/`). This is a **living artifact** other skills read — `review-and-validate` tests these links; do not recreate from scratch each review.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
PERSPECTIVE ORDER: [top → bottom, from define-perspectives]

PERSPECTIVE: [top perspective name]
  Objective: [text]
  Objective: [text]

PERSPECTIVE: [next perspective name]
  Objective: [text]
    → Drives: [objective above]
    → Mechanism: [statement] — Quality: [strong | weak | UNVALIDATED]
  Objective: [text]
    → Drives: ...
    → Mechanism: ...

[repeat down through perspectives]

STRUCTURAL FLAGS:
  ORPHAN OBJECTIVES: [list or none]
  UNFUNDED MANDATES: [list or none]
  OVER-STUFFED / REDUNDANT: [list with merge/demote suggestion]

MAP LOCATION: [where persisted]
```

## Quality checks before delivering

- [ ] Perspective order confirmed from define-perspectives or profile
- [ ] Every non-top objective has upward link with mechanism or UNVALIDATED tag
- [ ] Mechanism rubric applied — no invented causal prose
- [ ] Orphan, unfunded, over-stuffed, and redundant checks run
- [ ] Map persisted to profile location (or user told where to save)
