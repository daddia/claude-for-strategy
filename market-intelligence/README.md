# market-intelligence

Competitive landscape, incentive mapping, positioning, and information asymmetry.

## What this plugin does NOT do

- **Make portfolio or capital-allocation calls** — competitive findings inform decisions; [`corporate-strategy`](../corporate-strategy) owns fund/exit/double-down when a signal crosses materiality.
- **Replace primary research or verified market data** — competitor claims and market sizes need sourcing tags; untagged figures are flagged `[unverified —]`.
- **Monitor competitors without your signal taxonomy** — `competitive-signal-scan` uses the profile's competitor set and meaningful-signal definitions; vague definitions produce noisy or empty digests.
- **Design internal reward systems** — external incentive mapping lives here; internal misalignment is [`operating-model:align-rewards-and-incentives`](../operating-model).

## Agents

| Agent | What it does | Command |
|---|---|---|
| **Competitive Signal Scan** | Weekly scan for competitor moves that would change the strategic-group or incentive map; works with native web search, no connector required | scheduled agent |

Runs on the cadence set in the practice profile (default: weekly). A dedicated news/monitoring connector improves reliability and coverage but isn't required to get value on day one.

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/market-intelligence:cold-start-interview` | cold-start-interview | Learns market definition, positioning, incentive context, signal-monitoring preferences |
| `/market-intelligence:map-competitive-landscape` | map-competitive-landscape | Groups competitors by actual strategic logic (not product category), maps mobility barriers between groups, identifies white space and asks whether it's unoccupied or structurally unattractive |
| `/market-intelligence:map-incentives` | map-incentives | "Show me the incentive" — maps actual incentive structures (not stated motivations) for any player, internal or external, and tests whether predicted behavior follows from the incentive or only from taking stated motivation at face value |
| `/market-intelligence:test-positioning` | test-positioning | Forces an explicit statement of what you're choosing not to do; checks for "stuck in the middle"; stress-tests who the position alienates |
| `/market-intelligence:map-information-asymmetry` | map-information-asymmetry | Identifies who's informed and who's uninformed in a given situation, and what signaling/screening mechanisms exist or are missing |
| `/market-intelligence:forecast-competitive-response` | forecast-competitive-response | Predicts competitor reaction to a planned move, grounded in their actual incentive structure, distinguishing moves that invite retaliation from moves that don't |
| scheduled | competitive-signal-scan (agent) | Weekly competitor signal scan via native web search; optional `~~chat` digest |

## The skill that matters most: `map-information-asymmetry`

This is the most distinctive skill in the whole repo and the one with no close equivalent anywhere else in it. Most strategy toolkits never touch this — it's a genuinely different lens (who knows what, and what that asymmetry lets you do or exposes you to) rather than a repackaging of competitive analysis. Worth using even on situations that don't look like an obvious fit at first.

## Setup

Run `/market-intelligence:cold-start-interview` first. The market-definition question matters most — "who are we actually competing with" is frequently answered wrong (too narrow, by product category, missing the adjacent player who could pivot in), and everything downstream inherits that error if it's wrong here.

### Living profile

- **Cold-start interview** — writes the full profile after you confirm the interview summary.
- **Any other skill** — when a stable convention surfaces (signal taxonomy, competitor set, materiality thresholds), skills **propose a profile update**: show the exact change, ask for confirmation, write only if you say yes.
- **Edit directly** — small fixes without re-running setup.

## Usage

```
map-competitive-landscape → forecast-competitive-response (for a specific planned move)
map-incentives → forecast-competitive-response (incentive map grounds the response prediction)
map-incentives → operating-model:align-rewards-and-incentives (when the incentive problem is internal)
test-positioning ↔ map-information-asymmetry (a position is often a bet on which side of an asymmetry you're on)
```

## Boundary with `corporate-strategy`

This plugin operates at the competitive-dynamics level — who you're actually competing with, what incentives predict their behavior, and how they'll respond to a move. `corporate-strategy` operates at the portfolio/capital-allocation level — whether a competitive threat or opportunity should change what you fund, exit, or double down on. Run `map-competitive-landscape` and `forecast-competitive-response` here; hand off to `corporate-strategy:evaluate-strategic-option` when a signal becomes a capital-allocation decision.

## Data directory

The `data/` folder holds local competitive-intelligence artifacts when you are not using `~~whiteboard` or `~~documents`. You may store strategic-group maps from `map-competitive-landscape`, incentive maps from `map-incentives`, positioning briefs, and append-only signal digests the `competitive-signal-scan` agent references. Point skills at files here by path, or paste content when running a skill — both work. Files you add here are yours — only `.gitkeep` ships with the plugin.

## Customization

See [CONNECTORS.md](./CONNECTORS.md).