---
name: exec-memo
description: >
  This skill should be used when the user asks to "write an exec memo,"
  "BLUF this," "turn this into a one-pager," or needs a narrative or raw
  notes condensed into a conclusion-first executive memo.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "consulting practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Exec Memo

## When to use

BLUF executive memo from narrative, notes, or `narrative-builder` output. Conclusion first per `../../references/bluf-conventions.md`.

## What this skill does not do

- **Does not bury the bottom line** — BLUF is structural, not stylistic.
- **Does not exceed profile length** by shrinking the bottom line — cut detail section.
- **Does not ship board-final without gate** — confirm + reviewer note.

## Preconditions

| Input | If missing |
|---|---|
| Practice profile (length, audience) | Default one page; flag practice-setup |
| Source material or narrative | Ask for notes or run `narrative-builder` |

## Provisional mode

Raw notes only: compress inline; label structured first pass if MECE weak.

## Trust spine

Per `trust-conventions.md` — sourcing, assumptions, numbers, confidence, gate before exec-final.

- **Analytical Rigor:** Every WHY point traces to support; cut non-load-bearing detail.
- **Escalation:** Ask missing → make impossible to miss; unverified claims → tag not smooth over.

## Workflow

1. Read practice profile.
2. Use `narrative-builder` output if available; else compress notes inline.
3. Bottom line first (1–2 sentences, the answer).
4. WHY: 2–4 MECE points.
5. ASK: decision/resource/sign-off if any.
6. DETAIL: optional background last.
7. Check length vs profile.

## Output format

```
[BOTTOM LINE]

WHY:
1. [point]
2. [point]

ASK: [or omit]

DETAIL: [...]
```

## Worked example

**Input:** Notes on pricing failure. Bottom line: revert mid-tier increase.

**Excerpt:** BLUF states revert; WHY three MECE points (volume, elasticity, competitor); ASK: CFO sign-off by Friday.

## Quality checks before delivering

- [ ] Bottom line before context
- [ ] MECE WHY section
- [ ] ASK visible if needed
- [ ] Length vs profile
- [ ] Trust spine on figures

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/consulting/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/consulting:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Quiet mode for client-facing per profile.
