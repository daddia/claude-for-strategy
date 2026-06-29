<!--
Config location rules:
1. User data lives at ~/.claude/plugins/config/claude-for-strategy/okr/CLAUDE.md — create parent dirs as needed.
2. If a populated profile exists at ~/.claude/plugins/cache/claude-for-strategy/okr/*/CLAUDE.md but not at the config path, copy it forward before proceeding.
3. This file is the TEMPLATE. It ships with the plugin and is replaced on every plugin update. Never write user data here.

Shared org profile. Organisation-wide facts live in ~/.claude/plugins/config/claude-for-strategy/org-profile.md — read it before this file.
-->

# Practice Profile — okr

> **Template only** — not read at runtime. `/okr:practice-setup` writes your filled practice profile to `~/.claude/plugins/config/claude-for-strategy/okr/CLAUDE.md`; every other skill reads from that path **and** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`. Edit the user config files directly for small fixes; re-run the interview for material changes. Other skills **propose profile updates** (show the change, ask, then write on confirmation) — only `practice-setup` auto-applies a full write.

## Status
`template` — run `/okr:practice-setup` to fill this in.

## Who's using this

- **Role:** _(OKR cycle owner, team lead, chief of staff)_
- **Cascade scope:** _(company, department, team, individual)_

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| Atlassian (Jira / Confluence) | [PLACEHOLDER ✓/✗] | OKR artifacts in docs or plugin `data/` |
| Linear | [PLACEHOLDER ✓/✗] | OKR artifacts in docs or plugin `data/` |
| Slack | [PLACEHOLDER ✓/✗] | Check-in reminders inline only |
| `performance` plugin | [PLACEHOLDER ✓/✗] | `instrument-metrics` may duplicate metric work |

*Re-check: `/okr:practice-setup --check-integrations`*

## Plugin-specific operating model

- **Cycle length and calendar:** _(quarterly typical — start/end, planning window)_
- **Check-in frequency:** _(weekly, biweekly)_
- **Retro timing:** _(end of cycle, start of next)_
- **Calibration process:** _(exec review of targets and scoring)_
- **Artifact storage:** _(where objectives, KRs, and check-in log live)_

## Framework preferences

- **Philosophy:** _(commit-only vs commit + aspirational mix)_
- **Scoring scale:** _(0.0–1.0, percentage, RAG)_
- **Scoring formula:** _(linear interpolation baseline→target, or other)_
- **BSC / performance layering:** _(if installed — BSC themes vs OKR execution)_
- **Avoid / do not default to:**

## Definitions and thresholds

- **Max objectives per level:** _(e.g. 3–5)_
- **Max KRs per objective:** _(e.g. 2–5)_
- **Sandbagging risk:** _(history of target inflation/deflation)_
- **Aspirational KR expected score:** _(e.g. ~0.6–0.7 if mixed philosophy)_

## Output formats

- **OKR set:** _(wording style for Os and KRs, measurability rules)_
- **Check-in log entry:** _(confidence, blockers, next steps)_
- **Retro summary:** _(scoring table, learnings, carry-forwards)_

## Review gates

- **Target-setting approval:** _(manager, exec team, calibration session)_
- **End-of-cycle scoring sign-off:** _(who finalizes grades)_
- **Public vs internal OKRs:** _(what can be shared outside the org)_

## Seed examples

_(Prior cycle's OKRs with targets and actual scores — calibrates `set-targets` and `score-and-retro`.)_

- 

## Known gaps / things to revisit

-
