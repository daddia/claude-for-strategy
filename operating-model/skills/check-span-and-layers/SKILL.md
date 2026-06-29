---
name: check-span-and-layers
description: >
  This skill should be used when the user asks "is our org too top-heavy,"
  "do we have too many layers," "is this manager's span reasonable," or
  needs span of control and layer count diagnosed against known patterns
  for over- and under-management.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "operating-model practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Check Span and Layers

## When to use

Diagnose span of control and layer count — both over-management (narrow spans, excess layers) and under-management (wide spans where coaching needed).

## What this skill does not do

- **Does not redesign decision rights** — route to `/operating-model:design-decision-rights`.
- **Does not assess strategic structure fit** — route to `/operating-model:diagnose-structure-fit`.
- **Does not recommend blanket flattening** — changes tied to role-type reasoning.

## Preconditions

| Input | If missing |
|---|---|
| Span by function/level | Ask user for org data or HRIS export |
| Layer count top to frontline | Ask; estimate with `[review]` if partial |
| Practice profile targets | Use industry norms; flag `[PROVISIONAL]` |

## Provisional mode

Partial org data: assess available spans/layers; flag incomplete coverage in output header.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Spans assessed by role type; layers justified or flagged; latency estimated.
  - **Medium:** Some functions missing; recommendations qualified.
  - **Low:** No span data — halt.
- **Failure modes:**
  - **Strategic advice vs. support:** Recommendations are draft for exec/HR review.
  - **Client confidentiality:** Headcount data sensitive — CONFIDENTIAL header.
  - **Accountability gap:** Flags tied to role types, not generic "reduce layers."
  - **Analytical Rigor:** Every function/level in scope assessed.
  - **Incentive Gaming:** N/A for this shape.
- **Escalation triggers:** Layer count with no complexity justification — flag decision latency cost.

## Workflow

1. **Read practice profile** for span/layer data and targets.
2. **Assess span by function/level** against role type (coaching vs. independent work).
3. **Count layers** top to frontline; justify by complexity or flag accumulation.
4. **Estimate practical cost** of excess layers — decision latency, distortion.
5. **Recommend specific changes** with role-type rationale.
6. **Completeness check** before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
SPAN ANALYSIS:
[Function/Level] — Span: [N] — Role type: [...] — Assessment: [defensible / flag — too narrow / too wide]

LAYER ANALYSIS: [N] layers, top to frontline
  Justified by: [complexity] or [no clear justification — flag]
  Estimated decision latency: [rough approvals for typical decision]

RECOMMENDED CHANGES: [specific layers/spans, with role-type rationale]
```

## Worked example

**Input:** Engineering managers span 4 on mostly independent IC work; 7 layers to frontline in single-product company.

**Expected output (excerpt):**

```
SPAN ANALYSIS:
Engineering Manager — Span: 4 — Role type: independent ICs — Assessment: flag — too narrow

LAYER ANALYSIS: 7 layers — Justified by: no clear justification found — flag
RECOMMENDED CHANGES: Widen EM spans to 8–10; remove one coordination layer between VP and directors [review]
```

## Quality checks before delivering

- [ ] Span assessed against role type, not single universal number
- [ ] Layers justified or flagged
- [ ] Latency/distortion estimated when layers excess
- [ ] Recommendations specific, not blanket flattening
- [ ] Coverage gaps noted if data incomplete

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: exec/HR review, `diagnose-structure-fit`, or org design workshop.
