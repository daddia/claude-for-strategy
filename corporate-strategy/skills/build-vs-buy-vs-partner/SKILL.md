---
name: build-vs-buy-vs-partner
description: >
  This skill should be used when the user asks "should we build this,
  acquire it, or partner for it," has a capability gap that needs a
  build/buy/partner decision, or wants that decision checked against the
  known failure pattern each path tends toward.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "corporate-strategy practice"
  review_cadence: "quarterly"
  work_shape: "option-evaluation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Build vs. Buy vs. Partner

## When to use

When a capability gap needs build/buy/partner framing — forces each path's known failure pattern into the conversation, not cost comparison alone.

## What this skill does not do

- **Does not close capability gaps without strategic relevance** — question worth closing first.
- **Does not re-derive synergy discipline** — buy path defers to `synergy-stress-test`.
- **Does not pick path without naming failure pattern** — recommendation includes mitigation.

## Preconditions

| Input | If missing |
|---|---|
| Capability gap stated precisely | Ask before evaluating paths |
| Strategic priority link | Question whether gap worth closing |

## Provisional mode

Missing build track record: note haircut cannot be calibrated — `[review]`.

## Trust spine

- **Strategic advice vs. support (mandatory):** Compares paths with failure patterns; strategist owns choice.
- **Escalation:** No exit mechanism on partner path → flag; buy without synergy test → route to `synergy-stress-test`.

## Workflow

1. State capability gap and strategic relevance.
2. Core vs commodity test.
3. **Build:** time/cost + overrun failure pattern + haircut from track record.
4. **Buy:** headline terms + synergy handoff if live.
5. **Partner:** structure + exit mechanism.
6. Recommend with most likely failure pattern and mitigation.

## Output format

```
CAPABILITY GAP: [...]
CORE OR COMMODITY: [...]
BUILD: [...] — Failure pattern risk: [...]
BUY: [...] — [synergy-stress-test if live]
PARTNER: [...] — Exit mechanism: [...]
RECOMMENDATION: [build | buy | partner] — [failure pattern + mitigation]
```

## Worked example

**Input:** Need ML fraud model. Team has no ML delivery track record.

**Excerpt:** Commodity-adjacent capability; BUILD failure pattern high (overrun history); PARTNER exit mechanism missing — flag. Recommend partner with defined exit or buy `[review]`.

## Quality checks before delivering

- [ ] Core/commodity named
- [ ] Each path's failure pattern explicit
- [ ] Partner exit asked
- [ ] Buy synergies routed if needed

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `synergy-stress-test`, `evaluate-strategic-option`, or implementation planning.
