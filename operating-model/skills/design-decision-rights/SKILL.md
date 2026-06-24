---
name: design-decision-rights
description: >
  This skill should be used when the user asks to "build a RACI," "who
  actually owns this decision," "clarify decision rights," or has a
  decision or process that needs explicit roles assigned with
  single-point-accountability enforced.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "operating-model practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Design Decision Rights

## When to use

Assign RACI/RAPID roles with exactly one Accountable per decision — enforce single-point accountability and flag Consulted bloat.

## What this skill does not do

- **Does not diagnose structure fit** — route to `/operating-model:diagnose-structure-fit`.
- **Does not resolve political ownership** — forces a choice; strategist decides.
- **Does not implement governance systems** — produces artifact for adoption.

## Preconditions

| Input | If missing |
|---|---|
| Decisions or processes in scope | Ask user to list |
| Practice profile (RACI vs RAPID convention) | Default RACI; flag `[PROVISIONAL]` |
| Named roles/parties for assignment | Ask; halt if decisions unnamed |

## Provisional mode

Multiple Accountable proposed: flag diffused accountability; do not finalize until single owner chosen or explicitly `[review]`.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Every decision has exactly one Accountable; bloat flags applied.
  - **Medium:** Some ownership gaps with recommended owners.
  - **Low:** Zero Accountable on key decisions — halt output until resolved.
- **Failure modes:**
  - **Strategic advice vs. support:** Assignments are draft for exec confirmation.
  - **Client confidentiality:** RACI may expose sensitive authority lines — CONFIDENTIAL header.
  - **Accountability gap:** "Shared ownership" rejected; forces single Accountable.
  - **Analytical Rigor:** MECE decision coverage in scope.
  - **Incentive Gaming:** Consulted bloat flagged as latency/gaming risk.
- **Escalation triggers:** Unowned decisions found — name specifically, do not defer.

## Workflow

1. **Read practice profile** for decision-rights gaps and house convention.
2. **Assign roles** per decision — R/A/C/I or RAPID equivalent.
3. **Enforce exactly one Accountable** — stop if zero; flag if multiple.
4. **Check Consulted bloat** — long lists that slow decisions materially.
5. **Find unowned decisions** — no claimed owner during exercise.
6. **Completeness check** before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
DECISION: [name]
  Accountable: [single name/role — flag if zero or multiple initially proposed]
  Responsible: [...]
  Consulted: [...] — Bloat flag: [if applicable]
  Informed: [...]

[repeat per decision]

UNOWNED DECISIONS FOUND: [list or none]
```

## Worked example

**Input:** "Product pricing changes" — Accountable: Product VP and Finance VP.

**Expected output (excerpt):**

```
DECISION: Product pricing changes
  Accountable: FLAG — multiple proposed (Product VP, Finance VP); force choice [review]
UNOWNED DECISIONS FOUND: none
```

## Quality checks before delivering

- [ ] Exactly one Accountable per decision (or explicit flag)
- [ ] Consulted bloat assessed
- [ ] Unowned decisions listed
- [ ] House convention (RACI/RAPID) applied
- [ ] Output does not read as final governance policy

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: exec workshop to resolve flags, socialize artifact, or `stress-test-matrix-reporting`.
