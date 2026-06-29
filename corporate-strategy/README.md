# corporate-strategy

Growth strategy, portfolio and resource allocation, and strategic options.

## What this plugin does NOT do

- **Replace investment committee or board judgment** — portfolio calls are structured first passes; humans own capital allocation and divestiture decisions.
- **Pull live spend or headcount from BI without a connector** — `allocate-resources` works from data you point at; wiring `~~bi analytics` is account-specific.
- **Run competitive landscape or response analysis** — that is [`market-intelligence`](../market-intelligence); hand off here when a signal becomes a capital-allocation decision.
- **Build initiative-level business cases** — once a strategic direction is set, use [`transformation:business-case`](../transformation) for program-level cases.

## Agents

| Agent | What it does | Command |
|---|---|---|
| **Portfolio Review Reminder** | Quarterly prompt to run `allocate-resources` and recheck `exit-or-double-down` holds past their re-rating date | scheduled agent |

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/corporate-strategy:cold-start-interview` | cold-start-interview | Learns portfolio composition, growth ambition, capital allocation process, risk posture |
| `/corporate-strategy:assess-growth-vectors` | assess-growth-vectors | Categorizes growth initiatives core/adjacent/transformational, applies realistic success-rate priors per category, and does the arithmetic the growth ambition usually skips: does the portfolio of initiatives actually sum to the stated target |
| `/corporate-strategy:allocate-resources` | allocate-resources | Maps spend/headcount/attention against strategic priority; flags misallocation — especially legacy units absorbing resources disproportionate to their importance |
| `/corporate-strategy:exit-or-double-down` | exit-or-double-down | Forces the blank-page test on each unit, detects sunk-cost reasoning explicitly, and produces an exit/hold/double-down call |
| `/corporate-strategy:evaluate-strategic-option` | evaluate-strategic-option | Real-options framing for a major decision — staging, kill criteria set in advance, the case against written by the skill, not just collected |
| `/corporate-strategy:build-vs-buy-vs-partner` | build-vs-buy-vs-partner | Evaluates a capability gap against known failure priors per path (build underestimates cost, buy overestimates synergy, partner underestimates exit difficulty) |
| `/corporate-strategy:synergy-stress-test` | synergy-stress-test | Separates cost from revenue synergies, applies a base-rate haircut to revenue synergy claims, checks for double-counting |

## The skill that matters most: `exit-or-double-down`

Portfolio strategy fails more often by *not exiting* than by entering the wrong market. This skill is built to surface sunk-cost reasoning by name, not just produce a polite recommendation — expect it to be uncomfortable sometimes. That's the point.

## Setup

Run `/corporate-strategy:cold-start-interview` first. Your practice profile lands at `~/.claude/plugins/config/claude-for-strategy/corporate-strategy/CLAUDE.md`. The growth ambition number and the capital allocation stickiness question matter most — without a real target, `assess-growth-vectors` has nothing to test against; without knowing the org's allocation history, `allocate-resources` can't tell you anything you don't already suspect.

### Living profile

- **Cold-start interview** — writes the full profile after you confirm the interview summary.
- **Any other skill** — when a stable convention surfaces (portfolio review cadence, hold re-rating timelines, growth-category priors), skills **propose a profile update**: show the exact change, ask for confirmation, write only if you say yes.
- **Edit directly** — small fixes without re-running setup.

## Usage

```
assess-growth-vectors → allocate-resources → exit-or-double-down (recurring portfolio cycle)
evaluate-strategic-option → build-vs-buy-vs-partner (if the option is a capability gap)

→ synergy-stress-test (if the option is M&A)
```

## Boundary with `transformation:business-case`

`evaluate-strategic-option` operates at the portfolio/capital-allocation level — bigger bets, competing against every other claim on capital across the whole portfolio. `transformation:business-case` operates at the initiative level — once a strategic direction is set, what's the case for *this specific* transformation program. If you're deciding whether to enter a market or acquire a company, use this plugin. If you're deciding whether to fund a specific transformation initiative inside an already-chosen direction, use `transformation`.

## Boundary with `market-intelligence`

`market-intelligence` operates at the competitive-dynamics level — who you're actually competing with, what incentives predict their behavior, and how they'll respond to a move. This plugin operates at the portfolio/capital-allocation level — whether a competitive threat or opportunity should change what you fund, exit, or double down on. Run `map-competitive-landscape` and `forecast-competitive-response` in `market-intelligence`; hand off to `evaluate-strategic-option` here when a signal becomes a capital-allocation decision.

## Customization

See [CONNECTORS.md](./CONNECTORS.md).
