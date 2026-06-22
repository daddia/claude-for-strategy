---
name: decision-log
description: >
  This skill should be used when the user asks to "log this decision,"
  "record why we decided X," or needs a decision and its rationale added to
  a persisted, append-only decision log for later audit or onboarding
  reference.
allowed-tools: Read, Grep, Glob
disable-model-invocation: true
metadata:
  version: "0.1.0"
---

# Decision Log

Append a decision to a persisted, append-only log: decision, rationale, owner, date, and what would prompt revisiting it. This is an audit trail, not a working document — entries don't get edited after the fact, only added to.

## Process

1. **Read the practice profile** (`~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md`) for the decision log format and storage location.

2. **Get the current log** (file or pasted content) if one exists — this skill appends, it doesn't recreate the log each time.

3. **Capture the decision precisely** — the actual choice made, not the topic discussed. ("Identity will be a shared platform service, not per-product" is a decision; "discussed Identity architecture" is not.)

4. **Capture the rationale** — why this option over the alternatives, briefly. If the user only states the decision without rationale, ask — a decision log without rationale loses most of its value six months later when someone asks "why did we do it this way?"

5. **Capture the owner and date.**

6. **Capture the revisit trigger, if there is one** — what would prompt reopening this decision (a changed constraint, a date, a specific event). Not every decision needs one, but ask rather than assuming none exists.

7. **Output the full updated log**, appending the new entry — never modify or remove existing entries; if a past decision needs correcting, log a new entry that supersedes it and references the original by date, rather than editing history.

## Output format

```
[Full decision log, existing entries unchanged]

NEW ENTRY:
Date: [date]
Decision: [precise statement of what was decided]
Rationale: [why, vs. the alternatives]
Owner: [who made/owns this]
Revisit trigger: [if applicable, or "none specified"]
```
