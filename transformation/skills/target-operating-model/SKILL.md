---
name: target-operating-model
description: >
  This skill should be used when the user asks to "design the target
  operating model," "what should our TOM look like," or needs current-state
  and ambition translated into a future operating model across capability,
  organization, process, technology, and data.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
---

# Target Operating Model

Design a target operating model (TOM) across the standard layers, anchored to a stated ambition and current state — not a generic TOM template, a specific design for this organization's gap.

## Trust spine

```
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent an input — flag what's needed instead.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

## Purpose

Produce a TOM design a transformation lead can defend in architecture review and steering — each layer follows from the one above, uses the org's platform vocabulary, and flags where one layer's design constrains another.

## Precondition: load profiles

**Before designing, read both:**

- `~/.claude/plugins/config/claude-for-strategy/org-profile.md`
- `~/.claude/plugins/config/claude-for-strategy/transformation/CLAUDE.md`

If missing or template, surface cold-start bounce with `/transformation:cold-start-interview` or **"provisional"**.

### Provisional mode

Defaults: generic capability → org → process → tech → data layering; no named EA principles; platform layer uses `INPUT NEEDED: confirm house platform terms`. Tag `[PROVISIONAL]`.

## Workflow

### Step 1: Orient

| Question | Answer |
|---|---|
| **Current state** | Operating reality today — structure, systems, key processes |
| **Ambition** | Target outcome this TOM closes |
| **Scope** | Enterprise / BU / platform / product line |
| **Layers in scope** | All five or subset (confirm if user narrows) |
| **Audience** | Working design / architecture review / steering / board |
| **Evidence pack** | Architecture docs, org charts, process maps — what's available |

If ambition or current state is unclear, ask before designing.

### Step 2: EA principles check

Read `## Framework preferences → Enterprise architecture principles` and `## Definitions → Technology constraints` from the transformation profile.

For each design choice in the technology and data layers, note compliance or deviation:

```
EA CHECK:
- [Principle from profile] → [design choice aligns / deviates — explain]
```

Deviations require explicit flag — not silent overrides of house rules.

### Step 3: Layer-by-layer design

Design in order; each layer follows from the one above:

1. **Capabilities** — what the org must be able to do that it can't today. Mark **new** vs **existing-but-improved**.
2. **Organization** — structure, roles, reporting lines. Mark **new** vs **redesign of existing**.
3. **Process** — end-to-end processes that must change to use the new org/capabilities.
4. **Technology** — platform/system changes in the org's **own vocabulary** from the profile (not generic placeholders).
5. **Data** — ownership, quality, flow dependencies for the layers above.

Where evidence is missing for a layer, mark `INPUT NEEDED: [what document or interview would fill this]` — do not invent org structure or system names.

### Step 4: Interdependency check

Explicitly test cross-layer constraints:

| Check | Question |
|---|---|
| Org ↔ Process | Can processes actually run on the proposed structure? |
| Process ↔ Technology | Do systems support the redesigned processes? |
| Technology ↔ Data | Does data architecture support the tech choices? |
| Capability ↔ Org | Does structure deliver the capabilities claimed? |

Flag every material constraint in `INTERDEPENDENCY FLAGS`.

### Step 5: Change sizing

Summarize what's genuinely **new** vs **modification** — matters for change management and `business-case` cost sizing later.

### Step 6: Sequencing handoff

Note which TOM elements are prerequisites for others — headline sequencing only; detailed phasing goes to `roadmap-builder`.

### Step 7: Board-ready gate

Run trust-spine **GATE** before steering- or board-facing TOM finals.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
SCOPE: [enterprise | BU | platform | product line]
AUDIENCE: [working | architecture review | steering | board]

LOAD-BEARING ASSUMPTIONS:
- ...

GAP BEING CLOSED: [current state → ambition, one sentence]

EA PRINCIPLES CHECK:
- ...

CAPABILITIES: [list — new / existing-but-improved]
ORGANIZATION: [structure/roles — new / modified]
PROCESS: [key end-to-end processes affected]
TECHNOLOGY: [platform/system changes, house vocabulary]
DATA: [ownership, quality, flow]

INTERDEPENDENCY FLAGS:
- [layer A] constrains [layer B] because [...]

CHANGE SIZING: [new vs modified summary]
SEQUENCING HANDOFF: [what must land first for `roadmap-builder`]
EVIDENCE GAPS: [INPUT NEEDED]
```

## Quality checks before delivering

- [ ] Both profiles loaded (or `[PROVISIONAL]` tagged)
- [ ] Current state and ambition confirmed
- [ ] Technology layer uses profile vocabulary — not generic placeholders
- [ ] EA principles and tech constraints checked
- [ ] Interdependencies flagged — not designed in silos
- [ ] New vs modified marked for change sizing
- [ ] No invented system names, headcount, or cost figures

## Close with next steps

Branches: validate tech layer with architecture forum, run `maturity-assessment` on weak dimensions, build `business-case` for funded elements, hand off sequencing to `roadmap-builder`, or fill evidence gaps before steering circulation.
