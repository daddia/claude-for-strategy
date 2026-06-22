---
name: deck-outline
description: >
  This skill should be used when the user asks to "outline a deck on X,"
  "what's the storyline for this deck," "build a slide-by-slide outline," or
  needs a presentation structured before any actual slide design happens.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Deck Outline

Produce a storyline-first, action-titled deck outline — one sentence per slide stating its takeaway, governing thought up front, exhibit notes per slide. This is a markdown outline, not slides; if the user wants the actual deck built out, hand off to a presentation-building skill (e.g. the pptx skill, if installed) once the outline is approved.

## Trust spine

```
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent an input — flag what's needed instead.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

Full rules: `../../references/trust-conventions.md`.

## Process

1. **Read the practice profile** (`~/.claude/plugins/config/claude-for-strategy/consulting/CLAUDE.md`) for slide title style (action vs. descriptive), exhibit-numbering convention, and house template notes.

2. **Get or build the narrative.** If the user has already run `narrative-builder`, use that output directly. If not, ask whether to build the narrative first — a deck outline without an underlying governing thought and MECE key line just becomes a topic list.

3. **Map the pyramid to slides**:
   - **Slide 1 (or an executive summary slide):** the governing thought, stated as the headline, not a section header like "Overview."
   - **One slide (or small slide group) per key line point**, in the order that best serves the argument — usually the order of the key line itself.
   - **Supporting slides underneath each key line point** carry the evidence — one core exhibit or argument per slide, not a slide doing double duty.

4. **Write every slide title as an action title** (states the takeaway: "Three players now control 80% of volume" not "Market Overview"), unless the practice profile specifies descriptive titles.

5. **Note the exhibit for each slide** — what chart, table, or evidence it needs — without building the exhibit itself; that's a separate step once the outline is approved.

6. **Run the so-what test on every slide** (see `../../references/minto-pyramid.md`): if a slide doesn't support a key line point, cut it or flag it as "nice to have, not load-bearing."

## Output format

```
GOVERNING THOUGHT: [headline]

Slide 1 — [Action title for governing thought / executive summary]
  Exhibit: [none, or what it shows]

Slide 2 — [Action title for key line point 1]
  Exhibit: [...]
Slide 3 — [Action title, supporting evidence for point 1]
  Exhibit: [...]

Slide N — [Action title for key line point 2]
  ...
```

Flag any slide that doesn't clearly trace back to a key line point.
