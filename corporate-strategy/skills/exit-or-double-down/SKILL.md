---
name: exit-or-double-down
description: >
  This skill should be used when the user asks "should we exit this
  business," "is this worth continuing to fund," "do a portfolio pruning
  review," or needs an explicit exit/hold/double-down call on a unit —
  with sunk-cost reasoning named directly when it appears.
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
# Exit or Double Down

## When to use

Portfolio pruning — explicit exit/hold/double-down with blank-page test first and sunk-cost reasoning named when it appears.

## What this skill does not do

- **Does not treat sunk cost as forward evidence** — quoted and set aside.
- **Does not default to HOLD** — requires justification + kill criteria.
- **Does not invent financials** — INPUT NEEDED.
- **Does not name vague approver** — routing per profile.

## Preconditions

| Input | If missing |
|---|---|
| Org + corporate-strategy profiles | cold-start or `[PROVISIONAL]` |
| Unit scope and decision forum | Ask |

## Provisional mode

Generic exit criteria; `[PROVISIONAL]` on thresholds.

## Trust spine

- **Strategic advice vs. support (mandatory):** CALL is recommendation; named forum approves.
- Per trust-conventions; GATE before board/IC finals.

## Workflow

1. Orient — unit, forum, evidence, time pressure.
2. **Blank-page test first** — enter today at this investment?
3. Sunk-cost detection — quote patterns, set aside.
4. Exit criteria check — structural decline, capital destruction, growth odds.
5. Double-down criteria — position, leadership path, under-resourcing.
6. CALL: EXIT | HOLD | DOUBLE DOWN — forward rationale only.
7. Kill criteria if HOLD.
8. Approval routing per profile.
9. GATE if board-ready.

## Output format

```
CONFIDENCE: [...]
UNIT: [...]
BLANK-PAGE TEST: [...]
SUNK-COST CHECK: [...]
EXIT CRITERIA: [table]
DOUBLE-DOWN CRITERIA: [table]
CALL: [...]
KILL CRITERIA (if HOLD): [...]
APPROVAL ROUTING: [...]
```

## Worked example

**Input:** Legacy print unit, "we've spent $200M already" cited.

**Excerpt:** Blank-page: no. Sunk-cost quoted and set aside. EXIT criteria met on structural decline; CALL EXIT `[review]`.

## Quality checks before delivering

- [ ] Blank-page before other evidence
- [ ] Sunk cost named if present
- [ ] Hold justified with kill criteria
- [ ] Approver named

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: IC exit case, `allocate-resources` for double-down sizing.
