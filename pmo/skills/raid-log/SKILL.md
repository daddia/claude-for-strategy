---
name: raid-log
description: >
  This skill should be used when the user asks to "log this risk," "add an
  issue to the RAID log," "update the RAID log," or needs a risk,
  assumption, issue, or dependency added to or updated in a persisted RAID
  log.
allowed-tools: Read, Grep, Glob
disable-model-invocation: true
metadata:
  version: "0.1.0"
---

# RAID Log

Append to or update a persisted Risk/Assumption/Issue/Dependency log, using the user's own definitions of each category and severity scale from the practice profile.

## Trust spine

```
INCENTIVE GAMING: Guards against severity laundering — downgrading real risks to
  Assumptions or low severity to avoid escalation, or softening language so an item
  looks managed when it isn't. Severity requires a one-line rationale tied to the
  profile scale; entries meeting the escalation threshold are flagged now, not
  deferred to the next steering cycle.
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent an input — flag what's needed instead.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

Full rules: repo-root `references/trust-conventions.md`.

## Process

1. **Read the practice profile** (`~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md`) for the RAID format, severity scale, and the user's specific Risk/Issue/Assumption/Dependency distinctions.

2. **Get the current log.** Ask for the existing log (a file, a pasted table, or a path) if this isn't a brand-new log — this skill appends/updates, it doesn't start over each time. If no log exists yet, create one using the format from the practice profile (or a sensible default: ID, Type, Description, Severity, Owner, Status, Date logged, Date resolved).

3. **Classify the new entry** as Risk, Issue, Assumption, or Dependency using the user's own definitions — if ambiguous, ask rather than guessing, since misclassification undermines the log's value as a governance tool.

4. **Assign severity** using the practice profile's scale, with a one-line rationale — not just a number, the reasoning a reviewer would want to see.

5. **Assign or ask for an owner.** Don't leave entries unowned.

6. **Check escalation threshold** from the practice profile — if this entry meets the threshold, flag it explicitly as needing escalation now, not just logged for the next steering cycle.

7. **Output the full updated log**, not just the new row — the user should be able to save this directly back over the existing file.

## Output format

```
[Full RAID log table, existing rows unchanged, new/updated row(s) added]

ESCALATION FLAG: [if this entry meets the threshold from the practice profile, say so explicitly and why]
```
