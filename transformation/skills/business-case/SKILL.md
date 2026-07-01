---
name: business-case
description: >
  This skill should be used when the user asks to "build the business case
  for this transformation," "write up the cost-benefit for this initiative,"
  or needs scope, cost, benefit, sequencing, risk, and a specific ask pulled
  together into a decision-ready business case.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.4.0"
  owner: "transformation practice"
  review_cadence: "quarterly"
  work_shape: "option-evaluation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Business Case

## When to use

Decision-ready transformation business case — problem, options, cost/benefit, sequencing, risk, specific ask; BLUF structured.

## What this skill does not do

- **Does not invent financials** — tag assumptions; `INPUT NEEDED` for missing costs.
- **Does not approve funding** — draft for sponsor/finance gate.
- **Does not sequence roadmap** — hand off detail to `/transformation:roadmap-builder`.

## Preconditions

Load org + transformation profiles before building; provisional mode on user request.

## Provisional mode

See workflow section below — generic defaults with `[PROVISIONAL]` tags.

## Trust spine

Option-evaluation bands; benefit confidence labels; GATE before board/exec final. Guards invented financials and unsigned assumptions.

## Assumption audit

Before drafting options, surface every load-bearing assumption explicitly — not buried in tables:

| Assumption | Source | If wrong, what breaks |
|---|---|---|
| Adoption / uptake rate | [sourced / user estimate / unknown] | Benefit case collapses or shifts payback |
| Cost estimate completeness | [sourced / partial / missing] | ROI overstated |
| Timeline to value | [sourced / judgment / unknown] | Sequencing and funding tranches misaligned |
| Baseline performance | [measured / inferred / missing] | Delta benefits invented |
| Dependency readiness | [confirmed / assumed / unknown] | Recommended option not executable |

**Do not proceed to a defensible recommendation** when adoption, baseline, or cost completeness are all `unknown` without tagging confidence **structured first pass** and listing assumptions in `LOAD-BEARING ASSUMPTIONS`.

## Red flags

These checks are **non-negotiable** — halt and fix before delivering a board- or finance-facing final:

- **MUST NOT** present ROI, NPV, or payback without sourced baseline and cost inputs — use `INPUT NEEDED` instead.
- **MUST NOT** treat soft benefits as hard P&L without a confidence label and mechanism — optimism bias causes boards to fund on phantom cash.
- **Do not proceed** if the recommended option lacks kill/revisit criteria dated before the decision — without them, sunk-cost momentum tends to cause spend continuation after failure signals.
- **Hard stop:** any hard benefit line with Low confidence that carries more than 25% of the headline case value — escalate to sponsor before polish.

## Outside-view step

After Step 5 (benefit realism), run a **reference-class check** before sensitivity:

1. Name 2–3 comparable initiatives (same org, peer sector, or public case studies) with documented cost/benefit/timeline outcomes.
2. Compare this case's headline timeline and benefit uplift to the reference-class median — if this case is faster or larger than the class without explicit rationale, apply an optimism-bias uplift per HM Treasury Green Book guidance (state the % applied and why) or downgrade confidence.
3. Record in output: `OUTSIDE-VIEW: [reference class] — median realisation [X%]; this case [above/at/below] class; adjustment [none | haircut Y%]`.

**Always apply a reference-class haircut to benefit timelines** because optimism bias causes systematic overstatement of delivery speed and adoption — the Green Book documents this as a demonstrated, systematic tendency.

## Purpose

Produce a decision-ready business case the sponsor or finance team can act on in one pass — not a generic transformation template. Every option has scope, cost, benefit, and timeline; every benefit line carries a confidence label; the recommendation is stated before the supporting tables.

## Precondition: load profiles

**Before building the case, read both:**

- `~/.claude/plugins/config/claude-for-strategy/org-profile.md` — financial conventions, planning cadence, risk appetite, escalation
- `~/.claude/plugins/config/claude-for-strategy/transformation/CLAUDE.md` — delivery model, funding model, governance forums, business-case thresholds, risk posture

If either file is missing or still has template placeholders, surface this bounce:

> I notice your practice profile isn't configured yet — that's how I tailor options discipline, approval gates, and risk framing to your org.
>
> **Two choices:**
> - Run `/transformation:practice-setup` (a few minutes) to configure your profile, then I'll build a case calibrated to your governance and funding model.
> - Say **"provisional"** and I'll build against generic defaults — balanced risk posture, quarterly planning, standard four-option structure — and tag every output `[PROVISIONAL — configure your profile for tailored output]`.

### Provisional mode

If the user says "provisional," run the workflow using: balanced risk posture, no named approval gates (flag "confirm with finance/sponsor"), generic Now/Next/Later sequencing grain, business-case threshold = full case above $500K `[unverified — generic default]`. Tag the reviewer note and confidence line with `[PROVISIONAL]`. At the end, append:

> "That was a generic run. Run `/transformation:practice-setup` to calibrate approval gates, funding model, and business-case thresholds to your org."

## Workflow

**Before Step 1:** Read and apply `../../references/trust-conventions.md` — source-tagging, `[verify]` on model-only numbers, load-bearing assumptions at top, numbers provenance, confidence labeling, and board-ready gate.

### Step 1: Orient

Confirm before drafting:

| Question | Answer |
|---|---|
| **Decision type** | Invest / defer / stop / re-sequence / fund discovery |
| **Audience** | Board / ELT / sponsor / finance / delivery forum |
| **Initiative** | Name and scope boundary |
| **Evidence pack** | Costs, baseline, benefits, dependencies, risks — what's in hand vs missing |

If decision type or audience is unclear, ask once. The same underlying analysis produces different emphasis: finance needs cost rigor; board needs the ask and kill criteria; delivery forum needs sequencing and dependencies.

### Step 2: Evidence gap check

Inventory the evidence pack explicitly. **Do not silently assume missing inputs.**

| Input | Status |
|---|---|
| One-time and run-rate costs | Provided / partial / missing |
| Baseline metrics | Provided / partial / missing |
| Benefit quantification | Provided / partial / missing |
| Dependencies | Provided / partial / missing |
| Risk register | Provided / partial / missing |

**If financials are missing or partial:** produce a **structured first pass** — problem, options, qualitative benefits, sequencing, risks, and explicit `INPUT NEEDED` lines. **Do not fabricate ROI, NPV, or payback.** State: "ROI/payback withheld — baseline and cost inputs not provided."

**Connector-sourced figures:** When costs or benefits are pulled from `~~bi analytics`, `~~spreadsheet`, or finance MCP connectors, tag each number `[sourced: <connector>, <dataset>, <as-of>]` before it appears in options tables. Failed or partial connector pulls become `INPUT NEEDED`, not estimates.

**If only soft benefits exist:** quantify only what's sourced; classify the rest (see Step 4) and keep overall confidence at **structured first pass**.

### Step 3: State the problem precisely

What specifically isn't working, for whom, measured how. A vague problem produces a vague recommendation regardless of cost/benefit formatting.

### Step 4: Options discipline

Lay out exactly four option types unless the user narrows scope:

| Option | Purpose |
|---|---|
| **Do nothing** | True baseline — cost of inaction, not a straw man |
| **Minimum viable change** | Smallest credible move that addresses the core problem |
| **Recommended** | The option this case advocates |
| **Bolder option** | Higher scope/cost upside case for comparison |

For each: scope, one-time cost, ongoing cost, timeline to value. Use `INPUT NEEDED` for missing cost lines — never round-number placeholders.

### Step 5: Benefit realism

Classify every benefit line:

| Type | Definition |
|---|---|
| **Hard benefit** | Quantifiable P&L or cash impact with a traceable baseline |
| **Soft benefit** | Real but hard to monetize — productivity, satisfaction, speed |
| **Risk avoidance** | Cost or exposure prevented — state the risk event and range |
| **Capability value** | Strategic optionality — state what decision it unlocks later |

**Confidence label per benefit line:** High (sourced baseline + conservative assumption) / Medium (partial data or judgment-heavy) / Low (directional only). A case with any load-bearing Low-confidence hard benefit stays **structured first pass**.

### Step 6: Sensitivity table

When any hard benefit or cost is quantified, add a sensitivity table — vary the 1-2 load-bearing assumptions (adoption rate, cost estimate, timeline slip) and show impact on the headline outcome. If nothing is quantified, include:

```
SENSITIVITY: Withheld — no quantified benefits/costs to stress-test. Run again when [specific inputs] are available.
```

### Step 7: Sequencing, risks, and kill criteria

**Sequencing:** headline phasing for the recommended option. Hand off to `roadmap-builder` for detailed phasing if approved; stay at headline level here.

**Risks:** initiative-specific, not generic transformation boilerplate. Each risk: likelihood, mitigation, owner if known.

**Kill / revisit criteria** — set before the decision, not after momentum builds:

```
KILL / REVISIT CRITERIA:
- Abandon if: [specific, dated trigger]
- Revisit assumptions if: [specific trigger]
- Escalate to [forum from profile] if: [cost/schedule/risk threshold]
```

Check `## Review gates` in the transformation profile for named approval forums.

### Step 8: Recommendation and ask

**State the recommendation first** (BLUF), then supporting tables.

**Ask:** budget amount (or range), decision needed, by when, from whom. Route to the approval gate matching audience and dollar value from the profile — name a role, not "get approval."

### Step 9: Board-ready gate

If audience is board, ELT, or external finance sign-off, run the trust-spine **GATE** before the polished final. Working drafts and "for discussion" versions skip the gate but keep confidence labels.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
DECISION TYPE: [invest | defer | stop | re-sequence | fund discovery]
AUDIENCE: [board | ELT | sponsor | finance | delivery forum]

LOAD-BEARING ASSUMPTIONS:
- [assumption] — if wrong: [impact]

RECOMMENDATION: [one to two sentences — BLUF]

PROBLEM: [specific, measurable]

WHY THIS OPTION:
1. [point]
2. [point]
3. [point]

OPTIONS:
| Option | Scope | One-time cost | Ongoing cost | Benefit summary | Time to value |
|---|---|---|---|---|---|
| Do nothing | ... | ... | ... | ... | ... |
| Minimum viable | ... | ... | ... | ... | ... |
| Recommended | ... | ... | ... | ... | ... |
| Bolder | ... | ... | ... | ... | ... |

BENEFITS (recommended option):
| Benefit | Type | Amount/range | Confidence | Source |
|---|---|---|---|---|
| ... | hard/soft/risk avoidance/capability | ... | H/M/L | [sourced: …] or INPUT NEEDED |

SENSITIVITY:
| Assumption | Base | Downside | Upside | Impact on case |
|---|---|---|---|---|

SEQUENCING: [headline phasing]

RISKS:
| Risk | Likelihood | Mitigation | Owner |
|---|---|---|---|

KILL / REVISIT CRITERIA:
- ...

ASK: [budget/decision, by when, from whom]
APPROVAL ROUTING: [named forum/role per profile thresholds]

EVIDENCE GAPS: [what's still INPUT NEEDED before this becomes defensible]
```

## Quality checks before delivering

- [ ] Both profiles loaded (or `[PROVISIONAL]` tagged)
- [ ] Decision type and audience confirmed
- [ ] Four-option discipline applied (or scope explained if fewer)
- [ ] No invented financials — gaps flagged as `INPUT NEEDED`
- [ ] Every benefit line has type and confidence label
- [ ] Kill/revisit criteria are specific and dated
- [ ] Recommendation appears before detailed tables (BLUF)
- [ ] Board/exec final has reviewer note if gate was run

## Worked example

**Input:** Platform consolidation initiative; sponsor audience; partial cost data.

**Expected output (excerpt):**

```
RECOMMENDATION: Proceed with minimum viable consolidation — staged funding reduces risk [review]
CONFIDENCE: structured first pass
EVIDENCE GAPS: INPUT NEEDED — integration run-rate from finance
```

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/transformation/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/transformation:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. End with decision tree — fill cost inputs, approve and hand off to `roadmap-builder`, finance validation, defer, or escalate per profile forums.
