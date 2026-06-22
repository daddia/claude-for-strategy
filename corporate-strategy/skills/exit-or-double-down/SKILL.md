---
name: exit-or-double-down
description: >
  This skill should be used when the user asks "should we exit this
  business," "is this worth continuing to fund," "do a portfolio pruning
  review," or needs an explicit exit/hold/double-down call on a unit —
  with sunk-cost reasoning named directly when it appears.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
---

# Exit or Double Down

The hardest skill in this plugin, deliberately. Portfolios accumulate units nobody would choose to enter today but nobody's willing to be the one to kill — sustained by sunk cost, internal status, or simple inertia. This skill asks the blank-page question directly and calls out sunk-cost reasoning by name when it shows up, rather than letting it pass as a legitimate argument.

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

Produce an explicit exit / hold / double-down call with forward-looking rationale only — sunk cost named and set aside, kill criteria stated if hold is recommended, escalation routing to whoever must own the decision.

## Precondition: load profiles

**Before analyzing, read both:**

- `~/.claude/plugins/config/claude-for-strategy/org-profile.md`
- `~/.claude/plugins/config/claude-for-strategy/corporate-strategy/CLAUDE.md`

If missing or template, surface cold-start bounce with `/corporate-strategy:cold-start-interview` or **"provisional"**.

### Provisional mode

Defaults: balanced risk posture; generic exit criteria (declining structural position, persistent capital destruction, near-zero growth odds); no named IC/exit process. Tag `[PROVISIONAL]`.

## Workflow

### Step 1: Orient

| Question | Answer |
|---|---|
| **Unit** | Name and scope boundary |
| **Decision forum** | BU review / portfolio committee / board / IC |
| **Evidence pack** | Financials, market position, growth-vector assessment, allocation view |
| **Time pressure** | Active decision / exploratory / forced by budget cycle |

Read risk posture and M&A/divestiture process from profiles if configured.

### Step 2: Blank-page test (run first)

**Before any other evidence**, answer explicitly:

> If this unit didn't exist today and you were deciding fresh, with no history, would you choose to enter this business at this level of investment?

Answer yes/no with forward-looking rationale. This is the cleanest bypass for sunk-cost framing — run it before financial tables.

### Step 3: Sunk-cost detection

Scan the case for continuing for past-investment language:

| Phrase pattern | Action |
|---|---|
| "We've already spent $X" | Name as sunk-cost reasoning; set aside |
| "We're so close after everything we've spent" | Name and set aside |
| "We can't walk away now" (without forward case) | Name and set aside |

```
SUNK-COST CHECK: [quote detected language] or "none detected"
```

Sunk cost is not evidence about the future. Only forward inputs count: expected returns, structural position, odds of reaching defensible position from here.

### Step 4: Exit criteria check

Check unit against explicit exit criteria:

| Criterion | Met? | Evidence |
|---|---|---|
| Declining structural position, no path to #1/#2 | Y/N | [sourced observation] |
| Persistent capital destruction beyond threshold | Y/N | [sourced figures or INPUT NEEDED] |
| Growth-vector assessment shows near-zero success odds | Y/N / N/A | [from assess-growth-vectors if available] |

Use thresholds from profile when configured. Do not invent financial thresholds.

### Step 5: Double-down criteria check

Alternative case — all must be argued forward-looking:

| Criterion | Met? | Evidence |
|---|---|---|
| Defensible or improving structural position | Y/N | |
| Credible path to category leadership | Y/N | |
| Resourcing below what opportunity justifies | Y/N | [cross-check `allocate-resources` if available] |

### Step 6: Make the call

**EXIT | HOLD | DOUBLE DOWN**

- **Hold** requires its own justification — credible near-term re-rating, active turnaround with a **deadline**, not default comfort.
- If hold: state **kill criteria** now — "if we don't see X by date Y, we exit."

### Step 7: Escalation routing

Name who must approve per profile (`## Plugin-specific operating model → M&A / divestiture process`) — not "escalate to leadership."

### Step 8: Board-ready gate

Run trust-spine **GATE** before portfolio-committee or board finals. This decision is consequential — working analysis for the strategy team may stay structured first pass.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
UNIT: [name]
DECISION FORUM: [BU review | portfolio committee | board | IC]

LOAD-BEARING ASSUMPTIONS:
- ...

BLANK-PAGE TEST: [enter today at this investment level? yes/no — forward rationale]

SUNK-COST CHECK: [quoted language or none detected]

EXIT CRITERIA:
| Criterion | Met | Evidence |
|---|---|---|

DOUBLE-DOWN CRITERIA:
| Criterion | Met | Evidence |
|---|---|---|

CALL: [EXIT | HOLD | DOUBLE DOWN]
RATIONALE: [forward-looking only — sunk cost excluded]

KILL CRITERIA (if HOLD): [specific, dated — or N/A]

APPROVAL ROUTING: [named role/forum per profile]
EVIDENCE GAPS: [INPUT NEEDED]
```

## Quality checks before delivering

- [ ] Both profiles loaded (or `[PROVISIONAL]` tagged)
- [ ] Blank-page test answered before other evidence
- [ ] Sunk-cost language quoted and set aside when present
- [ ] Exit and double-down criteria checked explicitly
- [ ] Hold is justified — not default; kill criteria stated if hold
- [ ] No invented financials or market-share figures
- [ ] Approver named for the call

## Close with next steps

Branches: run `allocate-resources` to size double-down funding, take exit case to IC, set dated kill criteria and calendar revisit, gather missing financials, or pair with `evaluate-strategic-option` if exit can be staged.
