---
name: sponsor-roadmap
description: >
  This skill should be used when the user asks for a "sponsor roadmap,"
  "what should the executive sponsor do and when," "sponsor engagement
  plan," or needs visible sponsor actions aligned to program phases and
  readiness gaps.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "change-management practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Sponsor Roadmap

## When to use

Build a phase-aligned plan of sponsor visibility, actions, and asks — tuned to binding readiness constraints, not generic "executive support."

## What this skill does not do

- **Does not write comms copy** — route message drafting to `/change-management:communications-plan`.
- **Does not assign sponsor** — assumes named sponsor exists; flags if missing.
- **Does not replace steering governance** — major go/no-go stays with program forums.

## Preconditions

| Input | If missing |
|---|---|
| Program phases or milestones | Ask timeline; infer from roadmap if provided |
| Practice profile sponsor definitions | Use visible/available/active defaults; `[PROVISIONAL]` |
| Readiness assessment (recommended) | Build generic roadmap; flag untargeted asks |

## Provisional mode

Without named sponsor: produce role-based roadmap; flag `[review]` — cannot calibrate to individual capacity.

## Trust spine

- **Confidence bands** (`narrative-synthesis`):
  - **High:** Each checkpoint traces to readiness gap or phase gate; asks are specific and doable.
  - **Medium:** Phases clear; some asks generic pending readiness input.
  - **Low:** Sponsor unnamed or phases unstated — scaffold only.
- **Failure modes:**
  - **Analytical rigor:** Every ask must be observable — "support the change" is not an action.
  - **Strategic advice vs. support:** Sponsor chooses which asks to accept; roadmap presents options.

## Workflow

1. **Read practice profile** — sponsor visibility definitions, cadence, escalation path.

2. **If readiness assessment exists**, anchor high-priority checkpoints to binding constraint response (e.g. sponsor floor walk before go-live if frontline able-risk).

3. **Map program phases** — launch, build, pilot, go-live, sustain, reinforce (or user's labels from transformation roadmap).

4. **For each phase, define**:
   - **Visibility** — what the organization must see the sponsor do (town hall, video, site visit — per profile).
   - **Availability** — office hours, escalation path, decision turnaround.
   - **Active removal of blockers** — specific decisions or resource calls only the sponsor can make.
   - **Ask of sponsor** — time-bound, observable, tied to a segment or dimension.

5. **Anti-pattern check** — flag checkpoints that duplicate comms team work without sponsor-specific leverage; flag "send an email" as sole visible action.

## Output format

```
SPONSOR: [name or ROLE TBD — flag if unknown]
PROGRAM PHASES: [list]

PHASE: [name]
  Visibility: [observable actions]
  Availability: [cadence / channel]
  Active blockers: [decisions only sponsor can make]
  Ask: [specific, time-bound]
  Traces to: [readiness dimension or stakeholder segment]

[repeat per phase]

UNTARGETED ASKS: [generic items flagged for refinement, or "none"]
SPONSOR CAPACITY FLAGS: [too many asks in one week, or "none"]
```

## Worked example

**Input:** Go-live in 6 weeks, binding constraint = manager coaching not happening.

**Expected output:** Phase "pre-go-live" includes sponsor-led manager forum and explicit ask to remove conflicting priorities — not another all-hands slide.

## Quality checks before delivering

- [ ] Every ask is observable and time-bound
- [ ] High-priority asks trace to readiness gap if assessment provided
- [ ] Generic "support change" language removed

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/change-management/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/change-management:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `communications-plan` or hand to `/consulting:exec-memo` when installed.
