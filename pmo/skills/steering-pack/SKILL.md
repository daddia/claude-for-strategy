---
name: steering-pack
description: >
  This skill should be used when the user asks to "build the steering
  committee pack," "put together this month's steering deck," or needs an
  agenda plus RAG status plus key risks plus asks structured as a
  presentation outline for a governance meeting.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "pmo practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Steering Pack

## When to use

Steering committee deck outline — decisions first, escalation-filtered risks, action titles, appendix for detail.

## What this skill does not do

- **Does not fabricate status** — use `status-report` or verified inputs.
- **Does not present full RAID** — escalation threshold only in live deck.
- **Does not pad without decisions** — shorten pack if none pending.

## Preconditions

| Input | If missing |
|---|---|
| Org + pmo profiles | Tag `[PROVISIONAL]` |
| RAID + milestones or existing `status-report` | Skeleton with `INPUT NEEDED` |
| Time budget | Ask; default 60 min `[PROVISIONAL]` |

## Provisional mode

`[PROVISIONAL]` — monthly cadence; generic escalation thresholds.

## Trust spine

- **Confidence bands** (`narrative-synthesis`):
  - **High:** Decisions lead; risks filtered; action titles; time budget respected or bloat flagged.
  - **Medium:** Status derived from partial inputs with gaps listed.
  - **Low:** No inputs — skeleton only.
- **Failure modes:**
  - **Accountability gap:** Each decision slide has explicit Ask.
- **Escalation triggers:** Pack exceeds time budget — BLOAT FLAG.

## Purpose

Produce a steering pack where decisions come first and status supports them — filtered to escalation thresholds, action-titled slides, and an appendix for detail the room shouldn't sit through.

## Precondition: load profiles

**Before building the pack, read both:**

- `~/.claude/plugins/config/claude-for-strategy/org-profile.md`
- `~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md`

If missing or template, surface cold-start bounce with `/pmo:cold-start-interview` or **"provisional"**.

### Provisional mode

Defaults: monthly steering cadence; escalation = items with program-level schedule impact or unresolved >30 days; generic RAG thresholds. Tag `[PROVISIONAL]`.

## Workflow

### Step 1: Orient

| Question | Answer |
|---|---|
| **Meeting** | Steering committee name, date if known |
| **Time budget** | Total minutes — drives agenda weighting |
| **Decisions pending** | List or "derive from inputs" |
| **Inputs available** | RAID, milestones, prior `status-report`, decision log |

Read `## Governance structure` for steering cadence and escalation thresholds.

### Step 2: Input routing

| Input available | Action |
|---|---|
| `status-report` for this cycle exists | Use as status source — do not re-derive RAG from scratch |
| RAID + milestones only | Build status via same rules as `status-report`, then pack |
| Neither | Stop — request inputs; produce skeleton with `INPUT NEEDED` |

Do not fabricate status to fill slides.

### Step 3: Decisions first

Structure the pack so **decisions needed** are the first substantive content after agenda — not a status recap. For each decision:

```
Decision: [what must be decided]
Options: [2-3 real options, including defer]
Recommendation: [BLUF]
Ask: [what the committee must do — approve, choose, unblock]
```

If no decisions are pending, say so explicitly and shorten the pack — don't pad with status theater.

### Step 4: Escalation-filtered risks

Include only risks meeting the **escalation threshold** from the profile — not the full RAID log. For each:

- Action title (takeaway, not topic): "Identity migration is two weeks behind schedule" not "Risk Update"
- Severity, owner, mitigation, ask if any

### Step 5: Slide structure and action titles

Build slides in this order:

1. **Agenda** — time allocation weighted to decision items
2. **Overall program RAG** — one slide, headline only
3. **Decisions needed** — one slide per decision
4. **Key risks** — escalation threshold only
5. **Milestone status** — headline level
6. **Appendix** — full RAID reference, detailed milestones (not presented)

Apply action titles to every slide.

### Step 6: Bloat check

If the pack exceeds what fits the time budget or tries to present the full RAID log, flag explicitly:

```
BLOAT FLAG: [N] slides for [M] minutes — recommend moving [items] to appendix or a separate working session.
```

### Step 7: Board-ready gate

Run trust-spine **GATE** before the final pack circulates to steering or sponsors. Working outline for the PMO lead skips the gate.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
MEETING: [forum name, date if known]
TIME BUDGET: [minutes]

LOAD-BEARING ASSUMPTIONS:
- ...

AGENDA:
| Item | Minutes | Type |
|---|---|---|
| Decisions | ... | decision |
| ... | ... | ... |

OVERALL RAG: [status, one line — source: status-report or derived]

DECISIONS NEEDED:
Slide — [Action title]
  Decision: [...]  Options: [...]  Recommendation: [...]  Ask: [...]

KEY RISKS (above escalation threshold):
Slide — [Action title]
  [...]

MILESTONE STATUS:
Slide — [Action title]
  [...]

APPENDIX (not presented): [full RAID reference, detailed milestone data]
BLOAT FLAG: [if applicable]
EVIDENCE GAPS: [INPUT NEEDED]
```

## Quality checks before delivering

- [ ] Both profiles loaded (or `[PROVISIONAL]` tagged)
- [ ] Decisions lead — status supports, not replaces
- [ ] Risks filtered to escalation threshold — not full RAID
- [ ] Every slide has an action title
- [ ] Status sourced from `status-report` or verified inputs — not fabricated
- [ ] Time budget respected or bloat flagged
- [ ] Appendix holds detail stripped from the live deck

## Worked example

**Input:** 60-minute steering; 2 pending decisions; status-report exists; 3 risks above escalation threshold.

**Expected output (excerpt):**

```
AGENDA: Decisions 25 min | RAG 5 min | Risks 15 min | Milestones 10 min | Buffer 5 min
DECISIONS NEEDED:
Slide — Approve descoped Phase 2 go-live date
  Ask: Committee approves 30 Sept vs. hold for full scope [review]
```

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: run `status-report` if inputs thin, PMO review, GATE before committee circulation.
