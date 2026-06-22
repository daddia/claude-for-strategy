---
name: cascade
description: >
  This skill should be used when the user asks to "cascade these OKRs,"
  "break this down to team level," or has objectives/KRs at one level that
  need to flow down with a genuine contribution check, a capacity sanity
  check, and a check for goals that work against each other across teams.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Cascade

Three checks this skill runs that a naive cascade skips: whether a child objective is a real contribution rather than a restatement, whether too many children are competing for one parent's capacity, and whether two sibling teams' goals are quietly working against each other. The third is the one most cascade tools never do, and it's often where transformation programs actually stall.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for cascade levels and the rough ceiling on objectives-per-level / KRs-per-objective.

2. **Run the contribution test on every cascaded objective**: if this level's objective is fully achieved, does it move the needle on the specific parent KR it claims to serve? If achieving it wouldn't meaningfully move that KR, it doesn't belong in the cascade — even if it sounds related.

3. **Run the restatement check**: is the child objective genuinely this level's *contribution* to the parent, or the same goal with a different owner's name on it and the scope unchanged? Restatement adds a layer of bureaucracy without adding alignment — flag it and ask what this level would specifically do differently.

4. **Run the alignment/coverage check** across the whole cascade: does every leaf-level KR trace back to a real contribution? Flag orphaned KRs (no upward contribution) and uncovered parent KRs (no cascaded contribution at all — a coverage gap).

5. **Run the fan-out/capacity check**: how many child objectives are mapped to one parent KR, relative to what's plausible given the org size/structure recorded elsewhere in this repo's other plugins (or ask, if unknown)? Too many children competing for one parent's worth of capacity is a sign the parent KR is too broad, or that not everyone cascading into it can realistically be prioritized — name which.

6. **Run the cross-team conflict check** — the one most cascade exercises skip entirely. Look across sibling-level objectives/KRs (same parent, different owners) for goals that improve one team's number at another's expense: a speed-optimizing KR that depends on a process another team's KR wants to slow down for quality; a cost-reduction KR that depends on a service-level commitment another team has made. This requires actually reading the KRs against each other, not just checking they're individually well-formed — flag every pair you find, even if you're not certain it's a real conflict; a false positive here costs a clarifying conversation, a missed one costs a quarter.

## Output format

```
PARENT: [objective/KR]

  → [Child objective, owner] — Contribution: [genuine / restatement — explain]
  → [Child objective, owner] — Contribution: ...

FAN-OUT CHECK: [parent]: [N] children — [within plausible capacity / overloaded, explain]

ALIGNMENT CHECK:
  Orphaned KRs (no upward contribution): [...]
  Uncovered parent KRs (no cascaded contribution): [...]

CROSS-TEAM CONFLICT CHECK:
  [Team A's KR] vs. [Team B's KR]: [nature of the conflict, or "none found"]
```
