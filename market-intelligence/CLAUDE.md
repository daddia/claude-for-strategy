<!--
Config location rules:
1. User data lives at ~/.claude/plugins/config/claude-for-strategy/market-intelligence/CLAUDE.md — create parent dirs as needed.
2. If a populated profile exists at ~/.claude/plugins/cache/claude-for-strategy/market-intelligence/*/CLAUDE.md but not at the config path, copy it forward before proceeding.
3. This file is the TEMPLATE. It ships with the plugin and is replaced on every plugin update. Never write user data here.

Shared org profile. Organisation-wide facts live in ~/.claude/plugins/config/claude-for-strategy/org-profile.md — read it before this file.
-->

# Practice Profile — market-intelligence

> **Template only** — not read at runtime. `/market-intelligence:cold-start-interview` writes your filled practice profile to `~/.claude/plugins/config/claude-for-strategy/market-intelligence/CLAUDE.md`; every other skill reads from that path **and** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`. Edit the user config files directly for small fixes; re-run the interview for material changes. Other skills **propose profile updates** (show the change, ask, then write on confirmation) — only cold-start auto-applies a full write.

## Status
`template` — run `/market-intelligence:cold-start-interview` to fill this in.

## Who's using this

- **Role:** _(competitive strategy lead, CI analyst, product strategy partner)_
- **Primary consumers:** _(exec team, product, sales, corp strategy)_

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| Slack | [PLACEHOLDER ✓/✗] | Weekly digests inline only |
| Google Drive | [PLACEHOLDER ✓/✗] | User uploads landscape decks per task |

*Re-check: `/market-intelligence:cold-start-interview --check-integrations`*

## Plugin-specific operating model

- **Market definition scope:** _(how you draw category boundaries — not SIC codes)_
- **Competitive monitoring rhythm:** _(weekly scan, event-driven, quarterly deep dive)_
- **Response process:** _(when a signal triggers exec briefing vs logged for later)_
- **Win/loss feedback loop:** _(if used — source and cadence)_

## Framework preferences

- **Strategic group mapping:** _(how competitors are clustered)_
- **Positioning framework:** _(value prop, trade-offs, "won't do" list)_
- **Signal taxonomy:** _(pricing, product, talent, funding, partnership, etc.)_
- **Avoid / do not default to:**

## Definitions and thresholds

- **Known competitor set:** _(named players and groupings)_
- **Meaningful signal:** _(what actually counts — be specific for `competitive-signal-scan`)_
- **Materiality for escalation:** _(when a signal must reach corp strategy / exec)_
- **Incentive context:** _(internal stakeholders and external players whose incentives shape decisions)_

## Output formats

- **Competitive landscape deck:** _(structure, exhibit types)_
- **Signal digest:** _(length, severity tags, recommended action)_
- **Positioning brief:** _(sections, audience)_
- **Source attribution:** _(tag competitor claims and market figures per trust spine)_

## Review gates

- **Exec / corp strategy handoff:** _(when scan results become portfolio decisions)_
- **External distribution:** _(client-facing or board — human review required)_
- **Trust spine:** Competitor claims and market sizes tagged; no invented share data.

## Seed examples

_(Past competitive landscape deck, win/loss analysis, or positioning document.)_

- 

## Known gaps / things to revisit

-
