---
name: instrument-metrics
description: >
  This skill should be used when the user asks to "instrument this KR,"
  "where does this metric actually come from," or needs each key result
  mapped to an exact, reproducible measurement spec — formula, source,
  owner, refresh cadence.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Instrument Metrics

Maps each key result to a measurement spec precise enough that two people would calculate the same number independently. This is the one skill in the plugin with a real cross-plugin seam — read the handoff note before producing output.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for whether `performance` is installed.

2. **If `performance` is installed**: this skill's job narrows to the KR-to-metric *mapping* only — which KR maps to which named metric — and the formal definition (exact formula, data source, owner, refresh cadence, caveats) is deferred to `performance:metrics-glossary`. Say so explicitly in the output rather than silently duplicating a definition that has a canonical home elsewhere.

3. **If `performance` is not installed** (or the metric is genuinely new and not yet in that glossary): define it fully here —
   - **Exact formula** — the literal calculation, not a description.
   - **Data source** — the actual system/sheet/table.
   - **Owner** — who's accountable for the number.
   - **Refresh cadence** — how often it updates, and whether that cadence is fast enough to support the check-in frequency from the practice profile (a KR checked-in weekly against a metric that only refreshes monthly is a mismatch worth flagging).
   - **Caveats** — anything that would make two people calculate it differently if unstated.

4. **Flag ambiguous formulas** rather than picking a calculation method silently — same discipline as `performance:metrics-glossary`, applied here for KRs that don't have a home there.

## Output format

```
KR: [text]

[If performance installed:]
  Mapped metric: [name] — full definition owned by performance:metrics-glossary
  Cadence match: [check-in frequency vs. metric refresh cadence — flag mismatch if any]

[If performance not installed, or metric is new:]
  Formula: [exact calculation]
  Source: [system/sheet/table]
  Owner: [name/role]
  Refresh: [cadence]
  Cadence match: [as above]
  Caveats: [...]

[repeat per KR]

AMBIGUITY FLAGS: [any KR where the metric admits more than one calculation method]
```
