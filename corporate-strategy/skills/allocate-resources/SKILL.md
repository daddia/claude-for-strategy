---
name: allocate-resources
description: >
  This skill should be used when the user asks to "review our resource
  allocation," "are we funding the right things," "build a portfolio
  allocation view," or needs current spend, headcount, or management
  attention checked against strategic priority for misallocation.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
---

# Allocate Resources

The discipline: resources should follow strategic priority, not history, internal politics, or sunk cost. This skill maps what's actually being spent against what's actually most important, and names the gap when those two things don't match — which they usually don't, because allocation is sticky and strategy review is periodic.

## Trust spine

```
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent an input — flag what's needed instead.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

## Purpose

Produce a portfolio allocation diagnosis the strategy team can defend in a resource review — specific misallocation patterns named, reallocation moves recommended, not just a pretty matrix.

## Precondition: load profiles

**Before analyzing, read both:**

- `~/.claude/plugins/config/claude-for-strategy/org-profile.md`
- `~/.claude/plugins/config/claude-for-strategy/corporate-strategy/CLAUDE.md`

If missing or template, surface cold-start bounce with `/corporate-strategy:cold-start-interview` or **"provisional"**.

### Provisional mode

Defaults: generic portfolio units; three priority tiers (core / adjacent / exit candidate); no known allocation stickiness. Tag `[PROVISIONAL]`. All dollar and headcount figures must be user-provided — never invented.

## Workflow

### Step 1: Orient

| Question | Answer |
|---|---|
| **Portfolio scope** | Units included (BUs, products, segments) |
| **Allocation types** | Capital / headcount / management attention |
| **Review forum** | Working strategy / portfolio committee / board |
| **Time horizon** | Annual budget / rolling quarterly / ad hoc |
| **Evidence pack** | Spend data, headcount, priority ranking |

Read `## Definitions and thresholds` for portfolio units, strategic priority tiers, and allocation stickiness from the corporate-strategy profile.

### Step 2: Evidence pack — allocation data

| Input | Status | Source |
|---|---|---|
| Capital/budget by unit | Provided / partial / missing | [sourced: …] |
| Headcount by unit | Provided / partial / missing | [sourced: …] |
| Management attention estimate | Provided / partial / missing | [user estimate or INPUT NEEDED] |
| Strategic priority ranking | In profile / provided / missing | [source] |

**Ask rather than assume.** A rough management-attention estimate is more useful than skipping it — but mark it `[user estimate — not verified]` if not sourced.

**If priority ranking is missing:** stop and get or confirm ranking before comparing. Do not infer priority from current spend (that's the problem being diagnosed).

### Step 3: Allocation vs priority comparison

For each unit, map side by side:

```
[Unit] — Priority: [tier/rank] — Capital % — Headcount % — Attention
```

Tag all percentages `[sourced: …]` or `INPUT NEEDED`.

### Step 4: Pattern detection

Flag these patterns **by name**:

| Pattern | Definition | Flag when |
|---|---|---|
| **Legacy overfunding** | Low-priority unit absorbs disproportionate share | Priority tier X but resource share ≥Y points above peers |
| **Under-resourced growth bet** | Stated priority but funding below plausible minimum | Adjacent/transform bet in top tier but bottom quartile of spend |
| **Under-differentiated allocation** | Flat spend despite wide priority spread | Resource variance << priority variance |

For legacy overfunding, ask **why** explicitly — "always funded at this level" is a diagnosis, not a justification.

### Step 5: Growth bets check

Cross-check units or initiatives from `assess-growth-vectors` (if run) — especially adjacent and transformational bets. Are they resourced for a real chance, or starved because core defense absorbed the budget?

If `assess-growth-vectors` wasn't run, flag: "Growth-bet check partial — no growth-vector assessment in session."

### Step 6: Reallocation recommendation

Recommend **specific moves** — from → to, with strategic rationale plain enough to defend in the room. Not "rebalance toward growth" — "[Unit A] capital −X%, [Unit B] +X% because [priority + odds]."

Note allocation stickiness from profile — if reallocation historically lags strategy by N quarters, say so.

### Step 7: Portfolio committee gate

Run trust-spine **GATE** before board or portfolio-committee finals.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
SCOPE: [units included]
REVIEW FORUM: [working | portfolio committee | board]

LOAD-BEARING ASSUMPTIONS:
- ...

ALLOCATION VIEW:
| Unit | Priority tier/rank | Capital % | Headcount % | Attention | Flag |
|---|---|---|---|---|---|
| ... | ... | [sourced/INPUT NEEDED] | ... | ... | none / legacy overfunding / under-resourced bet |

UNDER-DIFFERENTIATION CHECK: [allocation spread vs priority spread — pass or fail]

GROWTH BETS CHECK: [resourced adequately / underfunded — cite units]

RECOMMENDED REALLOCATION:
| From | To | Type | Magnitude | Rationale |
|---|---|---|---|---|

STICKINESS NOTE: [from profile — expected lag to implement]
EVIDENCE GAPS: [INPUT NEEDED]
```

## Quality checks before delivering

- [ ] Both profiles loaded (or `[PROVISIONAL]` tagged)
- [ ] Priority ranking confirmed — not inferred from spend
- [ ] No invented budget or headcount figures
- [ ] Legacy overfunding and under-differentiation checked by name
- [ ] Reallocation is specific (from → to), not vague
- [ ] Growth bets cross-checked where data exists

## Close with next steps

Branches: provide missing spend data and re-run, take reallocation to portfolio committee, run `exit-or-double-down` on legacy overfunded units, pair with `assess-growth-vectors` for bet sizing, or document stickiness and set a reallocation trigger date.
