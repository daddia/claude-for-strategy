---
name: stress-test-matrix-reporting
description: >
  This skill should be used when the user asks "does our matrix structure
  actually work," "who wins when the two bosses disagree," "is this matrix
  reporting relationship viable," or has a dual-reporting relationship that
  needs a tie-breaker rule checked or forced into the open.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Stress-Test Matrix Reporting

A matrix relationship looks fine right up until the first real disagreement between the two bosses — at which point, without a written tie-breaker, it either causes paralysis or gets resolved by whoever has more power rather than whoever has the better case. This skill forces the tie-breaker question before that moment arrives, and separately checks whether the matrix exists for a genuine coordination reason or because the org couldn't decide between two organizing principles.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for known matrix relationships and tie-breaker rules.

2. **For each dual-reporting relationship, ask directly: when the two bosses disagree, who wins?** If a rule exists, confirm it's actually written down and known to the person in the matrixed role — a tie-breaker that exists only in one manager's head isn't a functioning tie-breaker. If no rule exists, flag this as a latent landmine regardless of how smoothly things have gone so far; smooth history just means it hasn't been tested yet.

3. **Check the origin story of the matrix.** Was it adopted because the work genuinely needs dual integration (e.g., a regional sales lead and a global product owner both have a real, ongoing stake in the same role), or because the org couldn't choose between two organizing principles (product vs. geography, business unit vs. function) and split the difference instead? If it looks like the latter, name it — a matrix adopted as an unresolved compromise tends to produce exactly the paralysis the tie-breaker check above is meant to catch, because neither side fully believes their authority is real.

4. **Recommend a specific tie-breaker** where none exists — naming which boss wins by default, and under what circumstances (if any) the other can escalate.

## Output format

```
MATRIXED ROLE: [name/role]
  Boss A: [...] — Boss B: [...]
  Tie-breaker: [exists and known to the role-holder] or [exists but undocumented/unknown
    to them — flag] or [does not exist — flag as latent landmine]

ORIGIN CHECK: [genuine dual coordination need] or [unresolved compromise between two
  organizing principles — name which]

RECOMMENDED TIE-BREAKER (where missing): [who wins by default, escalation path]
```
