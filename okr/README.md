# okr

Objectives and Key Results — drafting, target-setting, instrumentation, cascading, check-ins, and scoring. Split out as its own plugin rather than living inside `performance` because OKRs are a goal-setting *process* with phases and a cadence, not a measurement capability — `performance` measures what's happening; this plugin decides what should happen and tracks commitment to it.

## Agents

| Agent | What it does | Command |
|---|---|---|
| **OKR Cascader** | Maps company OKRs to team-level objectives with coverage checks | `/okr:cascade` |
| **Check-In Nudge** | Weekly confidence pulses to KR owners; flags staleness and sharp drops to the OKR lead | scheduled agent |

## What this plugin does NOT do

- **Own the canonical metric glossary** — `/okr:instrument-metrics` defers to [`performance`](../performance) `/performance:metrics-glossary` when that plugin is installed.
- **Set multi-year strategic themes or causal maps** — that is [`balanced-scorecard`](../balanced-scorecard); OKR owns quarterly execution commitment.
- **Push nudges without `~~chat`** — `check-in-nudge` compiles due KRs and flags from log data and surfaces them in conversation when no chat connector is configured.
- **Grade itself** — `score-and-retro` produces a structured recommendation; humans own final scores and culture.

## Getting started

Run `/okr:practice-setup` first. Your practice profile lands at `~/.claude/plugins/config/claude-for-strategy/okr/CLAUDE.md`. The philosophy question (commit-only vs. mixed aspirational) is the one that matters most — `set-targets` and `score-and-retro` behave differently depending on the answer.

### Living profile

- **Practice setup** — writes the full profile after you confirm the interview summary.
- **Any other skill** — when a stable convention surfaces (scoring formula, commit vs aspirational mix, cascade ceilings), skills **propose a profile update**: show the exact change, ask for confirmation, write only if you say yes.
- **Edit directly** — small fixes without re-running setup.

## Usage

The cycle, roughly:

```
draft-objectives → write-key-results → set-targets → instrument-metrics → cascade

↓

check-in (repeated through the cycle, or via the agent)

↓

score-and-retro
```

If [`performance`](../performance) is installed, `instrument-metrics` defers to `/performance:metrics-glossary` for the formal metric definition.

If [`balanced-scorecard`](../balanced-scorecard) is also installed, see that plugin's README before running both cascades on the same objective set.

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/okr:practice-setup` | practice-setup | Learns philosophy, scoring scale, cadence, cascade structure |
| `/okr:draft-objectives` | draft-objectives | Draft objectives; catch KR-disguised-as-objectives |
| `/okr:write-key-results` | write-key-results | Outcome-shaped KRs; catch vanity metrics |
| `/okr:set-targets` | set-targets | Commit vs aspirational labeling; sandbagging detection |
| `/okr:instrument-metrics` | instrument-metrics | Map each KR to an exact metric spec |
| `/okr:cascade` | cascade | Parent-contribution test; orphan/coverage check |
| `/okr:check-in` | check-in | Confidence-based pulse per KR |
| `/okr:score-and-retro` | score-and-retro | End-of-cycle grading; keep/kill/revise |
| scheduled | check-in-nudge (agent) | Weekly KR confidence nudges via `~~chat` |

## Data directory

The `data/` folder holds local OKR cycle artifacts when you are not using a `~~project tracker` or other connector. You may store the current cycle's objective/KR set, the append-only check-in log, and end-of-cycle scoring notes from `score-and-retro`.

## Customization

See [CONNECTORS.md](./CONNECTORS.md) for the category breakdown. **Calendar** drives check-in cadence; **chat** is the primary surface for `check-in-nudge`.
