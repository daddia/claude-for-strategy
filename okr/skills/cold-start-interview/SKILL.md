---
name: cold-start-interview
description: >
  This skill should be used when the user runs "/okr:cold-start-interview"
  (with optional --quick, --full, --redo, --check-integrations, or --resume),
  asks to "set up the okr plugin," "teach Claude our OKR process," or wants
  to redo that setup after the cadence, scoring approach, or cascade
  structure changes materially. Writes the shared org profile and the okr
  practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.2.0"
---

# Cold-Start Interview — okr

The philosophy question matters more here than in most plugins — get it wrong and every other skill calibrates to the wrong culture.

## Shared framework

Read and follow `../../references/cold-start-framework.md` with `okr` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-strategy/org-profile.md`  
**Plugin profile:** `~/.claude/plugins/config/claude-for-strategy/okr/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied (planning cadence may already be in org profile):

1. **Full mode:** include a prior cycle's OKR set — objectives, KRs, targets, scores.

2. **Philosophy** — commit-only vs mixed committed/aspirational; explain the distinction if unsure. Note sandbagging or overreach history.

3. **Scoring** — scale and formula (default linear interpolation baseline→target).

4. **Cadence** — cycle length, check-in frequency, retro timing (`check-in-nudge` agent).

5. **Cascade structure** — levels and rough ceilings on objectives/KRs per level.

6. **Cross-plugin:** whether `performance` is installed (metric handoff to `instrument-metrics`).

7. **Write profiles** — Philosophy and Scoring must not be silent defaults; state explicit choices.

8. **Confirm and summarize.**

## Living profile

**Profile paths:** org `org-profile.md`; plugin `okr/CLAUDE.md` under `~/.claude/plugins/config/claude-for-strategy/`.

- **Auto-apply:** this skill only, after user confirms the summary.
- **Propose profile update:** all other skills — org facts to org profile; OKR philosophy/scoring/cascade facts to plugin profile.
