---
name: communications-plan
description: >
  This skill should be used when the user asks for a "change comms plan,"
  "communications calendar for this transformation," "what do we tell each
  audience and when," or needs audience × message × channel × timing before
  go-live.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "change-management practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Communications Plan

## When to use

Build a structured comms plan from stakeholder segments and program milestones — completeness and sequencing, not polished copy.

## What this skill does not do

- **Does not send comms** — human approval per practice profile before external distribution.
- **Does not replace brand/comms team** — drafts structure; final voice and legal review stay with owners.
- **Does not map stakeholders** — route to `/change-management:stakeholder-impact-map` if audiences undefined.

## Preconditions

| Input | If missing |
|---|---|
| Stakeholder segments or audience list | Ask or infer from scope; flag gaps |
| Key milestones (go-live, pilot, training) | Ask timeline |
| Practice profile comms approval path | Note default approval; `[PROVISIONAL]` |

## Provisional mode

Without milestones: sequence by relative phase only (T-minus labels); flag dates as `[TBD]`.

## Trust spine

Structured-aggregation bands; every row has owner and approval note; no fabricated quotes from leadership.

## Workflow

1. **Read practice profile** — comms ownership, approval path, channel preferences.

2. **Use stakeholder impact map** if available — audiences = segments plus any additional governance audiences (steering, unions, regulators).

3. **For each milestone window**, define comms rows:
   - **Audience** — specific segment, not "all staff" unless truly universal.
   - **Message intent** — what they need to know, feel, or do (not full copy).
   - **Channel** — email, town hall, manager cascade, Slack, intranet — match segment reach from map.
   - **Timing** — date or T-minus relative to milestone.
   - **Sender** — who the audience must hear from (sponsor, manager, project, comms).
   - **Owner** — who drafts.
   - **Approval** — per profile path before send.

4. **Sequencing checks**:
   - Managers hear before their teams when cascade model applies.
   - "Why" before "what" before "how" for net-new change.
   - No surprise go-live announcement without prior awareness row — flag violation.

5. **Gap check** — high-impact segments with no comms row before go-live; duplicate messages to same audience same week.

## Output format

```
MILESTONES: [list with dates or T-labels]
APPROVAL PATH: [from profile or PROVISIONAL default]

| Timing | Audience | Message intent | Channel | Sender | Owner | Approval |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

SEQUENCING FLAGS: [violations, or "none"]
AUDIENCE GAPS: [high-impact segments with no row, or "none"]
DUPLICATE / NOISE FLAGS: [same audience overloaded, or "none"]
```

## Worked example

**Input:** CRM go-live Friday; no prior manager briefing row.

**Expected output:** SEQUENCING FLAGS — manager cascade missing before frontline announcement; add T-7 manager prep row.

## Quality checks before delivering

- [ ] Every high-impact segment has at least one pre-go-live row
- [ ] Approval path noted on every external-facing row
- [ ] Sequencing flags surfaced

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/change-management/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/change-management:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: draft copy in session or `/consulting:exec-memo` for sponsor summary when installed.
