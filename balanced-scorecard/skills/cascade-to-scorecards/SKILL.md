---
name: cascade-to-scorecards
description: >
  This skill should be used when the user asks to "cascade the scorecard to
  business units," "build a team-level scorecard," or needs corporate
  strategy-map objectives translated into business-unit or team scorecards
  via a genuine causal-mechanism test, not just contribution-counting.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Cascade to Scorecards

The test here is stricter than a simple contribution check: a cascaded objective should be the *operational implementation* of a specific corporate-map objective, with its own plausible mechanism — not just "this BU does something related to that corporate goal." This skill also has to handle a real BSC-specific wrinkle that OKR cascading doesn't: cascaded scorecards legitimately need some objectives that don't trace upward at all.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for cascade levels and whether locally-owned objectives are expected to be healthy at cascaded levels.

2. **For each corporate-map objective relevant to this business unit/team, draft the cascaded version** as this unit's operational implementation — specific enough that it's clear what this unit would actually do differently, not a restatement with a new owner.

3. **State the mechanism** linking the cascaded objective to its corporate parent, same discipline as `build-strategy-map` — "this unit achieving X operationalizes the corporate objective Y because [mechanism]."

4. **Distinguish legitimate local objectives from disconnection.** A cascaded scorecard with a local-only objective (e.g. a plant's safety objective with no corporate-map equivalent) can be entirely appropriate — flag it as **local, not traced**, and don't treat that as a failure on its own. The actual failure modes to flag are at the extremes:
   - **Fully generic cascade** — every objective is a corporate objective copy-pasted with no local specificity or insight added; this unit isn't actually thinking, just inheriting.
   - **Fully disconnected** — most or all objectives are local with no traced link to the corporate map at all; this unit's scorecard isn't serving the corporate strategy in any visible way, which may be fine for a genuinely autonomous unit but should be a deliberate call, not a default.

5. **Run the coverage check upward**: does every corporate-map objective relevant to this unit have at least one cascaded objective addressing it? A corporate objective with no cascaded support at this level is a gap worth naming.

6. **If `okr` is also installed and layered beneath this plugin** per the practice profile, note explicitly that this skill's output is the BSC-layer cascade — the OKR-layer quarterly execution commitments underneath these objectives are `okr`'s job, not this skill's, to avoid producing two competing cascade structures for the same unit.

## Output format

```
BUSINESS UNIT: [name]

Cascaded from [corporate objective]:
  → [Cascaded objective] — Mechanism: [...]

Local objective (not traced to corporate map): [objective] — [why it belongs here]

CASCADE HEALTH CHECK: [fully generic / appropriately mixed / fully disconnected] — [explain]
COVERAGE GAPS: [corporate objectives relevant to this unit with no cascaded support]
```
