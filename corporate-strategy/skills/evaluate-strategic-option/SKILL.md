---
name: evaluate-strategic-option
description: >
  This skill should be used when the user asks to "evaluate this strategic
  option," "should we make this move," "build the case for/against this
  deal," or has a major strategic decision (market entry, M&A, large
  capital commitment) that needs real-options framing rather than a binary
  go/no-go.
allowed-tools: Read, Grep, Glob, Write
metadata:
  version: "0.3.0"
  owner: "corporate-strategy practice"
  review_cadence: "quarterly"
  work_shape: "option-evaluation"
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Evaluate Strategic Option

## When to use

Major strategic decisions needing staging, steelmanned case against, downside sizing, and pre-commitment kill criteria — not binary go/no-go.

## What this skill does not do

- **Does not evaluate vague topics** — requires committable decision with scope, scale, timing.
- **Does not soften case against for sponsors** — steelman is mandatory.
- **Does not pick winner when trade-offs unquantifiable** — say so.
- **Does not ship board-final without GATE.**

## Preconditions

| Input | If missing |
|---|---|
| Corporate-strategy + org profiles | `[PROVISIONAL]` balanced posture |
| Precise option statement | Ask once to narrow |

## Provisional mode

`[PROVISIONAL]` on risk posture; structured first pass if downside inputs missing.

## Trust spine

- **Strategic advice vs. support (mandatory):** Trade-offs and triggers; IC/board owns decision.
- Per trust-conventions for sourcing, assumptions, numbers, confidence, GATE.

## Workflow

### Step 1: State option precisely

Reject vague topics; require committable decision.

### Step 2: Staging checklist

If plausible: initial commitment, scale trigger, abandon trigger, learning objective. If not: say why.

### Step 3: Case for (brief)

3–5 bullets; tag unsourced claims.

### Step 4: Case against (steelman — mandatory)

Hardest assumption, cannibalization, timing illusion, integration load, comparable bias, reversibility, sponsor momentum — apply checklist.

### Step 5: Downside sizing + survivability test

Direct loss, opportunity cost, reputation, org strain. Survivable on failure: yes/no/unclear with evidence.

### Step 6: Kill criteria (pre-commitment)

Dated, specific; stage-1 vs full-program if staged.

### Step 7: Recommendation

Proceed staged | proceed in full | do not proceed — with confidence band.

## Output format

```
CONFIDENCE: [...]
LOAD-BEARING ASSUMPTIONS: [...]
OPTION: [precise decision]
CAN THIS BE STAGED: [...]
CASE FOR: [...]
CASE AGAINST (steelman): [...]
DOWNSIDE SIZING: [table]
SURVIVABLE ON FAILURE: [...]
KILL CRITERIA: [...]
RECOMMENDATION: [...]
```

## Worked example

**Input:** Acquire Company X at $Ym by Q3.

**Excerpt:** Staged: $Zm pilot with scale trigger on retention ≥X%; case against surfaces integration load on named function; kill criteria by date if metric below threshold; recommendation proceed staged `[review]`.

## Quality checks before delivering

- [ ] Committable option, not topic
- [ ] Staging checklist applied
- [ ] Steelman case against
- [ ] Survivability answered
- [ ] Kill criteria dated and specific

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: IC memo, `synergy-stress-test`, or `exit-or-double-down`.
