<!--
Config location rules:
1. User data lives at ~/.claude/plugins/config/claude-for-strategy/consulting/CLAUDE.md — create parent dirs as needed.
2. If a populated profile exists at ~/.claude/plugins/cache/claude-for-strategy/consulting/*/CLAUDE.md but not at the config path, copy it forward before proceeding.
3. This file is the TEMPLATE. It ships with the plugin and is replaced on every plugin update. Never write user data here.

Shared org profile. Organisation-wide facts (sector, cadence, risk appetite, audiences, financial conventions, escalation, house style) live in ~/.claude/plugins/config/claude-for-strategy/org-profile.md — shared by all plugins. Read it before this plugin's practice profile. If it doesn't exist, `/practice-setup` will create it.
-->

# Practice Profile — consulting

> **Template only** — not read at runtime. `/consulting:practice-setup` writes your filled practice profile to `~/.claude/plugins/config/claude-for-strategy/consulting/CLAUDE.md`; every other skill reads from that path **and** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`. Edit the user config files directly for small fixes; re-run the interview for material changes. Other skills **propose profile updates** (show the change, ask, then write on confirmation) — only `practice-setup` auto-applies a full write.

## Status
`template` — run `/consulting:practice-setup` to fill this in.

## Who's using this

- **Role:** _(strategy consultant, narrative lead, engagement manager, internal comms)_
- **Primary deliverable:** _(decks, memos, doc reviews, mixed)_
- **Engagement context:** _(see org profile — internal vs client/advisory)_

## Available integrations

| Integration | Status | Fallback if unavailable |
|---|---|---|
| Google Drive | [PLACEHOLDER ✓/✗] | User uploads seed decks/memos per task |
| Slack | [PLACEHOLDER ✓/✗] | Deliverables inline in session |
| Google Calendar | [PLACEHOLDER ✓/✗] | User states review/meeting dates manually |

*Re-check: `/consulting:practice-setup --check-integrations`*

## Plugin-specific operating model

- **Default workflow:** _(deck-first, memo-first, or problem-dependent)_
- **Review cycle before sponsor/client:** _(who sees drafts, in what order)_
- **Hypothesis vs exploration default:** _(start with a governing thought or build up from evidence)_
- **Engagement artifacts to preserve:** _(issue trees, storyline outlines, exhibit lists)_

## Framework preferences

- **Narrative spine:** _(strict Minto pyramid, BLUF-first, or looser consultative narrative — see `../../references/minto-pyramid.md`)_
- **Grouping logic:** _(deductive chain vs inductive/MECE buckets — see `../../references/mece.md`)_
- **Argumentation:** _(hypothesis-driven vs exploratory — see `../../references/hypothesis-driven-approach.md`)_
- **Avoid / do not default to:**

## Definitions and thresholds

- **Governing thought placement:** _(first line vs built over opening paragraph)_
- **Slide title rule:** _(action titles stating takeaway vs descriptive/topic titles)_
- **Exhibit numbering:** _(e.g. "Exhibit 1:", figure numbers, none)_
- **Memo length default:** _(one page, two pages, no default)_
- **"Load-bearing" assumption:** _(what counts as needing explicit surfacing per `../../references/trust-conventions.md`)_

## Output formats

- **Deck:** _(title slide conventions, section dividers, appendix rules)_
- **Memo:** _(header block, recommendation placement, exhibit attachment rules)_
- **Doc review / red-team:** _(commentary format, severity scale if used)_
- **Reviewer note block:** _(use trust-spine reviewer note above deliverables when material claims are present)_

## Review gates

- **Trust spine:** Market figures, benchmarks, and dollar amounts tagged; no invented numbers; load-bearing assumptions surfaced.
- **Sponsor / client draft:** _(what must be true before sharing outside the working team)_
- **Board / exec final:** _(explicit human gate before external distribution — skills must not treat output as final)_
- **Quiet mode:** _(suppress skill narration in client/board-facing deliverables; keep reviewer note for internal reviewer)_

## Seed examples

_(2–3 decks, memos, or reviews the interview was run against. Skills pattern-match tone and structure — not content.)_

- 
- 

## Known gaps / things to revisit

-
