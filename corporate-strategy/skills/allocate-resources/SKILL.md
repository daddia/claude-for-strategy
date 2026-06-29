---
name: allocate-resources
description: >
  This skill should be used when the user asks to "review our resource
  allocation," "are we funding the right things," "build a portfolio
  allocation view," or needs current spend, headcount, or management
  attention checked against strategic priority for misallocation.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "corporate-strategy practice"
  review_cadence: "quarterly"
  work_shape: "option-evaluation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Allocate Resources

## When to use

For CSO, portfolio managers, or strategy leads diagnosing whether capital, headcount, and management attention match stated strategic priority — not history, politics, or sunk cost.

## What this skill does not do

- **Does not infer priority from current spend** — that's the failure mode being diagnosed.
- **Does not invent budget or headcount** — `INPUT NEEDED` when data missing.
- **Does not approve reallocation** — recommends specific from→to moves for portfolio forum.
- **Does not run growth-vector assessment** — cross-checks `assess-growth-vectors` if available.

## Preconditions

| Input | If missing |
|---|---|
| Org + corporate-strategy profiles | Surface cold-start or `[PROVISIONAL]` |
| Strategic priority ranking | Halt — get or confirm before comparing |
| Allocation data (capital, HC, attention) | Ask; mark partial/missing per row |

## Provisional mode

Defaults: generic portfolio units; three priority tiers; `[PROVISIONAL]` on all figures. User must provide dollars/headcount — never invented.

## Trust spine

- **Confidence bands** (`option-evaluation`): High = all options scored against same priority framework, sourced; Medium = criteria explicit, some data partial; Low = priority or spend unknown — structured first pass only.
- **Strategic advice vs. support (mandatory):** Reallocation table is recommendation input — `[review]` on each move; strategist and portfolio committee decide.
- **Escalation:** Missing priority → stop; inferring priority from spend → forbidden; board-final → GATE + reviewer note.

```
SOURCING / ASSUMPTIONS / NUMBERS / CONFIDENCE / GATE — per trust-conventions
```

## Workflow

### Step 1: Orient

Portfolio scope, allocation types, review forum, time horizon, evidence pack. Read profile definitions for units, tiers, stickiness.

### Step 2: Evidence pack

Capital/budget, headcount, management attention, priority ranking — status and source per row. Management attention: `[user estimate — not verified]` if unsourced.

### Step 3: Allocation vs priority comparison

Per unit: priority tier/rank alongside capital %, headcount %, attention. Tag `[sourced]` or `INPUT NEEDED`.

### Step 4: Pattern detection

| Pattern | Flag when |
|---|---|
| **Legacy overfunding** | Low priority, disproportionate share |
| **Under-resourced growth bet** | Top-tier bet, bottom-quartile spend |
| **Under-differentiated allocation** | Flat spend despite wide priority spread |

Ask why for legacy overfunding — history is diagnosis, not justification.

### Step 5: Growth bets check

Cross-check `assess-growth-vectors` if run; else flag partial check.

### Step 6: Reallocation recommendation

Specific from→to moves with rationale — not vague "rebalance toward growth."

### Step 7: Portfolio committee gate

GATE before board/portfolio-committee finals.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
SCOPE: [units]
REVIEW FORUM: [working | portfolio committee | board]

LOAD-BEARING ASSUMPTIONS: [...]

ALLOCATION VIEW:
| Unit | Priority | Capital % | Headcount % | Attention | Flag |
...

UNDER-DIFFERENTIATION CHECK: [...]
GROWTH BETS CHECK: [...]

RECOMMENDED REALLOCATION:
| From | To | Type | Magnitude | Rationale |
...

STICKINESS NOTE: [...]
EVIDENCE GAPS: [...]
```

## Worked example

**Input:** Unit A priority tier 3 (exit candidate), 28% capital share; Unit B tier 1 adjacent bet, 8% capital.

**Excerpt:** Unit A flagged legacy overfunding; Unit B under-resourced growth bet. Reallocation: A −10% capital → B +10% `[review]` — adjacent bet cannot scale at current funding.

## Quality checks before delivering

- [ ] Profiles loaded or `[PROVISIONAL]`
- [ ] Priority not inferred from spend
- [ ] No invented figures
- [ ] Patterns named explicitly
- [ ] Reallocation specific from→to
- [ ] Growth bets checked where data exists

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Branches: supply missing data, portfolio committee memo, `exit-or-double-down` on legacy units, `assess-growth-vectors`, or set reallocation trigger date.
