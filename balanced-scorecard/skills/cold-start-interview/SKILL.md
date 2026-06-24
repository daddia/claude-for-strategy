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
  version: "0.3.0"
  owner: "balanced-scorecard practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Cold-Start Interview — balanced-scorecard

## When to use

For strategy office, FP&A, or ops excellence leads configuring the balanced-scorecard plugin for the first time or after material change to sector model, perspective set, cadence, or cascade policy. Explicit invocation only (`disable-model-invocation: true`).

Sector determines the perspective set — get it right before anything else.

## What this skill does not do

- **Does not run BSC analysis skills** — sets up profiles that other skills read; does not build maps, measures, or scorecards during setup.
- **Does not auto-write without confirmation** — shows summary, waits for explicit yes, then writes.
- **Does not modify other plugins' profiles** — writes `org-profile.md` (shared) and `balanced-scorecard/CLAUDE.md` only.
- **Does not replace propose profile update** — other skills must show diffs and ask before profile changes.

## Preconditions

| Input | If missing |
|---|---|
| User intent (quick / full / redo / check-integrations / resume) | Detect existing setup per framework; offer quick vs full if unspecified |
| Write access to `~/.claude/plugins/config/claude-for-strategy/` | Explain path; create parent dirs on confirmed write |
| For `--resume`: `cold-start-resume.json` | Report no session; offer fresh start |

## Provisional mode

When user chooses `--quick` or org profile already complete:

- Skip org questions already answered in `org-profile.md`.
- Use sensible defaults for non-essential plugin fields; label defaults explicitly in summary (`[default — change on redo]`).
- Do not mark `Status: complete` with major blanks — use "see org profile" or "no strong preference" per framework.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Org + plugin summaries confirmed; sector and top perspective explicit; seed documents reviewed in full mode.
  - **Medium:** Quick mode with labeled defaults; some plugin fields deferred.
  - **Low:** Interview paused mid-way — resume file written; no profile write until resumed and confirmed.
- **Tag vocabulary:** `[review]` on ambiguous sector/top-perspective choices; `[verify]` on user-stated facts before writing to profile.
- **Failure modes:**
  - **Strategic advice vs. support:** Captures user's stated conventions; does not recommend perspective model — pressure-test questions only, strategist decides.
  - **Client confidentiality:** Profiles may contain proprietary org facts — remind user where files are stored; no paste into chat beyond summary.
  - **Accountability gap:** Summary shown before write; user must confirm explicitly — no silent profile updates.
  - **Analytical Rigor:** N/A — setup skill, not analysis.
  - **Incentive Gaming:** N/A — no scoring or tracking.
- **Escalation triggers:**
  - Hybrid sector (dual mission/financial primacy) → document pressure-test answer; flag `[review]` if unresolved.
  - Legacy profile at non-standard path → offer migration; do not delete without confirmation.
  - User cannot access seed documents → note gap; continue with interview answers only.
  - Install scope blocks file reads → explain user-scoped vs project-scoped per framework.

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

## Output format

Interview produces a **confirmation summary** (before write) and, on approval, written profile files:

```
ORG PROFILE CHANGES: [bullets or "none — already complete"]
PLUGIN PROFILE CHANGES: [bullets — sector, top perspective, map location, cadences, cascade policy, OKR layering]
DEFAULTS USED: [list or none]
FILES WRITTEN: [paths on confirmation]
```

## Worked example

**Input:** `--quick` for a for-profit SaaS. Org profile exists with industry and cadence. User answers: Financial top; map in Google Drive; quarterly scorecard review; annual map refresh; OKR installed for quarterly execution beneath BSC.

**Expected summary (excerpt, before write):**

```
ORG PROFILE CHANGES: none — already complete
PLUGIN PROFILE CHANGES:
  - Sector: for-profit; top perspective: Financial
  - Strategy map: Google Drive [link/path]; last refresh: 2024-Q4
  - Scorecard review: quarterly; map refresh: annual
  - Cascade: corporate → BU; local objectives allowed with flag
  - OKR layering: BSC = multi-year map; OKR = quarterly beneath objectives
DEFAULTS USED: target measure count ~20–25 [default]
```

User confirms → write both profile files → report paths and `--check-integrations` offer.

## Quality checks before delivering

- [ ] Existing setup detected per framework startup rules
- [ ] Org facts not re-asked when already in org profile
- [ ] Sector and top perspective explicit in summary
- [ ] Explicit confirmation received before any write
- [ ] `Status: complete` only when no major blanks remain
- [ ] Resume file deleted after successful write

## Outputs

Follows plugin `CLAUDE.md` § Outputs. After setup, natural next branches: `/balanced-scorecard:define-perspectives` (if perspectives not set), `/balanced-scorecard:build-strategy-map`, or `--check-integrations`.
