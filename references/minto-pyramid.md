# The Minto Pyramid — Condensed Reference

The governing convention behind `narrative-builder`, `deck-outline`, `exec-memo`, and `doc-reviewer`. Other plugins' narrative-producing skills carry a short inline version of this; this file is the full version.

## The core structure

Every piece of structured communication is a pyramid:

1. **Governing thought** (top) — the single answer/recommendation/conclusion. One sentence. If the reader stops here, they have the point.
2. **Key line** (second level) — 3-5 supporting arguments that, together, are sufficient and necessary to prove the governing thought. These must be **MECE** — see `mece.md` for the full grouping discipline.
3. **Support** (third level and below) — the evidence, data, and sub-arguments backing each key line point. Each support set is itself MECE relative to its parent point.

The structure answers an implicit question-and-answer dialogue: the governing thought answers the reader's top-of-mind question; each key line point answers "why?" or "how?" the reader would ask next.

## Two ways to group the key line

- **Deductive (argument chain):** A, therefore B, therefore C, therefore the governing thought. Each point depends on the one before it. Use when the logic is genuinely causal/sequential.
- **Inductive (grouped by similarity):** Several independent points of the same kind (e.g. three reasons, three options, three risks) that jointly support the governing thought without depending on each other. Use this far more often — most business arguments are inductive ("three reasons to act now," not a logical proof chain).

Don't mix the two within one key line — pick one mode per level.

## The "so-what" test

Every bullet, sentence, and slide should pass: **if I delete this, does the reader lose something they needed?** If not, cut it. A list of true facts is not an argument; facts only earn a place in the pyramid when they support a point the reader needs in order to accept the level above.

Apply at every level:
- Does this **governing thought** actually answer the reader's question, or just describe the situation?
- Does each **key line point** add a genuinely distinct reason, or restate another point in different words?
- Does each piece of **support** prove its parent point, or just relate to the same general topic?

## Top-down construction order

Build pyramids top-down even though the underlying analysis was bottom-up:

1. Start with the question the reader actually has (not the question you investigated).
2. State the answer — the governing thought — as if you already know it. (You usually do, by the time you're writing it up; if you don't, that's a sign the analysis isn't finished, not a reason to write around it.)
3. Anticipate the "why?" or "how?" the reader will ask next — that's your key line.
4. For each key line point, anticipate the next "why?" — that's your support.

## Common failure modes to flag in review

- **Buried governing thought** — conclusion appears on slide 12, or in the last paragraph of a memo.
- **Non-MECE key line** — points overlap, or a point is really two points jammed together, or something material is missing.
- **Topic titles, not action titles** — a slide titled "Market Overview" instead of "The market is consolidating around three players, none of which is us."
- **Evidence presented before the point it supports** — chronological/process narrative ("first we did X, then we found Y, then Z") instead of argument-led structure.
- **Mixed grouping logic within one level** — three deductive steps and one unrelated inductive point at the same level.

## Quick self-check before delivering any narrative output

1. Can the governing thought stand alone as the answer to the reader's real question?
2. Are there 3-5 key line points, genuinely MECE?
3. Does every piece of support pass the so-what test against its parent?
4. Would a skim of just the top two levels be enough for a time-pressed reader to act?
