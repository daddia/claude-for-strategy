# operating-model

Org design and decision rights.

## Components

| Command | What it does |
|---|---|
| `/operating-model:cold-start-interview` | Learns current structure, strategic priority it's meant to serve, known decision-rights gaps, reward mechanics |
| `/operating-model:diagnose-structure-fit` | Tests whether the structure actually matches the coordination need the strategy requires; flags "organized around the current leader's chart" |
| `/operating-model:design-decision-rights` | Builds a RACI/RAPID matrix and enforces single-point accountability — flags zero-A and multi-A decisions, flags R/C bloat |
| `/operating-model:check-span-and-layers` | Diagnoses span of control and layer count against known patterns for over- and under-management |
| `/operating-model:stress-test-matrix-reporting` | Forces an explicit tie-breaker for every dual-reporting relationship; flags matrix-as-unresolved-compromise |
| `/operating-model:align-rewards-and-incentives` | Star Model check — does the reward system reinforce or undermine the structure's intent; checks process and people fit too |

## The skill that matters most: `align-rewards-and-incentives`

Structure changes are cheap to draw and expensive to make real. This skill exists because the most common reorg failure isn't a bad org chart — it's a new org chart sitting on top of an unchanged reward system that quietly pays people to behave like the old structure still exists.

## Setup

Run `/operating-model:cold-start-interview` first. The "what is the structure meant to optimize for" question matters most — `diagnose-structure-fit` can't assess fit without a real answer to compare against.

## Usage

```
diagnose-structure-fit → design-decision-rights → check-span-and-layers

↓

stress-test-matrix-reporting (if matrix structure present)

↓

align-rewards-and-incentives
```

No scheduled agent ships with this plugin — org design review is naturally event-triggered (a reorg, an M&A integration, a leadership change, a strategy pivot), not calendar-driven. Re-run the relevant skill when one of those happens, rather than on a fixed schedule.

## Cross-plugin seams

- **`transformation:target-operating-model`** does a lighter-weight org layer as one part of a broader TOM design (alongside process, technology, and data). Use this plugin instead when org design itself — not the full TOM — is the primary problem, or hand off to this plugin for depth once `transformation:target-operating-model` has scoped the organization layer.
- **`market-intelligence:map-incentives`** applies the same "show me the incentive" logic externally (to competitors, customers); `align-rewards-and-incentives` applies it internally (to your own structure). They share a discipline, not an output — no duplication, just the same underlying idea pointed in two directions.

## Customization

See [CONNECTORS.md](./CONNECTORS.md).
