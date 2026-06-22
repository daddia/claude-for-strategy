---
name: check-span-and-layers
description: >
  This skill should be used when the user asks "is our org too top-heavy,"
  "do we have too many layers," "is this manager's span reasonable," or
  needs span of control and layer count diagnosed against known patterns
  for over- and under-management.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Check Span and Layers

Both directions of this failure are real and look different: too-narrow spans broadly across an org usually signal over-management and unnecessary layers; too-wide spans for roles that need real coaching or integration mean work falls through cracks. Layers compound the problem — each additional layer typically adds communication delay and some information distortion, and should be justified by genuine complexity, not assumed neutral.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for known span and layer data.

2. **Get span of control by function/level.** For each, assess against role type: narrow spans (roughly 1-5 direct reports) are defensible for highly technical, judgment-heavy, or closely-coached roles; broadly narrow spans across less specialized roles usually signal excess management layers rather than genuine coordination need. Wide spans (roughly 12+) are defensible for largely independent, self-directed roles; wide spans for roles needing real coaching or quality oversight are a red flag regardless of how efficient they look on an org chart.

3. **Count layers from the top to the frontline**, and assess whether the count is justified by genuine complexity (distinct businesses, regulatory separation, deep technical specialization) or has simply accumulated. More layers should be argued for explicitly, not treated as a neutral byproduct of growth.

4. **Estimate the practical cost of excess layers** — decision latency (how many approvals does a typical decision pass through) and information distortion (how much does a message change shape by the time it travels from frontline to top, or top to frontline) — even a rough estimate makes this concrete rather than abstract.

5. **Recommend specific changes** — flattening specific layers, widening or narrowing specific spans — tied to the role-type reasoning above, not a blanket "reduce layers" recommendation that ignores where layers are actually earning their place.

## Output format

```
SPAN ANALYSIS:
[Function/Level] — Span: [N] — Role type: [highly coordinated/specialized vs.
  independent/self-directed] — Assessment: [defensible / flag — too narrow / flag — too wide]

[repeat]

LAYER ANALYSIS: [N] layers, top to frontline
  Justified by: [genuine complexity — name it] or [no clear justification found — flag]
  Estimated decision latency: [rough — number of approvals for a typical decision]

RECOMMENDED CHANGES: [specific layers/spans, with role-type rationale]
```
