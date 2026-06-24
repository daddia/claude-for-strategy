---
name: benefits-map
description: >
  This skill should be used when the user asks to "map the benefits for
  this initiative," "build a benefits dependency network," "what are we
  actually claiming this will deliver," or needs an approved business
  case's benefit claims decomposed into enablers, business changes, and
  benefits before a register can be built.
tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Benefits Map

The discipline this catches: a delivered system is not a benefit, and neither is a process going live — both are enablers. A benefit only exists once someone is doing something differently *because* the enabler exists, and that different behavior produces a result someone will actually value. Most business cases blur enabler and benefit together; this skill forces them apart before a register gets built on the blurred version.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for the benefit type taxonomy and named framework, if any. If `transformation` or `corporate-strategy` is installed, read the relevant `transformation:business-case` or `corporate-strategy:evaluate-strategic-option` output as the seed rather than starting from a blank page — the case's cost/benefit table is the input, not a separate exercise.

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
