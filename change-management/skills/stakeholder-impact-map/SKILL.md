---
name: stakeholder-impact-map
description: >
  This skill should be used when the user asks to "map stakeholders for
  this change," "who is affected and how," "build a stakeholder impact
  analysis," or needs influence/impact segmentation with specific behavior
  and process changes before readiness assessment or comms planning.
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
# Stakeholder Impact Map

## When to use

Segment stakeholders by influence and impact; name specific behavior, process, and system changes per group before readiness or comms work.

## What this skill does not do

- **Does not assess readiness** — route to `/change-management:change-readiness-assessment`.
- **Does not draft comms** — route to `/change-management:communications-plan`.
- **Does not design org structure** — route to `/operating-model:diagnose-structure-fit` when installed.

## Preconditions

| Input | If missing |
|---|---|
| Initiative scope or change description | Ask what is changing and for whom |
| Practice profile | Proceed with default segments; `[PROVISIONAL]` |
| TOM or roadmap output | Build from user input; note SOURCE |

## Provisional mode

Without named groups: infer from scope; flag `[review]` on incomplete coverage.

## Trust spine

Structured-aggregation bands; every segment tied to a concrete change; no generic "all employees affected."

## Workflow

1. **Read the practice profile** — segmentation model and change methodology from config paths.

2. **If `transformation` is installed**, read `/transformation:target-operating-model` or `/transformation:roadmap-builder` output as seed — reuse stated capability, process, and org impacts rather than reinventing.

3. **List stakeholder segments** — not just names but roles/groups with similar change exposure (e.g. frontline ops, regional managers, finance close team).

4. **For each segment, document**:
   - **Influence** — can accelerate or block adoption (high/medium/low with rationale).
   - **Impact** — degree of behavior, process, system, or reporting change (high/medium/low).
   - **What changes for them** — specific old → new behaviors; not "improved ways of working."
   - **What they lose** — status, autonomy, familiar tools, relationships — resistance often starts here.
   - **Primary channel to reach them** — from practice profile or inferred; flag if unknown.

5. **Place segments on influence/impact grid** — identify manage-closely (high/high), keep-informed, keep-satisfied, monitor.

6. **Coverage check** — flag segments with high impact but no identified owner or channel; flag "everyone" buckets that hide real differences.

## Output format

```
SOURCE: [TOM / roadmap / user input]

SEGMENT: [name]
  Influence: [H/M/L] — [why]
  Impact: [H/M/L] — [why]
  What changes: [specific behaviors/processes/systems]
  What they lose: [named losses, or "none identified"]
  Grid quadrant: [manage closely | keep informed | keep satisfied | monitor]
  Reach channel: [channel or UNKNOWN — flag]

[repeat per segment]

COVERAGE GAPS: [high-impact segments with no owner/channel, or "none"]
GENERIC-BUCKET FLAGS: [segments too broad to action, or "none"]
```

## Worked example

**Input:** CRM rollout, "sales team affected."

**Expected output:** Split by role (AE vs sales ops vs sales manager); each with different process change; flag generic bucket.

## Quality checks before delivering

- [ ] Every segment has influence, impact, and specific changes
- [ ] Losses named where plausible
- [ ] Coverage gaps listed

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `change-readiness-assessment` or `communications-plan`.
