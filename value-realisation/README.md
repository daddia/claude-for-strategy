# value-realisation

Benefits mapping, baseline-and-accountability discipline, realisation tracking with attribution rigor, at-risk recovery decisions, and post-implementation review.

## Why this is a separate plugin from `performance`, `okr`, and `balanced-scorecard`

Those three plugins manage *ongoing, forward-looking* goals and measurement — what should we hit next quarter, how do we know we're on track. `value-realisation` answers a different question: did *this specific, already-approved investment* deliver the value its business case promised, on a finite window, traced back to one decision, with the result feeding directly into how confidently the *next* business case gets sized. It's a post-investment audit function, not a performance-management cadence.

## Components

| Command | What it does |
|---|---|
| `/value-realisation:cold-start-interview` | Learns your benefits framework, governance model, baseline discipline, and cadence — writes your practice profile |
| `/value-realisation:benefits-map` | Approved business case → Benefits Dependency Network (enabler → business change → benefit → objective); catches benefits that are really deliverables in disguise |
| `/value-realisation:benefits-register` | Mapped benefits → formal register entries — baseline-before-change enforcement, benefit type classification, single-point accountability (an owner who isn't the delivery PM) |
| `/value-realisation:benefits-tracking` | Periodic remeasurement against baseline, with an explicit attribution call — not just "the number moved," but "moved because of us" |
| `/value-realisation:benefits-recovery` | At-risk benefit → root-cause split (measurement lag / not embedded / enabler gap / theory problem / structurally lost) and a sunk-cost-clean continue-or-write-down decision |
| `/value-realisation:realisation-review` | End-of-window portfolio PIR — planned vs. actual, optimism-bias calibration fed back into future business cases |

## Setup

Run `/value-realisation:cold-start-interview` first. The baseline-discipline question matters most — if baselines are normally captured after a change has already gone live (common), say so plainly; `benefits-register` needs to know this to flag retrofitted baselines rather than treating them as clean.

## Usage

The loop, roughly:

```
benefits-map → benefits-register
↓
benefits-tracking (repeated through the realisation window)
↓ (if a benefit goes off-track)
benefits-recovery
↓ (at window close)
realisation-review → feeds back into the next transformation:business-case / corporate-strategy:evaluate-strategic-option
```

If [`transformation`](../transformation) is installed, run `benefits-map` directly against an approved `transformation:business-case` output rather than starting blank — the case's cost/benefit table is the natural seed. The same seam applies to `corporate-strategy:evaluate-strategic-option`, if installed, for option-level decisions upstream of a formal business case.

If [`performance`](../performance) is installed, `benefits-register` defers to `performance:metrics-glossary` for the formal metric definition (exact formula, source, owner, refresh cadence) — same seam pattern as `okr:instrument-metrics` and `balanced-scorecard:select-measures`. This plugin only owns the benefit-to-measure mapping, the baseline, and the accountability assignment.

If [`pmo`](../pmo) is installed, a `benefits-recovery` continue-or-write-down call is a governance decision worth a `pmo:decision-log` entry — this plugin doesn't duplicate that log.

If [`consulting`](../consulting) is installed, hand `realisation-review` output to `consulting:exec-memo` or `deck-outline` for a steering-committee version.

## Agents

`agents/realisation-checkpoint-reminder.md` runs on the cadence set in the practice profile (default: monthly) — prompts a `benefits-tracking` run for benefits due, and separately escalates any benefit approaching go-live with no baseline captured yet, since a missed baseline is unrecoverable once change starts. See the agent file for what happens with no `~~chat` connected.

## Data directory

The `data/` folder holds the local benefits register, dependency network, and tracking log when you are not using a `~~knowledge base` or `~~project tracker` connector. Point skills at files here by path, or paste content when running a skill — both work. Files you add here are yours — only `.gitkeep` ships with the plugin.

## Customization

See [CONNECTORS.md](./CONNECTORS.md) for the category breakdown.
