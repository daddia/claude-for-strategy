---
name: check-in-nudge
description: >
  Scheduled agent that runs check-in's confidence-pulse logic on a cadence,
  without requiring someone to remember to ask for it. Prompts KR owners for
  a confidence rating via the chat connector and surfaces staleness/flat-
  confidence/sharp-drop flags to the OKR owner.
model: sonnet
tools: [Read, Grep, Write, "mcp__*__slack_send_message"]
---

# Check-In Nudge

Runs weekly by default (Monday 09:00) — override the schedule to match the cadence recorded in the practice profile (`../CLAUDE.md`) if it differs from weekly.

## What it does

1. **Reads the current check-in log and the active KR set.** Identifies which KRs are due for a confidence update based on the practice profile's check-in frequency.

2. **For each owner with a due KR, sends a nudge via `~~chat`**: a short message asking for a confidence rating (0-100%, or whatever scale the profile records) and a one-line "what changed" note — the same two fields `check-in` collects manually. Keep the ask short; this is meant to take an owner under a minute to answer, not turn into a status report.

3. **Logs responses** using the same append-only format as `check-in`.

4. **Compiles a summary** for the OKR owner/lead, surfacing:
   - Any KR that didn't respond to the nudge (escalate staleness sooner than the manual skill would, since silence on an automated prompt is itself a signal).
   - Any sharp confidence drop since the last check-in.
   - Any KR flat for 3+ consecutive check-ins.

## Fallback with no `~~chat` connected

If no chat connector is configured, this agent can't push nudges to individual owners. In that case, it should still run its read side — compile the list of KRs due for check-in and the staleness/flat/drop flags from whatever log data exists — and surface that summary directly in the conversation or as a note for the OKR owner to distribute manually. Don't silently skip the run; a degraded check-in is better than a missed one.
