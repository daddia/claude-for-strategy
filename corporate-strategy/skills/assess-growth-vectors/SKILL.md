---
name: assess-growth-vectors
description: >
  This skill should be used when the user asks to "assess our growth
  options," "where should our growth come from," "build a growth strategy,"
  or has a portfolio of growth initiatives that need to be checked against
  a real growth target — not just sorted into categories.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Assess Growth Vectors

The arithmetic almost nobody does explicitly: list every growth initiative, apply a realistic — not hoped-for — probability of success to each based on how far it stretches from the core, sum the realistic contributions, and compare that sum to the stated growth target. Most growth strategies fail this test the moment it's run, which is exactly why it's worth running.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for the growth target (rate, horizon) and portfolio. If no target exists, stop and ask for one — this skill is meaningless without a real number to test against.

2. **Categorize every growth initiative**: core (extending what the org already does well, to people it already serves), adjacent (a real stretch in product, customer, or geography — but built on existing capability), or transformational (genuinely new capability, new customer, new business model). Classify honestly — initiatives get relabeled "adjacent" to sound safer than they are; push back if the stretch looks bigger than claimed.

3. **Apply a realistic success-rate prior per category**, explicitly stated rather than silently assumed: core bets succeed at high rates; adjacent bets succeed less often than sponsors expect; transformational bets fail more often than not even when well-run. State the assumed rate for each category so it's visible and arguable, not buried in the math.

4. **Calculate the realistic expected contribution** of each initiative (its stated upside × the category's success-rate prior, not the optimistic case taken at face value), and sum across the portfolio.

5. **State the growth gap explicitly**: realistic expected contribution vs. stated target. If there's a gap — and there usually is — say so in plain terms, don't soften it into "upside potential."

6. **If a gap exists, name the actual options**: add more initiatives (and where), accept a lower target, shift the mix toward higher-probability categories (fewer transformational bets, more adjacent), or extend the time horizon. Don't just report the gap and stop — that's the easy half of the job.

## Output format

```
GROWTH TARGET: [rate] over [horizon]

INITIATIVES:
[Initiative] — [Core | Adjacent | Transformational] — Stated upside: [value] —
  Success-rate prior: [X%] — Realistic contribution: [value]

[repeat per initiative]

TOTAL REALISTIC CONTRIBUTION: [sum] vs TARGET: [value] — GAP: [amount, or "none"]

IF GAP EXISTS — OPTIONS:
1. [more initiatives, where]
2. [lower target, to what]
3. [shift mix toward lower-risk categories]
4. [extend horizon]
```
