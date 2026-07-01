---
name: cascade-to-scorecards
description: >
  This skill should be used when the user asks to "cascade the scorecard to
  business units," "build a team-level scorecard," or needs corporate
  strategy-map objectives translated into business-unit or team scorecards
  via a genuine causal-mechanism test, not just contribution-counting.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "balanced-scorecard practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Cascade to Scorecards

## When to use

For strategy office or BU leaders translating a corporate strategy map into business-unit or team scorecards. Assumes a corporate map exists from `/balanced-scorecard:build-strategy-map`. Output is a structured cascade draft for strategist review.

## What this skill does not do

- **Does not build the corporate strategy map** — requires `build-strategy-map` output first.
- **Does not set quarterly OKRs** — if OKR plugin is layered beneath BSC per practice profile, route execution commitments to `/okr:cascade`.
- **Does not select measures or targets** — route to `/balanced-scorecard:select-measures` and `/balanced-scorecard:set-targets-and-initiatives`.
- **Does not validate empirical truth of mechanisms** — flags weak or missing mechanisms; hand off to `/balanced-scorecard:review-and-validate`.

## Preconditions

| Input | If missing |
|---|---|
| Corporate strategy map (from `build-strategy-map` or practice profile location) | Halt — cannot cascade without a parent map |
| Target BU/team name and scope | Ask before drafting |
| Practice profile cascade policy (levels, local-objective policy) | Read profile; if absent, ask whether local-only objectives are expected and flag `[review]` |

## Provisional mode

When corporate map is partial or BU scope is unclear:

- Label output as scaffold-only in CASCADE HEALTH CHECK.
- Flag coverage gaps explicitly; do not invent cascaded objectives to fill gaps.
- Tag mechanisms **UNVALIDATED** when the user cannot state how the BU operationalizes the corporate parent.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Every relevant corporate objective has a specific cascaded child with stated mechanism; local-only objectives explicitly flagged; coverage gaps listed.
  - **Medium:** Mostly complete; some mechanisms weak or generic cascade partially flagged.
  - **Low:** Scaffold only — missing parent map, fully generic or fully disconnected without deliberate call; explicitly marked incomplete.
- **Tag vocabulary:** `[verify]`, `[review]`, `UNVALIDATED`, `local, not traced` per plugin `CLAUDE.md`.
- **Failure modes:**
  - **Strategic advice vs. support:** Surfaces cascade structure and health flags; does not decide whether a BU should be autonomous vs. fully aligned — `[review]` on fully disconnected patterns.
  - **Client confidentiality:** Cascade content may expose BU strategy — apply CONFIDENTIAL header; destination check before distribution.
  - **Accountability gap:** CASCADE HEALTH CHECK and COVERAGE GAPS force engagement; generic copy-paste cascades flagged, not smoothed over.
  - **Analytical Rigor:** N/A — mechanism discipline inherited from `build-strategy-map`, not MECE decomposition here.
  - **Incentive Gaming:** N/A — no scoring or target-setting in this skill.
- **Escalation triggers:**
  - Fully disconnected cascade with no deliberate autonomy rationale → flag and ask strategist to confirm intentional design.
  - Fully generic cascade (copy-paste corporate objectives) → flag, require local operational specificity or explicit demotion.
  - Corporate objective relevant to BU with zero cascaded support → name in COVERAGE GAPS; do not silently omit.
  - OKR plugin installed and user expects quarterly KRs here → clarify seam; route to `/okr:cascade`.

## Workflow

1. **Read the practice profile** for cascade levels and whether locally-owned objectives are expected at cascaded levels.

2. **For each corporate-map objective relevant to this BU/team, draft the cascaded version** as operational implementation — specific enough that it's clear what this unit would do differently, not a restatement with a new owner.

3. **State the mechanism** linking cascaded objective to corporate parent: "this unit achieving X operationalizes corporate objective Y because [mechanism]." Apply same rubric as `build-strategy-map` — tag **UNVALIDATED** if missing; do not invent prose.

4. **Distinguish legitimate local objectives from disconnection.** Local-only objectives (e.g. plant safety with no corporate equivalent) → flag **local, not traced**; not a failure on its own. Flag extremes:
   - **Fully generic cascade** — corporate objectives copy-pasted with no local specificity.
   - **Fully disconnected** — most objectives local with no traced link; may be deliberate for autonomous units — flag `[review]`, not a silent default.

5. **Coverage check upward:** every corporate-map objective relevant to this unit has at least one cascaded objective? Name gaps.

6. **OKR seam:** if `okr` is installed per practice profile, note this output is the BSC-layer cascade; quarterly execution is `/okr:cascade`'s job.

7. **Completeness check:** every figure source-tagged or flagged `[verify]` before output.

## Output format

```
BUSINESS UNIT: [name]

Cascaded from [corporate objective]:
  → [Cascaded objective] — Mechanism: [...] — Quality: [strong | weak | UNVALIDATED]

Local objective (not traced to corporate map): [objective] — [why it belongs here]

CASCADE HEALTH CHECK: [fully generic / appropriately mixed / fully disconnected] — [explain]
COVERAGE GAPS: [corporate objectives relevant to this unit with no cascaded support]
```

## Worked example

**Input:** Corporate map objective "Grow enterprise ARR 20%." BU: EMEA Sales. User proposes cascaded objective "Hit EMEA quota" with no mechanism.

**Expected output (excerpt):**

```
BUSINESS UNIT: EMEA Sales

Cascaded from Grow enterprise ARR 20%:
  → Close $12M net-new enterprise ARR in EMEA — Mechanism: UNVALIDATED — user stated quota only, no operational link to corporate growth target — Quality: UNVALIDATED [review]

CASCADE HEALTH CHECK: appropriately mixed — one cascaded objective drafted but mechanism unstated
COVERAGE GAPS: none for stated corporate objective
```

## Quality checks before delivering

- [ ] Corporate parent map read and referenced
- [ ] Every cascaded objective has mechanism or UNVALIDATED tag
- [ ] Local-only objectives explicitly flagged, not hidden
- [ ] Generic vs. disconnected health check run
- [ ] Coverage gaps listed
- [ ] OKR seam noted if applicable
- [ ] Output does not read as a concluded alignment decision

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/balanced-scorecard/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/balanced-scorecard:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Natural next branches: select measures for cascaded objectives, cascade OKRs beneath BSC layer, or `review-and-validate` on UNVALIDATED mechanisms.
