---
name: kpi-tree-builder
description: >
  This skill should be used when the user asks to "build a KPI tree," "what
  drives this metric," "break this North Star down into drivers," or needs a
  top-level metric decomposed into leading indicators with clear ownership.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "performance practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# KPI Tree Builder

## When to use

Decompose a North Star into MECE drivers and leading indicators — math or causal chain must work, not decorative strategy diagrams.

## What this skill does not do

- **Does not build spreadsheets** — route to `/performance:tracker-builder`.
- **Does not invent North Star definition** — locks definition first or marks provisional.
- **Does not set OKR targets** — route to `/okr:set-targets`.

## Preconditions

| Input | If missing |
|---|---|
| Org + performance profiles | Tag `[PROVISIONAL]`; bounce to practice-setup |
| North Star metric name | Ask; halt decomposition until supplied |
| Relationship type (multiplicative/additive/causal) | Ask once |

## Provisional mode

`[PROVISIONAL]` — no predefined North Star from profile; generic categories without house codes.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** North Star locked; 3–5 MECE drivers; indicators with tight definitions and sources.
  - **Medium:** Some `INPUT NEEDED` sources; double-counting flagged.
  - **Low:** North Star definition ambiguous — halt decomposition.
- **Failure modes:**
  - **Strategic advice vs. support:** Tree is draft for analytics leadership review.
  - **Client confidentiality:** Metric definitions may be sensitive — CONFIDENTIAL header.
  - **Accountability gap:** Every indicator has owner or `INPUT NEEDED`.
  - **Analytical Rigor:** MECE drivers; double-counting and lagging-only branches flagged.
  - **Incentive Gaming:** Rejects decorative trees dressed as analysis.
- **Escalation triggers:** Math doesn't decompose — switch to causal chain explicitly or flag gap.

## Workflow

### Step 1: Orient

Read `## KPI taxonomy` from performance profile. Confirm North Star, relationship type, audience, purpose, evidence pack.

### Step 2: Definition lock

Confirm North Star formula, window, population, source, owner before decomposing.

### Step 3: MECE driver decomposition

3–5 drivers that multiply, sum, or causally determine North Star.

### Step 4: Leading indicators per driver

1–3 leading indicators with tight definitions; flag lagging-only gaps.

### Step 5: Double-counting check

### Step 6: Taxonomy alignment — use profile category codes.

### Step 7: Data source gaps — `INPUT NEEDED` not invented baselines.

### Step 8: Completeness check before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
NORTH STAR: [metric]
DEFINITION: [exact]
RELATIONSHIP TYPE: [multiplicative | additive | causal]
DATA SOURCE: [sourced | INPUT NEEDED]
OWNER: [role]

LOAD-BEARING ASSUMPTIONS: [...]

DRIVER 1: [name] [category code]
  Relationship to North Star: [...]
  Leading indicators: [table]

DOUBLE-COUNTING FLAGS: [...]
LAGGING-ONLY FLAGS: [...]
EVIDENCE GAPS: [...]
```

## Worked example

**Input:** North Star = Monthly Active Users. Multiplicative. Driver: new signups × retention rate.

**Expected output (excerpt):**

```
DRIVER 1: New signups [B2]
  Leading indicators: | Trial starts | Definition: unique accounts completing signup | leading |
DOUBLE-COUNTING FLAGS: none
```

## Quality checks before delivering

- [ ] Profiles loaded or `[PROVISIONAL]` tagged
- [ ] North Star definition locked before decomposition
- [ ] 3–5 MECE drivers with explicit math/causal link
- [ ] Double-counting checked
- [ ] Category codes from profile
- [ ] No invented baselines

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/performance/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/performance:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `tracker-builder`, `performance-narrative`, or fill `INPUT NEEDED` with analytics team.
