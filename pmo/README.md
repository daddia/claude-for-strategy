# pmo

RAID logs, status reporting, steering committee packs, milestone tracking, and decision logs for running a transformation program.

## Agents

| Agent | What it does | Command |
|---|---|---|
| **RAID Logger** | Logs/updates a Risk, Assumption, Issue, or Dependency; flags escalation | `/pmo:raid-log` |
| **Status Reporter** | RAID log + milestones → audience-specific RAG status report | `/pmo:status-report` |
| **Steering Pack Builder** | Status + RAID + pending decisions → decision-led steering deck outline | `/pmo:steering-pack` |
| **Milestone Tracker** | Plan vs actual → critical-path status with slippage and knock-on effects | `/pmo:milestone-tracker` |
| **Decision Logger** | Appends a decision + rationale to a persisted, append-only audit log | `/pmo:decision-log` |
| **Escalation Watcher** | Weekly + post-`raid-log` scan for items crossing escalation threshold | scheduled agent |
| **Slippage Watcher** | Weekly critical-path milestone check against tolerance; flags knock-on effects | scheduled agent |
| **Steering Prep** | N days before steering (from `~~calendar`), assembles RAID + milestones + decisions for `/pmo:steering-pack` | scheduled agent |

## What this plugin does NOT do

- **Write directly into Jira, Asana, Linear, or Monday.com** — V1 works against log content you paste or point to; connectors are the path to live tracker integration.
- **Replace the program manager** — it drafts reports and flags escalation; humans own decisions and stakeholder management.
- **Post watcher alerts without `~~chat`** — Escalation Watcher, Slippage Watcher, and Steering Prep compile flags from log data and surface them in conversation when no chat connector is configured.

## Getting started

Run `/pmo:cold-start-interview` first. Your practice profile lands at `~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md`. The RAG definition and Risk/Issue/Assumption/Dependency distinctions are the sections most worth getting precise — vague thresholds are the most common cause of status reports that don't tell anyone anything.

### Living profile

- **Cold-start interview** — writes the full profile after you confirm the interview summary.
- **Any other skill** — when a stable convention surfaces (RAG thresholds, RAID definitions, escalation rules), skills **propose a profile update**: show the exact change, ask for confirmation, write only if you say yes.
- **Edit directly** — small fixes without re-running setup.

No environment variables or external connectors are required for V1.

## Usage

Typical cycle:

```
raid-log (ongoing, as risks/issues arise)
  ↓
status-report (weekly/per cadence, reads current RAID + milestones)
  ↓
steering-pack (per steering cadence, reads status-report + pending decisions)

milestone-tracker — run alongside, whenever a plan-vs-actual check is needed
decision-log — run whenever a decision is made, independent of the reporting cycle
```

Scheduled agents (configure `~~chat`; `steering-prep` also needs `~~calendar`):

```
escalation-watcher — weekly + after each raid-log; posts threshold crossings or all-clear
slippage-watcher — weekly critical-path check; flags knock-on effects, not just dates
steering-prep — N days before steering; assembles RAID + milestones + decisions for steering-pack
```

If [`consulting`](../consulting) is installed, hand `steering-pack` output to `/consulting:doc-reviewer` for a structural check before the meeting.

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/pmo:cold-start-interview` | cold-start-interview | Learns governance cadence, RAID/RAG definitions, escalation thresholds |
| `/pmo:raid-log` | raid-log | Log/update RAID item; flag escalation |
| `/pmo:status-report` | status-report | RAID + milestones → RAG status report |
| `/pmo:steering-pack` | steering-pack | Status + RAID + decisions → steering deck outline |
| `/pmo:milestone-tracker` | milestone-tracker | Plan vs actual → critical-path status |
| `/pmo:decision-log` | decision-log | Append decision + rationale to audit log |
| scheduled | escalation-watcher (agent) | Weekly + post-`raid-log` escalation scan via `~~chat` |
| scheduled | slippage-watcher (agent) | Weekly critical-path slippage check via `~~chat` |
| scheduled | steering-prep (agent) | Pre-steering brief from `~~calendar` + RAID/milestones/decisions |

## Trust spine

`status-report` and `steering-pack` each carry a condensed trust-spine block (sourcing tags, surfaced assumptions, no invented numbers, confidence labeling, board-ready gate). Full rules: [`consulting/references/trust-conventions.md`](../consulting/references/trust-conventions.md) when the consulting plugin is installed, or [`references/trust-conventions.md`](../references/trust-conventions.md) at repo root.

## Customization

See [CONNECTORS.md](./CONNECTORS.md). `~~spreadsheet` and `~~project tracker` are the natural home for the RAID log, milestone plan, and decision log once you move off pasted markdown.
