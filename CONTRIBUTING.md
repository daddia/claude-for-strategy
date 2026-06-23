# Contributing to Claude for Strategy

Notes for anyone writing or editing a plugin in this repo. Keep this short — the
design principles that matter most for the quality of the output, not a style
guide.

## Before your first PR

Sign the CLA. The first time you open a pull request, the CLA Assistant bot will
comment with a link to the [CLA](CLA.md) and ask you to confirm. Reply with
`I have read the CLA Document and I hereby sign the CLA` and the check will pass.
You only need to do this once.

## Design principle: SKILL.md encodes the right behavior; CLAUDE.md and the trust
spine are the net

Every plugin in this repo ships with two layers of instruction:

1. **`<plugin>/skills/<skill>/SKILL.md`** — what this specific skill does, step by
   step. The narrow, task-specific scaffold.
2. **`<plugin>/CLAUDE.md`** plus the repo-wide **trust spine** (`consulting/references/trust-conventions.md`, mirrored at `references/trust-conventions.md`) — the practice profile template, sourcing-tag discipline, load-bearing assumptions surfaced up front, numbers provenance ("flag, don't invent"), confidence calibration, and the board-ready gate. The wide, plugin-level safety net.

**If a skill's correct output depends on a guardrail catching a mistake the
SKILL.md would have made, that's a design smell.** The SKILL.md should tell the
model what to do directly; the guardrails should catch what the SKILL.md missed.
Every time a guardrail has to rescue a skill, we're relying on the guardrail
firing consistently — and on a bad run, a weaker model, a terser prompt, or a
future editor who reads only the skill text, the rescue doesn't happen.

**Rule of thumb: if a QA test passes only because a guardrail fired, add the
behavior to the SKILL.md directly.** The guardrail stays (belt and suspenders),
but the skill now carries the knowledge it needs on its own.

Examples of this rule in practice:

- A growth-vector assessment should not only work because the practice profile
  happened to record a target. The skill should read the profile and **stop to
  ask for a growth target** when none exists — the analysis is meaningless
  without a real number to test against.
- A business case should not land a plausible TAM only because the trust spine
  says not to invent inputs. Cost and benefit lines should carry `INPUT NEEDED`
  when figures are missing — not a round placeholder tagged after the fact.
- A board-ready deck should not get a reviewer note only because
  `trust-conventions.md` mentions the gate. Consequential skills (`business-case`,
  `deck-outline`, `performance-narrative`, and peers) should embed the trust
  spine inline and run the confirmation flow before stamping a final.

## A few concrete things that follow

- **Put the doctrine in the skill.** If a skill produces a business case, carry
  BLUF, options including do-nothing, and the ask. If it cascades OKRs, carry
  the parent-contribution test. Not a pointer to "and also think about" — the
  actual checklist.
- **Attach provenance tags to numbers, not to paragraphs.** `[sourced: Gartner
  Market Guide for X, 2025, user-uploaded PDF]` next to the TAM;
  `[unverified — from training data, needs a real source]` on the benchmark line
  the recommendation leans on. Tags on surrounding prose get lost; tags on the
  load-bearing digit do not.
- **Make the stop pathway a scaffold, not an escape hatch.** If the right answer
  to some category of question is "I can't proceed without X," bake that into the
  skill as a hard gate. `corporate-strategy`'s `/assess-growth-vectors` no-target
  rule is the pattern: stated plainly, non-overridable, owned by the skill.
- **Write the gate header so the gate is default-on.** If there is an
  exemption, phrase the heading as the gate and narrow the exemption in a
  sub-bullet, not the other way around. A load-bearing parenthetical is a bug
  waiting to be reintroduced by the next edit.

## Workflow notes

- **Read the plugin's `CLAUDE.md` before editing any skill in that plugin.** The
  practice profile sections, integrations table, and house conventions shape what
  the skill should say and omit.
- **Use canonical skill names in prose.** When a skill tells the user "run
  `/foo`," `foo` must match the actual `skills/<foo>/` directory name.
- **Bump the plugin version on a material change.** Patch bumps for behavior
  additions; minor bumps for new skills or new required inputs.
- **Run the validators.** See [CLAUDE.md](CLAUDE.md) — `claude plugin validate`,
  `scripts/sync-references.py --check`, `scripts/check-marketplace-sync.py
  --check`, `scripts/check-skill-frontmatter.py --check`, and for cookbooks
  `scripts/lint-tool-scope.py`. Optional: `pre-commit install` runs the skill
  frontmatter linter on staged `SKILL.md` files.
- **Do not remove the trust spine from consequential skills or
  `trust-conventions.md`.** The net stays. The goal is a skill that doesn't need
  the net, not a plugin without one.
