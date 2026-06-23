---
name: narrative-builder
description: >
  This skill should be used when the user asks to "build a narrative from
  these notes," "what's my storyline here," "structure this into a pyramid,"
  or provides raw findings, interview notes, or analysis output and wants it
  turned into a governing thought with supporting argument structure.
work_shape: narrative-synthesis
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Narrative Builder

Turn raw input (notes, findings, analysis output, a brain-dump) into a Minto-structured narrative: one governing thought, 3-5 MECE key line points, and supporting evidence underneath each. Full method in `../../references/minto-pyramid.md` — read it before producing output if this is the first invocation in the session.

## Trust spine

```
ANALYTICAL RIGOR: Output is a structured outline — governing thought, 3–5 MECE key
  line points, support sub-bullets — not prose paragraphs. Overlap and gaps in MECE
  coverage are named explicitly in Known gaps / flags, not smoothed over with
  confident narrative. Grouping logic (deductive vs inductive) is stated so the
  reader can audit the argument structure rather than accept a polished storyline.
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

1. **Read the practice profile** (`~/.claude/plugins/config/claude-for-strategy/consulting/CLAUDE.md`) for the user's default audience, tone, and whether they prefer deductive or inductive grouping. If the profile is still the unfilled template, proceed with inductive/bucketed grouping as the default and flag once at the end that running the cold-start interview would sharpen future output.

2. **Identify the reader's real question.** Before structuring anything, state explicitly what question the reader has that this narrative needs to answer. If the input doesn't make this obvious, ask — don't guess and proceed on a wrong question.

3. **Draft the governing thought first**, even though the underlying analysis was done bottom-up. One sentence. It should be the answer, not a description of the topic or the process used to get there.

4. **Group the supporting points into 3-5 MECE key line points.** Check explicitly for overlap (cut or merge) and gaps (add or flag as a known gap). State which grouping logic was used (deductive or inductive) and why, if not obvious.

5. **Attach support to each key line point**, applying the so-what test from `../../references/minto-pyramid.md`: every piece of evidence either proves its parent point or gets cut.

6. **Output as a structured outline**, not prose paragraphs — governing thought at the top, key line points as a numbered list, support as sub-bullets. This is meant to be the skeleton other skills (`deck-outline`, `exec-memo`) or the user's own drafting build on top of.

7. **Flag, don't silently fix, structural problems** in the source material — if the input doesn't actually support a clean governing thought, or if there's a genuine gap in the MECE coverage, say so explicitly rather than papering over it.

## Output format

```
GOVERNING THOUGHT: [one sentence — the answer]

1. [Key line point 1]
   - [Support]
   - [Support]
2. [Key line point 2]
   - [Support]
3. [Key line point 3]
   - [Support]

Grouping logic: [deductive | inductive] — [one-line rationale]
Known gaps / flags: [anything the input didn't fully support]
```
