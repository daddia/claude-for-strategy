---
name: okr-cascade
description: >
  This skill should be used when the user asks to "cascade company OKRs to
  teams," "break these objectives down to team level," or has objectives/KRs
  at one level that need to flow down with contribution, coverage, capacity,
  and cross-team conflict checks.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "performance practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# OKR Cascade

## When to use

Map company OKRs to team level with contribution, coverage, capacity, and cross-team conflict checks — performance plugin's cascade view (see also `/okr:cascade`).

## What this skill does not do

- **Does not invent parent OKRs** — `INPUT NEEDED` if missing.
- **Does not draft objectives/KRs** — route to `/okr:draft-objectives` and `/okr:write-key-results`.
- **Does not publish company-wide without GATE** — confirm before board-visible finals.

## Preconditions

| Input | If missing |
|---|---|
| Org + performance profiles | Tag `[PROVISIONAL]`; bounce to cold-start |
| Parent objectives and KRs | Halt — `INPUT NEEDED: parent objectives and KRs` |
| Org structure for capacity/conflict checks | Ask; flag fan-out `[review]` |

## Provisional mode

`[PROVISIONAL]` — company→team two levels; ~5 objectives, ~4 KRs per objective defaults.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Contribution, coverage, fan-out, conflict checks complete.
  - **Medium:** Some capacity data gaps; conflicts flagged.
  - **Low:** Parent OKRs missing — halt.
- **Failure modes:**
  - **Strategic advice vs. support:** Cascade is draft for leadership workshop.
  - **Client confidentiality:** OKR content internal — CONFIDENTIAL header.
  - **Accountability gap:** Cross-team conflicts surfaced, not averaged away.
  - **Analytical Rigor:** Orphans and uncovered parents both checked.
  - **Incentive Gaming:** Sibling KR conflicts that game one metric at another's expense flagged.
- **Escalation triggers:** Overloaded parent KR — flag too broad or too many children.

## Workflow

### Step 1: Orient — parent/child levels, parent OKRs, org structure, cycle.

### Step 2: Contribution test per child objective.

### Step 3: Restatement check.

### Step 4: Alignment/coverage — orphans and uncovered parent KRs.

### Step 5: Fan-out and capacity check.

### Step 6: Cross-team conflict check across siblings.

### Step 7: Completeness and gaming-pattern check before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
PARENT LEVEL: [...] — CHILD LEVELS: [...] — CYCLE: [...]

PARENT: [objective] — KR: [...]
  → [Child objective, owner] — Contribution: [genuine | restatement]

FAN-OUT CHECK: [table]
ALIGNMENT CHECK: Orphaned KRs: [...] — Uncovered parent KRs: [...]
CROSS-TEAM CONFLICT CHECK: [...]
CAPACITY FLAGS: [...]
```

## Worked example

**Input:** Parent KR "Reduce churn to 8%." Child: "Ship onboarding v2."

**Expected output (excerpt):**

```
→ Ship onboarding v2 (Product) — Contribution: restatement — output-shaped, not churn-linked [review]
```

## Quality checks before delivering

- [ ] Parent OKRs not invented
- [ ] Contribution and restatement checks run
- [ ] Orphans and uncovered parents listed
- [ ] Cross-team conflicts checked
- [ ] GATE before company-wide publish

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: leadership session on conflicts, `/okr:cascade` for OKR-plugin workflow, or `tracker-builder`.
