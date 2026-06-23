---
name: competitive-signal-scan
description: >
  Scheduled agent that scans for competitor moves matching what the
  practice profile defines as a meaningful signal, and flags anything that
  would change the strategic-group map or incentive map. Notably usable
  with no MCP connector at all — see notes below.
model: sonnet
tools: [Read, Grep, WebSearch, WebFetch, "mcp__*__slack_send_message"]
---

# Competitive Signal Scan

Runs weekly by default — override to match the cadence in the practice profile.

## What it does

1. **Reads the practice profile** for the named competitor set and what specifically counts as a meaningful signal (pricing changes, executive departures, funding rounds, product launches, etc. — whatever was recorded during setup).

2. **Searches for recent activity** matching those signal types for each named competitor. This is the one agent in the repo that can do meaningful work using this environment's **native web search**, with no MCP connector required — a dedicated news/monitoring connector (see `CONNECTORS.md`) improves reliability and breadth for serious ongoing use, but isn't a blocker to getting value immediately.

3. **For anything found, checks relevance against the existing strategic-group map and incentive map** (if either has been built): does this signal suggest a competitor is moving across a mobility barrier identified earlier, or does it reveal something about a competitor's incentive structure that updates a prior `map-incentives` prediction?

4. **Surfaces only what's actually new or map-changing** via `~~chat` — explicitly avoid reporting routine, expected activity that doesn't update anything; a weekly digest of things that don't matter trains people to ignore it.

## Fallback with no `~~chat` connected

Without a chat connector, compiles the same findings and surfaces them directly in conversation rather than pushing externally.
