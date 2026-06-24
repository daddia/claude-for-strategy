---
name: realisation-checkpoint-reminder
description: >
  Scheduled agent that prompts a benefits-tracking run on the cadence
  set in the practice profile, and separately escalates any benefit
  approaching its business change's go-live with no baseline captured
  yet — a point-of-no-return distinct from an ordinary reminder.
schedule: "0 9 1 * *"
metadata:
  version: "0.1.0"
---

# Realisation Checkpoint Reminder

Runs monthly by default (9am on the 1st, per the cron schedule above) — override to match the practice profile's recorded tracking cadence if it differs from monthly.

## What it does

1. **Reads the current benefits register and tracking log.** Identifies which benefits are due for a `benefits-tracking` run this cycle, based on the profile's tracking cadence.

2. **Prompts the benefit owner(s) via `~~chat`** that tracking is due, and pulls the most recent measured value it can access to pre-stage the run rather than starting from nothing.

3. **Separately, and with higher urgency, scans the register for any benefit whose business change is scheduled to go live — or has already gone live — within the practice profile's baseline window, with no baseline value yet recorded.** This is escalated distinctly from the ordinary tracking reminder above, with an explicit note explaining why: once the business change starts, a clean pre-change baseline can no longer be captured, and the benefit's realisation claim becomes permanently harder to prove. This check should fire even between scheduled tracking cycles if a go-live date is close.

4. **Compiles a summary** for the benefits owner or value-realisation lead, surfacing:
   - Benefits due for tracking this cycle.
   - Any benefit with a missing-baseline escalation (flagged separately and first).
   - Any benefit that didn't respond to last cycle's tracking prompt (silence on a due tracking run is itself worth noting, not just re-prompting silently).

## Fallback with no `~~chat` connected

Without a chat connector, this agent can't push prompts to individual owners. It should still run its read side — compile the due-tracking list and, especially, the missing-baseline escalation — and surface that summary directly in the conversation or as a note for the value-realisation lead to distribute manually. The missing-baseline check in particular should never be silently skipped; a degraded reminder is better than a missed baseline.
