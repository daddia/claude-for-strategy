---
name: maturity-assessment
description: >
  This skill should be used when the user asks to "assess our digital
  maturity," "score our transformation maturity," "where do we stand
  digitally," or provides interview notes, survey results, or observations
  that need to be scored against a maturity framework.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.2.0"
---

# Maturity Assessment

Score current-state digital maturity against a capability model and produce a scorecard with a narrative explaining the score, not just the number.

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

Produce an evidence-backed maturity scorecard where every score cites specific observations — not generic level descriptions — and names the binding constraint that should drive sequencing.

## Precondition: load profiles

**Before scoring, read both:**

- `~/.claude/plugins/config/claude-for-strategy/org-profile.md`
- `~/.claude/plugins/config/claude-for-strategy/transformation/CLAUDE.md`

If missing or template, surface cold-start bounce with `/transformation:cold-start-interview` or **"provisional"**.

### Provisional mode

Default framework: six dimensions — Strategy, Customer Experience, Operations, Technology, Organization, Culture — scored 1–5 (1 = Ad hoc, 5 = Optimized). Tag `[PROVISIONAL]`. Note which dimensions use profile-defined names once configured.

## Workflow

### Step 1: Orient

| Question | Answer |
|---|---|
| **Framework** | Capability dimensions and scale from profile |
| **Input sources** | Interviews, surveys, observations, documents |
| **Scope** | Enterprise / BU / domain |
| **Audience** | Working session / steering / board |
| **Assessment purpose** | Baseline / re-score / gate for funding |

Confirm framework and scale from `## Framework preferences → Maturity framework` and `## Definitions → Maturity scoring scale`. Use exact dimension names from profile when configured.

### Step 2: Evidence coverage check

Map inputs to dimensions before scoring:

| Dimension | Evidence provided? | Source |
|---|---|---|
| [each dimension] | Yes / partial / none | [document, interview, observation] |

**Insufficient evidence rule:** score only what's covered. Mark uncovered dimensions **"insufficient evidence"** — do not guess a score from general industry knowledge.

If the user wants a directional view without evidence, produce **structured first pass** and label unscored dimensions explicitly.

### Step 3: Score each covered dimension

For each scored dimension:

- **Score** — on the configured scale
- **Evidence** — the specific observation that produced this score (not what a "3" usually looks like)
- **Level-up requirement** — what one level up would require for **this org specifically**

Tag any benchmark comparisons `[sourced: …]` or `[unverified — …]`.

### Step 4: Binding constraint identification

Across all dimensions, identify which one is **actually gating** overall progress — not just the lowest score. A flat profile often hides the one constraint that blocks everything else; call it out explicitly.

### Step 5: Sequencing implication

State what the binding constraint implies for `roadmap-builder` and `business-case` prioritization — one paragraph, BLUF style.

### Step 6: Narrative (BLUF)

Lead with headline finding (overall stage + binding constraint), then dimension breakdown.

### Step 7: Board-ready gate

Run trust-spine **GATE** before external or board-facing scorecards.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
FRAMEWORK: [dimensions and scale applied — profile or provisional default]
SCOPE: [enterprise | BU | domain]

LOAD-BEARING ASSUMPTIONS:
- ...

HEADLINE: [overall maturity stage + binding constraint — one sentence]

| Dimension | Score | Evidence | What level [N+1] requires |
|---|---|---|---|
| ... | ... | [specific observation] | ... |

BINDING CONSTRAINT: [dimension] — [why this gates the others]
SEQUENCING IMPLICATION: [what to prioritize given the constraint]
INSUFFICIENT EVIDENCE: [dimensions not scored + what's needed to score them]
EVIDENCE GAPS: [INPUT NEEDED]
```

## Quality checks before delivering

- [ ] Both profiles loaded (or `[PROVISIONAL]` tagged)
- [ ] Framework and scale match profile when configured
- [ ] Every score tied to specific evidence — not generic level descriptions
- [ ] Uncovered dimensions marked insufficient evidence — not guessed
- [ ] Binding constraint identified — not just lowest average
- [ ] No invented survey results or benchmark scores

## Close with next steps

Branches: gather evidence for insufficient dimensions, hand off sequencing to `roadmap-builder`, fund level-up work via `business-case`, re-run after discovery exit, or take binding-constraint finding to steering.
