<!--
Config location rules:
1. User data lives at ~/.claude/plugins/config/claude-for-strategy/operating-model/CLAUDE.md — create parent dirs as needed.
2. If a populated profile exists at ~/.claude/plugins/cache/claude-for-strategy/operating-model/*/CLAUDE.md but not at the config path, copy it forward before proceeding.
3. This file is the TEMPLATE. It ships with the plugin and is replaced on every plugin update. Never write user data here.

Shared org profile. Organisation-wide facts live in ~/.claude/plugins/config/claude-for-strategy/org-profile.md — read it before this file.
-->

# Practice Profile — operating-model

> **Template only** — not read at runtime. `/operating-model:cold-start-interview` writes your filled practice profile to `~/.claude/plugins/config/claude-for-strategy/operating-model/CLAUDE.md`; every other skill reads from that path **and** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`. Edit the user config files directly for small fixes; re-run the interview for material changes. Other skills **propose profile updates** (show the change, ask, then write on confirmation) — only cold-start auto-applies a full write.

## Status
`template` — run `/operating-model:cold-start-interview` to fill this in.

## Who's using this

- **Role:** _(org design lead, COO office, HR business partner, transformation architect)_
- **Mandate:** _(design new structure, fix decision rights, align incentives)_

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| HRIS | [PLACEHOLDER ✓/✗] | User provides org chart exports manually |
| Google Drive | [PLACEHOLDER ✓/✗] | User uploads RACI and org docs per task |
| Slack | [PLACEHOLDER ✓/✗] | Recommendations inline only |

*Re-check: `/operating-model:cold-start-interview --check-integrations`*

## Plugin-specific operating model

- **Current structure type:** _(functional, divisional, matrix, network)_
- **What structure optimizes for:** _(efficiency, innovation, customer intimacy, global/local balance)_
- **Org design process:** _(diagnose → design → socialize → implement)_
- **Decision-rights design cadence:** _(workshops, exec review, board notification)_

## Framework preferences

- **Decision-rights framework:** _(RACI, RAPID, DACI, or custom)_
- **Span and layers norms:** _(target spans by level, max layers)_
- **Matrix management rules:** _(dual reporting, tie-breakers)_
- **Rewards alignment method:** _(how stated values map to real incentives)_
- **Avoid / do not default to:**

## Definitions and thresholds

- **Span of control targets:** _(by function/level if known)_
- **Layer count:** _(top to frontline)_
- **Contested decisions:** _(known unclear or disputed ownership)_
- **Matrix relationships:** _(existing dual reports and tie-breaker rules)_
- **Reward mechanism:** _(how managers/teams are actually measured and paid)_

## Output formats

- **Org design memo:** _(options, recommendation, transition plan)_
- **Decision-rights artifact:** _(RACI/RAPID table format)_
- **Span/layers report:** _(thresholds and flags)_
- **Rewards alignment brief:** _(misalignment findings and fixes)_

## Review gates

- **HR / people leadership:** _(comp and role design changes)_
- **Exec approval:** _(structural changes with headcount or reporting impact)_
- **Sensitive content:** _(comp details — internal only, explicit gate before wider share)_

## Seed examples

_(Current org chart, RACI docs, compensation plan summaries.)_

- 

## Known gaps / things to revisit

-
