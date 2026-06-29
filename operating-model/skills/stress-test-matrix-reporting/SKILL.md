---
name: stress-test-matrix-reporting
description: >
  This skill should be used when the user asks "does our matrix structure
  actually work," "who wins when the two bosses disagree," "is this matrix
  reporting relationship viable," or has a dual-reporting relationship that
  needs a tie-breaker rule checked or forced into the open.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "operating-model practice"
  review_cadence: "quarterly"
  work_shape: "governance-tracking"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Stress-Test Matrix Reporting

## When to use

Force tie-breaker rules into the open for dual-reporting relationships — before first real boss disagreement.

## What this skill does not do

- **Does not eliminate matrix** — assesses viability and recommends tie-breakers.
- **Does not assign RACI** — route to `/operating-model:design-decision-rights`.
- **Does not diagnose full structure** — route to `/operating-model:diagnose-structure-fit`.

## Preconditions

| Input | If missing |
|---|---|
| Matrix relationships (role, Boss A, Boss B) | Ask user to list |
| Practice profile tie-breaker rules | Compare against user input |
| Role-holder awareness of rules | Ask if unknown — flag undocumented |

## Provisional mode

Smooth history with no tie-breaker: still flag **latent landmine** — untested ≠ safe.

## Trust spine

- **Confidence bands** (`governance-tracking`):
  - **High:** Every matrix relationship assessed; tie-breaker status and origin check complete.
  - **Medium:** Some rules undocumented but inferable — flag for formalization.
  - **Low:** Relationships unnamed — halt.
- **Failure modes:**
  - **Strategic advice vs. support:** Recommended tie-breakers are draft for both bosses and HR.
  - **Client confidentiality:** Reporting lines politically sensitive — CONFIDENTIAL header.
  - **Accountability gap:** Missing tie-breaker flagged as landmine, not smoothed over.
  - **Analytical Rigor:** N/A — governance shape.
  - **Incentive Gaming:** Origin check catches compromise-matrix adopted to avoid choosing organizing principle.
- **Escalation triggers:** No tie-breaker on active matrix — recommend specific default before next disagreement.

## Workflow

1. **Read practice profile** for matrix relationships and tie-breaker rules.
2. **Per dual-reporting relationship:** who wins when bosses disagree?
3. **Confirm rule is written and known** to matrixed role-holder.
4. **Origin check** — genuine dual need vs. unresolved compromise between organizing principles.
5. **Recommend tie-breaker** where missing — default winner and escalation path.
6. **Gaming-pattern check** before output: compromise matrices named.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
MATRIXED ROLE: [name/role]
  Boss A: [...] — Boss B: [...]
  Tie-breaker: [exists and known | exists but unknown — flag | does not exist — landmine]

ORIGIN CHECK: [genuine dual coordination need | unresolved compromise — name which]

RECOMMENDED TIE-BREAKER (where missing): [who wins by default, escalation path]

[repeat per relationship]
```

## Worked example

**Input:** Regional sales lead reports to Regional VP and Global Product VP; no written tie-breaker; smooth 2 years.

**Expected output (excerpt):**

```
Tie-breaker: does not exist — flag as latent landmine
ORIGIN CHECK: unresolved compromise between geography and product organizing principles [review]
RECOMMENDED TIE-BREAKER: Product VP wins on roadmap priorities; Regional VP wins on local pricing [review]
```

## Quality checks before delivering

- [ ] Every matrix relationship in scope covered
- [ ] Tie-breaker status assessed (including undocumented)
- [ ] Origin check completed
- [ ] Recommended tie-breaker specific where missing
- [ ] Gaming-pattern check run

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: exec alignment session, update practice profile, or `design-decision-rights`.
