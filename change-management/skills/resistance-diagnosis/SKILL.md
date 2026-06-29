---
name: resistance-diagnosis
description: >
  This skill should be used when the user describes "resistance to the
  change," "people pushing back," "adoption stalling," or "blockers on the
  people side" and needs root-cause split and response options before
  escalation or comms rework.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "change-management practice"
  review_cadence: "quarterly"
  work_shape: "hypothesis-driven-analysis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Resistance Diagnosis

## When to use

Diagnose observed resistance — separate symptoms from root causes; offer response options across sponsor, comms, training, and structural levers without mandating a single fix.

## What this skill does not do

- **Does not log governance decisions** — route continue/escalate calls to `/pmo:decision-log` when installed.
- **Does not label people as blockers** — describes behaviors and incentives, not character.
- **Does not recommend punitive action by default** — escalation is an option, not the default response.

## Preconditions

| Input | If missing |
|---|---|
| Observed resistance (quotes, behaviors, metrics) | Ask for specific examples |
| Stakeholder segment affected | Ask who; link to map if available |
| Practice profile resistance taxonomy | Use loss/competence/habit/politics defaults |

## Provisional mode

With anecdote only: hypothesize root causes; flag `[review]` — need corroboration before major escalation.

## Trust spine

- **Confidence bands** (`hypothesis-driven-analysis`):
  - **High:** Multiple independent observations; root cause tied to named loss or incentive.
  - **Medium:** Single source or manager report; hypotheses labeled.
  - **Low:** Vague "they don't like it" — ask for behaviors before prescribing.
- **Failure modes:**
  - **Analytical rigor:** Distinguish active sabotage from passive workarounds from capacity overload.
  - **Strategic advice vs. support:** Present response options; leadership owns escalation and trade-offs.

## Workflow

1. **Read practice profile** — resistance taxonomy, escalation thresholds, sponsor model.

2. **Document observed resistance** — behaviors (skipping training, shadow IT, public criticism, quiet non-use), not labels ("toxic," "blocker").

3. **Classify root cause** (may be multiple):
   - **Loss** — status, autonomy, relationships, job security.
   - **Competence** — fear of failing at new process; insufficient skill.
   - **Habit** — old way is faster under pressure; no muscle memory yet.
   - **Politics** — incentive misalignment; another leader's priority conflicts.
   - **Capacity** — change stacked on BAU with no time budget — often misread as attitude.

4. **Test hypotheses** — what evidence would confirm or falsify each cause; what question to ask the segment or manager.

5. **Response options** (pick subset relevant — do not recommend all):
   - **Sponsor** — visible removal of conflicting priority, personal ask to holdout influencer.
   - **Comms** — reframe WIIFM, address loss explicitly, manager talking points.
   - **Training** — job aid, coaching, safe practice environment.
   - **Structural** — metric change, role clarity, decision-rights fix (hand off to operating-model if needed).
   - **Timing** — narrow scope, pilot, defer — with trade-off stated.
   - **Escalation** — per profile threshold; what decision is needed from steering.

6. **Flag if resistance is rational** — when the new process is genuinely worse for the segment, say so `[review]` — comms cannot fix a bad design.

## Output format

```
SEGMENT: [name]
OBSERVED BEHAVIORS: [specific, sourced]

ROOT CAUSE ANALYSIS:
  Loss: [evidence or "not primary"]
  Competence: [...]
  Habit: [...]
  Politics: [...]
  Capacity: [...]

PRIMARY HYPOTHESIS: [cause] — [mechanism]
FALSIFICATION TEST: [question or evidence to gather]

RESPONSE OPTIONS:
  Sponsor: [option or "N/A"]
  Comms: [...]
  Training: [...]
  Structural: [...]
  Timing: [...]
  Escalation: [decision needed, or "below threshold"]

RATIONAL RESISTANCE FLAG: [yes — design issue | no]
```

## Worked example

**Input:** "Sales won't use the CRM."

**Expected output:** Split competence (slow on mobile) vs habit (spreadsheet faster); primary hypothesis = habit under quota pressure; sponsor option = remove parallel reporting ask; not "mandatory training again" as sole fix.

## Quality checks before delivering

- [ ] Behaviors documented, not personality labels
- [ ] Multiple causes considered
- [ ] Response options include trade-offs
- [ ] Rational resistance checked

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `sponsor-roadmap`, `communications-plan`, or `/pmo:decision-log` for escalation.
