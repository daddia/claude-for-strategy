---
name: cold-start-interview
description: >
  This skill should be used when the user runs
  "/pmo:cold-start-interview" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  pmo plugin," "teach Claude our governance cadence," or
  wants to redo that setup after the governance structure or reporting
  format changes materially. Writes the shared org profile and the pmo
  practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.2.0"
---

# Cold-Start Interview — pmo

Run before `raid-log`, `status-report`, `steering-pack`, `milestone-tracker`, or `decision-log` produce tailored output.

## Shared framework

Read and follow `../../references/cold-start-framework.md` with `pmo` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied (governance forums and escalation path may already be in org profile):

1. **Full mode:** review an existing status report, RAID log, or steering pack.

2. **Governance structure** — steering cadence; concrete escalation thresholds; RAID format and Risk/Issue/Assumption/Dependency definitions.

3. **Status reporting** — audiences, concrete RAG thresholds, cadence per audience.

4. **Milestone tracking** — where the plan lives; slippage tolerance before "at risk."

5. **Decision log** — format and storage location.

6. **Write profiles** — be precise on RAG and RAID distinctions.

7. **Confirm and summarize.**

## Living profile

**Profile paths:** org `org-profile.md`; plugin `pmo/CLAUDE.md` under `~/.claude/plugins/config/claude-for-strategy/`.

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills — org facts to org profile; RAID/RAG/milestone facts to plugin profile.
