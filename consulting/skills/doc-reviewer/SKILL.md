---
name: doc-reviewer
description: >
  This skill should be used when the user asks to "review this deck for
  structure," "critique this memo," "is this narrative tight," or provides an
  existing document or deck and wants a structural critique against pyramid
  and so-what discipline rather than a line edit or rewrite.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
  owner: "consulting practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Doc Reviewer

## When to use

When the user wants a structured structural critique of an existing deck or memo — partner-style markup, not a rewrite.

## What this skill does not do

- **Does not rewrite the document** — critique only; rewrite is separate request.
- **Does not line-edit prose** — pyramid, MECE, so-what, trust spine.
- **Does not approve for external send** — flags gate issues; user decides.

## Preconditions

| Input | If missing |
|---|---|
| Full document readable end-to-end | Report read failure; do not partial-critique |

## Provisional mode

Partial read (large doc): record coverage in reviewer note; critique only read sections.

## Trust spine

- **Confidence bands** (`narrative-synthesis`): High = full doc read, ranked fixes; Low = partial read flagged.
- **Analytical Rigor:** MECE and governing-thought tests with specific locations, not generic "tighten up."
- **Escalation:** Buried governing thought → priority fix #1; recommendation without sourcing → CONFIDENCE flag.

```
SOURCING / ASSUMPTIONS / NUMBERS / CONFIDENCE / GATE — per trust-conventions.md
```

## Workflow

1. Read full document end to end.
2. Governing-thought test — location of actual conclusion.
3. MECE test — overlaps and gaps, specific.
4. So-what test — sections that don't earn place.
5. Title discipline — quote 2–3 weak titles + stronger versions.
6. Grouping-logic mixing — name location.
7. Trust-spine checks.
8. Rank priority fixes by reader cost.

## Output format

```
GOVERNING THOUGHT TEST: [pass/fail + specifics]
MECE TEST: [pass/fail + specifics]
SO-WHAT TEST: [...]
TITLE DISCIPLINE: [...]
GROUPING LOGIC: [...]
TRUST SPINE: [sourcing, assumptions, numbers, confidence, gate]
PRIORITY FIXES (ranked): 1. ... 2. ... 3. ...
```

## Worked example

**Input:** Memo with recommendation in paragraph 4, topic slide titles, untagged $50M claim.

**Excerpt:** GOVERNING THOUGHT TEST: fail — conclusion paragraph 4, should be line 1. SOURCING: $50M revenue claim slide 7 untagged.

## Quality checks before delivering

- [ ] Full doc read (or coverage stated)
- [ ] No rewrite included
- [ ] Fixes ranked by impact
- [ ] Specific quotes/locations, not generic advice

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: user applies fixes, or request rewrite via `narrative-builder` / `exec-memo`.
