---
name: draft-objectives
description: >
  This skill should be used when the user asks to "define our objectives,"
  "draft OKR objectives," "is this a good objective," or provides candidate
  objectives that need to be checked for whether they're genuinely
  qualitative and strategic rather than a metric wearing an objective's
  clothes.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Draft Objectives

The core failure mode this skill exists to catch: an objective that's actually a key result with delusions of grandeur — a number with a sentence wrapped around it. A real objective is qualitative, directional, and would obviously matter even if you couldn't put a number on it yet.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for cascade level and the rough objectives-per-level ceiling.

2. **For each candidate objective, run the test**: would achieving this be obviously good even without a number attached? If the draft already contains a quantity, percentage, or target baked into the wording ("Increase revenue by 20%," "Reduce churn to under 5%"), it's a key result, not an objective — say so explicitly, and propose the actual objective underneath it ("Become the clear value leader in the mid-market segment," with the revenue/churn number relocated to `write-key-results`).

3. **Check strategic linkage.** If this is a cascaded level, does the objective plausibly connect to something above it (a parent KR, or the org's stated strategy)? An objective with no visible connection to anything above it is either mis-scoped or belongs to a level that doesn't have a clear parent yet — flag which.

4. **Check the count.** Compare against the practice profile's ceiling (default 3-5 per level if unset). More than that and focus is gone in practice even if it reads fine on paper — flag the set as a whole, don't just wave each one through individually.

5. **Check for vague inspirational mush** in the other direction — an objective so abstract it can't meaningfully guide what KRs would prove it ("Be great at customer experience"). The test: could two different people write completely unrelated KR sets for this and both plausibly be right? If so, it's too vague — push for specificity without smuggling a number back in.

## Output format

```
Objective 1: [text]
  Verdict: [PASS — qualitative, bounded, strategically linked]
          or [FLAG — contains a number; likely KR-in-disguise; suggested objective: ...]
          or [FLAG — too vague to guide distinct KRs; suggest narrowing to: ...]
  Strategic linkage: [what this connects to, or "none found — flag"]

[repeat per objective]

SET-LEVEL CHECK: [count vs. ceiling; any overlap between objectives]
```
