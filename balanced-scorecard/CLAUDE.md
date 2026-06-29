<!--
Config location rules:
1. User data lives at ~/.claude/plugins/config/claude-for-strategy/balanced-scorecard/CLAUDE.md — create parent dirs as needed.
2. If a populated profile exists at ~/.claude/plugins/cache/claude-for-strategy/balanced-scorecard/*/CLAUDE.md but not at the config path, copy it forward before proceeding.
3. This file is the TEMPLATE. It ships with the plugin and is replaced on every plugin update. Never write user data here.

Shared org profile. Organisation-wide facts live in ~/.claude/plugins/config/claude-for-strategy/org-profile.md — read it before this file.
-->

# Practice Profile — balanced-scorecard

> **Template only** — not read at runtime. `/balanced-scorecard:practice-setup` writes your filled practice profile to `~/.claude/plugins/config/claude-for-strategy/balanced-scorecard/CLAUDE.md`; every other skill reads from that path **and** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`. Edit the user config files directly for small fixes; re-run the interview for material changes. Other skills **propose profile updates** (show the change, ask, then write on confirmation) — only `practice-setup` auto-applies a full write.

## Status
`template` — run `/balanced-scorecard:practice-setup` to fill this in.

## Who's using this

- **Role:** _(strategy office, FP&A, ops excellence, nonprofit mission owner)_
- **BSC scope:** _(enterprise, BU, department)_

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| Google Drive / whiteboard | [PLACEHOLDER ✓/✗] | User describes map location manually |
| Slack | [PLACEHOLDER ✓/✗] | Review reminders inline only |
| `performance` plugin | [PLACEHOLDER ✓/✗] | Metric definitions stay in BSC artifacts |

*Re-check: `/balanced-scorecard:practice-setup --check-integrations`*

## Plugin-specific operating model

- **Strategy map vs scorecard cadence:** _(map annual / triggered; scorecard quarterly typical)_
- **Cascade levels:** _(corporate → BU → team)_
- **Local objectives policy:** _(allowed at cascaded levels vs must trace to corporate map)_
- **Integration with OKR / performance:** _(layering rules — who owns multi-year vs quarterly)_

## Framework preferences

- **Sector model:** _(for-profit, nonprofit, public sector, hybrid — drives perspective set)_
- **Perspective set:** _(names and order, top of causal chain)_
- **Top perspective:** _(Financial vs Mission/Stakeholder — the ultimate "why")_
- **Causal map conventions:** _(arrows, objective wording, theme groupings)_
- **Avoid / do not default to:** _(e.g. Financial-at-top for mission-driven orgs)_

## Definitions and thresholds

- **Target measure count:** _(~20–25 classic guidance, or your ceiling)_
- **Scoring / status convention:** _(RAG, numeric, % to target)_
- **Strategy map location:** _(where live map lives — `build-strategy-map` updates, not recreates)_
- **Last full map refresh:** _(date)_

## Output formats

- **Strategy map:** _(layout, perspective bands, linkage notation)_
- **Scorecard table:** _(perspectives, objectives, measures, targets, initiatives)_
- **Cascade worksheet:** _(how BU/team maps align to corporate)_

## Review gates

- **Annual map refresh:** _(trigger — strategy change, leadership change)_
- **Quarterly scorecard review:** _(who attends, what decisions)_
- **Measure handoff to `performance`:** _(when formal metric definition moves plugins)_

## Seed examples

_(Existing strategy map or scorecard — highest-value seed for causal theory calibration.)_

- 

## Known gaps / things to revisit

-
