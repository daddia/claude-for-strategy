# transformation

Digital maturity assessment, transformation roadmaps, target operating model design, technology strategy briefs, and transformation business cases.

## Agents

| Agent | What it does | Command |
|---|---|---|
| **Maturity Assessor** | Interview notes/observations → maturity scorecard with binding-constraint analysis | `/transformation:maturity-assessment` |
| **Roadmap Architect** | Current state + ambition → phased Now/Next/Later roadmap | `/transformation:roadmap-builder` |
| **TOM Designer** | Current state + ambition → target operating model across capability/org/process/tech/data | `/transformation:target-operating-model` |
| **Tech Decision Brief** | Platform/architecture decision → options + recommendation, BLUF-structured | `/transformation:tech-strategy-brief` |
| **Business Case Builder** | Initiative scope → problem, options, cost/benefit, sequencing, risk, ask | `/transformation:business-case` |
| **Assumption-Decay Watcher** | Business cases, roadmaps, decision log → assumptions with revisit-trigger dates now due | scheduled agent |
| **Roadmap-Drift Watcher** | Roadmap vs. actual progress → initiatives slipping phase, with knock-on effects | scheduled agent |

## What this plugin does NOT do

- **Certify maturity scores or ROI** — assessments and business cases are structured first passes for your validation.
- **Replace enterprise architecture or vendor selection** — `tech-strategy-brief` frames decisions; it does not run RFPs or sign contracts.
- **Auto-sync roadmap status from your project tracker** — Roadmap-Drift Watcher compares plan vs. evidence you point to; live tracker integration is via connectors you wire yourself.

## Getting started

Run `/transformation:cold-start-interview` first. Your practice profile lands at `~/.claude/plugins/config/claude-for-strategy/transformation/CLAUDE.md`. Record your platform vocabulary, delivery track model, and risk posture — `roadmap-builder` and `business-case` both read this directly.

### Living profile

- **Cold-start interview** — writes the full profile after you confirm the interview summary.
- **Any other skill** — when a stable convention surfaces (platform vocabulary, roadmap tracks, maturity dimensions), skills **propose a profile update**: show the exact change, ask for confirmation, write only if you say yes.
- **Edit directly** — small fixes without re-running setup.

No environment variables or connectors are required for V1. Optional MCP servers are listed in [CONNECTORS.md](./CONNECTORS.md). For scheduled watchers, connect `~~chat` so Assumption-Decay and Roadmap-Drift summaries reach you; install [`pmo`](../pmo) if you want Assumption-Decay to scan the decision log for revisit triggers.

## Usage

Typical chains:

```
maturity-assessment → roadmap-builder (binding constraint informs sequencing)
roadmap-builder → target-operating-model (execution-level detail on one phase)
tech-strategy-brief → business-case (a single decision feeding into the broader case)
```

Scheduled agents (configure `~~chat`):

```
assumption-decay-watcher — weekly + after business-case/roadmap/decision-log updates; posts due revisit triggers
roadmap-drift-watcher — weekly phase-slippage check with downstream knock-on effects
```

If [`consulting`](../consulting) is also installed, hand off `business-case` or `tech-strategy-brief` output to `/consulting:deck-outline` for a steering committee version.

If [`operating-model`](../operating-model) is also installed, hand off `target-operating-model` org-layer output to `/operating-model:diagnose-structure-fit` or `/operating-model:design-decision-rights` when org design — not the full TOM — needs depth.

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/transformation:cold-start-interview` | cold-start-interview | Learns platform vocabulary, delivery model, maturity framework |
| `/transformation:maturity-assessment` | maturity-assessment | Observations → maturity scorecard with binding-constraint analysis |
| `/transformation:roadmap-builder` | roadmap-builder | Current state + ambition → phased roadmap |
| `/transformation:target-operating-model` | target-operating-model | Current state + ambition → TOM |
| `/transformation:tech-strategy-brief` | tech-strategy-brief | Architecture decision → options + recommendation |
| `/transformation:business-case` | business-case | Initiative scope → full business case |
| scheduled | assumption-decay-watcher (agent) | Weekly + post-update scan for due revisit-trigger assumptions via `~~chat` |
| scheduled | roadmap-drift-watcher (agent) | Weekly roadmap phase-slippage check via `~~chat` |

## Trust spine

`roadmap-builder`, `target-operating-model`, `tech-strategy-brief`, and `business-case` each carry a condensed trust-spine block (sourcing tags, surfaced assumptions, no invented numbers, confidence labeling, board-ready gate). Full rules: [`consulting/references/trust-conventions.md`](../consulting/references/trust-conventions.md) when the consulting plugin is installed, or [`references/trust-conventions.md`](../references/trust-conventions.md) at repo root.

## Customization

See [CONNECTORS.md](./CONNECTORS.md) — `~~observability` and `~~hosting` are the categories most specific to this plugin. V1 skills produce markdown output; wiring those connectors lets `tech-strategy-brief` and `target-operating-model` ground against real system context.
