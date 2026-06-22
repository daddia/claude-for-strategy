---
name: milestone-tracker
description: >
  This skill should be used when the user asks to "where are we against
  plan," "check milestone status," "what's on the critical path," or
  provides a milestone plan and actuals that need a critical-path status
  check with slippage flagged.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Milestone Tracker

Check current progress against a milestone plan, identify the critical path, and flag slippage against the tolerance recorded in the practice profile — not just a list of dates, an assessment of what the slippage actually threatens.

## Process

1. **Read the practice profile** (`~/.claude/plugins/config/claude-for-strategy/pmo/CLAUDE.md`) for where the milestone plan lives and the slippage tolerance (how much delay before something is "at risk" vs. just noted).

2. **Get the milestone plan and current actuals.** Ask for both if not provided — don't infer progress from partial information.

3. **Identify the critical path** — which milestones, if delayed, push out the end date, versus which have float (can slip without affecting the overall timeline). This distinction matters more than a flat list of every milestone's status.

4. **For each critical-path milestone, compare planned vs. actual/forecast date.** Apply the tolerance from the practice profile to classify: on track, at risk (within tolerance but trending late), or slipped (beyond tolerance).

5. **For anything at risk or slipped, state the knock-on effect** — what downstream milestone or the overall end date is now threatened, not just that this one item is late.

6. **For non-critical-path items with float, note status but don't escalate** — distinguishing genuine threats to the timeline from cosmetic schedule noise is the actual value of this skill.

## Output format

```
CRITICAL PATH STATUS:
[Milestone] — Planned: [date] | Actual/Forecast: [date] | Status: [on track | at risk | slipped]
  Knock-on effect: [if at risk/slipped — what this threatens downstream]

NON-CRITICAL (float available):
[Milestone] — [status, brief]

OVERALL END DATE: [on track | at risk | slipped] — [why, in one line]
```
