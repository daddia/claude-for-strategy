---
name: hypothesis-tree
description: >
  This skill should be used when the user asks to "build a hypothesis tree,"
  "structure this as an issue tree," "what are our hypotheses for X," or
  presents a problem statement that needs to be broken into falsifiable
  sub-hypotheses before analysis starts.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Hypothesis Tree

Break a problem statement into a root hypothesis and MECE sub-hypotheses, each falsifiable and each tied to the evidence that would prove or disprove it. Full approach in `../../references/hypothesis-driven-approach.md` — read it before producing output if this is the first invocation in the session.

## Process

1. **Restate the problem as a question** if the user hasn't already framed it that way. Confirm this is actually the question that matters before building a tree around it.

2. **Propose a root hypothesis** — the most likely answer, stated as a falsifiable claim, not a topic. If genuinely unsure between two plausible root hypotheses, present both and ask which to build out, rather than picking arbitrarily.

3. **Break the root into 3-5 MECE sub-hypotheses.** Apply the same MECE discipline as Minto's key line: no overlap, nothing material missing. Each sub-hypothesis must be falsifiable on its own.

4. **For each sub-hypothesis, name the smallest piece of evidence** that would meaningfully move it toward true or false. Bias toward fast/cheap evidence over exhaustive evidence — flag if a sub-hypothesis seems to require disproportionate effort relative to how much it would move the root.

5. **State the expected so-what for each branch**, both directions: what changes about the recommendation if this sub-hypothesis turns out true, and what changes if false. If a branch's so-what is "nothing changes either way," cut the branch and say why.

6. **Output as a tree**, not prose.

## Output format

```
ROOT HYPOTHESIS: [falsifiable claim]

1. [Sub-hypothesis 1]
   Evidence needed: [smallest test]
   If TRUE: [so-what]
   If FALSE: [so-what]
2. [Sub-hypothesis 2]
   Evidence needed: ...
   If TRUE: ...
   If FALSE: ...
3. [Sub-hypothesis 3]
   ...

Cut branches: [anything considered and excluded, with why]
```

## Handoff

This output is the direct input to `workplan-builder`, which translates each branch into an owned, timed workstream.
