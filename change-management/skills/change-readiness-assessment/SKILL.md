---
name: change-readiness-assessment
description: >
  This skill should be used when the user asks "are we ready for go-live,"
  "assess change readiness," "what is the binding constraint on adoption,"
  or needs a structured readiness scorecard before sponsor or steering decisions.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "change-management practice"
  review_cadence: "quarterly"
  work_shape: "hypothesis-driven-analysis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Change Readiness Assessment

## When to use

Assess people-side readiness across practice-defined dimensions; identify the binding constraint blocking adoption — not an average score.

## What this skill does not do

- **Does not map stakeholders** — route to `/change-management:stakeholder-impact-map` if segments are missing.
- **Does not certify go-live** — outputs are for human sign-off per practice profile gates.
- **Does not invent adoption metrics** — no fabricated survey scores or sentiment percentages.

## Preconditions

| Input | If missing |
|---|---|
| Initiative context and timeline | Ask scope and target go-live |
| Stakeholder impact map (recommended) | Assess at highest level available; flag gap |
| Practice profile readiness dimensions | Use default set; `[PROVISIONAL]` |

## Provisional mode

Without stakeholder map: assess program-level readiness only; flag `[review]` on segment-specific claims.

## Trust spine

- **Confidence bands** (`hypothesis-driven-analysis`):
  - **High:** Dimensions scored with cited evidence; binding constraint named with mechanism.
  - **Medium:** Some dimensions self-reported or single-source; constraint hypothesized.
  - **Low:** Scope or timeline unstated — halt or score scaffold only.
- **Failure modes:**
  - **Analytical rigor:** Separate "willing" from "able"; don't conflate sponsor agreement with frontline readiness.
  - **Client confidentiality:** Readiness politics sensitive — CONFIDENTIAL header when material.

## Workflow

1. **Read practice profile** — readiness dimensions, RAG definitions, past change history notes.

2. **Score each dimension** (from profile or defaults: leadership alignment, sponsor visibility, past change fatigue, capacity, skills/training, culture fit, resistance plan in place):
   - **Evidence** — what supports the score (named artifact, interview, observation — not vibes).
   - **RAG** — per profile definitions or Red/Amber/Green with explicit criteria.
   - **Gap** — what would need to be true to move one notch.

3. **Run the willing-vs-able test** on the lowest-scoring frontline-facing dimension — leadership often scores Amber on alignment while frontline scores Red on ability; the binding constraint is usually the latter.

4. **Identify binding constraint** — single dimension whose failure would block adoption even if others pass; explain the mechanism (e.g. training incomplete → revert to old process under pressure).

5. **Recommend response type** — sponsor, comms, training, structural, or timing — without picking a single mandated action; link to downstream skills.

## Output format

```
INITIATIVE: [name]
TARGET GO-LIVE: [date or window]
OVERALL PEOPLE READINESS RAG: [R/B/G] — [one-line rationale]

DIMENSION: [name]
  RAG: [R/B/G]
  Evidence: [source-tagged]
  Gap to next level: [specific]
  Willing vs able: [willing | able | both at risk — note]

BINDING CONSTRAINT: [dimension] — [mechanism]
RECOMMENDED RESPONSE TYPES: [sponsor | comms | training | structural | defer — options, not mandate]

UNSCORED / NEEDS EVIDENCE: [list, or "none"]
```

## Worked example

**Input:** Go-live in 3 weeks, leadership "aligned," no training delivered to call-center agents.

**Expected output:** Binding constraint = skills/training (able, not willing); overall Red; defer or narrow scope flagged `[review]`.

## Quality checks before delivering

- [ ] Every dimension has evidence or explicit gap
- [ ] Binding constraint named with mechanism
- [ ] No invented adoption statistics

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/change-management/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/change-management:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `sponsor-roadmap` or `resistance-diagnosis`.
