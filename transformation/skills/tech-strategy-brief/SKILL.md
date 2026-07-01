---
name: tech-strategy-brief
description: >
  This skill should be used when the user asks to "write a decision brief for
  this platform choice," "brief this architecture decision," or needs a
  technology strategy decision (platform, vendor, build-vs-buy, architecture
  pattern) framed as options with a recommendation.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "transformation practice"
  review_cadence: "quarterly"
  work_shape: "option-evaluation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Tech Strategy Brief

## When to use

BLUF decision brief for technology strategy calls — options including do-nothing, recommendation first, explicit ask.

## What this skill does not do

- **Does not make architecture decisions** — draft for ARB/sign-off.
- **Does not invent vendor pricing** — tag `[verify]` or `INPUT NEEDED`.
- **Does not skip do-nothing option** — always one of the real choices.

## Preconditions

| Input | If missing |
|---|---|
| Precise decision statement | Ask to narrow |
| Transformation practice profile | Proceed `[PROVISIONAL]` on platform vocabulary |

## Provisional mode

Without EA principles from profile: flag recommendations `[review]` against house rules once configured.

## Trust spine

Option-evaluation bands; recommendation before detail; conditions that would flip recommendation stated; GATE before board/exec final.

## Workflow

1. Read practice profile for platform vocabulary and risk posture.
2. State decision precisely.
3. Lay out options including do-nothing.
4. Per option: requirements, cost (time/disruption/lock-in), main risk.
5. State recommendation first (BLUF).
6. 2–4 MECE reasoning points.
7. Explicit ask — sign-off, budget, date.
8. Flag what would change the recommendation.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
RECOMMENDATION: [one to two sentences — stated first]

REASONING:
1. [...]
2. [...]

OPTIONS:
| Option | Requires | Cost | Main risk |
|---|---|---|---|

ASK: [decision needed, by when, from whom]
WOULD FLIP RECOMMENDATION IF: [...]
```

## Worked example

**Input:** Shared Identity platform vs per-product IdP.

**Expected output (excerpt):**

```
RECOMMENDATION: Adopt shared Identity platform — reduces duplicate security review [review]
WOULD FLIP RECOMMENDATION IF: Regulatory separation requires per-BU identity boundary [review]
```

## Quality checks before delivering

- [ ] Decision precise, not vague architecture improvement
- [ ] Do-nothing option included
- [ ] Recommendation before options detail
- [ ] Flip conditions stated
- [ ] Figures source-tagged

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/transformation/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/transformation:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: ARB sign-off, `business-case` for funding, or `target-operating-model` alignment.
