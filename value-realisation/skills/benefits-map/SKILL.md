---
name: benefits-map
description: >
  This skill should be used when the user asks to "map the benefits for
  this initiative," "build a benefits dependency network," "what are we
  actually claiming this will deliver," or needs an approved business
  case's benefit claims decomposed into enablers, business changes, and
  benefits before a register can be built.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.4.0"
  owner: "value-realisation practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Benefits Map

## When to use

Decompose benefit claims into enabler → business change → benefit → strategic objective before register build.

## What this skill does not do

- **Does not set baselines** — route to `/value-realisation:benefits-register`.
- **Does not track actuals** — route to `/value-realisation:benefits-tracking`.

## Preconditions

| Input | If missing |
|---|---|
| Practice profile | Proceed with default chain; `[PROVISIONAL]` |
| Source business case or strategic option | Build from user input; note SOURCE |

## Provisional mode

Default enabler→change→benefit chain; conservative deadweight and cash-type flags.

## Trust spine

Structured-aggregation bands; benefit-washing and deadweight checks; orphan/coverage gaps flagged.

## Assumption audit

Before building chains, audit assumptions embedded in the source business case:

| Assumption | Status | If wrong, what breaks |
|---|---|---|
| Business change will occur as described | [named roles / generic / missing] | Benefit-washing undetected |
| Baseline will be captured before go-live | [committed / planned / unknown] | Register built on retrofitted numbers |
| Benefit type classification (cash vs non-cash) | [explicit / implied / wrong] | Headline value overstated |
| Deadweight / attribution | [considered / ignored / unknown] | Inflated initiative credit |
| Strategic objective linkage | [traced / asserted / orphan] | Portfolio alignment fiction |

Echo material assumptions in the output when status is not `explicit` or `committed`.

## Red flags

Value-realisation mapping has **non-negotiable** quality gates:

- **MUST NOT** accept "system delivered" as a benefit — deliverables are enablers; missing business change causes benefit-washing.
- **Do not proceed** to register handoff if cash-releasable benefits are labeled as guaranteed cash-releasing — misclassification causes finance to book unrealised savings.
- **Hard stop:** orphan benefits with no strategic objective and no user acknowledgment — scope creep tends to cause unfunded workstreams.
- **MUST NOT** skip the deadweight check on quantified benefits — existing trends cause false attribution.

## Outside-view step

After step 6 (deadweight), apply a **base-rate realisation check** per benefit type:

1. Pull org track record from the value-realisation profile if configured; otherwise use conservative industry base rates (cash-releasing hard benefits often realise 50–70% of plan at 12 months post go-live — tag `[model knowledge — verify]`).
2. For each quantified benefit, state: `BASE-RATE CHECK: planned [X] vs class median realisation [Y%] — [aligned / optimistic — flag for business-case calibration]`.
3. If multiple benefits are optimistic vs. class, recommend `/value-realisation:realisation-review` calibration input for future cases.

**Always run a base-rate realisation check on quantified benefits** because benefit-washing causes registers to track deliverables that never produce measurable value.

## Workflow

1. **Read the practice profile** — `~/.claude/plugins/config/claude-for-strategy/org-profile.md` and `~/.claude/plugins/config/claude-for-strategy/value-realisation/CLAUDE.md` — for the benefit type taxonomy and named framework, if any. If `transformation` or `corporate-strategy` is installed, read the relevant `/transformation:business-case` or `/corporate-strategy:evaluate-strategic-option` output as the seed rather than starting from a blank page — the case's cost/benefit table is the input, not a separate exercise.

2. **For each benefit claimed in the source material, build the chain**:
   - **Enabler** — the capability actually being delivered (a system, a process, a policy, a tool).
   - **Business change** — what someone does differently *because* the enabler exists. Name the actual role and the actual changed behavior, not "improved ways of working."
   - **Benefit** — the measurable improvement that results from the business change. This is what gets tracked, not the enabler.
   - **Strategic objective** — the corporate goal this benefit ultimately serves.

3. **Run the benefit-washing test on every claimed benefit**: if the enabler were delivered and *nobody changed how they work*, would this benefit still show up? If yes, it isn't really dependent on the business change — question whether it's a benefit at all, or an assumption riding along on the project that should be reframed or dropped. If the honest answer is "only if people work differently," confirm that dependency is named explicitly in the chain — an unembedded business change is the single most common reason a mapped benefit later fails to materialize, and `benefits-recovery` will need this dependency stated to diagnose that failure mode later.

4. **Classify every benefit by type**: cash-releasing (frees actual budget that can be removed), cash-releasable (frees capacity that *could* be cashed but might instead be reinvested), or non-cash/qualitative (real, but not financially quantifiable — don't force a fake number onto it). Flag explicitly if a cash-releasable benefit is being presented in the source material as if it were guaranteed cash-releasing — that's a common and material distortion to catch before it reaches a register.

5. **Check every benefit traces to a stated strategic objective.** Flag orphan benefits — plausible-sounding improvements with no real strategic linkage — and question whether they belong in scope at all. Separately, check coverage the other way: does every stated strategic objective actually have a benefit mapped to it that would prove it, or is there a gap a skeptical reader would notice?

6. **Flag deadweight candidates** — benefits that would plausibly have occurred anyway, without this initiative, due to an existing trend or a change already underway elsewhere. Naming this at mapping stage, before it's baked into a register's headline numbers, is far cheaper than discovering it during `benefits-tracking`'s attribution check.

## Output format

```
SOURCE: [business case / strategic option this map is built from, or "none — built from user input"]

BENEFIT: [name]
  Enabler: [what's actually being delivered]
  Business change: [who does what differently, specifically]
  Benefit type: [cash-releasing | cash-releasable | non-cash/qualitative]
  Strategic objective served: [name]
  Benefit-washing check: [PASS — genuinely dependent on the business change]
                        or [FLAG — would occur even with no behavior change; reconsider]
  Deadweight check: [clean] or [FLAG — plausible without this initiative; estimate the
    deadweight share if possible]

[repeat per benefit]

ORPHAN BENEFITS (no strategic linkage): [list, or "none"]
COVERAGE GAPS (objective with no mapped benefit): [list, or "none"]
CASH-RELEASABLE-PRESENTED-AS-CASH FLAGS: [list, or "none"]
```

## Worked example

**Input:** "New CRM delivered" claimed as benefit.

**Expected output:** FLAG benefit-washing — enabler only; business change and measurable benefit required.

## Quality checks before delivering

- [ ] Every benefit has enabler/change/benefit chain
- [ ] Benefit-washing test run
- [ ] Orphan and coverage gaps listed

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `benefits-register`.
