---
name: design-decision-rights
description: >
  This skill should be used when the user asks to "build a RACI," "who
  actually owns this decision," "clarify decision rights," or has a
  decision or process that needs explicit roles assigned with
  single-point-accountability enforced.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Design Decision Rights

The discipline a naive RACI skips: exactly one party Accountable per decision. Zero accountable parties means the decision will stall or get endlessly re-opened; more than one means the same failure wearing a different disguise — diffused accountability that looks like coverage but isn't. This skill enforces both directions and also checks for the slower failure: too many people Consulted, inflating decision latency.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for existing decision-rights gaps already flagged.

2. **For each decision or process in scope, assign roles** — Responsible (does the work), Accountable (owns the outcome, answers for it), Consulted (input sought before deciding), Informed (told after). RAPID terms (Recommend/Agree/Perform/Input/Decide) work the same way if that's the house convention — check the practice profile.

3. **Enforce exactly one Accountable/Decide party per decision.** If zero are named, stop and ask who actually should own it rather than leaving it unassigned. If more than one are named, flag this explicitly as diffused accountability and force a choice — "shared ownership" is rarely real ownership when something goes wrong.

4. **Check for Consulted/Input bloat.** If the list of people who must be consulted before a decision is long enough that reaching them all would take weeks, flag it — that's a decision-speed problem hiding inside what looks like thorough governance. Recommend trimming to who genuinely needs to weigh in versus who'd just like to be asked.

5. **Check for decisions with no clear home at all** — if walking through the org's actual decisions turns up one nobody in the exercise claims ownership of, name it specifically rather than letting it pass as an oversight to fix later.

## Output format

```
DECISION: [name]
  Accountable: [single name/role — flag if zero or multiple were initially proposed]
  Responsible: [...]
  Consulted: [...] — Bloat flag: [if list is long enough to slow the decision materially]
  Informed: [...]

[repeat per decision]

UNOWNED DECISIONS FOUND: [any decision with no claimed owner during this exercise]
```
