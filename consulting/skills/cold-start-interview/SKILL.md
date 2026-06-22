---
name: cold-start-interview
description: >
  This skill should be used when the user runs "/consulting:cold-start-interview"
  (with optional --quick, --full, --redo, --check-integrations, or --resume),
  asks to "set up consulting", "configure my narrative conventions", or
  "teach Claude my deck/memo style" for the first time, or wants to redo that
  setup after it materially changes. Writes the shared org profile and the
  consulting practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.2.0"
---

# Cold-Start Interview — consulting

Run this before any other skill in the plugin produces meaningfully tailored output. Skipping setup is the most common reason output comes back generic.

## Shared framework

Read and follow `../../references/cold-start-framework.md` with `consulting` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/consulting/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied (default audiences and house writing style may already be in org profile):

1. **Quick vs full** — full mode reviews 2–3 seed decks, memos, or doc reviews for tone and structure.

2. **Operating model** — deck-first vs memo-first workflow; who reviews before sponsor/client.

3. **Narrative conventions** — Minto strictness, grouping logic (deductive vs inductive/MECE), governing thought placement.

4. **Deck and memo conventions** — action vs topic slide titles; exhibit numbering; memo length; house templates.

5. **Review gates** — trust-spine expectations; when output is draft vs sponsor-ready vs board-final.

6. **Write profiles** to the paths above, following `../../references/org-profile-template.md` and `../../CLAUDE.md`. Do not modify the installed plugin templates. Use "no strong preference — will infer per task" or "see org profile" rather than leaving blanks.

7. **Confirm and summarize** in plain language. Remind the user they can edit config files directly, accept **propose profile update** from other skills, or re-run with `--redo`.

## Living profile

**Profile paths:** org `org-profile.md`; plugin `consulting/CLAUDE.md` under `~/.claude/plugins/config/claude-for-strategy/`.

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills — org facts (audience, tone, terminology) to org profile; narrative/deck/memo conventions to plugin profile.

## Notes

- If the user has no strong opinions, record "no strong preference" and let downstream skills default to `../../references/minto-pyramid.md`, `../../references/hypothesis-driven-approach.md`, `../../references/bluf-conventions.md`, `../../references/mece.md`, and `../../references/trust-conventions.md`.
