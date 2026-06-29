<!--
Config location rules:
1. User data lives at ~/.claude/plugins/config/claude-for-strategy/performance/CLAUDE.md — create parent dirs as needed.
2. If a populated profile exists at ~/.claude/plugins/cache/claude-for-strategy/performance/*/CLAUDE.md but not at the config path, copy it forward before proceeding.
3. This file is the TEMPLATE. It ships with the plugin and is replaced on every plugin update. Never write user data here.

Shared org profile. Organisation-wide facts live in ~/.claude/plugins/config/claude-for-strategy/org-profile.md — read it before this file.
-->

# Practice Profile — performance

> **Template only** — not read at runtime. `/performance:practice-setup` writes your filled practice profile to `~/.claude/plugins/config/claude-for-strategy/performance/CLAUDE.md`; every other skill reads from that path **and** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`. Edit the user config files directly for small fixes; re-run the interview for material changes. Other skills **propose profile updates** (show the change, ask, then write on confirmation) — only `practice-setup` auto-applies a full write.

## Status
`template` — run `/performance:practice-setup` to fill this in.

## Who's using this

- **Role:** _(performance lead, FP&A partner, ops analyst, agency principal)_
- **Primary consumers:** _(board, sponsor, delivery leadership, clients)_

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| Google Drive / Sheets | [PLACEHOLDER ✓/✗] | User describes tracker structure manually |
| Slack | [PLACEHOLDER ✓/✗] | Performance narratives inline only |
| Atlassian | [PLACEHOLDER ✓/✗] | Delivery metrics from user uploads |
| Linear | [PLACEHOLDER ✓/✗] | Delivery metrics from user uploads |

*Re-check: `/performance:practice-setup --check-integrations`*

## Plugin-specific operating model

- **Metric governance:** _(who owns definitions, who approves changes)_
- **Tracker refresh rhythm:** _(daily log, weekly rollup, monthly close)_
- **Reporting cadence per audience:** _(board, sponsor, team)_
- **OKR / BSC relationship:** _(if other plugins installed — who owns what layer)_

## Framework preferences

- **North Star / driver tree:** _(how top metrics decompose)_
- **Metric categories:** _(e.g. Digital Product Performance, Delivery Performance)_
- **Variance explanation method:** _(volume/price/mix, plan vs actual narrative)_
- **Avoid / do not default to:**

## Definitions and thresholds

- **North Star metric(s):**
- **Naming convention:** _(e.g. B2/B3 codes vs plain names)_
- **Tracker tool and structure:** _(summary sheet, daily/period log, formulas)_
- **RAG / status thresholds:** _(what triggers amber or red)_
- **Data source per metric:** _(see org profile hierarchy when overlapping)_

## Output formats

- **Tracker layout:** _(tabs, columns, movement columns, formula patterns)_
- **Performance narrative:** _(length, BLUF, exhibit rules)_
- **Metric definition sheet:** _(required fields — owner, source, cadence, formula)_

## Review gates

- **Finance validation:** _(before board/sponsor numbers are treated as official)_
- **Metric definition changes:** _(who must approve)_
- **Trust spine:** No invented actuals; tag estimates and benchmarks.

## Seed examples

_(Existing tracker, metric glossary, or reporting pack the interview was run against.)_

- 

## Known gaps / things to revisit

-
