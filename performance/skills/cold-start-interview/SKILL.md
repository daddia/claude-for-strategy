---
name: cold-start-interview
description: >
  This skill should be used when the user runs
  "/performance:cold-start-interview" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  performance plugin," "teach Claude our KPI structure," or wants
  to redo that setup after the metric taxonomy or tracker structure changes
  materially. Writes the shared org profile and the performance practice
  profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.2.0"
---

# Cold-Start Interview — performance

Run before `tracker-builder`, `kpi-tree-builder`, `metrics-glossary`, or `performance-narrative` produce tailored output.

## Shared framework

Read and follow `../../references/cold-start-framework.md` with `performance` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/performance/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied (data systems and default audiences may already be in org profile):

1. **Full mode:** review an existing tracker if one exists.

2. **KPI taxonomy** — North Star metric(s); category codes and exact meanings.

3. **Tracker structure** — tool, summary sheet columns, daily/period log mechanism (AVERAGEIFS/SUMIFS etc.), refresh cadence.

4. **Reporting** — narrative audience and cadence (refine org default audiences if needed).

5. **Write profiles** — be precise on tracker structure; use "no existing tracker — `tracker-builder` will propose Daily Log + summary" if none.

6. **Confirm and summarize.**

## Living profile

**Profile paths:** org `org-profile.md`; plugin `performance/CLAUDE.md` under `~/.claude/plugins/config/claude-for-strategy/`.

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills — org facts to org profile; KPI/tracker/reporting facts to plugin profile.
