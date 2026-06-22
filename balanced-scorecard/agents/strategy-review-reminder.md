---
name: strategy-review-reminder
description: >
  Scheduled agent that prompts a review-and-validate run on the scorecard
  cadence, and separately tracks the much slower strategy-map refresh
  cadence so the two don't get conflated into the same rhythm.
---

# Strategy Review Reminder

Runs quarterly by default (9am on the 1st of Jan/Apr/Jul/Oct, per the cron schedule above) — override to match the practice profile's recorded scorecard review frequency if it differs.

## What it does

1. **On the quarterly trigger**, prompts the user via `~~chat` that a `review-and-validate` run is due, and pulls the current measure values it can access to pre-stage the review rather than starting from a blank prompt.

2. **Separately tracks the map-refresh date** recorded in the practice profile's "Last full map refresh" field. This is checked on every run but only surfaced as its own prompt when the annual (or profile-recorded) interval has elapsed — it should not fire every quarter alongside the scorecard reminder, since conflating the two cadences is exactly the failure mode this plugin is designed to avoid.

3. **If `review-and-validate` has flagged an accumulation of theory-problem links** in recent runs (check the persisted review history), escalate the map-refresh prompt early regardless of the scheduled date, with a note explaining why — accumulated theory problems are a legitimate trigger for an early refresh, not just the calendar.

## Fallback with no `~~chat` connected

Without a chat connector, this agent can't push a reminder. It should still run its read side — check both cadences against the practice profile and the review history — and surface whichever prompt is due directly in the conversation or as a note for the user to action manually.
