<!--
Config location rules:
1. User data lives at ~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md — create parent dirs as needed.
2. If a populated profile exists at ~/.claude/plugins/cache/claude-for-strategy/pmo/*/CLAUDE.md but not at the config path, copy it forward before proceeding.
3. This file is the TEMPLATE. It ships with the plugin and is replaced on every plugin update. Never write user data here.

Shared org profile. Organisation-wide facts live in ~/.claude/plugins/config/claude-for-strategy/org-profile.md — read it before this file.
-->

# Practice Profile — pmo

> **Template only** — not read at runtime. `/pmo:practice-setup` writes your filled practice profile to `~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md`; every other skill reads from that path **and** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`. Edit the user config files directly for small fixes; re-run the interview for material changes. Other skills **propose profile updates** (show the change, ask, then write on confirmation) — only `practice-setup` auto-applies a full write.

## Status
`template` — run `/pmo:practice-setup` to fill this in.

## Who's using this

- **Role:** _(program manager, PMO lead, transformation office)_
- **Program scope:** _(single initiative, portfolio of workstreams, enterprise transformation)_

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| Slack | [PLACEHOLDER ✓/✗] | Status digests and escalation nudges degraded |
| Google Calendar | [PLACEHOLDER ✓/✗] | Steering prep without calendar context |
| Atlassian (Jira) | [PLACEHOLDER ✓/✗] | RAID and milestones from user uploads |
| Linear | [PLACEHOLDER ✓/✗] | RAID and milestones from user uploads |
| Asana | [PLACEHOLDER ✓/✗] | RAID and milestones from user uploads |
| Google Drive | [PLACEHOLDER ✓/✗] | User uploads status packs per task |

*Re-check: `/pmo:practice-setup --check-integrations`*

## Plugin-specific operating model

- **Governance cadence:** _(steering committee, working group, exec checkpoint)_
- **Status reporting rhythm per audience:** _(sponsor, steering, team)_
- **Milestone plan source:** _(Jira, spreadsheet, MS Project, etc.)_
- **Decision log practice:** _(where recorded, who maintains)_

## Framework preferences

- **RAID model:** _(columns, severity scale, ownership rules)_
- **RAG status model:** _(workstream health definitions)_
- **Critical path method:** _(how slippage is flagged, float tolerance)_
- **Avoid / do not default to:**

## Definitions and thresholds

- **Risk vs Issue vs Assumption vs Dependency:** _(your distinctions — vague definitions break status reports)_
- **RAG thresholds:** _(specific Red / Amber / Green criteria — not vibes)_
- **Escalation triggers:** _(severity, impact, or time-based — complement org escalation model)_
- **Slippage tolerance:** _(days or % before "at risk")_

## Output formats

- **Status report:** _(sections, length, RAG table layout)_
- **RAID log:** _(columns, ID scheme, review cadence)_
- **Decision log entry:** _(decision, rationale, owner, date)_
- **Steering pack:** _(pre-read vs live deck)_

## Review gates

- **Steering committee:** _(what must be true before steering — open issues, decision asks)_
- **Escalation above working level:** _(thresholds and approvers)_
- **External / sponsor distribution:** _(human review before send)_

## Seed examples

_(Prior status report, RAID log, or steering pack the interview was run against.)_

- 

## Known gaps / things to revisit

-
