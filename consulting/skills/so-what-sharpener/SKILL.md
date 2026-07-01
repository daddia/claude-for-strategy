---
name: so-what-sharpener
description: >
  This skill should be used when the user asks "what's the so-what here,"
  "sharpen this insight," "this is just facts, what does it mean," or
  provides a list of observations or data points that need to be turned into
  insight statements.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "consulting practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# So-What Sharpener

## When to use

Sharpen observations into insight via observation → implication → insight chain. Smallest Minto unit before full narrative.

## What this skill does not do

- **Does not skip implication step** — catches lazy insights.
- **Does not force insight on non-load-bearing facts** — "No insight earned" section.
- **Does not build full pyramid** — use `narrative-builder` for that.

## Preconditions

| Input | If missing |
|---|---|
| Observations or data points | Ask user to list |
| Decision context | Ask what decision insights must support |

## Provisional mode

Missing decision context: implications literal only; insights tagged `[review]`.

## Trust spine

- **Analytical Rigor (mandatory):** Explicit three-step chain per point; merge redundant insights.
- Per `trust-conventions.md` on tagged figures in observations.

## Workflow

For each observation:
1. State observation unchanged.
2. State implication (literal).
3. State insight (so-what for decision).
4. Flag observations with no earned insight.
5. Group and merge overlapping insights.

## Output format

```
Observation: [...]
  → Implication: [...]
  → Insight: [...]

No insight earned: [...]
```

## Worked example

**Input:** "Mid-tier ARPU down 12% QoQ." Decision: pricing revert?

**Excerpt:** Implication: mid-tier spending less; Insight: increase likely priced out intended segment — reconsider pricing `[review]`.

## Quality checks before delivering

- [ ] Three-step chain per point
- [ ] No insight earned section when applicable
- [ ] Overlaps merged

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/consulting/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/consulting:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `/consulting:narrative-builder` to assemble insights.
