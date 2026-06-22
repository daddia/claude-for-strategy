---
name: cold-start-interview
description: >
  This skill should be used when the user runs
  "/balanced-scorecard:cold-start-interview" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  balanced-scorecard plugin," "teach Claude our strategy map," or wants to
  redo that setup after the sector, perspective model, or cadence changes
  materially. Writes the shared org profile and the balanced-scorecard
  practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.2.0"
---

# Cold-Start Interview — balanced-scorecard

Sector determines the perspective set — get it right before anything else.

## Shared framework

Read and follow `../../references/cold-start-framework.md` with `balanced-scorecard` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/balanced-scorecard/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied (sector and planning cadence may already be in org profile):

1. **Full mode:** include an existing strategy map or scorecard.

2. **Sector model** — for-profit vs nonprofit/public/hybrid; top of causal chain (Financial vs Mission/Stakeholder). Perspective renames only when they clarify logic.

3. **Strategy map** — exists, location, last refresh.

4. **Measures** — target count (~20–25 default) and scoring/status convention.

5. **Cadences** — scorecard review vs strategy map review (separate, slower map cadence).

6. **Cascade** — levels and whether local objectives off the corporate map are healthy or should be flagged.

7. **Cross-plugin:** whether `okr` is installed and how layers relate.

8. **Write profiles** — sector and top perspective must be explicit, not silent defaults.

9. **Confirm and summarize.**

## Living profile

**Profile paths:** org `org-profile.md`; plugin `balanced-scorecard/CLAUDE.md` under `~/.claude/plugins/config/claude-for-strategy/`.

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills — org facts to org profile; BSC perspective/measure/cadence facts to plugin profile.
