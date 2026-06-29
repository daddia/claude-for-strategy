# performance

KPI trees, metrics tracker builder, metrics glossary, and performance narratives.

## Agents

| Agent | What it does | Command |
|---|---|---|
| **KPI Tree Builder** | North Star metric → MECE drivers → leading indicators | `/performance:kpi-tree-builder` |
| **Tracker Builder** | Builds a `.xlsx` — Daily Log tab wired to Summary via live formulas | `/performance:tracker-builder` |
| **Board Narrative Writer** | Metrics/results → BLUF-structured narrative for your stated audience | `/performance:performance-narrative` |
| **KPI Breach Watcher** | Daily scan for metrics crossing targets/thresholds; Honeycomb for telemetry | scheduled agent |
| **Cadence Reporter** | Assembles period performance narrative draft on reporting cadence | scheduled agent |

## What this plugin does NOT do

- **Draft, cascade, check in on, or score OKRs** — that is the [`okr`](../okr) plugin (`/okr:cascade` for company→team breakdown); this plugin owns measurement definitions and reporting.
- **Pull live metrics without a connector** — `tracker-builder` replicates your spreadsheet pattern; telemetry metrics need `~~observability` or manual log input.
- **Ship board-ready narratives without human review** — Cadence Reporter drafts on schedule; you verify every figure before anything reaches the board.

## Getting started

Run `/performance:cold-start-interview` first — this is the plugin where setup matters most. Your practice profile lands at `~/.claude/plugins/config/claude-for-strategy/performance/CLAUDE.md`. If you already have a tracker (Daily Log feeding a summary sheet via `AVERAGEIFS`/`SUMIFS`), describe its exact structure during setup so `tracker-builder` replicates *your* pattern.

### Living profile

- **Cold-start interview** — writes the full profile after you confirm the interview summary.
- **Any other skill** — when a stable convention surfaces (metric codes, tracker columns, reporting cadence), skills **propose a profile update**: show the exact change, ask for confirmation, write only if you say yes.
- **Edit directly** — small fixes without re-running setup.

`tracker-builder` builds real spreadsheet files. No additional setup beyond the cold-start interview.

## Usage

Typical chains:

```
kpi-tree-builder → tracker-builder (drivers/indicators become tracked metrics)
tracker-builder → performance-narrative (numbers → board-ready writeup)
metrics-glossary stands alone as ongoing reference documentation
```

Scheduled agents (configure `~~chat` and, for telemetry metrics, `~~observability`):

```
kpi-breach-watcher — daily threshold scan; posts breaches or all-clear
cadence-reporter — period narrative draft on reporting cadence; human review before board
```

If [`consulting`](../consulting) is installed, hand `performance-narrative` output to `/consulting:exec-memo` or `/consulting:deck-outline`.

If [`okr`](../okr) is installed, `metrics-glossary` is the canonical source for metric definitions that `/okr:instrument-metrics` maps key results to.

If [`balanced-scorecard`](../balanced-scorecard) is installed, `metrics-glossary` is also the canonical source for formal definitions that `/balanced-scorecard:select-measures` defers to.

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/performance:cold-start-interview` | cold-start-interview | Learns KPI taxonomy, tracker structure, reporting cadence |
| `/performance:kpi-tree-builder` | kpi-tree-builder | North Star → MECE drivers → leading indicators |
| `/performance:tracker-builder` | tracker-builder | Builds `.xlsx` with Daily Log → Summary formulas |
| `/performance:metrics-glossary` | metrics-glossary | Metric list → single source-of-truth definitions |
| `/performance:performance-narrative` | performance-narrative | Metrics/results → BLUF narrative |
| scheduled | kpi-breach-watcher (agent) | Daily threshold breach scan via `~~chat`; Honeycomb for telemetry |
| scheduled | cadence-reporter (agent) | Period narrative draft on reporting cadence via `~~chat` |

## Trust spine

`performance-narrative` carries a condensed trust-spine block (sourcing tags, surfaced assumptions, no invented numbers, confidence labeling, board-ready gate). Full rules: [`consulting/references/trust-conventions.md`](../consulting/references/trust-conventions.md) when the consulting plugin is installed, or [`references/trust-conventions.md`](../references/trust-conventions.md) at repo root.

## Customization

See [CONNECTORS.md](./CONNECTORS.md) — `tracker-builder` outputs a `.xlsx` file directly; wiring a live `~~spreadsheet` connector is a future enhancement, not required for V1.
