---
name: cascade
description: >
  This skill should be used when the user asks to "cascade these OKRs,"
  "break this down to team level," or has objectives/KRs at one level that
  need to flow down with a genuine contribution check, a capacity sanity
  check, and a check for goals that work against each other across teams.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "okr practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Cascade

## When to use

OKR cycle owners cascading objectives/KRs down levels — with contribution, capacity, alignment, and cross-team conflict checks naive cascades skip.

## What this skill does not do

- **Does not draft objectives** — route to `/okr:draft-objectives`.
- **Does not write KRs** — route to `/okr:write-key-results`.
- **Does not set targets** — route to `/okr:set-targets`.

## Preconditions

| Input | If missing |
|---|---|
| Parent objectives/KRs to cascade | Ask user to provide |
| Practice profile (cascade levels, ceilings) | Proceed with defaults (3–5 objectives, 2–5 KRs); flag `[review]` |
| Child-level draft objectives/KRs | Ask user to provide or offer to draft via other skills |

## Provisional mode

Without org structure data: fan-out/capacity check labeled `[review]`; cross-team conflict check still runs on provided KRs.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** MECE cascade coverage, contribution tests complete, conflicts named.
  - **Medium:** Some restatements or coverage gaps flagged.
  - **Low:** Parent KRs missing or child set incomplete — scaffold only.
- **Failure modes:**
  - **Strategic advice vs. support:** Flags restatements and conflicts; does not resolve ownership disputes.
  - **Client confidentiality:** OKR content may be internal-only — CONFIDENTIAL header.
  - **Accountability gap:** Cross-team conflicts surfaced for conversation, not silently merged.
  - **Analytical Rigor:** Contribution test MECE; orphans and uncovered parents listed.
  - **Incentive Gaming:** Catches cross-team KR pairs that game one metric at another's expense.
- **Escalation triggers:** Overloaded fan-out on single parent KR — flag parent KR too broad.

## Workflow

1. **Read the practice profile** for cascade levels and objectives/KR ceilings.
2. **Run contribution test** on every cascaded objective — does achieving it move the parent KR?
3. **Run restatement check** — contribution vs. same goal with different owner.
4. **Run alignment/coverage check** — orphaned KRs and uncovered parent KRs.
5. **Run fan-out/capacity check** — too many children on one parent KR.
6. **Run cross-team conflict check** — sibling KRs that improve one team at another's expense.
7. **Completeness check** before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
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

## Worked example

**Input:** Parent KR "Reduce enterprise churn to 8%." Child A: "Ship onboarding v2"; Child B: "Slow release cadence for QA depth."

**Expected output (excerpt):**

```
PARENT: Reduce enterprise churn to 8%
  → Ship onboarding v2 (Product) — Contribution: restatement — output-shaped, not churn-linked [review]
  → Improve 90-day retention cohort by 5pts (Product) — Contribution: genuine

CROSS-TEAM CONFLICT CHECK:
  Product release-cadence KR vs. Platform stability KR: speed vs. quality tension on shared customers [review]
```

## Quality checks before delivering

- [ ] Contribution test on every child objective
- [ ] Orphans and uncovered parents listed
- [ ] Fan-out/capacity assessed
- [ ] Cross-team conflict check run across siblings
- [ ] Output does not read as approved cascade

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: revise children via `draft-objectives`/`write-key-results`, or escalate conflicts to leadership.
