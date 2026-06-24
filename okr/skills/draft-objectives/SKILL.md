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
  version: "0.3.0"
  owner: "okr practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---

# Draft Objectives

## When to use

When candidate objectives need the KR-in-disguise test — qualitative, directional, strategically linked — not numbers wearing objective clothes.

## What this skill does not do

- **Does not write KRs** — route numbers to `/okr:write-key-results`.
- **Does not set targets** — route to `/okr:set-targets`.
- **Does not cascade** — route to `/okr:cascade`.

## Preconditions

| Input | If missing |
|---|---|
| Candidate objectives | Ask user to provide |
| Practice profile (cascade level, ceiling) | Default 3–5 per level; flag `[PROVISIONAL]` |
| Parent strategy or parent KR (if cascaded) | Ask; flag linkage gap if absent |

## Provisional mode

Without parent linkage: flag every objective **Strategic linkage: none found**; do not PASS without connection at cascaded levels.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** MECE objective set within ceiling; each PASS with linkage.
  - **Medium:** Some vague or KR-in-disguise flags with suggested rewrites.
  - **Low:** Majority metric-laundered or inspirational mush — scaffold only.
- **Failure modes:**
  - **Strategic advice vs. support:** Verdicts are diagnostic; strategist owns final wording.
  - **Client confidentiality:** Objectives may be pre-release — CONFIDENTIAL header.
  - **Accountability gap:** KR-in-disguise rejected with number relocated, not silently accepted.
  - **Analytical Rigor:** Set-level count and overlap check MECE.
  - **Incentive Gaming:** Guards metric laundering — objectives that are pre-committed metrics or vanity goals dressed as strategy.
- **Escalation triggers:** Set exceeds ceiling with no deprioritization plan — flag focus risk.

## Workflow

1. **Read practice profile** for cascade level and objectives-per-level ceiling.
2. **For each candidate:** would achieving this be good without a number? Reject quantity-in-objective as KR-in-disguise.
3. **Check strategic linkage** to parent KR or org strategy.
4. **Check count** against ceiling — flag set if over.
5. **Check vague inspirational mush** — two people could write unrelated KRs?
6. **Completeness check** before output: set-level overlap assessed.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
LOAD-BEARING ASSUMPTIONS: [if any]

Objective 1: [text]
  Verdict: [PASS | FLAG — KR-in-disguise | FLAG — too vague]
  Strategic linkage: [what this connects to, or "none found — flag"]

[repeat per objective]

SET-LEVEL CHECK: [count vs. ceiling; any overlap between objectives]
```

## Worked example

**Input:** "Increase revenue by 20%"; "Be great at customer experience."

**Expected output (excerpt):**

```
Objective 1: Increase revenue by 20%
  Verdict: FLAG — KR-in-disguise; suggested objective: Become clear value leader in mid-market segment
  Strategic linkage: none stated [review]

Objective 2: Be great at customer experience
  Verdict: FLAG — too vague; suggest narrowing to: Reduce onboarding friction for enterprise tier

SET-LEVEL CHECK: 2 objectives — within ceiling; overlap: none
```

## Quality checks before delivering

- [ ] KR-in-disguise test on every candidate
- [ ] Strategic linkage checked for cascaded levels
- [ ] Set count vs. ceiling
- [ ] Vague objectives flagged with narrowing suggestions
- [ ] Figures source-tagged or omitted

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `write-key-results`, `cascade`, or revise flagged objectives.
