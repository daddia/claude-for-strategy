---
name: build-strategy-map
description: >
  This skill should be used when the user asks to "build our strategy map,"
  "draft objectives for the scorecard," "what's our causal chain," or has
  candidate objectives that need an explicit causal mechanism linking each
  one to the perspective above it — the actual intellectual core of a
  balanced scorecard, not just objectives sorted into four boxes.
allowed-tools: Read, Grep, Glob, Write
metadata:
  version: "0.3.0"
  owner: "balanced-scorecard practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Build Strategy Map

## When to use

For strategy office, FP&A, or ops excellence practitioners building or refreshing a balanced scorecard strategy map. Assumes familiarity with BSC vocabulary; output is a structured draft for strategist review, not a board-ready conclusion.

Use when candidate objectives exist and need causal linkage across perspectives — the intellectual core of a scorecard, not objectives sorted into four boxes.

## What this skill does not do

- **Does not set perspective order** — run `/balanced-scorecard:define-perspectives` first if no agreed top-of-chain exists.
- **Does not select measures or targets** — route to `/balanced-scorecard:select-measures` and `/balanced-scorecard:set-targets-and-initiatives`.
- **Does not validate empirical truth of mechanisms** — flags UNVALIDATED links for `/balanced-scorecard:review-and-validate`; does not invent causal prose to make the map look complete.
- **Does not cascade to BU/team scorecards** — use `/balanced-scorecard:cascade-to-scorecards`.

## Preconditions

| Input | If missing |
|---|---|
| Perspective order (from `define-perspectives` or practice profile) | Halt — route to `/balanced-scorecard:define-perspectives`; a map without an agreed causal top is building on sand |
| Candidate objectives or themes to structure | Ask for them; do not draft objectives from thin air without labeling output as scaffold-only |
| Practice profile (`~/.claude/plugins/config/claude-for-strategy/balanced-scorecard/CLAUDE.md`) | Proceed with labeled assumptions from `org-profile.md`; flag `[review]` on sector/top-perspective choices |

## Provisional mode

When inputs are thin (objectives named but mechanisms unstated, or perspective order assumed not confirmed):

- Label output **CONFIDENCE: structured first pass** — never **defensible recommendation**.
- Tag every unstated mechanism **UNVALIDATED — no mechanism stated**; do not supply plausible-sounding causal prose.
- List missing inputs explicitly in STRUCTURAL FLAGS.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** MECE-complete map, every figure source-tagged, every upward link has a stated mechanism graded strong or weak.
  - **Medium:** Mostly complete, some mechanisms weak or marked `needs_review`, structural flags listed openly.
  - **Low:** Scaffold only — missing perspective confirmation, orphan objectives, or majority UNVALIDATED links; explicitly marked incomplete.
- **Tag vocabulary:** `[verify]`, `[review]`, `[model knowledge — verify]`, `[sourced: <where>]`, `UNVALIDATED` per house conventions in plugin `CLAUDE.md`.
- **Failure modes:**
  - **Strategic advice vs. support:** Surfaces causal structure and flags; does not declare which objectives belong on the map. UNVALIDATED tags and `[review]` on weak mechanisms keep judgment with the strategist.
  - **Client confidentiality:** Map content may include proprietary strategy — apply CONFIDENTIAL header from plugin `CLAUDE.md`; destination check before any exec-facing export.
  - **Accountability gap:** STRUCTURAL FLAGS block (orphans, unfunded mandates) forces engagement; gate before board-/exec-facing final with explicit confirmation and reviewer note.
  - **Analytical Rigor:** N/A for this shape — mechanism falsifiability is handled via rubric and handoff to `review-and-validate`, not MECE decomposition.
  - **Incentive Gaming:** N/A for this shape — no status scoring or target-setting here.
- **Escalation triggers:**
  - Novel sector model (e.g. dual-mission B-corp) where top perspective is genuinely ambiguous → pressure-test per `define-perspectives`, flag `[review]`, do not force a single top.
  - User asks to invent mechanisms they cannot state → tag UNVALIDATED, escalate to `review-and-validate` or a facilitated workshop; do not fill in.
  - More than four objectives per perspective persist after merge suggestion → flag over-stuffing, route extras to `set-targets-and-initiatives`.
  - Conflicting causal claims between objectives → surface both, ask strategist to resolve; do not pick a winner.

## Causal mechanism doctrine

Every objective below the top perspective must link upward with a **mechanism statement**:

```
Achieving [this objective] is expected to drive [objective above] because [mechanism].
```

### Mechanism quality rubric

| Quality | Test | Action |
|---|---|---|
| **Strong** | Names actor or process, intermediate effect, and why it reaches the parent objective; falsifiable in `review-and-validate` | Accept |
| **Weak** | Logical connection but vague or unmeasurable ("improve culture," "drive excellence") | Accept with flag — hard to test later |
| **Invalid** | Tautology, correlation asserted as causation, or "related to" with no chain | Reject — require rewrite or tag **UNVALIDATED** |
| **Missing** | User cannot state a mechanism | Tag **UNVALIDATED — no mechanism stated**; do not invent plausible prose |

| Invalid / weak | Strong |
|---|---|
| "More revenue drives financial results" (tautology) | "Reducing churn from 8% to 5% retains $Xm ARR, directly improving operating margin" |
| "Better customer experience improves customer perspective" (vague) | "NPS improvement from onboarding redesign increases referral rate, growing new-logo revenue" |
| "Learning objective supports growth" (no chain) | "Certifying 200 sellers on new platform cuts demo-to-close time by 2 weeks, raising win rate" |

## Workflow

### Step 1: Confirm perspective order

Read practice profile and any `define-perspectives` output. State perspective order explicitly in the output header.

### Step 2: Draft objectives

**2–4 objectives per perspective.** Draft top-down or bottom-up — either works — but test every link in the **upward** direction.

### Step 3: Require mechanism on every upward link

Apply the rubric above. Every link gets Mechanism: [statement] or [UNVALIDATED — reason].

### Step 4: Structural integrity checks

| Check | Definition | If found |
|---|---|---|
| **Orphan objective** | Lower-perspective objective with no stated upward link | Ask what it's for; add mechanism or remove from map |
| **Unfunded mandate** | Top-perspective objective with nothing beneath plausibly driving it | Flag as wish, not strategy — add supporting objectives or demote |
| **Over-stuffing** | More than ~4 objectives in one perspective | Suggest merge or demote extras to initiatives (`set-targets-and-initiatives`) |
| **Redundancy** | Two objectives in same perspective that are the same thing in different words | Merge |

### Step 5: Completeness and source-tag check

Before output: confirm every market figure, benchmark, or dollar amount is `[sourced: <where>]` or `[verify]`; no invented inputs.

### Step 6: Persist the map

Write to the location in the practice profile (whiteboard, doc path, or plugin `data/`). This is a **living artifact** other skills read — `review-and-validate` tests these links; do not recreate from scratch each review.

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

## Worked example

**Input:** For-profit SaaS. Perspectives confirmed (Financial → Customer → Internal Process → L&G). User provides: Financial objective "Grow ARR 25%"; Customer "Improve onboarding NPS"; L&G "Certify all AEs on new demo platform" — no mechanism stated for L&G link.

**Expected output (excerpt):**

```
CONFIDENCE: structured first pass
PERSPECTIVE ORDER: Financial → Customer → Internal Process → Learning & Growth

PERSPECTIVE: Financial
  Objective: Grow ARR 25% YoY

PERSPECTIVE: Customer
  Objective: Improve onboarding NPS from 32 to 50
    → Drives: Grow ARR 25% YoY
    → Mechanism: Higher NPS reduces early churn, improving net retention — Quality: weak [review]

PERSPECTIVE: Learning & Growth
  Objective: Certify all AEs on new demo platform by Q2
    → Drives: (no Internal Process objective stated)
    → Mechanism: UNVALIDATED — no mechanism stated; orphan until linked

STRUCTURAL FLAGS:
  ORPHAN OBJECTIVES: L&G objective lacks Internal Process parent
  UNFUNDED MANDATES: none
  OVER-STUFFED / REDUNDANT: none
```

## Quality checks before delivering

- [ ] Perspective order confirmed from define-perspectives or profile
- [ ] Every non-top objective has upward link with mechanism or UNVALIDATED tag
- [ ] Mechanism rubric applied — no invented causal prose
- [ ] Orphan, unfunded, over-stuffed, and redundant checks run
- [ ] Every figure source-tagged or flagged `[verify]`
- [ ] Map persisted to profile location (or user told where to save)
- [ ] Output does not read as a concluded board decision where `output_class` is draft-for-review

## Outputs

Follows plugin `CLAUDE.md` § Outputs — decision tree and reviewer note on delivery. Natural next branches after a map draft: cascade to scorecards, select measures, or schedule `review-and-validate` on UNVALIDATED links.
