---
name: synergy-stress-test
description: >
  This skill should be used when the user asks to "stress-test these
  synergies," "is this deal's synergy case realistic," or has a deal or
  partnership's projected synergies that need cost/revenue separation,
  evidence checks, and a base-rate haircut.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
---

# Synergy Stress Test

The base-rate problem this skill exists to apply: cost synergies are reasonably reliable to project and capture; revenue synergies are notoriously overestimated and underdelivered, almost across the board, because they depend on customer and market behavior the acquirer doesn't control. Most synergy cases blend the two into one number, which lets an unreliable revenue estimate borrow credibility from a reliable cost estimate. This skill won't let that happen.

## Trust spine

```
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent deal economics — flag INPUT NEEDED for purchase price, hurdle rate,
  or synergy values not provided.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

## Precondition: load profiles

Read `~/.claude/plugins/config/claude-for-strategy/corporate-strategy/CLAUDE.md` for synergy haircut defaults and past-deal track record. If the profile records org-specific realization rates, **use those instead of the default haircuts below** and cite the profile.

## Base-rate anchor

`[unverified — industry pattern from training data; replace with org track record when profile has it]`

| Synergy type | Typical realization vs deal model |
|---|---|
| **Cost** — strong evidence (named actions) | ~70–90% of projected |
| **Cost** — weak evidence (generic % of base) | ~40–60% of projected |
| **Revenue** — any evidence tier | ~20–40% of projected |

Revenue synergies underdeliver more often than cost synergies because they depend on customer behavior the acquirer does not control. Apply haircuts **by line item**, stated explicitly — never silently.

## Process

### Step 1: Separate cost and revenue — no blended lines

Every claimed synergy is **cost** or **revenue**. If genuinely mixed, split into components with separate evidence and haircuts.

| Type | Definition |
|---|---|
| **Cost synergy** | Expense reduction — headcount, facilities, procurement, IT consolidation |
| **Revenue synergy** | Top-line uplift — cross-sell, pricing power, channel access, share gain |

### Step 2: Grade evidence per line item

**Cost synergy evidence tiers:**

| Tier | Definition | Default haircut | Adjusted value |
|---|---|---|---|
| **Strong** | Named action with named owner (e.g. "close Newark DC, migrate to Atlanta by Q2") | 10–20% | As-claimed × (0.80–0.90) |
| **Moderate** | Action class identified but not named asset/function | 25–35% | As-claimed × (0.65–0.75) |
| **Weak** | Generic % applied to a cost base ("10% G&A savings") | 40–60% | As-claimed × (0.40–0.60) |

**Revenue synergy evidence tiers:**

| Tier | Definition | Default haircut | Adjusted value |
|---|---|---|---|
| **Strong** | Named segment + stated mechanism + pilot or historical precedent cited | 40–50% | As-claimed × (0.50–0.60) |
| **Moderate** | Mechanism stated but no pilot or precedent | 60–70% | As-claimed × (0.30–0.40) |
| **Weak** | Assertion only ("cross-sell uplift," "pricing power") — **weakest form** | 75–90% | As-claimed × (0.10–0.25) |

For each line: state tier, haircut %, arithmetic, and **why** the tier applies. Override defaults only with sourced org track record.

### Step 3: Mechanism check for revenue lines

Demand a **mechanism**, not an assertion. Minimum acceptable mechanism statement:

```
[Customer segment] will [behavior change] because [acquirer capability],
observable as [metric] within [timeframe].
```

If mechanism is missing, classify as **Weak** regardless of how confident the deck sounds.

### Step 4: Double-counting check

Scan for the same saving or gain claimed twice. Common patterns:

| Pattern | Example |
|---|---|
| Headcount in two line items | "IT consolidation" and "G&A reduction" both count the same roles |
| Revenue and margin from one price move | Price increase counted as revenue synergy and margin expansion |
| One-time and run-rate | Same facility closure counted in year-1 and run-rate |
| Integration cost omitted | Synergy assumes merged platform but integration spend not netted |

List every flag with both line items named.

### Step 5: Recompute deal economics

```
TOTAL SYNERGY VALUE:
  As-claimed (cost):     $[...]
  As-claimed (revenue):  $[...]
  Haircut-adjusted (cost):    $[...]
  Haircut-adjusted (revenue): $[...]
  Haircut-adjusted total:     $[...]
```

If purchase price, hurdle rate, or synergy-dependent IRR/NPV inputs are missing, state **`INPUT NEEDED`** — do not fabricate deal math.

**Bar test:** Does the case still clear at the haircut-adjusted number?

| Question | Answer |
|---|---|
| Synergy-dependent value creation still positive at adjusted total? | yes / no / INPUT NEEDED |
| Deal attractive on cost synergies alone (revenue = 0)? | yes / no / INPUT NEEDED |
| Deal only works at as-claimed (optimistic) number? | If yes, say so directly — this is a material finding |

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
HAIRCUT SOURCE: [profile track record | default base-rate table above]

COST SYNERGIES:
| Item | As-claimed | Evidence tier | Haircut | Adjusted | Rationale |
|---|---|---|---|---|---|
| ... | ... | strong/moderate/weak | % | $... | ... |

REVENUE SYNERGIES:
| Item | As-claimed | Mechanism stated | Evidence tier | Haircut | Adjusted | Rationale |
|---|---|---|---|---|---|---|
| ... | ... | yes/no | ... | % | $... | ... |

DOUBLE-COUNTING FLAGS:
- [line A] ↔ [line B]: [why double-counted]

TOTALS:
  As-claimed total: $[...]
  Haircut-adjusted total: $[...]

DEAL BAR TEST:
  Clears at adjusted number: [yes | no | INPUT NEEDED]
  Works on cost-only: [yes | no | INPUT NEEDED]
  Only works at optimistic number: [yes | no]

RECOMMENDATION: [proceed with adjusted case | renegotiate / restructure | do not rely on revenue synergies for approval]
```

## Quality checks before delivering

- [ ] Every line classified cost vs revenue — no blended items
- [ ] Every line has evidence tier, explicit haircut %, and arithmetic
- [ ] Revenue lines without mechanism classified Weak
- [ ] Double-counting scan completed
- [ ] Bar test answers plainly if case only works at optimistic number
- [ ] No invented deal economics — gaps flagged INPUT NEEDED
