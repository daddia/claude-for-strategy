---
name: narrative-builder
description: >
  This skill should be used when the user asks to "build a narrative from
  these notes," "what's my storyline here," "structure this into a pyramid,"
  or provides raw findings, interview notes, or analysis output and wants it
  turned into a governing thought with supporting argument structure.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
  owner: "consulting practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Narrative Builder

## When to use

Turn raw input into Minto pyramid: governing thought, 3–5 MECE key line points, support bullets. See `../../references/minto-pyramid.md`.

## What this skill does not do

- **Does not produce prose memo/deck** — skeleton for `deck-outline` / `exec-memo`.
- **Does not paper over gaps** — flags unsupported governing thoughts.
- **Does not guess reader question** — ask if unclear.

## Preconditions

| Input | If missing |
|---|---|
| Raw findings/notes | Ask user to provide |
| Reader's real question | Ask before structuring |
| Practice profile | Default inductive; flag cold-start |

## Provisional mode

Thin input: governing thought flagged `[review]`; Known gaps section required.

## Trust spine

- **Analytical Rigor (mandatory):** Outline not prose; MECE gaps/overlaps named; grouping logic stated.
- Per `trust-conventions.md`.

## Workflow

1. Read practice profile.
2. State reader's question explicitly.
3. Draft governing thought (answer, not topic).
4. 3–5 MECE key line points; state deductive vs inductive.
5. Support sub-bullets with so-what test.
6. Flag structural problems in source — don't silently fix.

## Output format

```
GOVERNING THOUGHT: [...]

1. [Key line point 1]
   - [Support]
2. [...]

Grouping logic: [deductive | inductive] — [rationale]
Known gaps / flags: [...]
```

## Worked example

**Input:** Interview notes on pricing. Question: should we revert mid-tier increase?

**Excerpt:** Governing thought answers revert yes; three MECE key lines; gap flagged: no competitor primary research.

## Quality checks before delivering

- [ ] Governing thought is the answer
- [ ] MECE explicit
- [ ] Outline format, not paragraphs
- [ ] Gaps flagged

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `/consulting:deck-outline` or `/consulting:exec-memo`.
