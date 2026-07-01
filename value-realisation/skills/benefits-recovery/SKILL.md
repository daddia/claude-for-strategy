---
name: benefits-recovery
description: >
  This skill should be used when the user asks "this benefit is off
  track, what do we do," "should we keep chasing this saving or write
  it off," "diagnose why this benefit isn't showing up," or needs an
  at-risk benefit's root cause split apart and a continue-or-write-down
  decision made without sunk-cost bias.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "value-realisation practice"
  review_cadence: "quarterly"
  work_shape: "option-evaluation"
  permission_tier: advisory
  output_class: "decision-support"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Benefits Recovery

## When to use

At-risk benefits — root-cause split and continue-vs-write-down without sunk-cost bias.

## What this skill does not do

- **Does not remeasure** — uses tracking history from `benefits-tracking`.
- **Does not edit register silently** — write-down updates register with reason.

## Preconditions

| Input | If missing |
|---|---|
| Register entry + tracking history | Ask |
| Practice profile | Default conservative recovery test |

## Provisional mode

Marginal cost/remaining value estimates tagged `[review]` when data thin.

## Trust spine

Option-evaluation bands; sunk-cost bias flagged; MEASUREMENT LAG stand-down honored.

## Workflow

1. **Read the practice profile** — `~/.claude/plugins/config/claude-for-strategy/org-profile.md` and `~/.claude/plugins/config/claude-for-strategy/value-realisation/CLAUDE.md` — the benefit's register entry, and its full tracking history — the pattern across periods matters more than the most recent number alone.

2. **Run the diagnostic split.** Classify the root cause as exactly one of:
   - **MEASUREMENT LAG** — too little time has passed since the business change to expect the benefit to show up yet. Not actually at risk; say so and stand down the escalation rather than treating every early AT-RISK flag as real trouble.
   - **NOT EMBEDDED** — the business change itself wasn't adopted: training didn't land, the old process is still being used alongside or instead of the new one, the system is live but unused as designed. The fix is adoption work, not redesign.
   - **ENABLER GAP** — the underlying capability was descoped, delayed, or built differently than the benefit map assumed. The fix is closing the capability gap, not pushing harder on adoption of something that isn't actually there yet.
   - **THEORY PROBLEM** — the business change was embedded as designed, the enabler works as built, and the benefit still hasn't moved. The causal assumption made back in `benefits-map` was wrong. This needs revisiting the map's logic, not more push on execution that was never the actual gap — say this plainly even though it's the less comfortable conclusion.
   - **STRUCTURALLY LOST** — the realisation window has passed, or the business conditions the original case assumed no longer hold (the market moved, the cost line was restructured for unrelated reasons first). The benefit cannot be recovered as originally framed, regardless of further effort.

3. **For NOT EMBEDDED, ENABLER GAP, or THEORY PROBLEM, run the sunk-cost-clean recovery test**:
   - State the **remaining value** still achievable if recovery succeeds.
   - State the **marginal cost to recover from today** — the cost of the specific remediation needed from this point forward, not cumulative spend to date on the initiative.
   - Recommend **CONTINUE** only if marginal cost is credibly less than remaining value and a concrete remediation plan exists. Recommend **WRITE DOWN AND REALLOCATE** otherwise. If "we've already invested so much" appears anywhere in the reasoning for continuing, flag it explicitly as sunk-cost bias and ask whether the recommendation still holds once that reasoning is set aside.

4. **For STRUCTURALLY LOST, recommend a formal write-down.** The benefit moves to LAPSED in the register with the specific reason captured — don't let a lost benefit quietly drop out of the register with no recorded explanation; `realisation-review` needs that reason later for its optimism-bias calibration.

5. **If recommending CONTINUE, name the concrete operational change** — who does what differently from this point. A recovery decision with no specific remediation action attached is hope with extra paperwork, not a plan.

6. **Flag this decision to `pmo:decision-log`** if that plugin is installed — a continue-or-write-down call is a governance decision worth recording outside this plugin's own files.

## Output format

```
BENEFIT: [name]

ROOT CAUSE: [MEASUREMENT LAG | NOT EMBEDDED | ENABLER GAP | THEORY PROBLEM | STRUCTURALLY LOST]
  Evidence: [what in the tracking history supports this classification]

[if MEASUREMENT LAG]
VERDICT: stand down — re-check at [next due date]

[if NOT EMBEDDED / ENABLER GAP / THEORY PROBLEM]
Remaining value: [estimate]
Marginal cost to recover (from today): [estimate]
Sunk-cost check: [no sunk-cost reasoning present] or
  [FLAG — "already invested" language present; recommendation re-tested without it]
DECISION: [CONTINUE — plan: ...] or [WRITE DOWN AND REALLOCATE — reason: ...]
OPERATIONAL CHANGE (if CONTINUE): [who does what differently, from when]

[if STRUCTURALLY LOST]
DECISION: WRITE DOWN — reason for register: [specific reason]

LOGGED TO pmo:decision-log: [yes, if installed] or [pmo not installed — record manually]
```

## Worked example

**Input:** Benefit AT-RISK; team says "we've invested too much to stop."

**Expected output:** Sunk-cost FLAG; recommendation re-tested without cumulative spend reasoning.

## Quality checks before delivering

- [ ] Root cause classified with evidence
- [ ] Sunk-cost language checked
- [ ] CONTINUE has operational change plan

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/value-realisation/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/value-realisation:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `pmo:decision-log`, update register, or `realisation-review`.
