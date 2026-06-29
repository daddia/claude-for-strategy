---
name: deck-outline
description: >
  This skill should be used when the user asks to "outline a deck on X,"
  "what's the storyline for this deck," "build a slide-by-slide outline," or
  needs a presentation structured before any actual slide design happens.
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
# Deck Outline

## When to use

For consultants building a storyline-first, action-titled deck outline before slide design. Markdown outline only — hand off to presentation tools after approval.

## What this skill does not do

- **Does not build slides** — outline only; pptx or design tools after approval.
- **Does not invent narrative** without governing thought — route to `narrative-builder` if needed.
- **Does not rewrite source analysis** — maps pyramid to slides.

## Preconditions

| Input | If missing |
|---|---|
| Practice profile (slide title style, exhibits) | Proceed with action titles default; flag practice-setup |
| Governing thought / narrative | Ask to run `narrative-builder` first |

## Provisional mode

Thin narrative: label structured first pass; flag slides that don't trace to key line.

## Trust spine

- **Confidence bands** (`narrative-synthesis`): High = every slide traces to key line; Medium = some exhibit TBD; Low = topic list without governing thought — flag.
- **Analytical Rigor:** Every slide supports a key line point; cut or flag non-load-bearing slides.
- **Escalation:** Slide without key-line parent → flag or cut; board-final → gate + reviewer note.

Full rules: `../../references/trust-conventions.md`.

## Workflow

1. Read practice profile for slide title style and exhibit conventions.
2. Use `narrative-builder` output if available; else ask to build narrative first.
3. Map pyramid: governing thought slide → key line slides → supporting evidence (one exhibit per slide).
4. Action titles unless profile says descriptive.
5. Note exhibit per slide without building it.
6. So-what test per `minto-pyramid.md` — cut non-load-bearing slides.

## Output format

```
GOVERNING THOUGHT: [headline]

Slide 1 — [Action title]
  Exhibit: [...]
Slide 2 — [Action title for key line point 1]
  Exhibit: [...]
...
```

Flag slides that don't trace to a key line point.

## Worked example

**Input:** Governing thought: "Mid-tier price increase destroyed volume — revert pricing." Three MECE key lines.

**Excerpt:** Slide 1 action title states governing thought; Slides 2–4 map one key line each with exhibit notes (cohort chart, elasticity model, competitor scan).

## Quality checks before delivering

- [ ] Governing thought on slide 1, not "Overview"
- [ ] Action titles (unless profile overrides)
- [ ] Every slide traces to key line
- [ ] Trust spine applied to exhibit claims

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: approve outline → build slides, or `/consulting:so-what-sharpener` on weak titles.
