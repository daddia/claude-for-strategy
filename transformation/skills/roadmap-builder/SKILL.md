---
name: roadmap-builder
description: >
  This skill should be used when the user asks to "build a transformation
  roadmap," "sequence this into now/next/later," "lay out the delivery
  plan," or provides a current state and an ambition that need sequencing
  into a phased roadmap.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.4.0"
  owner: "transformation practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Roadmap Builder

## When to use

Sequence transformation ambition into phased roadmap — dependency map before phase placement, not flat initiative lists.

## What this skill does not do

- **Does not build business case** — route to `/transformation:business-case`.
- **Does not invent capacity** — flag overloaded phases.
- **Does not use generic Now/Next/Later** when profile defines named track model.

## Preconditions

Load org + transformation profiles; provisional mode available.

## Provisional mode

Defaults: Now/Next/Later; balanced risk — see workflow below.

## Trust spine

Structured-aggregation bands; every initiative has phase rationale tied to dependencies; GATE before board/exec final.

## Assumption audit

Before dependency mapping, audit initiative-prioritisation assumptions:

| Assumption | Status | If wrong, what breaks |
|---|---|---|
| Initiative list is complete | [confirmed / partial / unknown] | Critical path missing |
| Dependency direction (A blocks B) | [confirmed / assumed / unknown] | Wrong phase order |
| Team capacity per phase | [sourced / estimated / unknown] | Overloaded phases hidden |
| Funding tranche timing | [confirmed / assumed / unknown] | Now-quarter commitments unfunded |
| Risk posture applied | [from profile / default / user-stated] | Wrong sequencing bias |

Surface audited assumptions in `LOAD-BEARING ASSUMPTIONS` when any status is `assumed` or `unknown`.

## Red flags

Initiative prioritisation failures are **non-negotiable** to flag before governance publish:

- **MUST NOT** assign initiatives to phases without a one-line dependency rationale — flat lists cause false parallelism.
- **Do not proceed** to board-final if a phase exceeds plausible capacity without a `CAPACITY FLAGS` line — overload causes slip cascades.
- **Hard stop:** sequencing high-variance bets in Now when risk posture is conservative without explicit user override — misaligned posture causes funding for foundations to stall.
- **MUST NOT** invent dates, FTE, or budget to justify phase placement — use `INPUT NEEDED`.

## Outside-view step

After Step 5 (phase placement), run a **reference-class sequencing check**:

1. Name comparable transformation or product programs (internal post-mortems or peer benchmarks) with documented phase-slip patterns.
2. Compare this roadmap's Now-quarter load and critical-path length to the class median — if this plan is more aggressive, state the optimism gap.
3. Record: `OUTSIDE-VIEW: [reference class] — typical slip [X weeks/quarters]; this plan [aligned/aggressive]; re-sequence trigger if [condition].`

**Always compare Now-quarter density to reference-class delivery throughput** because programs that pack more concurrent critical-path items than peer programs tend to cause milestone slip that invalidates the sequencing argument.

## Purpose

Produce a sequencing argument — not a flat initiative list. Each item is placed in a phase because of dependencies, risk posture, and capacity, with explicit flags where the roadmap exceeds what the org can plausibly deliver.

## Precondition: load profiles

**Before sequencing, read both:**

- `~/.claude/plugins/config/claude-for-strategy/org-profile.md`
- `~/.claude/plugins/config/claude-for-strategy/transformation/CLAUDE.md`

If missing or still template, surface the practice setup bounce (same pattern as `business-case`) with `/transformation:practice-setup` or **"provisional"**.

### Provisional mode

Defaults: Now (this quarter) / Next (1–2 quarters) / Later (beyond); balanced risk posture; no named governance gates. Tag `[PROVISIONAL]`. Ask once whether this is portfolio-level (Now/Next/Later) or execution-level (would benefit from a named track model once configured).

## Workflow

### Step 1: Orient

| Question | Answer |
|---|---|
| **Current state** | What's true today — capabilities, constraints, in-flight work |
| **Ambition** | Where this is headed — one sentence |
| **Roadmap grain** | Portfolio (horizons) vs execution (tracks/sprints) |
| **Audience** | Working team / sponsor / steering / board |
| **Planning horizon** | How far out — matches profile labels if configured |

If current state or ambition is vague, stop and clarify. A roadmap sequences a gap; vague endpoints produce vague sequencing.

### Step 2: Track model routing

Read `## Framework preferences → Roadmap track model` from the transformation profile.

| Profile state | Action |
|---|---|
| Named track model configured | Use **exact track names and order** from profile |
| Template / empty | Default to Now / Next / Later; note in output which model was used |
| User says execution-level but only horizons exist | Flag: "Execution-level roadmap requested — configure track model in profile for finer grain" |

Do not substitute a generic model when the profile names a specific one.

### Step 3: Dependency mapping

Before assigning phases, map dependencies:

```
DEPENDENCY MAP (working):
[Initiative A] blocks → [Initiative B] because [reason]
[Initiative C] unblocks → [Initiative D]
```

Initiatives with unresolved dependency inputs get `INPUT NEEDED: confirm whether [X] blocks [Y]` — do not guess sequencing order.

### Step 4: Risk posture application

Read risk posture from org profile or transformation profile (`conservative / balanced / aggressive`). State which is applied:

| Posture | Sequencing bias |
|---|---|
| Conservative | Platform/foundation first; defer high-variance bets |
| Balanced | Mix foundational and value delivery per dependency logic |
| Aggressive | Front-load higher-risk, higher-reward items where dependencies allow |

### Step 5: Phase placement

Place each initiative in a phase with a **one-line rationale** — what it depends on, what it unblocks, why this phase and not the next.

### Step 6: Capacity and gate alignment

**Capacity check:** compare phase load to org size/structure from profiles. Flag overloaded phases explicitly.

**Gate alignment:** check `## Review gates` in the transformation profile — note which initiatives require discovery exit, architecture review, investment approval, or release gate before the next phase can start.

### Step 7: Kill / revisit criteria

For the overall roadmap and any high-risk phase:

```
KILL / REVISIT CRITERIA:
- Re-sequence if: [trigger — e.g. dependency slips, funding not approved]
- Pause program if: [trigger]
- Revisit horizon labels if: [trigger]
```

### Step 8: Board-ready gate

Run the trust-spine **GATE** before a governance-facing or board-final roadmap. Working drafts for the delivery team skip the gate.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
TRACK MODEL APPLIED: [named model from profile | Now/Next/Later provisional default]
RISK POSTURE APPLIED: [conservative | balanced | aggressive]

LOAD-BEARING ASSUMPTIONS:
- ...

AMBITION: [one sentence]

DEPENDENCY MAP:
- ...

[Track/Phase 1 name]:
  - [Initiative] — [rationale: depends on / unblocks / why here]
  - ...

[Track/Phase 2 name]:
  - ...

DEPENDENCIES (cross-phase): [explicit flags]
CAPACITY FLAGS: [overloaded phases, with rationale]
GATE ALIGNMENT: [initiatives requiring named approval before progression]
KILL / REVISIT CRITERIA: [...]
EVIDENCE GAPS: [INPUT NEEDED items]
```

## Quality checks before delivering

- [ ] Both profiles loaded (or `[PROVISIONAL]` tagged)
- [ ] Current state and ambition confirmed before sequencing
- [ ] Named track model used when configured — not silently replaced
- [ ] Every initiative has phase-placement rationale
- [ ] Dependencies mapped before phase assignment
- [ ] Capacity risk flagged where phases look overloaded
- [ ] No invented dates, costs, or capacity figures

## Worked example

**Input:** Identity platform must precede customer portal; three initiatives in Now quarter.

**Expected output (excerpt):**

```
Now: Identity platform — Rationale: blocks portal SSO dependency
CAPACITY FLAGS: Now quarter overloaded — 3 initiatives vs. 2-team capacity [review]
```

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `business-case`, resolve capacity flags, or GATE before steering publish.
