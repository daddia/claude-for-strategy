---
name: define-perspectives
description: >
  This skill should be used when the user asks to "define our perspectives,"
  "set up our scorecard structure," "should we use the standard four
  perspectives," or needs to decide the perspective set and causal-chain
  order before any objectives get drafted.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
---

# Define Perspectives

The real decision here isn't naming four boxes — it's deciding which perspective sits at the top of the causal chain, because that's the perspective every other objective in the map ultimately has to serve. Get this wrong and the whole map optimizes toward the wrong end state.

## Precondition: load profiles

Read `~/.claude/plugins/config/claude-for-strategy/balanced-scorecard/CLAUDE.md` and `org-profile.md` for sector, mission constraints, and any existing perspective vocabulary.

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

## Process

### Step 1: Confirm sector and top perspective

Apply the checklist above. State the choice and rationale explicitly in the output.

### Step 2: Set full perspective list and order

**Four perspectives by default**, top of causal chain first:

| Order (for-profit default) | Standard name | Causal role |
|---|---|---|
| 1 (top) | Financial | Ultimate end — what success means economically |
| 2 | Customer | What the org must deliver to customers/stakeholders to achieve Financial |
| 3 | Internal Process | What processes must excel to serve Customer |
| 4 (foundation) | Learning & Growth | People, culture, systems that enable Internal Process |

For mission-driven orgs, reorder so Mission/Stakeholder Impact is #1 and Financial Sustainability is an enabling perspective (typically #4 or paired with L&G — state the role clearly).

Use org vocabulary when it **clarifies causal role** — if renaming, state what causal job the renamed perspective plays (not cosmetic relabeling).

### Step 3: Fifth-perspective gate

If the user proposes a fifth perspective (Sustainability, Risk, Innovation, etc.):

| Test | Action |
|---|---|
| Can this live inside Internal Process or Learning & Growth without losing strategic force? | Fold it in — explain where |
| User can articulate why it cannot fold and what trade-off it forces | Keep as fifth — rare |
| Default | **Resist** — fifth perspectives dilute fixed-structure trade-off discipline |

### Step 4: Output for build-strategy-map

The perspective set with causal order explicit is the direct input to `build-strategy-map`. Do not draft objectives here.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
SECTOR: [for-profit | nonprofit | public sector | hybrid]

TOP-PERSPECTIVE DECISION:
  Choice: [Financial | Mission/Stakeholder Impact | other]
  Rationale: [checklist row or pressure-test answer]

PERSPECTIVES (top of causal chain first):
1. [Name] — [causal role: ultimate end this map serves]
2. [Name] — [causal role: what it must produce to serve #1]
3. [Name] — [causal role: what it must produce to serve #2]
4. [Name] — [causal role: foundational enabler]

RENAMES APPLIED: [any, with causal-clarity rationale — or none]
FIFTH-PERSPECTIVE REQUEST: [none | proposed | accepted/rejected with reason]
```

## Quality checks before delivering

- [ ] Top perspective chosen via checklist or pressure test — not defaulted blindly
- [ ] Mission-driven orgs do not default to Financial-at-top without rationale
- [ ] Every perspective has stated causal role in the chain
- [ ] Fifth perspective gate applied if requested
- [ ] Output ready as input to build-strategy-map (no objectives drafted here)
