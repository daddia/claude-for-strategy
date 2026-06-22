---
name: doc-reviewer
description: >
  This skill should be used when the user asks to "review this deck for
  structure," "critique this memo," "is this narrative tight," or provides an
  existing document or deck and wants a structural critique against pyramid
  and so-what discipline rather than a line edit or rewrite.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Doc Reviewer

Critique an existing deck or memo's structure against Minto discipline. This produces a structured critique, not a rewrite — the point is to give the user a sharp diagnostic they apply themselves, the same way a reviewing partner would mark up a draft rather than silently fix it.

## Trust spine

This review pass includes trust-discipline checks alongside pyramid structure. Full rules: `../../references/trust-conventions.md`.

```
SOURCING: Flag material numbers and external claims missing `[sourced: <where>]` or
  `[unverified — from training data, needs a real source]` tags.
ASSUMPTIONS: Flag load-bearing assumptions that are unstated, buried below the recommendation,
  or stated without impact-if-wrong — flag, don't fix.
NUMBERS: Flag invented inputs, placeholder metrics, or fake precision; should be INPUT NEEDED
  or explicitly unverified.
CONFIDENCE: Flag recommendation language when key inputs are unverified or missing; output should
  be labeled defensible recommendation vs structured first pass.
GATE: Flag board-/exec-facing finals produced without explicit confirmation and a reviewer note
  recording what wasn't verified.
```

## Process

1. **Read the full document first**, end to end, before critiquing anything — a structural review needs the whole shape, not a paragraph-by-paragraph read.

2. **Run the governing-thought test**: Is there a single, identifiable answer, and does it appear near the top? If the actual conclusion is buried, name where it currently sits and where it should move.

3. **Run the MECE test on the main supporting structure**: Are there 3-5 main points? Do any overlap? Is anything material missing? Call out specific points that overlap or specific gaps, not just "this could be tighter."

4. **Run the so-what test on supporting material**: Walk the major sections/slides and flag any that don't clearly trace back to a key line point — these are candidates to cut or demote to an appendix.

5. **Check title/heading discipline**: Are section headers and slide titles action titles stating a takeaway, or topic labels? Quote 2-3 specific examples of weak titles and what a stronger version would say, rather than a general comment.

6. **Check for grouping-logic mixing**: Does the document mix deductive and inductive structure within the same level without realizing it? Point to the specific spot.

7. **Run the trust-spine checks** (see block above): sourcing tags on material numbers and claims, load-bearing assumptions surfaced at the top, no invented inputs, honest confidence labeling, and a reviewer note on board-/exec-facing finals.

8. **Summarize as a structured critique**, ranked by how much each issue actually costs the reader (a buried governing thought matters more than an inconsistent exhibit label).

## Output format

```
GOVERNING THOUGHT TEST: [pass/fail + specifics]
MECE TEST: [pass/fail + specific overlaps or gaps]
SO-WHAT TEST: [sections/slides that don't earn their place]
TITLE DISCIPLINE: [specific weak titles + suggested stronger versions]
GROUPING LOGIC: [any mixing, with location]

TRUST SPINE:
SOURCING: [untagged material numbers/claims, with location]
ASSUMPTIONS: [hidden or unstated load-bearing assumptions]
NUMBERS: [invented inputs or fake precision]
CONFIDENCE: [recommendation language vs sourcing state]
GATE: [final without confirmation/reviewer note, if applicable]

PRIORITY FIXES (ranked):
1. ...
2. ...
3. ...
```

Do not rewrite the document as part of this skill — that's a separate request if the user wants it after seeing the critique.
