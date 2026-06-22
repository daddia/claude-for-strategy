---
name: define-perspectives
description: >
  This skill should be used when the user asks to "define our perspectives,"
  "set up our scorecard structure," "should we use the standard four
  perspectives," or needs to decide the perspective set and causal-chain
  order before any objectives get drafted.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Define Perspectives

The real decision here isn't naming four boxes — it's deciding which perspective sits at the top of the causal chain, because that's the perspective every other objective in the map ultimately has to serve. Get this wrong and the whole map optimizes toward the wrong end state.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for sector.

2. **Confirm or set the top perspective explicitly**:
   - For-profit, no unusual mission constraint: standard order, Financial at the top — Learning & Growth and Internal Process are means; Customer and Financial are ends, with Financial as the ultimate end.
   - Mission-driven (nonprofit, public sector, or a for-profit with an explicit non-financial primary mandate): propose relocating Financial to an enabling/stewardship perspective ("Financial Sustainability" — how the org funds itself to keep delivering) and putting a Mission or Stakeholder Impact perspective at the top instead. State this explicitly as a structural change, not a renaming — the causal logic flows differently, not just the label.
   - If genuinely ambiguous (e.g. a B-corp with real financial and mission mandates both claimed as primary), say so and ask which one the organization would sacrifice the other for under real pressure — that answer reveals the actual top perspective, regardless of stated values.

3. **Set the full perspective list and order**, four perspectives by default. Use standard names (Financial/Mission, Customer, Internal Process, Learning & Growth) unless the org's own vocabulary clarifies the causal logic better — if proposing a rename, state what causal role the renamed perspective plays so it's clear the rename isn't just cosmetic.

4. **Resist a fifth perspective** if proposed (e.g. "Sustainability," "Risk," "Innovation" as standalone perspectives) — check first whether it can be folded into an existing perspective without losing anything. A fifth perspective dilutes the discipline of forcing trade-offs across a fixed structure; only keep it if the user can articulate why it can't live inside Internal Process or Learning & Growth and still make the case.

5. **Output the perspective set with the causal order made explicit** — this becomes the direct input to `build-strategy-map`.

## Output format

```
SECTOR: [for-profit | nonprofit | public sector | hybrid]

PERSPECTIVES (top of causal chain first):
1. [Name] — [its causal role: the ultimate end this map serves]
2. [Name] — [causal role: what it must produce to serve #1]
3. [Name] — [causal role: what it must produce to serve #2]
4. [Name] — [causal role: the foundational enabler]

RENAMES APPLIED: [any, with the causal-clarity rationale]
FIFTH-PERSPECTIVE REQUEST: [none, or what was proposed and why it was/wasn't folded in]
```
