---
name: cold-start-interview
description: >
  This skill should be used when the user runs
  "/corporate-strategy:cold-start-interview" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  corporate-strategy plugin," or wants to redo setup after the portfolio,
  growth ambition, or capital allocation process changes materially. Writes
  the shared org profile and the corporate-strategy practice profile.
allowed-tools: Read, Grep, Glob, Write
metadata:
  version: "0.2.0"
---

# Cold-Start Interview — corporate-strategy

## Shared framework

Read and follow `../../references/cold-start-framework.md` with `corporate-strategy` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/corporate-strategy/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied (sector, planning cadence, risk appetite, and escalation may already be in org profile):

1. **Full mode:** include a recent portfolio review or growth strategy deck.

2. **Portfolio** — businesses/products/segments and any strategic priority ranking.

3. **Growth ambition** — target rate, horizon, and source (board vs internal). Never leave blank — if unset, record that `assess-growth-vectors` must ask first.

4. **Capital allocation** — who decides, how often, known stickiness between strategy and funding.

5. **Risk posture and track record** — past M&A, entries, exits, and outcomes (calibrates `evaluate-strategic-option` and `synergy-stress-test`).

6. **Write profiles** following `../../references/org-profile-template.md` and `../../CLAUDE.md`.

7. **Confirm and summarize.**

## Living profile

**Profile paths:** org `org-profile.md`; plugin `corporate-strategy/CLAUDE.md` under `~/.claude/plugins/config/claude-for-strategy/`.

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills — org facts to org profile; portfolio/growth/allocation facts to plugin profile.
