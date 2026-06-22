---
name: cold-start-interview
description: >
  This skill should be used when the user runs
  "/transformation:cold-start-interview" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  transformation plugin," "teach Claude our platform context," or
  wants to redo that setup after the transformation program or platform
  context changes materially. Writes the shared org profile and the
  transformation practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.2.0"
---

# Cold-Start Interview — transformation

Run before `roadmap-builder`, `maturity-assessment`, `target-operating-model`, `tech-strategy-brief`, or `business-case` produce tailored output.

## Shared framework

Read and follow `../../references/cold-start-framework.md` with `transformation` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/transformation/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied (sector, risk appetite, financial conventions, and escalation may already be in org profile):

1. **Quick vs full** — full mode reviews a prior roadmap, architecture doc, or TOM design.

2. **Operating model** — delivery model, release cadence, funding model, governance forums, platform vocabulary, planning horizon labels.

3. **Framework preferences** — roadmap track model (exact names/order), maturity framework, enterprise architecture principles.

4. **Definitions** — maturity scoring scale, transformation metrics, technology constraints, business-case thresholds.

5. **Review gates** — discovery exit, steering decisions, investment/approval gates, release go/no-go.

6. **Role context** — where the user sits relative to the program (leading, advising, reporting).

7. **Write profiles** following `../../references/org-profile-template.md` and `../../CLAUDE.md`. Mark unanswered items as "no strong preference — will use generic defaults" so downstream skills fall back sensibly.

8. **Confirm and summarize.**

## Living profile

**Profile paths:** org `org-profile.md`; plugin `transformation/CLAUDE.md` under `~/.claude/plugins/config/claude-for-strategy/`.

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills — org facts to org profile; delivery/roadmap/maturity/EA facts to plugin profile.
