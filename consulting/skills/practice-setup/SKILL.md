---
name: practice-setup
description: >
  This skill should be used when the user runs "/consulting:practice-setup"
  (with optional --quick, --full, --redo, --check-integrations, or --resume),
  asks to "set up consulting", "configure my narrative conventions", or
  "teach Claude my deck/memo style" for the first time, or wants to redo that
  setup after it materially changes. Writes the shared org profile and the
  consulting practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "consulting practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Practice Setup — consulting

## When to use

Run before any other consulting skill produces tailored output. For narrative leads, engagement managers, or consultants configuring deck/memo conventions. Explicit invocation only.

## What this skill does not do

- **Does not produce deliverables** — configures profiles other skills read.
- **Does not auto-write without confirmation** — summary first, write on explicit yes.
- **Does not modify plugin templates** in the repo — writes user config only.

## Preconditions

| Input | If missing |
|---|---|
| User intent (quick/full/redo/check-integrations/resume) | Detect setup; offer quick vs full |
| Write access to config path | Explain path on confirmed write |

## Provisional mode

Quick mode or complete org profile: skip answered org questions; use "no strong preference" for unset plugin fields per Notes below.

## Trust spine

- **Confidence bands** (`structured-aggregation`): High = confirmed summary + seed review in full mode; Medium = quick with defaults; Low = paused — resume file only.
- **Failure modes:** Captures user conventions, does not impose Minto strictness; confidentiality on seed docs; explicit confirmation before write.
- **Escalation:** Legacy profile paths → offer migration; install scope blocks reads → explain per framework.

## Shared framework

Read and follow `../../references/practice-setup-framework.md` with `consulting` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/consulting/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied:

1. **Quick vs full** — full mode reviews 2–3 seed decks, memos, or doc reviews for tone and structure.
2. **Operating model** — deck-first vs memo-first; who reviews before sponsor/client.
3. **Narrative conventions** — Minto strictness, grouping logic, governing thought placement.
4. **Deck and memo conventions** — action vs topic slide titles; exhibit numbering; memo length.
5. **Review gates** — trust-spine expectations; draft vs sponsor-ready vs board-final.
6. **Write profiles** per framework; no blanks — use "no strong preference" or "see org profile".
7. **Confirm and summarize.**

## Living profile

- **Auto-apply:** this skill only, after confirmation.
- **Propose profile update:** all other skills.

## Notes

If no strong opinions, record "no strong preference" and default downstream to `minto-pyramid.md`, `hypothesis-driven-approach.md`, `bluf-conventions.md`, `mece.md`, `trust-conventions.md`.

## Output format

```
ORG PROFILE CHANGES: [...]
PLUGIN PROFILE CHANGES: [operating model, narrative, deck/memo, review gates]
DEFAULTS USED: [...]
FILES WRITTEN: [on confirmation]
```

## Worked example

**Input:** `--quick`, memo-first firm, strict Minto, action slide titles. Org profile complete.

**Summary excerpt:** Plugin profile: memo-first; Minto strict; action titles; sponsor review before client; trust spine on all material claims.

## Quality checks before delivering

- [ ] Framework startup rules followed
- [ ] Explicit confirmation before write
- [ ] No strong preference recorded where user deferred

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `/consulting:deck-outline`, `/consulting:exec-memo`, or `--check-integrations`.
