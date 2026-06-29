# market-intelligence

Competitive landscape, incentive mapping, positioning, and information asymmetry.

## Agents

| Agent | What it does | Command |
|---|---|---|
| **Competitive Signal Scan** | Weekly scan for competitor moves that would change the strategic-group or incentive map; works with native web search, no connector required | scheduled agent |

Runs on the cadence set in the practice profile (default: weekly). A dedicated news/monitoring connector improves reliability and coverage but isn't required to get value on day one.

## Components

| Command | What it does |
|---|---|
| `/market-intelligence:cold-start-interview` | Learns market definition, positioning, incentive context, signal-monitoring preferences |
| `/market-intelligence:map-competitive-landscape` | Groups competitors by actual strategic logic (not product category), maps mobility barriers between groups, identifies white space and asks whether it's unoccupied or structurally unattractive |
| `/market-intelligence:map-incentives` | "Show me the incentive" — maps actual incentive structures (not stated motivations) for any player, internal or external, and tests whether predicted behavior follows from the incentive or only from taking stated motivation at face value |
| `/market-intelligence:test-positioning` | Forces an explicit statement of what you're choosing not to do; checks for "stuck in the middle"; stress-tests who the position alienates |
| `/market-intelligence:map-information-asymmetry` | Identifies who's informed and who's uninformed in a given situation, and what signaling/screening mechanisms exist or are missing |
| `/market-intelligence:forecast-competitive-response` | Predicts competitor reaction to a planned move, grounded in their actual incentive structure, distinguishing moves that invite retaliation from moves that don't |

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

## Customization

See [CONNECTORS.md](./CONNECTORS.md).