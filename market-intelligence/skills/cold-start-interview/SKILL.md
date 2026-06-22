---
name: cold-start-interview
description: >
  This skill should be used when the user runs
  "/market-intelligence:cold-start-interview" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  market-intelligence plugin," or wants to redo setup after the market
  definition, positioning, or competitor set changes materially. Writes the
  shared org profile and the market-intelligence practice profile.
allowed-tools: Read, Grep, Glob, Write
metadata:
  version: "0.2.0"
---

# Cold-Start Interview — market-intelligence

## Shared framework

Read and follow `../../references/cold-start-framework.md` with `market-intelligence` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/market-intelligence/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied (sector may already be in org profile):

1. **Full mode:** include a recent competitive landscape deck or win/loss analysis.

2. **Market definition** — who you actually compete with vs. what a skeptical outsider would list. Push on narrow answers.

3. **Positioning** — current claim and what's deliberately ruled out. Flag if no trade-off is named.

4. **Incentive context** — internal and external incentive structures with specifics for `map-incentives`.

5. **Signal monitoring** — what counts as a meaningful signal and preferred scan cadence.

6. **Write profiles** following `../../CLAUDE.md`.

7. **Confirm and summarize.**

## Living profile

**Profile paths:** org `org-profile.md`; plugin `market-intelligence/CLAUDE.md` under `~/.claude/plugins/config/claude-for-strategy/`.

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills — org facts to org profile; market/positioning/signal facts to plugin profile.
