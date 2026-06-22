---
name: okr-cascade
description: >
  This skill should be used when the user asks to "cascade company OKRs to
  teams," "break these objectives down to team level," or has objectives/KRs
  at one level that need to flow down with contribution, coverage, capacity,
  and cross-team conflict checks.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
---

# OKR Cascade

Map company-level OKRs down to team-level objectives — running contribution, restatement, coverage, fan-out capacity, and cross-team conflict checks so the cascade adds alignment rather than bureaucracy.

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

Produce a cascaded OKR set where every child objective is a genuine contribution to a parent KR, capacity is plausible, and sibling teams aren't quietly working against each other — the failure modes most cascade exercises skip.

## Precondition: load profiles

**Before cascading, read both:**

- `~/.claude/plugins/config/claude-for-strategy/org-profile.md`
- `~/.claude/plugins/config/claude-for-strategy/performance/CLAUDE.md`

If missing or template, surface cold-start bounce with `/performance:cold-start-interview` or **"provisional"**.

### Provisional mode

Defaults: company → team cascade (two levels); ceiling ~5 objectives per level, ~4 KRs per objective `[unverified — generic OKR hygiene]`. Tag `[PROVISIONAL]`.

Read `## Reporting → OKR cascade structure` from the performance profile for configured levels and limits.

## Workflow

### Step 1: Orient

| Question | Answer |
|---|---|
| **Parent level** | Company / BU / department — what's being cascaded from |
| **Child levels** | Teams / squads / individuals — target depth |
| **Parent OKRs** | Objectives and KRs provided or INPUT NEEDED |
| **Org structure** | Teams and owners — for capacity and conflict checks |
| **Audience** | Working session / leadership review / company-wide publish |
| **Cycle** | Quarter / half / year |

If parent OKRs are missing, stop — produce structure with `INPUT NEEDED: parent objectives and KRs`. Do not invent company goals.

### Step 2: Contribution test

For every cascaded child objective, ask:

> If this level's objective is fully achieved, does it move the needle on the **specific parent KR** it claims to serve?

| Result | Action |
|---|---|
| Genuine contribution | Keep — document the link |
| Weak or tangential | Flag — reframe or remove |
| No movement | Remove — even if it sounds related |

### Step 3: Restatement check

Detect when a child objective is the **same goal with a different owner** — scope unchanged, no level-specific contribution.

```
→ [Child objective, owner] — Contribution: genuine | restatement — [explain]
```

Restatement adds bureaucracy without alignment. Ask what this level would do **differently** from the parent.

### Step 4: Alignment and coverage check

Across the full cascade:

| Check | Flag |
|---|---|
| **Orphaned KRs** | Leaf KRs with no upward contribution path |
| **Uncovered parent KRs** | Parent KRs with no cascaded contribution at all |

Coverage gaps are as important as orphans — a parent KR with no children is a planning hole.

### Step 5: Fan-out and capacity check

For each parent KR, count child objectives mapped to it.

Compare to org size/structure from org profile or user input:

| Fan-out | Verdict |
|---|---|
| Within plausible capacity | Note count |
| Overloaded | Flag — parent KR too broad, or too many teams competing for one parent's capacity; name which |

Do not invent team sizes — use profile or ask.

### Step 6: Cross-team conflict check

Read sibling-level objectives/KRs (same parent, different owners) **against each other** — not just individually.

Look for pairs where one team's KR improves at another's expense:

| Conflict type | Example |
|---|---|
| Speed vs quality | Team A optimizes cycle time; Team B optimizes defect rate on same flow |
| Cost vs service level | Team A cuts cost; Team B holds SLA Team A depends on |
| Capacity grab | Two teams' KRs assume the same shared resource |

Flag every plausible pair — false positives cost a clarifying conversation; missed conflicts cost a quarter.

```
CROSS-TEAM CONFLICT CHECK:
  [Team A KR] vs [Team B KR]: [nature] or none found
```

### Step 7: Publish gate

Before company-wide or board-visible cascade finals, run trust-spine **GATE**. Working drafts for OKR workshops skip the gate.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
PARENT LEVEL: [company | BU | department]
CHILD LEVELS: [teams | squads | individuals]
CYCLE: [quarter | half | year]

LOAD-BEARING ASSUMPTIONS:
- ...

PARENT: [objective]
  KR: [parent KR]

  → [Child objective, owner] — Contribution: [genuine | restatement — explain]
    KR: [child KR]
  → ...

FAN-OUT CHECK:
| Parent KR | # children | Verdict |
|---|---|---|

ALIGNMENT CHECK:
  Orphaned KRs: [...]
  Uncovered parent KRs: [...]

CROSS-TEAM CONFLICT CHECK:
  [pairs and nature, or none found]

CAPACITY FLAGS: [overloaded parent KRs]
EVIDENCE GAPS: [INPUT NEEDED]
```

## Quality checks before delivering

- [ ] Both profiles loaded (or `[PROVISIONAL]` tagged)
- [ ] Parent OKRs provided — not invented
- [ ] Contribution test run on every child objective
- [ ] Restatements flagged — not passed through as alignment
- [ ] Orphans and uncovered parent KRs both checked
- [ ] Fan-out compared to plausible capacity
- [ ] Cross-team conflicts checked across siblings — not just individual KR quality

## Close with next steps

Branches: resolve flagged conflicts in a leadership session, narrow overloaded parent KRs, fill coverage gaps for uncovered parents, hand off instrumentation to `tracker-builder`, or confirm gate before company-wide publish.
