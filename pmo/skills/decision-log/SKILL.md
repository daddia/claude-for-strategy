---
name: decision-log
description: >
  This skill should be used when the user asks to "log this decision,"
  "record why we decided X," or needs a decision and its rationale added to
  a persisted, append-only decision log for later audit or onboarding
  reference.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "pmo practice"
  review_cadence: "quarterly"
  work_shape: "governance-tracking"
  permission_tier: artefact-writer
  output_class: "tracking-update"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Decision Log

## When to use

Append decisions to persisted, append-only audit log — choice made, rationale, owner, revisit trigger.

## What this skill does not do

- **Does not edit past entries** — supersede with new entry referencing original date.
- **Does not log topics discussed** — requires precise decision statement.

## Preconditions

| Input | If missing |
|---|---|
| Decision statement | Ask — distinguish decision from topic |
| Rationale | Ask — required for audit value |
| Practice profile (format, location) | Use sensible default; flag `[PROVISIONAL]` |

## Provisional mode

Without rationale: halt and ask before appending.

## Trust spine

- **Confidence bands** (`governance-tracking`):
  - **High:** Decision, rationale, owner, date, revisit trigger captured; append-only preserved.
  - **Medium:** Revisit trigger "none specified" when user confirms none.
  - **Low:** Topic not decision — reject entry.
- **Failure modes:**
  - **Accountability gap:** Owner required; no anonymous decisions.
  - **Incentive Gaming:** N/A — audit trail focus.
- **Escalation triggers:** User asks to edit history — supersede pattern only.

## Workflow

1. Read practice profile for format and location.
2. Get current log — append only.
3. Capture decision precisely, rationale, owner, date, revisit trigger.
4. Output full updated log with NEW ENTRY block.
5. Gaming-pattern check: no retroactive edits.

## Output format

```
[Full decision log, existing entries unchanged]
NEW ENTRY:
Date: [date]
Decision: [precise statement]
Rationale: [why vs alternatives]
Owner: [who]
Revisit trigger: [trigger or none specified]
```

## Worked example

**Input:** "We decided Identity will be a shared platform service."

**Expected entry:** Decision precise; rationale asks if missing; owner recorded.

## Quality checks before delivering

- [ ] Decision not topic
- [ ] Rationale present
- [ ] Append-only — no edits to prior entries
- [ ] Owner named

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: reference in `steering-pack` or onboarding brief.
