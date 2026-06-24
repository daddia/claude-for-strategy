---
name: status-report
description: >
  This skill should be used when the user asks to "write this week's status
  report," "draft the program status update," or needs a RAG-rated status
  report produced for a specific audience from the current RAID log and
  milestone status.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "pmo practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Status Report

## When to use

Audience-specific RAG status report from RAID and milestones — BLUF first; sponsor vs steering vs team calibration.

## What this skill does not do

- **Does not fabricate RAID/milestone status** — `INPUT NEEDED` skeleton only.
- **Does not replace steering pack** — route to `/pmo:steering-pack` for governance deck.
- **Does not RAG-wash** — profile thresholds required.

## Preconditions

| Input | If missing |
|---|---|
| Org + pmo profiles | Tag `[PROVISIONAL]`; bounce to cold-start |
| RAID log (open items) | Stop — ask; skeleton with `INPUT NEEDED` only |
| Milestone status | Stop — ask; skeleton with `INPUT NEEDED` only |
| Audience | Ask once; default sponsor with `[PROVISIONAL]` |

## Provisional mode

`[PROVISIONAL]` — generic RAG thresholds; confirm audience.

## Trust spine

- **Confidence bands** (`narrative-synthesis`):
  - **High:** BLUF, profile RAG rules quoted, sourced RAID/milestones, Red/Amber action+ask.
  - **Medium:** Partial inputs; structured first pass with gaps listed.
  - **Low:** Missing RAID and milestones — skeleton only, no fake Green.
- **Failure modes:**
  - **Incentive Gaming:** Guards RAG-washing — vague "on track" without thresholds.
- **Escalation triggers:** Red workstream — explicit ask in BLUF.

## Purpose

Produce a status report the intended reader can act on in two minutes (sponsor) or use for working-level triage (team) — grounded in actual RAID and milestone inputs, not plausible-sounding fabrication.

## Precondition: load profiles

**Before drafting, read both:**

- `~/.claude/plugins/config/claude-for-strategy/org-profile.md`
- `~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md`

If missing or template, surface cold-start bounce with `/pmo:cold-start-interview` or **"provisional"**.

### Provisional mode

Defaults: RAG = Green / Amber / Red with generic thresholds (Red = missed critical milestone or unresolved blocker >2 weeks; Amber = at risk within 2 weeks; Green = on track); audiences = sponsor, steering, working team. Tag `[PROVISIONAL]`. Ask user to confirm audience if not stated.

## Workflow

### Step 1: Orient

| Question | Answer |
|---|---|
| **Audience** | Sponsor / steering committee / working team |
| **Reporting period** | Week ending / sprint / month |
| **Program or workstreams** | Names and scope |
| **Distribution** | Internal working / external sponsor / governance forum |

Read `## Status reporting` from the pmo profile for audience list, RAG definitions, and cadence. **Use the profile's concrete RAG thresholds** — not vague "mostly on track."

### Step 2: Evidence pack — do not fabricate

Required inputs:

| Input | Status | Source |
|---|---|---|
| RAID log (open items) | Provided / partial / missing | [file, tool, user message] |
| Milestone status | Provided / partial / missing | [source from profile or user] |
| Prior status report | Optional | [if provided, use for continuity] |

**If RAID or milestones are missing:** stop and ask. Do not invent plausible Red/Amber/Green status. You may produce a **structured first pass** skeleton with `INPUT NEEDED: current RAID log` and `INPUT NEEDED: milestone status` — but not fake item lists.

### Step 3: Overall RAG determination

Apply profile RAG definitions workstream by workstream, then roll up to program level. State the rule applied:

```
RAG RULE APPLIED: [quote threshold from profile or provisional default]
```

If rollup logic is ambiguous (one Red workstream, rest Green), state assumption: "Program Amber because [workstream X] is Red and [reason]."

### Step 4: BLUF — bottom line first

Write before detail:

- Overall status + one-line reason
- The one or two things that most need attention
- Explicit ask (decision, escalation, awareness only)

This is the only section a time-pressed sponsor should need.

### Step 5: Workstream structure

Group by workstream or theme — not a flat RAID dump. Each workstream: RAG + one-line status.

### Step 6: Red and Amber escalation

For every Red or Amber item:

| Field | Content |
|---|---|
| What's wrong | Specific, not generic |
| Why | Root cause if known; `INPUT NEEDED` if not |
| Action | What's being done |
| Ask | What the reader must do — or "none" |

### Step 7: Milestone status

On track / at risk / slipped — with specifics for anything not on track. Reference milestone source; tag dates `[sourced: …]`.

### Step 8: Audience calibration

| Audience | Detail level |
|---|---|
| Sponsor | BLUF + asks only; 2-minute read |
| Steering | BLUF + escalated risks + decisions needed |
| Working team | Full workstream detail; every Red/Amber item |

Flag if the draft exceeds the audience's expected length.

### Step 9: External distribution gate

Run trust-spine **GATE** before sponsor-facing, steering, or any external distribution final. Internal working-team drafts skip the gate but keep confidence labels.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
AUDIENCE: [sponsor | steering | working team]
PERIOD: [reporting period]
RAG RULE APPLIED: [threshold source]

LOAD-BEARING ASSUMPTIONS:
- ...

OVERALL STATUS: [RAG] — [one-line reason]
HEADLINE: [what most needs attention]
ASK: [explicit — or "none"]

BY WORKSTREAM:
[Workstream 1] — [RAG]
  [Red/Amber detail if applicable]
[Workstream 2] — [RAG]
  ...

MILESTONE STATUS:
| Milestone | Status | Notes | Source |
|---|---|---|---|

ESCALATIONS (Red/Amber only):
| Item | What's wrong | Why | Action | Ask |
|---|---|---|---|---|

EVIDENCE GAPS: [INPUT NEEDED items]
```

## Quality checks before delivering

- [ ] Both profiles loaded (or `[PROVISIONAL]` tagged)
- [ ] Audience confirmed — report calibrated to that reader
- [ ] RAID and milestones sourced — not fabricated
- [ ] RAG uses profile thresholds — stated explicitly
- [ ] BLUF appears before workstream detail
- [ ] Every Red/Amber has action and ask
- [ ] Sponsor version is short enough to read in two minutes

## Worked example

**Input:** Sponsor audience; one Red workstream (integration slipped); RAID provided.

**Expected output (excerpt):**

```
OVERALL STATUS: Amber — integration workstream Red threatens Q3 go-live
HEADLINE: Integration milestone 2 weeks late on critical path [sourced: milestone tracker]
ASK: Sponsor decision on descoping vs. adding vendor capacity [review]
```

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: provide missing inputs and re-run, `steering-pack`, or confirm GATE before external distribution.
