# balanced-scorecard

Strategy maps and balanced scorecards — perspective design, causal strategy mapping, measure selection, targets and initiatives, cascaded scorecards, and reviews that test whether the strategy's underlying theory held up, not just whether the numbers moved.

## Why this is a separate plugin from `okr`

OKRs and BSC are two different answers to "how do you connect strategy to what people measure and do," not two modes of the same tool. OKR is bottom-up and outcome-focused, built for adaptive quarterly alignment. BSC is top-down, built around an explicit causal theory of the business across four perspectives, and is meant to be revisited far less often than it's reviewed. The skill sets genuinely differ — BSC's center of gravity is `build-strategy-map`, which has no OKR equivalent.

**If you run both:** a common pattern is BSC setting the multi-year strategic themes and causal map, with OKR cascading quarterly execution commitments underneath specific BSC objectives. Don't run `/balanced-scorecard:cascade-to-scorecards` and `/okr:cascade` on the same objective set independently — pick which plugin owns which layer and record it in both practice profiles.

## Agents

| Agent | What it does | Command |
|---|---|---|
| **Strategy Review Reminder** | Prompts quarterly `review-and-validate`; separately flags when annual map-refresh is due | scheduled agent |

## What this plugin does NOT do

- **Replace your strategy offsite or executive judgment** — the map is a structured hypothesis about causality, not a certified strategy.
- **Duplicate metric definitions** — `select-measures` defers to [`performance`](../performance) `metrics-glossary` when that plugin is installed.
- **Run OKR check-ins or quarterly goal-setting** — that is the [`okr`](../okr) plugin.
- **Prove causality from one bad quarter** — `review-and-validate` separates execution failure from theory failure; it does not auto-rewrite the map.

## Getting started

Run `/balanced-scorecard:practice-setup` first. Your practice profile lands at `~/.claude/plugins/config/claude-for-strategy/balanced-scorecard/CLAUDE.md`. The sector question matters most — it determines the perspective set and which perspective sits at the top of the causal chain. Getting this wrong (e.g. defaulting to Financial-at-top for a mission-driven org) means every downstream skill optimizes the map toward the wrong ultimate objective.

### Living profile

- **Practice setup** — writes the full profile after you confirm the interview summary.
- **Any other skill** — when a stable convention surfaces (perspective names, measure ceiling, review cadence), skills **propose a profile update**: show the exact change, ask for confirmation, write only if you say yes.
- **Edit directly** — small fixes without re-running setup.

## Usage

The build sequence, roughly:

```txt
define-perspectives → build-strategy-map → select-measures → set-targets-and-initiatives

↓

cascade-to-scorecards

↓

review-and-validate (recurring, per cadence)
```

`build-strategy-map` is revisited far less often than the rest — typically annually, or when something fundamental about the strategy changes. Don't let the quarterly `review-and-validate` rhythm pull you into re-opening the map every cycle.

If [`performance`](../performance) is installed, `select-measures` defers to `/performance:metrics-glossary` for formal metric definitions.

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/balanced-scorecard:practice-setup` | practice-setup | Learns sector, perspective model, cadence, cascade structure |
| `/balanced-scorecard:define-perspectives` | define-perspectives | Perspective set and causal-chain top perspective |
| `/balanced-scorecard:build-strategy-map` | build-strategy-map | Objectives per perspective with explicit causal mechanisms |
| `/balanced-scorecard:select-measures` | select-measures | Lead/lag classification per measure |
| `/balanced-scorecard:set-targets-and-initiatives` | set-targets-and-initiatives | Targets plus named strategic initiatives |
| `/balanced-scorecard:cascade-to-scorecards` | cascade-to-scorecards | Cascade to BU/team scorecards |
| `/balanced-scorecard:review-and-validate` | review-and-validate | Score measures; test causal links against outcomes |
| scheduled | strategy-review-reminder (agent) | Quarterly review prompt; annual map-refresh tracker |

## Data directory

The `data/` folder is the local home for BSC artifacts when you are not using `~~whiteboard` or an external doc. Set the strategy map location in your practice profile to this plugin's `data/` and `build-strategy-map` will persist the living map there. You may also store scorecard measure snapshots and append-only review history from `review-and-validate`.

## Customization

See [CONNECTORS.md](./CONNECTORS.md) — Miro is pre-wired for `~~whiteboard`; the strategy map is fundamentally a diagram.
