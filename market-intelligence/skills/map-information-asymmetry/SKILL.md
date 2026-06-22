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
  version: "0.1.0"
---

# Map Information Asymmetry

The most distinctive skill in this plugin. Most strategic analysis assumes both sides see roughly the same picture; this skill assumes they usually don't, and asks what that means. The discipline: identify exactly what each side knows that the other doesn't, determine which side you're on, and reason about signaling (the informed party credibly proving what they know) and screening (the uninformed party testing for it) — because the asymmetry itself, not just the surrounding deal terms, often determines who wins.

## Process

1. **State the situation precisely** — a negotiation, a market transaction, a hiring decision, a customer relationship, a deal under evaluation.

2. **List what each party knows that the other plausibly doesn't.** Be specific and concrete — not "they know more about their business," but the actual category of hidden information (true cost structure, true churn rate, true intent to renew, true quality of an asset being sold).

3. **Determine which side is structurally informed and which is uninformed**, and which side you're actually on. This is the step most people skip because it requires admitting, sometimes, that you're the uninformed party in your own deal.

4. **If you're the informed party**: what credible, *costly* signal could you send that an uninformed party would find believable precisely because it would be expensive or risky for a low-quality counterpart to fake? A signal that costs nothing to send is not a signal — anyone can send it. Name the actual costly signal available, or note that none exists yet.

5. **If you're the uninformed party**: what screening mechanism could you apply to force the informed party to reveal information indirectly (a structure where their choices reveal their type — e.g., an earnout structure that only a seller confident in future performance would accept)? Name the specific mechanism, not just "do more diligence."

6. **Apply the "market for lemons" logic where it fits**: if quality is genuinely hard to verify before commitment, the market tends to adversely select toward lower quality unless a credible signal or screen breaks the spiral — check whether that dynamic is actually present here, and if so, whether anything currently breaks it.

7. **State the strategic implication directly**: is the current strategy knowingly exploiting an informed position, unknowingly giving one away, or exposed to one held against it? This is the actual point of the exercise — don't stop at describing the asymmetry without saying what it means for the decision at hand.

## Output format

```
SITUATION: [the deal/negotiation/relationship in question]

WHAT [PARTY A] KNOWS THAT [PARTY B] DOESN'T: [specific, concrete]
WHAT [PARTY B] KNOWS THAT [PARTY A] DOESN'T: [specific, concrete]

YOUR POSITION: [informed | uninformed] on [which specific asymmetry]

IF INFORMED: Available costly signal: [specific mechanism, or "none currently available"]
IF UNINFORMED: Available screening mechanism: [specific mechanism, or "none currently applied"]

ADVERSE SELECTION RISK: [present / not present — explain]

STRATEGIC IMPLICATION: [exploiting an advantage / giving one away / exposed to one — be direct]
```
