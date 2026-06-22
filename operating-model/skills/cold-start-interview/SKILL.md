---
name: cold-start-interview
description: >
  This skill should be used when the user runs
  "/operating-model:cold-start-interview" (with optional --quick, --full,
  --redo, --check-integrations, or --resume), asks to "set up the
  operating-model plugin," or wants to redo setup after the structure,
  decision rights, or reward mechanics change materially. Writes the shared
  org profile and the operating-model practice profile.
allowed-tools: Read, Grep, Glob, Write
metadata:
  version: "0.2.0"
---

# Cold-Start Interview — operating-model

## Shared framework

Read and follow `../../references/cold-start-framework.md` with `operating-model` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/operating-model/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied:

1. **Full mode:** include a current org chart and any existing RACI documentation as seed documents.

2. **Structure fit** — what the structure is meant to optimize for (efficiency/scale, innovation/speed, customer intimacy, coordination across geography/business lines). Push for a real answer; `diagnose-structure-fit` needs a genuine priority.

3. **Decision-rights gaps** — decisions everyone privately agrees are unclear or contested in ownership.

4. **Matrix relationships** — dual reporting and whether tie-breaker rules exist ("no known tie-breaker" is valid).

5. **Span and layers** — typical team sizes by function, layers from top to frontline.

6. **Rewards and incentives** — how people are actually measured and paid, not the values document. Re-ask if the answer sounds sanitized.

7. **Write profiles** to the paths above, following `../../CLAUDE.md`.

8. **Confirm and summarize.**

## Living profile

**Profile paths:** org `org-profile.md`; plugin `operating-model/CLAUDE.md` under `~/.claude/plugins/config/claude-for-strategy/`.

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills — org facts to org profile; structure/RACI/span/rewards facts to plugin profile.
