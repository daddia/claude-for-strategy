---
name: evaluate-strategic-option
description: >
  This skill should be used when the user asks to "evaluate this strategic
  option," "should we make this move," "build the case for/against this
  deal," or has a major strategic decision (market entry, M&A, large
  capital commitment) that needs real-options framing rather than a binary
  go/no-go.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
---

# Evaluate Strategic Option

The discipline a binary go/no-go skips: most strategic options don't need to be committed to in full immediately — they can be staged, with a defined trigger to scale and a defined trigger to abandon, set *before* any money moves. This skill also writes the case against the option itself, rather than just collecting objections from whoever in the room happens to disagree.

## Trust spine

```
STRATEGIC ADVICE VS. SUPPORT: Presents trade-offs and pre-commitment triggers; does not
  substitute for IC/board judgment. Recommendation states what the analysis supports —
  the decision-maker owns the call.
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent an input — flag what's needed instead.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

## Precondition: load profiles

Read `~/.claude/plugins/config/claude-for-strategy/corporate-strategy/CLAUDE.md` and `org-profile.md` for risk posture, past option track record, and IC/board gates. If missing, use balanced risk posture and tag `[PROVISIONAL]`.

## Process

### Step 1: State the option precisely

The **actual decision**, not the topic.

| Vague (reject) | Precise (use) |
|---|---|
| "Should we grow inorganically?" | "Should we acquire Company X at $Y EV by date Z?" |
| "Should we enter Asia?" | "Should we commit $Nm to a Singapore hub with 40 FTE in Q3?" |

If the user gives a topic, ask once to narrow to a committable decision with scope, scale, and timing.

### Step 2: Staging decision — can this be staged?

Run this checklist before defaulting to all-or-nothing:

| Staging is **plausible** when | Staging is **not plausible** when |
|---|---|
| A pilot, JV, or limited deployment preserves optionality | Regulatory or contractual deadline forces full commitment |
| Learning value exists before irreversible capital | Winner-take-all market where delay forfeits position |
| Sunk cost of the initial stage is survivable | Exclusive deal window — delay loses the asset |
| Scale-up and abandon triggers can be defined with observable metrics | Physics of the investment require full build-out (e.g. greenfield plant) |

If staging is plausible, **propose a staged structure** (template below). If not, say so explicitly and explain why — do not force a staging frame that doesn't fit.

**Staged commitment template:**

```
INITIAL COMMITMENT: [scope, $, duration, decision rights retained]
SCALE TRIGGER: By [date], if [metric/evidence] ≥ [threshold], commit to [next stage]
ABANDON TRIGGER: By [date], if [metric/evidence] < [threshold], exit with [max loss]
LEARNING OBJECTIVE: [what this stage must prove before scale]
```

### Step 3: Case for (brief)

State the best case in 3–5 bullets. This usually already exists — don't relitigate at length. Tag unsourced market claims.

### Step 4: Case against (steelman — mandatory)

Write the **strongest argument to kill the option**, as if arguing to a skeptical IC — not a one-line caveat. Work through this checklist; include every item that applies, with the uncomfortable version stated plainly:

| Objection class | What to surface |
|---|---|
| **Hardest assumption buried** | What must be true that hasn't been tested? |
| **Cannibalization / portfolio conflict** | What existing business suffers if this succeeds? |
| **Timing illusion** | Is "we must move now" real or manufactured urgency? |
| **Integration / org load** | Who absorbs complexity — named function, not "the org"? |
| **Comparable bias** | Are cited precedents survivorship-biased or context-different? |
| **Reversibility overstated** | What costs are truly sunk after stage 1? |
| **Sponsor momentum** | Would this pass without the current executive sponsor? |

Do not soften because the option has sponsors. This section is the skill's reason to exist.

### Step 5: Downside sizing

Size the **failure case**, not just the upside:

| Loss type | What to quantify or flag INPUT NEEDED |
|---|---|
| Direct financial loss | Capital at risk, revenue foregone |
| Opportunity cost | What else doesn't get funded |
| Reputation / regulatory | Customer, partner, or regulator reaction |
| Organizational strain | Key-talent drain, distraction from core |

**Survivability test:** If this fails outright, can the org absorb the loss without covenant breach, forced divestiture, or layoffs at a scale that damages core operations? Answer **yes / no / unclear** with evidence — not optimism.

Cross-check risk appetite from the profile. An option that is strategically attractive but not survivable on failure is a different recommendation than one that is merely unattractive.

### Step 6: Kill criteria (set now, before commitment)

Write triggers **before** commitment so walking away later is a pre-agreed decision, not a sunk-cost political fight:

```
KILL CRITERIA (pre-commitment):
- Abandon if by [date]: [specific metric or event]
- Abandon if: [integration milestone] not achieved by [date]
- Escalate to [forum] if: [cost/schedule overrun] exceeds [threshold]
```

If staging applies, separate **stage-1 abandon triggers** from **full-program kill criteria**. Reference `exit-or-double-down` when prior options lacked this discipline.

### Step 7: Recommendation

| Recommendation | When |
|---|---|
| **Proceed staged** | Staging is plausible; upside justifies stage-1 risk; kill criteria are specific |
| **Proceed in full** | Staging not plausible; case for survives steelman; downside survivable |
| **Do not proceed** | Case against wins on survivability, evidence, or strategic fit; or kill criteria already breached |

State confidence band. If trade-offs aren't quantifiable yet, say so — don't pick a winner anyway.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
LOAD-BEARING ASSUMPTIONS:
- [assumption] — if wrong: [impact]

OPTION: [precise statement of the decision]

CAN THIS BE STAGED: [yes — initial / scale / abandon structure] or [no — why]

CASE FOR:
- [bullet]

CASE AGAINST (steelman):
- [bullet per checklist item that applies]

DOWNSIDE SIZING:
| Loss type | Estimate | Source |
|---|---|---|
| ... | ... | [sourced / INPUT NEEDED] |

SURVIVABLE ON FAILURE: [yes | no | unclear] — [evidence]

KILL CRITERIA (set now, before commitment):
- ...

RECOMMENDATION: [proceed staged | proceed in full | do not proceed] — [why]
```

## Quality checks before delivering

- [ ] Option stated as a committable decision, not a topic
- [ ] Staging checklist applied (staged structure or explicit irreversibility rationale)
- [ ] Case against is steelmanned, not a caveat paragraph
- [ ] Downside includes survivability test
- [ ] Kill criteria are dated and specific
- [ ] Board/exec final runs trust-spine GATE if applicable
