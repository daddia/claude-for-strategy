---
name: pre-mortem-and-red-team
description: >
  This skill should be used when the user asks to "run a pre-mortem on
  this decision," "red-team this recommendation," "what could kill this
  strategy," or has a near-final option, deal, or program that needs
  dis-confirming evidence, devil's-advocate challenge, and decision-quality
  scoring before commitment.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "consulting practice"
  review_cadence: "quarterly"
  work_shape: "option-evaluation"
  permission_tier: advisory
  output_class: "decision-support"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Pre-Mortem and Red Team

## When to use

Stress-test a recommendation, deal, or program **before** commitment — structured pre-mortem (assume failure, work backward), dis-confirming evidence hunt, devil's-advocate pass, and decision-quality score.

Use after analysis is drafted (`business-case`, `evaluate-strategic-option`, `map-competitive-landscape`) and before board, IC, or sponsor sign-off.

## What this skill does not do

- **Does not veto decisions** — surfaces failure modes and evidence gaps; strategist decides proceed / pivot / stop.
- **Does not replace legal, compliance, or security review** — flags when those lanes are needed.
- **Does not invent dis-confirming data** — names searches and witnesses needed; tags model knowledge `[verify]`.

## Preconditions

| Input | If missing |
|---|---|
| The recommendation or option under test | Ask — cannot pre-mortem without a stated bet |
| Decision audience and stakes | Ask once; calibrates depth |
| Supporting analysis artifact | Proceed from user summary; flag thin evidence |

## Provisional mode

Thin input: run abbreviated pre-mortem on stated recommendation only; confidence **structured first pass**; list evidence needed for full red-team.

## Trust spine

- **Confidence bands** (`option-evaluation`):
  - **High:** Dis-confirming search run; devil's-advocate challenges tied to evidence; decision-quality score with explicit kill triggers.
  - **Medium:** Pre-mortem complete; some dis-confirming paths unexplored — listed.
  - **Low:** Recommendation paraphrase only — scaffold, not clearance.
- **Strategic advice vs. support (mandatory):** Surfaces challenges; does not silently pick stop/go — `[review]` on proceed recommendation.
- **Accountability gap:** Decision-quality score forces engagement; no "looks fine" conclusion without scored dimensions.
- Per `../../references/trust-conventions.md` for GATE before external distribution.

## Assumption audit

| Assumption | Status | If wrong, what breaks |
|---|---|---|
| Success conditions are explicit | [stated / implied / missing] | Pre-mortem targets wrong failure |
| Key dependencies named | [complete / partial / unknown] | Blind spots in failure tree |
| Dissenting stakeholders identified | [named / unknown] | Devil's advocate too friendly |
| Evidence for headline claim | [sourced / partial / narrative only] | Red team argues past the analysis |

## Red flags

Pre-commitment review **non-negotiables**:

- **MUST NOT** declare proceed without a completed devil's-advocate pass — consensus without challenge tends to cause groupthink approval.
- **Do not proceed** to High confidence without listing at least three dis-confirming evidence items sought (found or `NOT FOUND — gap`).
- **Hard stop:** recommendation unchanged after red-team with zero mitigation actions — that signals checklist theatre, not decision quality.
- **MUST NOT** treat absence of dis-confirming evidence as confirmation — absence may mean search was too shallow.

## Outside-view step

Before the pre-mortem narrative, anchor with a **base-rate failure check**:

1. Name the reference class of similar decisions (deals, programs, strategies).
2. State the class base rate for failure, delay, or value miss (tag sources).
3. Ask: **does this proposal assume it will beat the class base rate?** If yes, name the mechanism — otherwise flag optimism.

**Always compare the proposal to class base-rate failure** because teams systematically believe their plan is the exception — untreated base rates tend to cause repeat of known failure modes.

## Workflow

**Before Step 1:** Read and apply `../../references/trust-conventions.md` — source-tagging, `[verify]` on model-only numbers, load-bearing assumptions at top, numbers provenance, confidence labeling, and board-ready gate.

### Step 1: Freeze the bet

Restate recommendation, success criteria, timeline, and stakeholders in one paragraph. Confirm with user.

### Step 2: Pre-mortem (prospective hindsight)

Assume the initiative failed badly 12–18 months out. Work backward: list 5–8 plausible failure stories — each with **early warning signal** and **leading indicator** that could be monitored now.

### Step 3: Dis-confirming evidence pass

For each load-bearing claim in the recommendation, ask: **what evidence would prove this wrong?** Run (or specify) searches for:

- Contradicting market or competitor data
- Internal track record contradicting the plan
- Expert or stakeholder dissent

Record each item: `DIS-CONFIRMING: [claim] — sought [evidence] — result [found / not found / gap]`.

**Must actively hunt dis-confirming evidence** because confirmation bias causes teams to assemble only supporting facts before major commits.

### Step 4: Devil's-advocate pass

Assign a explicit challenger stance (even if solo user — "argue as skeptical IC member"):

- Steelman the **stop** or **defer** case in three bullets.
- Name the **weakest link** in the recommendation's logic chain.
- State what would change the decision — kill triggers.

Do not soften the devil's-advocate voice to preserve rapport — softened challenge tends to cause false confidence.

### Step 5: Decision-quality score

Score 1–5 (1 = weak, 5 = strong) on:

| Dimension | Score | Rationale |
|---|---|---|
| Clarity of success criteria | | |
| Quality of dis-confirming search | | |
| Outside-view / base-rate alignment | | |
| Mitigations for top failure modes | | |
| Kill triggers defined and dated | | |

**Overall decision quality:** [average or min dimension] — proceed only with `[review]` if any dimension ≤2.

### Step 6: Red-team verdict

Synthesize: **Proceed / Proceed with conditions / Defer / Stop** — each condition or kill trigger explicit. GATE before board/exec externalization.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
BET UNDER TEST: [one paragraph]

BASE-RATE CHECK: [reference class] — failure/delay rate [X%] — proposal assumes [beats class / aligned / worse than class]

PRE-MORTEM FAILURE STORIES:
1. [story] — early warning: [...] — leading indicator: [...]
[repeat]

DIS-CONFIRMING EVIDENCE:
| Claim | Evidence sought | Result |
|---|---|---|

DEVIL'S ADVOCATE (stop/defer case):
- [...]

DECISION-QUALITY SCORE:
| Dimension | 1-5 | Note |
|---|---|---|
OVERALL: [score] — [review] if ≤2 on any dimension

VERDICT: [Proceed | Proceed with conditions | Defer | Stop]
CONDITIONS / KILL TRIGGERS: [...]
```

## Worked example

**Input:** Approve $8M CRM replacement; 9-month timeline; projected $5M benefits.

**Expected output (excerpt):**

```
BASE-RATE CHECK: CRM replacements in peer set — 45% miss timeline by >6 months [verify]
DIS-CONFIRMING: adoption at go-live — sought prior rollout NPS — NOT FOUND — gap
DEVIL'S ADVOCATE: Defer until integration dependency on Identity phase proven
DECISION-QUALITY SCORE: dis-confirming search = 2 — overall 2.4 [review]
VERDICT: Proceed with conditions — kill if Identity slip >8 weeks
```

## Quality checks before delivering

- [ ] Pre-mortem has ≥5 failure stories with early warnings
- [ ] Dis-confirming evidence table complete (gaps explicit)
- [ ] Devil's-advocate pass present and not softened
- [ ] Decision-quality score filled; low dimensions flagged `[review]`
- [ ] Base-rate / outside-view check included

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/consulting/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/consulting:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: revise `/transformation:business-case`, run `/consulting:exec-memo` for IC, or `/consulting:doc-reviewer` on updated narrative.
