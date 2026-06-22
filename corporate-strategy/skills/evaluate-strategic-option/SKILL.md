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
  version: "0.1.0"
---

# Evaluate Strategic Option

The discipline a binary go/no-go skips: most strategic options don't need to be committed to in full immediately — they can be staged, with a defined trigger to scale and a defined trigger to abandon, set *before* any money moves. This skill also writes the case against the option itself, rather than just collecting objections from whoever in the room happens to disagree.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for risk posture and track record on past options.

2. **State the option precisely** — the actual decision, not the topic. ("Should we acquire Company X" not "should we grow inorganically.")

3. **Ask whether this can be staged.** Most options framed as all-or-nothing aren't actually all-or-nothing — propose a smaller initial commitment with explicit scale-up and abandon triggers, and state what evidence, observed by what date, would justify each. If the option genuinely can't be staged (a single irreversible decision), say so and explain why rather than forcing a staging structure that doesn't fit.

4. **Write the case against, in full, as if arguing to kill it.** Not a one-line caveat — the actual best argument someone skeptical would make, including the most uncomfortable version. This is the step most prone to being skipped under momentum; do it explicitly and don't soften it because the option has sponsors.

5. **Size the downside explicitly**, not just the upside case that got the option proposed: what's lost if this fails outright, and is that loss survivable at the org's current risk capacity.

6. **State the kill criteria up front**, in writing, before commitment — "if we don't see X by date Y, we abandon" — so the decision to walk away later is a pre-agreed trigger, not a fresh political fight under sunk-cost pressure (see `exit-or-double-down` for what happens when this discipline wasn't applied up front).

## Output format

```
OPTION: [precise statement of the decision]

CAN THIS BE STAGED: [yes — initial commitment, scale trigger, abandon trigger] or
  [no — irreversible, why]

CASE FOR: [the actual best case, briefly — this usually already exists]

CASE AGAINST (written in full): [the steelmanned objection]

DOWNSIDE SIZING: [what's lost if this fails outright; survivable at current risk capacity? y/n]

KILL CRITERIA (set now, before commitment): [specific, dated]

RECOMMENDATION: [proceed staged | proceed in full | do not proceed] — [why]
```
