<!--
SKILL AUTHORING TEMPLATE — claude-for-strategy

Copy this file to <plugin>/skills/<skill-name>/SKILL.md and fill it in.
Replace every [PLACEHOLDER] — don't ship a section with placeholder text
still in it.

Read references/skill-design-framework.md before filling this in. Every
section below exists to satisfy a specific parameter or failure mode in that
document, noted in parentheses. Filling in every section here gets you to
Schema (Parameter 12) automatically. It does NOT automatically satisfy the
substantive parameters — Work Shape, Confidence Bands, Failure Modes — those
require real thought about what THIS skill actually does, not just a filled
template.
-->
---
name: skill-name
description: >
  State both WHAT this skill does and WHEN to use it, third-person,
  trigger-rich. This is the ONLY thing Claude reads before deciding whether
  to fire this skill — put the actual triggering language here, not just in
  the body. Spell out adjacent phrasings a user might say, not just the
  formal task name.
allowed-tools: Read, Grep, Glob
  # Read/Write/Glob/Grep only = 🟢 on Trust Surface (Parameter 10).
  # Anything beyond this (Bash, WebFetch, WebSearch, MCP wildcards) is
  # elevated — add it only with a one-line reason in this comment; skills-qa
  # will ask for one anyway.
metadata:
  version: "0.1.0"
  owner: "team-or-role"           # Parameter 5 — named owner, required for first-party skills
  review_cadence: "quarterly"     # Parameter 5 — review trigger
  work_shape: "[PLACEHOLDER]"     # Parameter 2 — MUST be exactly one of:
                                   #   hypothesis-driven-analysis
                                   #   option-evaluation
                                   #   structured-aggregation
                                   #   narrative-synthesis
                                   #   governance-tracking
                                   # See skill-design-framework.md#work-shapes.
                                   # No value outside this list. If this
                                   # skill genuinely needs a sixth shape,
                                   # that's a change to the framework doc
                                   # FIRST, in the same PR as this skill —
                                   # never a quiet new value here.
  output_class: "draft-for-review"  # Parameter 3 — Delegation Threshold,
                                     # made structural instead of a prose
                                     # disclaimer. One of: draft-for-review /
                                     # decision-support / structured-data /
                                     # tracking-update — match what the
                                     # output actually does.
  sourcing_policy: "volatile-facts-must-be-sourced"
  # NOT the Parameter 11 freshness mechanism. This is about which claims
  # inside THIS skill's output need a [verify] tag — see
  # skill-design-framework.md#11-freshness for why these are kept separate.
  # If this skill ships a references/ folder, ALSO declare the four real
  # freshness fields (see skill-installer/references/freshness.md):
  # last_verified: "YYYY-MM-DD"
  # freshness_window: "N days|months|years"
  # freshness_category: "market-data | methodology | benchmark | ..."
  # verified_against: "[citation or source]"
---

# Skill Name

## When to use

[What this skill is FOR — engagement types, work shapes, audience. This
elaborates the frontmatter description for a human reader; it does not
replace it, since the description is what Claude reads at selection time.
State the in-scope half of Scope Boundaries (Parameter 8) here.]

## What this skill does not do

[The out-of-scope half of Parameter 8, stated as design intent, not a
disclaimer. What input types should push a user to a different skill, and
which one?]

## Preconditions

[Minimum required inputs (Parameter 4). For each: what happens if it's
missing or incomplete — ask, halt, or proceed with a labeled assumption per
the no-silent-supplement rule? "Proceed silently" is not a valid answer for
any input here.]

## Provisional mode

[If this skill is allowed to proceed on thin or incomplete input per
Preconditions, what changes in its behavior? This is where Low Confidence
(Parameter 6) gets operationalized — name the uncertainty explicitly, don't
suppress it. Calibrate against this skill's declared `work_shape` using the
band table in skill-design-framework.md#work-shapes.]

## Trust spine

- **Confidence bands** (Parameter 6), per this skill's `work_shape` — copy
  the relevant row from skill-design-framework.md's calibration table and
  make it concrete for this skill: High → [...], Medium → [...],
  Low → [...].
- **Tag vocabulary in use:** this skill uses the house tags defined in
  `CLAUDE.md` § Shared guardrails (`[verify]`, `[review]`,
  `[model knowledge — verify]`, provenance tags). Do not invent
  skill-specific markers.
- **Failure modes addressed** (Parameter 7 — every mode mandatory for this
  skill's `work_shape` is required; others may be marked N/A with a reason):
  a. Strategic advice vs. strategic support — [how the strategist stays the
     decision-maker]
  b. Client confidentiality implications — [N/A with reason, or how it's
     handled]
  c. Accountability gap — [how the output format forces engagement with the
     judgment, e.g. via `[review]`, rather than presenting a single
     concluded answer]
  d. Analytical Rigor — [N/A with reason, or how output stays traceable to
     a MECE/falsifiable structure]
  e. Incentive Gaming — [N/A with reason, or the specific gaming pattern
     this skill guards against and how]
- **Escalation triggers** (Parameter 9): [novel input, out-of-playbook
  context, conflicting signals, complexity exceeding design — name the ones
  that apply to this skill specifically].

## Workflow

[Numbered steps. Include an explicit validate step before output. If
`work_shape` is `hypothesis-driven-analysis` or `narrative-synthesis`,
include a MECE/falsifiability check; if `structured-aggregation`, include a
completeness/source-tagging check; if `governance-tracking`, include a
gaming-pattern check before the output is finalized.]

## Output format

[The exact deliverable shape — not just "a memo," the actual structure.]

## Worked example

[At least one realistic input → expected output. A skill without this is a
Material Concern on Schema (Parameter 12) — do not skip it.]

## Quality checks before delivering

[Self-check before output goes out: MECE/source-tag check if applicable,
confirm every flagged item uses house tag vocabulary, confirm the output
doesn't read as a concluded decision where `output_class` says
draft-for-review.]

## Outputs

[Do not redefine the decision tree, the "one question I'd ask" line, or the
dashboard offer here — those are canonical in `CLAUDE.md` § Outputs and
apply by default. Only add content here for a justified deviation from the
house format, and state what the deviation is and why.]
