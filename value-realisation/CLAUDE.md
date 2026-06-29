<!--
Config location rules:
1. User data lives at ~/.claude/plugins/config/claude-for-strategy/value-realisation/CLAUDE.md — create parent dirs as needed.
2. If a populated profile exists at ~/.claude/plugins/cache/claude-for-strategy/value-realisation/*/CLAUDE.md but not at the config path, copy it forward before proceeding.
3. This file is the TEMPLATE. It ships with the plugin and is replaced on every plugin update. Never write user data here.

Shared org profile. Organisation-wide facts live in ~/.claude/plugins/config/claude-for-strategy/org-profile.md — read it before this file. Sector, planning cadence, risk appetite, financial conventions, and escalation belong there — not here.
-->

# Practice Profile — value-realisation

> **Template only** — not read at runtime. `/value-realisation:cold-start-interview` writes your filled practice profile to `~/.claude/plugins/config/claude-for-strategy/value-realisation/CLAUDE.md`; every other skill reads from that path **and** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`. Edit the user config files directly for small fixes; re-run the interview for material changes. Other skills **propose profile updates** (show the change, ask, then write on confirmation) — only cold-start auto-applies a full write.

## Status
`template` — run `/value-realisation:cold-start-interview` to fill this in.

## Who's using this

- **Role:** _(benefits owner, value-realisation lead, transformation PMO, finance business partner)_
- **Scope:** _(single initiative, program portfolio, enterprise benefits register)_
- **Relationship to delivery:** _(post-implementation audit vs embedded in program team)_

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| Slack | [PLACEHOLDER ✓/✗] | Checkpoint reminders surface inline; owner nudges degraded |
| Google Mail | [PLACEHOLDER ✓/✗] | Stakeholder context from user uploads |
| Google Drive | [PLACEHOLDER ✓/✗] | User uploads business cases and registers per task |
| Google Calendar | [PLACEHOLDER ✓/✗] | Go-live and baseline cutoff dates stated manually |
| Atlassian (Jira / Confluence) | [PLACEHOLDER ✓/✗] | Benefits register and tracking from user uploads |
| Linear | [PLACEHOLDER ✓/✗] | Benefits tracking from user uploads |
| Asana | [PLACEHOLDER ✓/✗] | Benefits tracking from user uploads |

*Re-check: `/value-realisation:cold-start-interview --check-integrations`*

## Plugin-specific operating model

- **Benefit owner role:** _(who typically holds this — a business sponsor, ops lead — and is it already distinguished from the delivery PM today?)_
- **Escalation path for at-risk benefits:** _(who decides to continue funding recovery vs. write down)_
- **Decision log / RAID home:** _(e.g. `pmo:decision-log`, or somewhere else)_
- **Typical realisation window:** _(e.g. 6/12/24 months post go-live)_
- **Tracking cadence:** _(monthly, quarterly)_
- **Realisation review cadence/trigger:** _(end of window, program closure, annual portfolio cycle)_

## Framework preferences

- **Named framework, if any:** _(e.g. Cranfield Benefits Management, HM Treasury's five-case model, an internal house framework — or none yet)_
- **Benefit type taxonomy:** _(cash-releasing / cash-releasable / non-cash — your own labels if different)_
- **Benefit-to-objective linkage convention:** _(how benefits trace to strategic objectives, OKRs, or BSC themes)_
- **Avoid / do not default to:**

## Definitions and thresholds

- **Current baseline discipline:** _(are baselines normally captured before change starts, or reconstructed afterward — be honest here; this is the single most common gap)_
- **Default measurement source:** _(system of record, manual extract, survey)_
- **Attribution convention:** _(formal counterfactual/control group, or judgment-based discount for external factors)_
- **Baseline window before go-live:** _(how far ahead missing baselines trigger escalation)_
- **At-risk threshold:** _(variance from baseline or target that triggers recovery review)_

## Output formats

- **Benefits dependency network:** _(notation for enabler → change → benefit → objective)_
- **Benefits register entry:** _(baseline, target, owner, realisation date fields)_
- **Tracking period record:** _(attribution call required per period)_
- **Recovery decision:** _(root-cause classification + continue-or-write-down)_
- **Realisation review:** _(portfolio PIR sections, optimism-bias calibration output)_

## Review gates

- **Baseline capture:** _(what must be true before go-live — no retrofitted baseline treated as clean without flag)_
- **Continue-or-write-down:** _(who approves recovery spend vs. formal write-down)_
- **Portfolio PIR:** _(audience and distribution before steering or finance)_
- **Trust spine:** No invented benefit numbers; tag benchmarks and attribution assumptions per org financial conventions.

## Seed examples

_(A prior business case with a benefits section, an existing benefits register or tracker, a past post-implementation review.)_

-

## Known gaps / things to revisit

-
