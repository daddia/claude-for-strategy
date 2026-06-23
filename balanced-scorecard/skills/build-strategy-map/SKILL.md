---
name: build-strategy-map
description: >
  This skill should be used when the user asks to "build our strategy map,"
  "draft objectives for the scorecard," "what's our causal chain," or has
  candidate objectives that need an explicit causal mechanism linking each
  one to the perspective above it — the actual intellectual core of a
  balanced scorecard, not just objectives sorted into four boxes.
work_shape: structured-aggregation
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Build Strategy Map

A strategy map without stated mechanisms is just four lists with arrows drawn out of habit. The discipline this skill enforces: every objective must state, in causal language, *why* achieving it would produce the effect claimed in the perspective above — "if we achieve X, we expect Y because [mechanism]," not just an arrow pointing upward.

## Trust spine

```
ANALYTICAL RIGOR: Every upward link requires a stated mechanism ("because …") or
  is tagged UNVALIDATED — do not supply plausible-sounding causal prose on the
  user's behalf. Orphan objectives, unfunded mandates, and redundant objectives
  within a perspective are listed explicitly in the output block, not hidden
  behind clean-looking arrows.
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent an input — flag what's needed instead.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

Full rules: `../../references/trust-conventions.md` (consulting plugin) or repo-root `references/trust-conventions.md`.

## Process

1. **Get the perspective order** from `define-perspectives` (or the practice profile if already set).

2. **Draft 2-4 objectives per perspective**, starting from the top perspective and working down, OR starting from the bottom and working up — either is fine, but the causal link must be tested in the upward direction regardless of drafting order: does this objective, if achieved, plausibly cause the effect claimed above it.

3. **For every objective below the top perspective, require an explicit mechanism statement**: "Achieving [this objective] is expected to drive [objective above] because [the actual causal reasoning — not just 'it's related']." If the user can't state a mechanism, don't supply a plausible-sounding one on their behalf — flag the link as an **unvalidated arrow of faith** and carry it forward to `review-and-validate`, where it gets tested against real data rather than asserted now.

4. **Check for orphan objectives** — an objective in a lower perspective with no stated upward link to anything. Ask what it's actually for; either it's missing its mechanism statement, or it doesn't belong in this map (it may be operationally important without being *strategically* mapped here).

5. **Check for unfunded mandates** — an objective at or near the top with no objective beneath it plausibly driving it. A Financial or Mission objective with nothing in Customer, Internal Process, or Learning & Growth supporting it is a wish, not a strategy.

6. **Check for over-stuffing within a perspective** — more than ~4 objectives in one perspective usually means some should be merged or demoted to initiatives (see `set-targets-and-initiatives`) rather than carried as top-level strategic objectives.

7. **Check for redundancy within a perspective** — two objectives that are really the same thing in different words; merge them.

8. **Persist the map** to the location recorded in the practice profile (`~~whiteboard`, a doc, or this plugin's `data/`) — this is a living artifact other skills read from, not a one-off output.

## Output format

```
PERSPECTIVE: [top perspective name]
  Objective: [text]
  Objective: [text]

PERSPECTIVE: [next perspective name]
  Objective: [text]
    → Drives: [objective above] — Mechanism: [stated causal reasoning] or
      [UNVALIDATED — no mechanism stated; flagged for review-and-validate]
  Objective: [text]
    → Drives: ...

[repeat down through perspectives]

ORPHAN OBJECTIVES: [any with no upward link, and why they're in the map anyway, or a
  recommendation to remove]
UNFUNDED MANDATES: [any top-perspective objective with no real support beneath it]
OVER-STUFFED / REDUNDANT: [any perspective flagged, with the merge/demote suggestion]
```
