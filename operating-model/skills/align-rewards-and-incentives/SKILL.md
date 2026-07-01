---
name: align-rewards-and-incentives
description: >
  This skill should be used when the user asks "will this reorg actually
  stick," "does our reward system support the structure we want," "why are
  people still behaving the old way after the reorg," or needs the
  proposed or current structure checked against rewards, process, and
  people capability for genuine alignment — the Star Model integration
  check.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "operating-model practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Align Rewards and Incentives

## When to use

Star Model integration check — whether rewards, processes, and capabilities reinforce structure intent, not just the org chart.

## What this skill does not do

- **Does not redesign structure** — route to `/operating-model:diagnose-structure-fit`.
- **Does not map external incentives** — route to `/market-intelligence:map-incentives` for competitors/partners.
- **Does not implement comp changes** — recommends specific changes for HR/leadership.

## Preconditions

| Input | If missing |
|---|---|
| Structure intent (current or proposed) | Ask what behavior the structure should produce |
| Reward mechanism (practice profile or user) | Ask how people are measured/paid; flag `[PROVISIONAL]` |
| Process and capability context | Ask; proceed with labeled gaps |

## Provisional mode

Without comp detail: reward fit labeled `[review]`; do not assert "supports" without mechanism evidence.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Reward, process, people checks complete with specific mechanisms named.
  - **Medium:** Some gaps inferred; verdict qualified.
  - **Low:** Structure intent unstated — halt.
- **Failure modes:**
  - **Strategic advice vs. support:** Verdict is diagnostic; leadership owns implementation.
  - **Client confidentiality:** Comp details highly sensitive — CONFIDENTIAL header; internal-only gate.
  - **Accountability gap:** "Structure alone sufficient" only when all three fits support intent.
  - **Analytical Rigor:** MECE across reward/process/people dimensions.
  - **Incentive Gaming:** Predicts behavior from actual incentives, not values statements.
- **Escalation triggers:** Reward system actively undermines structure — state plainly reorg will fail without reward change.

## Workflow

1. **Read practice profile** for how people are measured and paid.
2. **State structure's intent** plainly.
3. **Check reward fit** — apply `map-incentives` logic internally; predict behavior if unchanged.
4. **Check process fit** — approval chains, planning cycles assuming old structure.
5. **Check people/capability fit** — skills the new structure assumes.
6. **Recommend specific changes** beyond org chart.
7. **Completeness check** before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
STRUCTURE'S INTENT: [what behavior this is meant to produce]

REWARD FIT: [supports / undermines] — [specific mechanism, predicted behavior if unchanged]
PROCESS FIT: [processes still assuming old structure, if any]
PEOPLE/CAPABILITY FIT: [capability assumed — present / gap]

RECOMMENDED CHANGES (beyond the org chart): [reward, process, capability — specific]

VERDICT: [structure change alone is sufficient] or [structure change will likely NOT
  produce the intended behavior without the changes above]
```

## Worked example

**Input:** Matrix for cross-functional delivery; bonuses 100% on functional P&L.

**Expected output (excerpt):**

```
REWARD FIT: undermines — functional bonuses predict siloed behavior despite matrix [review]
VERDICT: structure change will likely NOT produce intended behavior without reward changes
```

## Quality checks before delivering

- [ ] Structure intent stated
- [ ] Reward fit uses incentive mechanism, not values doc
- [ ] Process and capability gaps named
- [ ] Verdict direct when misalignment real
- [ ] Comp-sensitive content gated

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/operating-model/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/operating-model:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: HR/people leadership review, `design-decision-rights`, or revise structure.
