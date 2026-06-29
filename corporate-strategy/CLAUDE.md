<!--
Config location rules:
1. User data lives at ~/.claude/plugins/config/claude-for-strategy/corporate-strategy/CLAUDE.md — create parent dirs as needed.
2. If a populated profile exists at ~/.claude/plugins/cache/claude-for-strategy/corporate-strategy/*/CLAUDE.md but not at the config path, copy it forward before proceeding.
3. This file is the TEMPLATE. It ships with the plugin and is replaced on every plugin update. Never write user data here.

Shared org profile. Organisation-wide facts live in ~/.claude/plugins/config/claude-for-strategy/org-profile.md — read it before this file.
-->

# Practice Profile — corporate-strategy

> **Template only** — not read at runtime. `/corporate-strategy:practice-setup` writes your filled practice profile to `~/.claude/plugins/config/claude-for-strategy/corporate-strategy/CLAUDE.md`; every other skill reads from that path **and** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`. Edit the user config files directly for small fixes; re-run the interview for material changes. Other skills **propose profile updates** (show the change, ask, then write on confirmation) — only `practice-setup` auto-applies a full write.

## Status
`template` — run `/corporate-strategy:practice-setup` to fill this in.

## Who's using this

- **Role:** _(CSO, head of strategy, portfolio manager, corp dev lead)_
- **Decision scope:** _(group portfolio, BU strategy, M&A pipeline)_

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| Slack | [PLACEHOLDER ✓/✗] | Portfolio-review reminders inline only |
| Google Calendar | [PLACEHOLDER ✓/✗] | User states review dates manually |
| Google Drive | [PLACEHOLDER ✓/✗] | User uploads portfolio decks per task |

*Re-check: `/corporate-strategy:practice-setup --check-integrations`*

## Plugin-specific operating model

- **Portfolio review cadence:** _(annual deep dive, quarterly refresh)_
- **Option evaluation process:** _(who proposes, who stress-tests, who decides)_
- **Capital allocation rhythm:** _(annual budget, rolling quarterly reallocation, ad hoc)_
- **M&A / divestiture process:** _(if applicable — stage gates, IC involvement)_

## Framework preferences

- **Portfolio lenses:** _(BCG matrix, McKinsey horizons, custom segments)_
- **Growth vector framework:** _(organic, inorganic, adjacency expansion)_
- **Capital allocation method:** _(ROIC/WACC, strategic buckets, guardrails)_
- **Avoid / do not default to:**

## Definitions and thresholds

- **Portfolio units:** _(businesses, products, segments this plugin reasons about)_
- **Strategic priority tiers:** _(core, adjacent, exit candidates — or your labels)_
- **Growth target:** _(rate, horizon, source — board vs internal)_
- **Allocation stickiness:** _(known lag between strategy and funding)_
- **Synergy haircut / stress-test default:** _(based on track record of past deals)_
- **Risk tolerance for strategic options:** _(conservative, balanced, aggressive — see org profile if set)_

## Output formats

- **Portfolio review memo:** _(structure, exhibit expectations)_
- **Strategic option memo:** _(options table, recommendation placement)_
- **Resource allocation recommendation:** _(format, required financial tags)_
- **Synergy / integration brief:** _(assumptions that must be explicit)_

## Review gates

- **Investment committee / board strategy session:** _(what requires IC vs exec team)_
- **Capital reallocation:** _(thresholds and approvers — see org escalation model)_
- **Trust spine:** No invented market sizes or deal multiples; tag sources and assumptions.

## Seed examples

_(Current or recent portfolio review, growth strategy deck, or post-mortem on a past deal.)_

- 

## Known gaps / things to revisit

-
