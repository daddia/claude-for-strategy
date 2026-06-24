---
name: synergy-stress-test
description: >
  This skill should be used when the user asks to "stress-test these
  synergies," "is this deal's synergy case realistic," or has a deal or
  partnership's projected synergies that need cost/revenue separation,
  evidence checks, and a base-rate haircut.
allowed-tools: Read, Grep, Glob, Write
metadata:
  version: "0.3.0"
  owner: "corporate-strategy practice"
  review_cadence: "quarterly"
  work_shape: "hypothesis-driven-analysis"
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Synergy Stress Test

## When to use

Stress-test deal synergies — separate cost vs revenue, grade evidence, apply haircuts, bar-test deal economics. Revenue synergies must not borrow credibility from cost lines.

## What this skill does not do

- **Does not blend cost and revenue lines.**
- **Does not invent deal economics** — INPUT NEEDED for price/hurdle.
- **Does not approve deal** — recommendation on adjusted case.
- **Does not skip mechanism check on revenue.**

## Preconditions

| Input | If missing |
|---|---|
| Synergy line items | Ask user or deck |
| Profile synergy haircut / track record | Use default base-rate table; cite source |
| Purchase price / hurdle for bar test | INPUT NEEDED — no fabricated IRR |

## Provisional mode

Default haircuts tagged `[unverified — industry pattern]` unless profile has org track record.

## Trust spine

- **Analytical Rigor (mandatory):** Per-line tier, haircut arithmetic, double-count scan.
- Per trust-conventions; GATE before board finals.

## Base-rate anchor

| Type | Typical realization |
|---|---|
| Cost strong evidence | ~70–90% |
| Cost weak | ~40–60% |
| Revenue any tier | ~20–40% |

Use profile overrides when configured.

## Workflow

1. Separate every line: cost vs revenue.
2. Grade evidence per line; state tier, haircut %, adjusted value.
3. Revenue mechanism check — missing mechanism → Weak.
4. Double-counting scan.
5. Recompute totals; bar test at adjusted number.

## Output format

```
CONFIDENCE: [...]
COST SYNERGIES: [table]
REVENUE SYNERGIES: [table]
DOUBLE-COUNTING FLAGS: [...]
TOTALS: [...]
DEAL BAR TEST: [...]
RECOMMENDATION: [...]
```

## Worked example

**Input:** $30M cost synergy (generic 10% G&A) + $50M revenue cross-sell (no mechanism).

**Excerpt:** Cost weak → ~50% haircut; revenue Weak → ~80% haircut; only works at optimistic number — material finding.

## Quality checks before delivering

- [ ] No blended lines
- [ ] Every line tier + arithmetic
- [ ] Revenue without mechanism = Weak
- [ ] Double-count scan done
- [ ] Bar test plain if optimistic-only

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: renegotiate, `evaluate-strategic-option`, or IC with cost-only case.
