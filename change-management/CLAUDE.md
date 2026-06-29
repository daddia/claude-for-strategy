<!--
Config location rules:
1. User data lives at ~/.claude/plugins/config/claude-for-strategy/change-management/CLAUDE.md — create parent dirs as needed.
2. If a populated profile exists at ~/.claude/plugins/cache/claude-for-strategy/change-management/*/CLAUDE.md but not at the config path, copy it forward before proceeding.
3. This file is the TEMPLATE. It ships with the plugin and is replaced on every plugin update. Never write user data here.

Shared org profile. Organisation-wide facts live in ~/.claude/plugins/config/claude-for-strategy/org-profile.md — read it before this file.
-->

# Practice Profile — change-management

> **Template only** — not read at runtime. `/change-management:practice-setup` writes your filled practice profile to `~/.claude/plugins/config/claude-for-strategy/change-management/CLAUDE.md`; every other skill reads from that path **and** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`. Edit the user config files directly for small fixes; re-run setup for material changes. Other skills **propose profile updates** (show the change, ask, then write on confirmation) — only practice-setup auto-applies a full write.

## Status
`template` — run `/change-management:practice-setup` to fill this in.

## Who's using this

- **Role:** _(change lead, OCM practitioner, transformation program manager, HR business partner supporting change)_
- **Program scope:** _(single initiative, multi-workstream transformation, enterprise-wide change)_
- **Where you sit relative to the program:** _(leading OCM, embedded in workstream, advising sponsor)_

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| Slack | [PLACEHOLDER ✓/✗] | Comms drafts and readiness nudges inline only |
| Google Calendar | [PLACEHOLDER ✓/✗] | User states town hall and go-live dates manually |
| Atlassian (Jira/Confluence) | [PLACEHOLDER ✓/✗] | User uploads stakeholder maps and comms plans per task |
| Google Drive | [PLACEHOLDER ✓/✗] | User uploads change plans and prior OCM artefacts per task |

*Re-check: `/change-management:practice-setup --check-integrations`*

## Plugin-specific operating model

- **Change methodology:** _(Prosci ADKAR, Kotter, house framework, or pragmatic hybrid — name it)_
- **Change network model:** _(executive sponsors, change champions, super-users, communities of practice — your terms)_
- **Comms ownership:** _(central comms team, program OCM, workstream leads — who drafts vs approves vs sends)_
- **Training ownership:** _(L&D, workstream, vendor — who builds and delivers)_
- **Readiness gate:** _(what must be true before go-live — sponsor visible, training complete, resistance plan in place)_

## Framework preferences

- **Readiness dimensions:** _(e.g. leadership alignment, past change history, capacity, culture, skills — your checklist)_
- **Stakeholder segmentation:** _(influence/impact grid, ADKAR by group, or custom segments)_
- **Resistance taxonomy:** _(loss types, competence fears, habit inertia, political blockers — your labels)_
- **Sponsor engagement model:** _(visible/available/active — your definitions and cadence)_
- **Avoid / do not default to:**

## Definitions and thresholds

- **"Ready" vs "willing":** _(your distinction — people who agree vs people who can actually perform)_
- **Minimum sponsor visibility:** _(what counts as sponsor showing up — town hall, email, floor walk)_
- **Comms approval path:** _(who signs off before external send)_
- **Escalation for blocking resistance:** _(threshold before sponsor or steering involvement)_
- **Go-live readiness RAG:** _(Red/Amber/Green criteria for people-side readiness — complement program RAG from pmo)_

## Output formats

- **Stakeholder impact map:** _(grid layout, narrative per segment, or both)_
- **Readiness assessment:** _(scorecard vs narrative; evidence requirements)_
- **Sponsor roadmap:** _(phase columns, checkpoint list, ask per checkpoint)_
- **Communications plan:** _(audience × message × channel × timing × owner table)_
- **Resistance diagnosis:** _(root-cause split + response options — not a single mandated fix)_

## Review gates

- **Comms external send:** _(human approval before distribution outside working team)_
- **Sponsor-facing materials:** _(what sponsor must review before use)_
- **Go-live people readiness:** _(explicit gate — who signs off that adoption risk is acceptable)_
- **Trust spine:** No invented adoption rates or sentiment scores; tag assumptions per org financial and people conventions.

## Seed examples

_(Prior stakeholder map, comms plan, readiness assessment, or sponsor checklist the interview was run against.)_

-

## Known gaps / things to revisit

-
