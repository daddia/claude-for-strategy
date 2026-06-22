---
name: workplan-builder
description: >
  This skill should be used when the user asks to "turn this into a workplan,"
  "build a hypothesis-driven workplan," "who's doing what on this analysis,"
  or has a hypothesis tree (from this plugin or elsewhere) that needs owners,
  timelines, and data sources attached.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Workplan Builder

Translate a hypothesis tree into an executable workplan: one row per sub-hypothesis, with the analysis needed, the data source, an owner, a timeline, and the expected so-what restated so it can be checked against the actual result later.

## Process

1. **Get the hypothesis tree.** If the user hasn't provided one, ask whether to run `hypothesis-tree` first or whether they're supplying their own structure directly.

2. **For each sub-hypothesis, populate the workplan row**:
   - **Hypothesis** — carried over verbatim from the tree.
   - **Analysis** — the specific method (not just "analyze the data" — name the actual technique: a cohort comparison, a sensitivity model, a structured interview set).
   - **Data source** — where the evidence actually comes from. If unknown, flag it rather than inventing a plausible-sounding source.
   - **Owner** — ask if not supplied; don't assign names without confirmation.
   - **Timeline** — ask for real constraints (a steering committee date, a sprint boundary) rather than defaulting to an arbitrary number of days.
   - **Expected so-what** — carry over from the tree. This is written *before* the analysis runs, deliberately, so the actual result can be checked against it afterward.

3. **Sanity-check effort against payoff.** If a row's analysis looks disproportionately heavy relative to its expected so-what, flag it — that's usually a sign the hypothesis tree needs revisiting, not that the workplan should just proceed as drafted.

4. **Output as a table**, ready to drop into a tracker or deck.

## Output format

| Hypothesis | Analysis | Data source | Owner | Timeline | Expected so-what |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

Flag any row where effort looks disproportionate to payoff, and any row missing a confirmed owner, timeline, or data source — don't silently fill these with placeholders.
