<!--
Config location rules:
1. User data lives at ~/.claude/plugins/config/claude-for-strategy/transformation/CLAUDE.md — create parent dirs as needed.
2. If a populated profile exists at ~/.claude/plugins/cache/claude-for-strategy/transformation/*/CLAUDE.md but not at the config path, copy it forward before proceeding.
3. This file is the TEMPLATE. It ships with the plugin and is replaced on every plugin update. Never write user data here.

Shared org profile. Organisation-wide facts live in ~/.claude/plugins/config/claude-for-strategy/org-profile.md — read it before this file. Sector, planning cadence, risk appetite, financial conventions, and escalation belong there — not here.
-->

# Practice Profile — transformation

> **Template only** — not read at runtime. `/transformation:practice-setup` writes your filled practice profile to `~/.claude/plugins/config/claude-for-strategy/transformation/CLAUDE.md`; every other skill reads from that path **and** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`. Edit the user config files directly for small fixes; re-run the interview for material changes. Other skills **propose profile updates** (show the change, ask, then write on confirmation) — only `practice-setup` auto-applies a full write.

## Status
`template` — run `/transformation:practice-setup` to fill this in.

## Who's using this

- **Role:** _(transformation lead, enterprise architect, program director, advisor to sponsor)_
- **Where you sit relative to the program:** _(leading, advising, reporting to sponsor)_
- **Scope:** _(enterprise-wide, business unit, platform, or product line)_

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| Slack | [PLACEHOLDER ✓/✗] | Assumption-Decay and Roadmap-Drift watchers degraded; inline alerts only |
| Google Calendar | [PLACEHOLDER ✓/✗] | Steering prep without calendar context |
| Atlassian (Jira) | [PLACEHOLDER ✓/✗] | Roadmap/milestone status from user uploads |
| Linear | [PLACEHOLDER ✓/✗] | Roadmap/milestone status from user uploads |
| Asana | [PLACEHOLDER ✓/✗] | Roadmap/milestone status from user uploads |
| Google Drive | [PLACEHOLDER ✓/✗] | User uploads architecture docs and roadmaps per task |

*Re-check: `/transformation:practice-setup --check-integrations`*

## Plugin-specific operating model

- **Delivery model:** _(e.g. dual-track discovery/delivery, SAFe ARTs, stage-gate, federated squads)_
- **Release cadence:** _(continuous, monthly, quarterly, major/minor rhythm)_
- **Funding model:** _(central transformation fund, BU-funded, capex/opex split, stage-gate funding)_
- **Governance forums:** _(steering committee name, frequency, decision rights — complement org profile forums)_
- **Platform / architecture vocabulary:** _(named services — Identity, Events & Analytics, Edge BFF — or your terms)_
- **Planning horizon labels:** _(e.g. Now = this quarter, Next = 1–2 quarters, Later = beyond)_

## Framework preferences

- **Roadmap track model:** _(e.g. Strategy / Discovery / Delivery Refine / Delivery / Release — exact names and order)_
- **Maturity framework:** _(capability dimensions — Strategy / CX / Operations / Technology / Org / Culture, or other)_
- **Enterprise architecture principles:** _(list house EA rules — cloud-first, API-led, buy-build-partner, etc.)_
- **Target operating model method:** _(capabilities + processes + org + tech, or your variant)_
- **Avoid / do not default to:** _(generic Now/Next/Later if a named model exists)_

## Definitions and thresholds

- **Maturity scoring scale:** _(1–5 numeric, or Ad hoc / Emerging / Defined / Managed / Optimized)_
- **Transformation metrics:** _(north-star transformation KPIs — adoption, cost-out, cycle time, NPS, etc.)_
- **Technology constraints:** _(mandatory stacks, banned vendors, data residency, integration standards)_
- **Risk posture for sequencing:** _(conservative / balanced / aggressive — see org profile if recorded there)_
- **Business-case thresholds:** _(when a full case vs lightweight note is required)_

## Output formats

- **Roadmap:** _(horizon columns, track rows, dependency notation)_
- **Business case:** _(sections required — problem, options, cost/benefit, sequencing, risk, ask)_
- **Maturity assessment:** _(heatmap vs narrative, evidence requirements)_
- **TOM / tech strategy brief:** _(standard sections and depth)_

## Review gates

- **Discovery exit:** _(what evidence must exist before delivery funding)_
- **Steering committee:** _(what decisions require steering vs working-level)_
- **Investment / approval gates:** _(funding tranches, architecture review board, security review)_
- **Release gate:** _(go/no-go criteria, rollback rules)_
- **Trust spine:** No invented financials; tag benchmarks and assumptions per org financial conventions.

## Seed examples

_(Platform docs, prior roadmaps, TOM designs, or business cases the interview was run against.)_

- 

## Known gaps / things to revisit

-
