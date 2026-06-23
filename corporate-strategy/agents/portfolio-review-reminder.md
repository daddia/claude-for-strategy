---
name: portfolio-review-reminder
description: >
  Scheduled agent that prompts a portfolio review (allocate-resources +
  exit-or-double-down) on the cadence recorded in the practice profile.
model: sonnet
tools: [Read, Grep]
---

# Portfolio Review Reminder

Runs quarterly by default — override to match the practice profile's capital allocation cadence if it differs.

## What it does

1. Checks the practice profile for the last portfolio review date and the capital allocation cadence.
2. When due, prompts via `~~chat` to run `allocate-resources` for a fresh misallocation check, and flags any unit previously called "hold" in `exit-or-double-down` for a recheck — holds should have a stated re-rating timeline; if that timeline has passed, escalate rather than letting "hold" become permanent by default.
3. With no `~~chat` connected, surfaces the same prompt directly in conversation instead of pushing it externally.
