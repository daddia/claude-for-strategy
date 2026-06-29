---
name: benefits-register
description: >
  This skill should be used when the user asks to "build the benefits
  register," "set baselines and owners for these benefits," "who's
  accountable for this benefit," or needs each mapped benefit turned
  into a formal register entry — baseline, target, owner, and
  realisation date — before tracking can begin.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "value-realisation practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Benefits Register

## When to use

Turn mapped benefits into register entries — baseline, target, owner distinct from delivery PM.

## What this skill does not do

- **Does not accept retrofitted baselines as clean** — RETROFITTED BASELINE flag carries forward.
- **Does not duplicate metric definitions** — hand off to `performance:metrics-glossary` when installed.

## Preconditions

| Input | If missing |
|---|---|
| `benefits-map` output | Ask user to map first or provide chain |
| Practice profile baseline discipline | Flag conservatively |

## Provisional mode

Owner same as PM → governance gap flag, not silent default.

## Trust spine

Structured-aggregation bands; baseline-before-change enforced; double-counting checked.

## Workflow

1. **Read the practice profile** — `~/.claude/plugins/config/claude-for-strategy/org-profile.md` and `~/.claude/plugins/config/claude-for-strategy/value-realisation/CLAUDE.md` — for the baseline-discipline answer from setup and the benefit type taxonomy, and read `benefits-map` output for the benefit chain being registered.

2. **For each benefit, capture**:
   - **Measure** — the exact formula, not a description. If `performance` is installed, hand off the formal metric definition to `performance:metrics-glossary` and reference it here rather than duplicating it — same seam pattern as `okr:instrument-metrics` and `balanced-scorecard:select-measures`. This skill owns the benefit-to-measure mapping, the baseline, and the accountability assignment, not the metric's formal definition.
   - **Baseline value, baseline date, and baseline source.**
   - **Target value and realisation date** — the date the benefit is expected to be *fully* realised, which is usually later than go-live; don't let the two dates collapse into one without asking.
   - **Benefit type** — carried forward from `benefits-map`.

3. **Enforce baseline-before-change, explicitly.** Compare the baseline date to the business change's go-live date (or planned go-live, if not yet live):
   - Baseline date clearly precedes go-live → clean.
   - Baseline date is on or after go-live, or no baseline exists and the change has already gone live → flag as **RETROFITTED BASELINE**. State plainly that this benefit's realisation claim is now compromised — any apparent improvement from this point can no longer be cleanly separated from improvement that may have already happened before measurement started. Don't record a retrofitted baseline as if it were a normal one; the flag should travel with this benefit into every later tracking cycle.

4. **Assign the benefit owner, and push back if the proposed owner is the delivery PM or project sponsor.** Ask who in the business actually inherits the changed way of working and will still be answerable for the number a year after the project team has disbanded. If the user has no good answer yet, record that explicitly as an open governance gap rather than defaulting to the PM by convenience — an unassigned or wrongly-assigned owner is the most common reason a benefit is never followed up after go-live.

5. **Check for double-counting** if registers from other initiatives are available or referenced — the same capacity or cost-line benefit claimed as cash savings in more than one business case at once. Flag any overlap found.

## Output format

```
BENEFIT: [name] — Type: [cash-releasing | cash-releasable | non-cash/qualitative]
  Measure: [exact formula, or "see performance:metrics-glossary"]
  Baseline: [value] as of [date] — Source: [system/extract/survey]
  Baseline check: [CLEAN — predates go-live] or [RETROFITTED — flag carries forward]
  Target: [value] by [realisation date] (go-live: [date], if different)
  Owner: [name/role] — [confirmed distinct from delivery PM] or
    [FLAG — same person as delivery PM/sponsor; governance gap]

[repeat per benefit]

DOUBLE-COUNTING FLAGS: [list, or "none"]
```

## Worked example

**Input:** Baseline dated after go-live.

**Expected output:** Baseline check: RETROFITTED — flag carries forward to all tracking cycles.

## Quality checks before delivering

- [ ] Baseline vs go-live checked per benefit
- [ ] Owner distinct from delivery PM or flagged
- [ ] Double-counting assessed

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `benefits-tracking`.
