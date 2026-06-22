---
name: steering-prep
description: >
  N days before the next steering committee meeting (from ~~calendar),
  assembles current RAID, milestones, and pending decisions into a
  steering-pack prompt ready for review.
tools: [Read, Grep]
---

# Steering Prep

Runs daily by default (09:00, per the cron schedule above) and checks whether the prep window is open — N days before the next steering committee date.

## What it does

1. **Reads the next steering committee date from `~~calendar`.** If no calendar connector is configured, fall back to the steering cadence recorded in the practice profile (`~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md`) and estimate the next date from the last known steering meeting.

2. **Determines whether today falls within the prep window** — N days before the steering date. Default N is 5 unless the practice profile records a different lead time.

3. **When the prep window is open, assembles inputs for a steering pack:**
   - Current RAID log (escalated items first)
   - Critical-path milestone status (plan vs. actual, slippage flags)
   - Pending decisions from the decision log that need committee action

4. **Produces a steering-pack prompt** — not the finished deck, but a structured brief that `/pmo:steering-pack` (or the Steering Pack Builder agent) can turn into a decision-led deck outline: agenda, overall RAG, decisions needed, key risks, explicit asks. Lead with decisions, not status recap.

5. **Posts the prep brief to `~~chat`** with a note that the steering meeting is N days away and a `/pmo:steering-pack` run is recommended. If no chat connector is configured, write the brief to a file in the workspace instead.

6. **When the prep window is not open, exits quietly** — no post, no file. The daily schedule is only a check; output happens once per steering cycle when the window opens.

## Fallback with no `~~chat` connected

If no chat connector is configured, still run the read side when the prep window is open — assemble RAID, milestones, and pending decisions into the steering-pack prompt and write it to a file. Without `~~calendar`, use the practice profile's steering cadence to estimate the next date; note the assumption in the output.
