# change-management

Stakeholder impact mapping, change readiness assessment, sponsor roadmaps, communications planning, and resistance diagnosis — the people side of transformation, separate from program governance and operating model design.

## Agents

| Agent | What it does | Command |
|---|---|---|
| **Stakeholder Impact Mapper** | Initiative scope → influence/impact segmentation with specific behavior changes per group | `/change-management:stakeholder-impact-map` |
| **Readiness Assessor** | Context + stakeholders → people-side readiness scorecard with binding-constraint analysis | `/change-management:change-readiness-assessment` |
| **Sponsor Roadmap Builder** | Program phases → sponsor visibility, actions, and asks per checkpoint | `/change-management:sponsor-roadmap` |
| **Comms Planner** | Audiences and milestones → audience × message × channel × timing × owner plan | `/change-management:communications-plan` |
| **Resistance Diagnostician** | Observed resistance → root-cause split and response options | `/change-management:resistance-diagnosis` |

## Why this is a separate plugin from `transformation`, `operating-model`, and `pmo`

`transformation` designs *what* changes and sequences the work. `operating-model` designs *how the org is structured* to execute. `pmo` runs *program governance* — RAID, status, milestones, decisions. `change-management` owns the *people adoption path*: who is affected, whether they are ready, how sponsors show up, what gets communicated when, and how resistance gets diagnosed before it blocks go-live.

## What this plugin does NOT do

- **Replace L&D or comms teams** — training build and brand-approved send still belong to those functions; this plugin structures the plan and drafts.
- **Certify readiness or predict adoption rates** — assessments are structured first passes for your validation, not HR analytics.
- **Own program RAID or milestone tracking** — route blocking issues to [`/pmo:raid-log`](../pmo) when that plugin is installed.
- **Design org structure or decision rights** — route org-layer questions to [`/operating-model:diagnose-structure-fit`](../operating-model) when installed.

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/change-management:practice-setup` | practice-setup | Learns change methodology, sponsor model, comms approval path, and readiness gates — writes your practice profile |
| `/change-management:stakeholder-impact-map` | stakeholder-impact-map | Initiative scope → influence/impact segmentation with specific behavior and process changes per group |
| `/change-management:change-readiness-assessment` | change-readiness-assessment | Context + stakeholder map → readiness scorecard with binding-constraint analysis |
| `/change-management:sponsor-roadmap` | sponsor-roadmap | Program phase → sponsor visibility, actions, and asks per checkpoint |
| `/change-management:communications-plan` | communications-plan | Audiences and milestones → audience × message × channel × timing × owner plan |
| `/change-management:resistance-diagnosis` | resistance-diagnosis | Observed resistance → root-cause split and response options (sponsor, comms, training, structural) |

## Setup

Run `/change-management:practice-setup` first. The readiness-gate and sponsor-visibility questions matter most — vague "executive support" defaults produce generic sponsor roadmaps.

### Living profile

- **Practice setup** — writes the full profile after you confirm the interview summary.
- **Any other skill** — when a stable convention surfaces (resistance taxonomy, comms approval path, readiness RAG), skills **propose a profile update**: show the exact change, ask for confirmation, write only if you say yes.
- **Edit directly** — small fixes without re-running setup.

## Usage

Typical chains:

```
stakeholder-impact-map → change-readiness-assessment (who + how ready)
change-readiness-assessment → sponsor-roadmap (binding constraint informs sponsor asks)
stakeholder-impact-map → communications-plan (segments drive audiences)
resistance-diagnosis → sponsor-roadmap or communications-plan (targeted response)
```

If [`transformation`](../transformation) is installed, seed `stakeholder-impact-map` from `/transformation:target-operating-model` or `/transformation:roadmap-builder` output — the "what changes for whom" detail should not be reinvented.

If [`pmo`](../pmo) is installed, a `/change-management:resistance-diagnosis` escalation that needs a governance decision belongs in `/pmo:decision-log` — this plugin does not duplicate that log.

If [`consulting`](../consulting) is installed, hand `/change-management:communications-plan` or `/change-management:sponsor-roadmap` output to `/consulting:exec-memo` for a sponsor-ready one-pager.

## Trust spine

`change-readiness-assessment`, `sponsor-roadmap`, and `communications-plan` carry a condensed trust-spine block (sourcing tags, surfaced assumptions, no invented adoption numbers, confidence labeling). Full rules: [`consulting/references/trust-conventions.md`](../consulting/references/trust-conventions.md) when the consulting plugin is installed, or [`references/trust-conventions.md`](../references/trust-conventions.md) at repo root.

## Customization

See [CONNECTORS.md](./CONNECTORS.md) — `~~chat`, `~~calendar`, and `~~knowledge base` are the categories most specific to this plugin. V1 skills produce markdown output; wiring connectors lets skills ground against real comms history, calendar cadence, and stored change plans.
