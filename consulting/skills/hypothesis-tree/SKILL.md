---
name: hypothesis-tree
description: >
  This skill should be used when the user asks to "build a hypothesis tree,"
  "structure this as an issue tree," "what are our hypotheses for X," or
  presents a problem statement that needs to be broken into falsifiable
  sub-hypotheses before analysis starts.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "consulting practice"
  review_cadence: "quarterly"
  work_shape: "hypothesis-driven-analysis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Hypothesis Tree

## When to use

Break a problem into falsifiable root and MECE sub-hypotheses before analysis. See `../../references/hypothesis-driven-approach.md`.

## What this skill does not do

- **Does not run analysis** — names evidence needed; `workplan-builder` executes.
- **Does not use topic labels as nodes** — every node falsifiable.
- **Does not keep branches with no so-what either direction** — cut and list.

## Preconditions

| Input | If missing |
|---|---|
| Problem as question | Restate and confirm before tree |
| Root hypothesis ambiguity | Present both roots; ask which to build |

## Provisional mode

Uncertain root: two candidate roots with user choice; label structured first pass.

## Trust spine

- **Analytical Rigor (mandatory):** MECE sub-hypotheses; evidence-needed per branch; cut branches listed.
- **Confidence bands** (`hypothesis-driven-analysis`): High = triangulated evidence plan; Medium = single source; Low = assumption-driven — label load-bearing assumption.
- Per `trust-conventions.md` for sourcing, numbers, gate.

## Workflow

1. Restate problem as question; confirm.
2. Propose falsifiable root hypothesis.
3. 3–5 MECE sub-hypotheses.
4. Smallest evidence test per sub-hypothesis.
5. So-what if TRUE and if FALSE; cut if neither matters.
6. Output as tree.

## Output format

```
ROOT HYPOTHESIS: [falsifiable claim]

1. [Sub-hypothesis 1]
   Evidence needed: [...]
   If TRUE: [...]
   If FALSE: [...]
...

Cut branches: [...]
```

## Worked example

**Input:** "Why did mid-tier churn spike?"

**Excerpt:** Root: price increase caused mid-tier churn. Sub-hypothesis: elasticity >15% in segment; evidence: cohort comparison Q1 vs Q4.

## Quality checks before delivering

- [ ] Falsifiable nodes only
- [ ] MECE check explicit
- [ ] Cut branches documented
- [ ] Handoff-ready for workplan-builder

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `/consulting:workplan-builder`.
