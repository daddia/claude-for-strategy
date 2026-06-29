---
name: raid-log
description: >
  This skill should be used when the user asks to "log this risk," "add an
  issue to the RAID log," "update the RAID log," or needs a risk,
  assumption, issue, or dependency added to or updated in a persisted RAID
  log.
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
# RAID Log

## When to use

Append/update persisted RAID log using profile definitions and severity scale — escalation threshold enforced.

## What this skill does not do

- **Does not downgrade severity to avoid escalation** — severity laundering guarded.
- **Does not leave entries unowned.**
- **Does not output only new row** — full updated log for save-back.

## Preconditions

| Input | If missing |
|---|---|
| Entry to log (description) | Ask |
| Current RAID log | Create new if none; use profile format |
| Practice profile (RAID definitions, severity, escalation) | Sensible default; `[PROVISIONAL]` |

## Provisional mode

Ambiguous Risk vs Assumption: ask using profile definitions — don't guess.

## Trust spine

- **Confidence bands** (`governance-tracking`):
  - **High:** Classified, severity with rationale, owner assigned, escalation flagged if threshold met.
  - **Medium:** Classification confirmed with user.
  - **Low:** Severity without rationale — require one-line rationale.
- **Failure modes:**
  - **Incentive Gaming:** Guards severity laundering — downgrading risks to assumptions or softening language.
- **Escalation triggers:** Entry meets profile threshold — **ESCALATION FLAG** explicit, not deferred.

## Workflow

1. Read profile for RAID format, definitions, severity scale.
2. Get current log.
3. Classify entry — ask if ambiguous.
4. Assign severity with one-line rationale.
5. Assign owner.
6. Check escalation threshold.
7. Output full updated log + ESCALATION FLAG if applicable.
8. Gaming-pattern check before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
[Full RAID log table]

ESCALATION FLAG: [if threshold met — why]
```

## Worked example

**Input:** "Vendor may slip delivery" logged as Assumption, severity Low, no owner.

**Expected output:** Reclassify as Risk `[review]`; severity rationale required; owner assigned; escalation assessed.

## Quality checks before delivering

- [ ] Profile definitions used for classification
- [ ] Severity has rationale
- [ ] Owner assigned
- [ ] Full log output
- [ ] Escalation flag when threshold met
- [ ] Gaming-pattern check run

## Propose profile update

When a stable convention surfaces during this run (RAID column names, Risk/Issue/Assumption definitions, severity scale, escalation thresholds), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/pmo:cold-start-interview` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: escalate now, include in `status-report`, or `steering-pack`.
