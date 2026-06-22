---
name: kpi-tree-builder
description: >
  This skill should be used when the user asks to "build a KPI tree," "what
  drives this metric," "break this North Star down into drivers," or needs a
  top-level metric decomposed into leading indicators with clear ownership.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
---

# KPI Tree Builder

Decompose a North Star metric into drivers and leading indicators, with definitions tight enough that two people would calculate each one the same way.

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

Produce a KPI tree where the math or causal chain works, leading indicators give early warning, and every metric has an owner and data source — not a decorative strategy diagram.

## Precondition: load profiles

**Before decomposing, read both:**

- `~/.claude/plugins/config/claude-for-strategy/org-profile.md`
- `~/.claude/plugins/config/claude-for-strategy/performance/CLAUDE.md`

If missing or template, surface cold-start bounce with `/performance:cold-start-interview` or **"provisional"**.

### Provisional mode

Defaults: no predefined North Star — user must supply; generic metric categories without house codes. Tag `[PROVISIONAL]`.

## Workflow

### Step 1: Orient

| Question | Answer |
|---|---|
| **North Star metric** | Name and exact definition |
| **Relationship type** | Multiplicative / additive / causal chain |
| **Audience** | Working team / sponsor / board |
| **Purpose** | New tree / refresh / tracker build prep for `tracker-builder` |
| **Evidence pack** | Existing glossary, tracker structure, prior tree |

Read `## KPI taxonomy` from the performance profile for North Star metric(s), category codes, and naming convention.

### Step 2: Definition lock

**Confirm the North Star definition before decomposing.** Ambiguity at the top propagates through every driver.

```
NORTH STAR: [name]
DEFINITION: [formula, inclusion/exclusion rules, time window, population]
DATA SOURCE: [sourced: …] or INPUT NEEDED
OWNER: [role/team] or INPUT NEEDED
```

If definition is ambiguous, ask once. Do not decompose until locked or explicitly marked `DEFINITION PROVISIONAL`.

### Step 3: MECE driver decomposition

Decompose into **3–5 MECE drivers** — factors that mathematically or causally determine the North Star.

| Preference | Use when |
|---|---|
| Math works | Drivers multiply or sum to North Star |
| Causal chain | Clear A → B → North Star when math isn't clean |

Reject loose thematic groupings that don't decompose the number.

### Step 4: Leading indicators per driver

For each driver, identify **1–3 leading indicators** — metrics that move *before* the driver.

| Indicator | Definition | Data source | Owner |
|---|---|---|---|
| ... | tight enough for two people to calculate the same way | [sourced/INPUT NEEDED] | [role] |

**Lagging-only flag:** if only lagging indicators exist, name the measurement gap.

### Step 5: Double-counting check

Test whether the same underlying behavior appears in two branches. Flag overlaps and resolve — merge branches or redefine drivers.

### Step 6: Taxonomy alignment

Tag drivers and indicators with **existing category codes** from the profile (e.g. B2, B3). Do not invent new taxonomy codes when the profile defines one.

### Step 7: Data source gaps

Every metric needs a traceable source or `INPUT NEEDED: [system/field]`. No invented baselines.

### Step 8: Board-ready gate

Run trust-spine **GATE** before board- or exec-facing metric trees used in performance narratives.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]

NORTH STAR: [metric]
DEFINITION: [exact — formula, window, population]
RELATIONSHIP TYPE: [multiplicative | additive | causal]
DATA SOURCE: [sourced: …] or INPUT NEEDED
OWNER: [role]

LOAD-BEARING ASSUMPTIONS:
- ...

DRIVER 1: [name] [category code]
  Relationship to North Star: [math or causal link]
  Leading indicators:
  | Indicator | Definition | Source | Owner | Lead/lag |
  |---|---|---|---|---|
  | ... | ... | ... | ... | leading |

DRIVER 2: ...

DOUBLE-COUNTING FLAGS: [overlap found and resolution]
LAGGING-ONLY FLAGS: [drivers with no real leading indicator]
EVIDENCE GAPS: [INPUT NEEDED]
```

## Quality checks before delivering

- [ ] Both profiles loaded (or `[PROVISIONAL]` tagged)
- [ ] North Star definition locked before decomposition
- [ ] 3–5 MECE drivers — math or causal chain explicit
- [ ] Every indicator has tight definition and data source
- [ ] Category codes from profile — not invented
- [ ] Double-counting checked
- [ ] No invented baselines or targets

## Close with next steps

Branches: hand off to `tracker-builder` for sheet structure, run `performance-narrative` once data exists, fill INPUT NEEDED sources with analytics team, or propose profile update for new North Star definition.
