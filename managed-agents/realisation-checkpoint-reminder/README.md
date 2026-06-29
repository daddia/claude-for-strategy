# Realisation Checkpoint Reminder — managed-agent cookbook

## Overview

Prompts a benefits-tracking run on the cadence set in the practice profile and separately escalates benefits approaching go-live with no baseline captured yet. Same source as the [`realisation-checkpoint-reminder`](../../value-realisation/agents/realisation-checkpoint-reminder.md) Claude Code agent — this directory is the Managed Agent cookbook for `POST /v1/agents`.

This is a **cookbook, not a product.** It assumes the benefits register and tracking log live in the workspace (markdown, spreadsheet export, or files under `value-realisation/data/`). Teams that keep registers in Confluence or Jira should wire a read connector on the reader tier or export to a local file before the run.

## Before you deploy

- **Register metadata can be stale.** Owners change, baselines get retrofitted without updating the flag, go-live dates slip. The value-realisation lead verifies context before chasing owners.
- **Missing baseline is a point-of-no-return.** Once the business change starts, a clean pre-change baseline cannot be captured. The missing-baseline section is listed first for a reason — treat it as higher urgency than ordinary tracking reminders.
- **Quiet months are not clean portfolios.** An empty escalation list may mean the register is incomplete, not that every benefit is on track.

## Deploy

```bash
export ANTHROPIC_API_KEY=sk-ant-...
../../scripts/deploy-managed-agent.sh realisation-checkpoint-reminder
```

Or post the resolved manifest from this directory to `POST /v1/agents` using the [Managed Agents API](https://docs.claude.com/en/api/managed-agents).

## Steering events

See [`steering-examples.json`](./steering-examples.json). The default monthly sweep uses the first example. The other two cover pre-go-live baseline scans and quarterly portfolio reviews.

## Security & handoffs

Benefits register rows and tracking log entries are **untrusted input.** Three-tier isolation:

| Tier | Touches untrusted docs? | Tools | Connectors |
|---|---|---|---|
| **`reader`** | **Yes** | `Read`, `Grep` only | None |
| `compute` / Orchestrator | No | `Read`, `Grep`, `Glob`, `Agent` | None |
| **`write-holder`** (Write-holder) | No | `Read`, `Write` | None |

`reader` returns length-capped, schema-validated JSON. `compute` is pure computation over that JSON plus the practice profile on disk — no MCP, no web. `write-holder` produces `./out/realisation-checkpoint-<date>.md` and emits a `handoff_request` for Slack delivery.

**Handoffs:** the orchestrator routes the `handoff_request` from `write-holder` to a Slack send worker using the channel from the practice profile's **benefits-checkpoint-alerts** field. The agent never sends Slack messages itself.

**Related skills:** a `handoff_request` can route into [`benefits-tracking`](../../value-realisation/skills/benefits-tracking/SKILL.md) when an owner responds to a due-tracking prompt, or into [`benefits-recovery`](../../value-realisation/skills/benefits-recovery/SKILL.md) when a benefit is persistently off-track. Watchers never call each other directly — routing is the orchestrator's job.

**Not guaranteed:** this agent surfaces leads; the benefits owner or value-realisation lead decides what to chase.

## Adaptation notes

Before you trust the output on your workflow:

- **Point at your register source.** The default reader tier reads local files only. If the register lives in Confluence via Atlassian MCP, add an `mcp_toolset` for `atlassian` on `reader.yaml` only — never on compute or write-holder.
- **Set the Slack channel.** Set **benefits-checkpoint-alerts** in the practice profile before the first scheduled run or the handoff will dead-letter.
- **Confirm tracking cadence and baseline window.** The compute tier reads these from the value-realisation practice profile. Verify they match your governance model before enabling scheduled runs.
- **Cadence.** Monthly is the default (`0 9 1 * *`). High-volatility programmes may run weekly; stable portfolios may run quarterly. The cadence lives in your workflow engine — the cookbook does not schedule itself.
