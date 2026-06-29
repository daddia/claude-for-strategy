---
name: define-perspectives
description: >
  This skill should be used when the user asks to "define our perspectives,"
  "set up our scorecard structure," "should we use the standard four
  perspectives," or needs to decide the perspective set and causal-chain
  order before any objectives get drafted.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "balanced-scorecard practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Define Perspectives

## When to use

For strategy office or FP&A practitioners deciding the perspective set and causal-chain order before drafting objectives. The real decision isn't naming four boxes — it's which perspective sits at the top of the causal chain, because every other objective ultimately has to serve that end.

## What this skill does not do

- **Does not draft objectives** — output feeds `/balanced-scorecard:build-strategy-map` only.
- **Does not select measures or targets** — route to `/balanced-scorecard:select-measures` and `/balanced-scorecard:set-targets-and-initiatives`.
- **Does not decide hybrid top perspective for the user** — runs pressure test and surfaces trade-offs; strategist chooses.
- **Does not replace practice-setup** — reads practice profile; run `/balanced-scorecard:practice-setup` if profile is empty.

## Preconditions

| Input | If missing |
|---|---|
| Practice profile and org profile | Read if present; if sector unknown, ask before applying checklist |
| Sector / mission constraint awareness | Ask — do not default to for-profit Financial-at-top |
| User confirmation on ambiguous hybrid | Flag `[review]`; do not fake a single top when pressure test is unresolved |

## Provisional mode

When sector is unclear or user has not answered pressure test:

- Label **CONFIDENCE: structured first pass**.
- Present checklist options with `[review]` on unresolved hybrid.
- Do not proceed to `build-strategy-map` handoff without stated top perspective or explicit dual-track flag.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Sector confirmed, top perspective chosen via checklist or documented pressure-test answer, every perspective has stated causal role.
  - **Medium:** Mostly complete; weak rename rationale or fifth-perspective proposal under review.
  - **Low:** Scaffold only — sector unknown or hybrid unresolved; dual-track flagged explicitly.
- **Tag vocabulary:** `[review]` on subjective structural choices; `[verify]` on user-stated sector facts.
- **Failure modes:**
  - **Strategic advice vs. support:** Surfaces checklist and pressure test; does not pick Financial vs Mission for hybrid orgs without user answer.
  - **Client confidentiality:** Perspective choices may reveal org strategy — apply CONFIDENTIAL header when appropriate.
  - **Accountability gap:** TOP-PERSPECTIVE DECISION block forces explicit rationale; unresolved hybrid → dual-track note, not silent default.
  - **Analytical Rigor:** N/A — structural framing, not MECE analysis.
  - **Incentive Gaming:** N/A — no scoring or tracking.
- **Escalation triggers:**
  - Hybrid org with no pressure-test answer → ask test; flag dual-track if genuinely cannot choose.
  - Fifth perspective proposed → run gate; default resist unless user articulates trade-off.
  - Mission-driven org with Financial-at-top requested without rationale → flag `[review]`, cite checklist.
  - Cosmetic renames without causal role → reject rename or require causal-clarity rationale.

## Top-perspective decision (inline checklist)

Run this **before** naming perspectives. The top perspective is the ultimate end the entire map serves.

| Sector / constraint | Top perspective | Causal logic |
|---|---|---|
| **For-profit**, no unusual mission constraint | **Financial** | L&G and Internal Process are means → Customer is intermediate end → Financial is ultimate end |
| **Mission-driven** (nonprofit, public sector, explicit non-financial primary mandate) | **Mission** or **Stakeholder Impact** | Mission is ultimate end → Financial moves to **enabling/stewardship** role ("Financial Sustainability" — how the org funds delivery) |
| **Hybrid** (e.g. B-corp claiming dual primacy) | **Ask the pressure test** | See below |

### Pressure test (when ambiguous)

Ask: **"Under real pressure — budget cut, donor loss, activist campaign — which would the organization sacrifice for the other?"**

| Answer reveals | Top perspective |
|---|---|
| Would cut mission programs to preserve margin | Financial |
| Would accept losses to preserve mission outcomes | Mission / Stakeholder Impact |
| Genuinely cannot choose | Say so — map may need dual-track review cadence; do not fake a single top |

This is a structural decision, not a rename. Mission-at-top flows causality differently than Financial-at-top.

## Workflow

### Step 1: Load profiles

Read `~/.claude/plugins/config/claude-for-strategy/balanced-scorecard/CLAUDE.md` and `org-profile.md` for sector, mission constraints, and existing perspective vocabulary.

### Step 2: Confirm sector and top perspective

Apply the checklist above. State the choice and rationale explicitly in the output.

### Step 3: Set full perspective list and order

**Four perspectives by default**, top of causal chain first:

| Order (for-profit default) | Standard name | Causal role |
|---|---|---|
| 1 (top) | Financial | Ultimate end — what success means economically |
| 2 | Customer | What the org must deliver to customers/stakeholders to achieve Financial |
| 3 | Internal Process | What processes must excel to serve Customer |
| 4 (foundation) | Learning & Growth | People, culture, systems that enable Internal Process |

For mission-driven orgs, reorder so Mission/Stakeholder Impact is #1 and Financial Sustainability is an enabling perspective (typically #4 or paired with L&G — state the role clearly).

Use org vocabulary when it **clarifies causal role** — if renaming, state what causal job the renamed perspective plays (not cosmetic relabeling).

### Step 4: Fifth-perspective gate

If the user proposes a fifth perspective (Sustainability, Risk, Innovation, etc.):

| Test | Action |
|---|---|
| Can this live inside Internal Process or Learning & Growth without losing strategic force? | Fold it in — explain where |
| User can articulate why it cannot fold and what trade-off it forces | Keep as fifth — rare |
| Default | **Resist** — fifth perspectives dilute fixed-structure trade-off discipline |

### Step 5: Handoff check

Perspective set with causal order explicit is direct input to `build-strategy-map`. No objectives drafted here.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
SECTOR: [for-profit | nonprofit | public sector | hybrid]

TOP-PERSPECTIVE DECISION:
  Choice: [Financial | Mission/Stakeholder Impact | other | dual-track]
  Rationale: [checklist row or pressure-test answer]

PERSPECTIVES (top of causal chain first):
1. [Name] — [causal role: ultimate end this map serves]
2. [Name] — [causal role: what it must produce to serve #1]
3. [Name] — [causal role: what it must produce to serve #2]
4. [Name] — [causal role: foundational enabler]

RENAMES APPLIED: [any, with causal-clarity rationale — or none]
FIFTH-PERSPECTIVE REQUEST: [none | proposed | accepted/rejected with reason]
```

## Worked example

**Input:** Nonprofit food bank. User states mission outcomes matter more than surplus margin under donor pressure.

**Expected output (excerpt):**

```
CONFIDENCE: defensible recommendation
SECTOR: nonprofit

TOP-PERSPECTIVE DECISION:
  Choice: Mission / Stakeholder Impact
  Rationale: Pressure test — would accept losses to preserve meals served

PERSPECTIVES (top of causal chain first):
1. Mission Impact — ultimate end: households food-secure in service area
2. Program Delivery — what must excel to drive mission outcomes
3. Internal Process — operational efficiency enabling delivery
4. Financial Sustainability — enabling perspective: funding model sustains programs

FIFTH-PERSPECTIVE REQUEST: none
```

## Quality checks before delivering

- [ ] Top perspective chosen via checklist or pressure test — not defaulted blindly
- [ ] Mission-driven orgs do not default to Financial-at-top without rationale
- [ ] Every perspective has stated causal role in the chain
- [ ] Fifth perspective gate applied if requested
- [ ] Output ready as input to build-strategy-map (no objectives drafted here)
- [ ] Hybrid unresolved cases flagged dual-track, not forced to single top

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Natural next branch: `/balanced-scorecard:build-strategy-map` with confirmed perspective order.
