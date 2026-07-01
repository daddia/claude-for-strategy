---
name: map-information-asymmetry
description: >
  This skill should be used when the user asks to "where's the
  information asymmetry here," "are we the informed or uninformed party,"
  "how do we signal quality / screen for it," or has a negotiation, deal,
  or market situation where one party plausibly knows something the other
  doesn't.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "market-intelligence practice"
  review_cadence: "quarterly"
  work_shape: "hypothesis-driven-analysis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Map Information Asymmetry

## When to use

Negotiations, deals, hiring, customer relationships — when one party plausibly knows something the other doesn't and signaling/screening mechanics matter.

## What this skill does not do

- **Does not value the deal** — surfaces asymmetry implications; does not replace financial modeling.
- **Does not invent hidden information** — asks user or flags gaps `[review]`.
- **Does not recommend proceed/abandon** — states strategic implication; strategist decides.

## Preconditions

| Input | If missing |
|---|---|
| Situation stated precisely (deal, negotiation, relationship) | Ask once to narrow |
| Parties identified | Ask who is on each side |
| Known private information categories | Proceed with `[PROVISIONAL]` — label asymmetries as hypotheses |

## Provisional mode

Without diligence data: map hypothesized asymmetries tagged `[review]`; do not assert informed/uninformed position as fact.

## Trust spine

- **Confidence bands** (`hypothesis-driven-analysis`):
  - **High:** Concrete hidden-info categories per party; costly signal or screen mechanism named; adverse-selection assessed.
  - **Medium:** Some categories inferred; signal/screen options listed with gaps.
  - **Low:** Situation vague — refuse to map until scoped.
- **Failure modes:**
  - **Strategic advice vs. support:** Strategic implication is diagnostic, not a deal recommendation.
  - **Client confidentiality:** Deal terms and hidden info highly sensitive — CONFIDENTIAL header.
  - **Accountability gap:** Forces admission when user is uninformed party — `[review]` on exposure.
  - **Analytical Rigor:** Specific hidden-info categories; costly-signal test applied (cheap signals rejected).
  - **Incentive Gaming:** N/A — information-structure focus.
- **Escalation triggers:** Adverse-selection spiral present with no credible signal/screen — flag blocking risk.

## Workflow

1. **State the situation precisely.**
2. **List what each party knows that the other plausibly doesn't** — specific categories, not vague "knows more."
3. **Determine informed vs. uninformed side** — including when user is uninformed.
4. **If informed:** name credible costly signal available, or "none currently available."
5. **If uninformed:** name screening mechanism, or "none currently applied."
6. **Apply market-for-lemons logic** where quality is hard to verify pre-commitment.
7. **State strategic implication** — exploiting advantage, giving one away, or exposed.
8. **MECE check:** both parties' hidden-info lists complete for stated situation.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
SITUATION: [the deal/negotiation/relationship in question]

WHAT [PARTY A] KNOWS THAT [PARTY B] DOESN'T: [specific, concrete]
WHAT [PARTY B] KNOWS THAT [PARTY A] DOESN'T: [specific, concrete]

YOUR POSITION: [informed | uninformed] on [which specific asymmetry]

IF INFORMED: Available costly signal: [specific mechanism, or "none currently available"]
IF UNINFORMED: Available screening mechanism: [specific mechanism, or "none currently applied"]

ADVERSE SELECTION RISK: [present / not present — explain]

STRATEGIC IMPLICATION: [exploiting an advantage / giving one away / exposed to one — be direct]
```

## Worked example

**Input:** Acquiring a SaaS target; seller claims 5% churn; buyer lacks cohort data.

**Expected output (excerpt):**

```
CONFIDENCE: structured first pass
SITUATION: Acquisition of TargetCo at 8x ARR

WHAT SELLER KNOWS THAT BUYER DOESN'T: True logo churn by cohort, expansion vs. contraction drivers
WHAT BUYER KNOWS THAT SELLER DOESN'T: Integration cost estimate, synergy capture timeline

YOUR POSITION: uninformed on churn quality

IF UNINFORMED: Available screening mechanism: tiered earnout tied to net retention at 12 months [review]

ADVERSE SELECTION RISK: present — churn unverified pre-close may select for overstated retention

STRATEGIC IMPLICATION: exposed — price assumes stated churn; structure or diligence required before proceeding [review]
```

## Quality checks before delivering

- [ ] Hidden information specific, not vague
- [ ] Informed/uninformed position stated honestly
- [ ] Costly-signal test applied (cheap signals rejected)
- [ ] Strategic implication stated directly
- [ ] Output does not read as deal recommendation

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/market-intelligence/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/market-intelligence:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: diligence plan, deal-structure revision, or corp-strategy evaluation.
