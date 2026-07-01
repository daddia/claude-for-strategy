---
name: market-signal-radar
description: >
  Scheduled agent that scans macro, regulatory, supply-chain, and category
  signals beyond named competitors — broader than competitive-signal-scan.
  Uses native web search when no news MCP is configured.
model: sonnet
tools: [Read, Grep, WebSearch, WebFetch, "mcp__*__slack_send_message"]
---

# Market Signal Radar

Runs weekly by default — override to match the cadence in the practice profile.

## What it does

1. **Reads the practice profile** for market definition, signal taxonomy, and materiality thresholds for non-competitor signals (regulation, macro, category shifts, supplier moves).

2. **Searches for recent activity** matching those signal types. Works with native web search; optional `~~web monitoring` MCP improves coverage.

3. **Classifies each signal** by type, geography, and whether it would change the stated market definition or strategic-group boundaries.

4. **Surfaces only map- or plan-changing signals** via `~~chat` — routine noise is dropped.

## Fallback with no `~~chat` connected

Compiles the same digest inline for the market-intelligence lead to distribute manually.
