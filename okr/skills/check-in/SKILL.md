---
name: check-in
description: >
  This skill should be used when the user asks to "do a check-in on our
  KRs," "what's our confidence on this objective," "update our OKR
  status," or needs a confidence-based pulse logged for one or more key
  results — distinct from a project status report, which this is not.
allowed-tools: Read, Grep, Glob, Write
metadata:
  version: "0.3.0"
  owner: "okr practice"
  review_cadence: "quarterly"
  work_shape: "governance-tracking"
  permission_tier: artefact-writer
  output_class: "tracking-update"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Check-In

## When to use

Confidence pulse on KRs — "honest % chance of hitting target by cycle end" — not a project status update. Appends to persistent check-in log.

## What this skill does not do

- **Does not replace project status reports** — route to `/pmo:status-report`.
- **Does not score the cycle** — route to `/okr:score-and-retro`.
- **Does not set targets** — route to `/okr:set-targets`.

## Preconditions

| Input | If missing |
|---|---|
| KRs due for check-in | Ask which KRs to pulse |
| Practice profile (frequency, scale) | Default 0–100% confidence; flag `[PROVISIONAL]` |
| Existing check-in log (if any) | Start new log; note first entry |

## Provisional mode

Without prior log: no staleness/flat flags on first round; sharp-drop flags N/A until second entry.

## Trust spine

- **Confidence bands** (`governance-tracking`):
  - **High:** Every KR has confidence + what-changed line; flags applied per rules.
  - **Medium:** Some KRs missing what-changed — flag incomplete entries.
  - **Low:** Status-update narrative substituted for confidence numbers — reject format.
- **Failure modes:**
  - **Strategic advice vs. support:** Surfaces confidence and flags; does not recommend abandoning KRs.
  - **Client confidentiality:** Check-in log may be internal — CONFIDENTIAL header.
  - **Accountability gap:** Flat confidence across 3+ check-ins forces conversation flag.
  - **Analytical Rigor:** N/A — tracking shape.
  - **Incentive Gaming:** Flat or inflated confidence without what-changed flagged as disengagement pattern.
- **Escalation triggers:** Sharp confidence drop — surface prominently for manager conversation.

## Workflow

1. **Read practice profile** for check-in frequency and scoring scale.
2. **Get current check-in log** — append only, never restart.
3. **For each KR due:** confidence rating + required one-line what-changed.
4. **Flag staleness** — no check-in past one cycle beyond profile frequency.
5. **Flag flat confidence** — unchanged across 3+ consecutive check-ins.
6. **Flag sharp drops** — significant fall since last check-in.
7. **Gaming-pattern check** before output: confidence numbers have what-changed rationale.
8. **Persist** full updated log (append-only).

## Output format

```
[Full check-in log, existing entries unchanged]
NEW ENTRIES:

KR: [text]
  Confidence: [X%] (previous: [Y%])
  What changed: [one line]
  Flag: [none] or [stale | flat | sharp drop — escalate]

[repeat per KR checked in this round]
```

## Worked example

**Input:** KR "NPS 50 by Q3." Last confidence 70%. User: "Major customer churned; fix in progress."

**Expected output (excerpt):**

```
KR: NPS 50 by Q3
  Confidence: 45% (previous: 70%)
  What changed: Major customer churned; remediation in progress
  Flag: sharp drop — escalate
```

## Quality checks before delivering

- [ ] Confidence number per KR (not status narrative only)
- [ ] What-changed line present for every new entry
- [ ] Staleness, flat, and sharp-drop rules applied
- [ ] Log appended, not overwritten
- [ ] Gaming-pattern check run

## Propose profile update

When a stable convention surfaces during this run (check-in frequency, confidence scale, staleness thresholds, flat-confidence rules), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/okr/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/okr:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: manager conversation on flagged KRs, revise targets via `set-targets`, or continue cadence (`check-in-nudge` agent).

## Note

Logic also shipped as scheduled agent — see `agents/check-in-nudge.md`.
