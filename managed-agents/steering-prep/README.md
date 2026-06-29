# Steering Prep — managed-agent cookbook

## Overview

N days before the next steering committee meeting, assembles current RAID, milestones, and pending decisions into a steering-pack prompt ready for review. Same source as the [`steering-prep`](../../pmo/agents/steering-prep.md) Claude Code agent — this directory is the Managed Agent cookbook for `POST /v1/agents`.

This is a **cookbook, not a product.** It assumes programme artefacts live in the workspace (markdown RAID, milestone exports, decision log). Teams that keep RAID and milestones in Jira, Linear, Asana, or Monday.com should wire a read connector on the reader tier or export to local files before the run.

## Before you deploy

- **Steering dates from calendar or profile estimates can be wrong.** Calendar invites get moved without updating the programme profile; cadence estimates drift. Before distributing a prep brief, the programme lead confirms the steering date and agenda.
- **RAG calls and slippage flags follow tracker metadata; they do not replace judgment.** A Green milestone may still need discussion; a Red call may be stale. The brief is a router into `/pmo:steering-pack`, not a committee pack.
- **Quiet days are not skip days.** When the prep window is closed the agent exits without a file — that means today is outside the window, not that steering prep is unnecessary.

## Deploy

```bash
export ANTHROPIC_API_KEY=sk-ant-...
# Optional — enable gcal on reader.yaml for calendar-backed steering dates
export GOOGLE_CALENDAR_MCP_URL=...
# When deploy script ships:
# ../../scripts/deploy-managed-agent.sh steering-prep
```

Until `scripts/deploy-managed-agent.sh` lands in this repo, post the resolved manifest from this directory to `POST /v1/agents` using the Managed Agents API.

## Steering events

See [`steering-examples.json`](./steering-examples.json). The default daily check uses the first example. The other two cover forced prep without calendar and a decisions-only subset.

## Security & handoffs

RAID rows, milestone comments, decision-log entries, and calendar titles are **untrusted input.** Three-tier isolation:

| Tier | Touches untrusted docs? | Tools | Connectors |
|---|---|---|---|
| **`reader`** | **Yes** | `Read`, `Grep` only | gcal (optional, off by default) |
| `compute` / Orchestrator | No | `Read`, `Grep`, `Glob`, `Agent` | None |
| **`write-holder`** (Write-holder) | No | `Read`, `Write` | None |

`reader` returns length-capped, schema-validated JSON. `compute` is pure computation over that JSON plus the practice profile on disk — no MCP, no web. `write-holder` produces `./out/steering-prep-<date>.md` when the prep window is open and emits a `handoff_request` for Slack delivery.

**Handoffs:** the orchestrator routes the `handoff_request` from `write-holder` to a Slack send worker using the channel from the practice profile's **steering-prep-alerts** field. The agent never sends Slack messages itself.

**Related agents:** a `handoff_request` can also route into [`steering-pack`](../../pmo/skills/steering-pack/SKILL.md) when the programme lead wants a full deck outline from the brief. Named agents never call each other directly — routing is the orchestrator's job.

**Not guaranteed:** this agent assembles inputs; the programme lead decides what reaches the committee.

## Adaptation notes

Before you trust the output on your workflow:

- **Point at your RAID and milestone sources.** The default reader tier reads local files only. If RAID lives in Jira via Atlassian MCP, Linear via Linear MCP, Asana via Asana MCP, or Monday.com via Monday MCP, add an `mcp_toolset` for `atlassian`, `linear`, `asana`, or `monday` on `reader.yaml` only — never on compute or write-holder.
- **Enable calendar when available.** Flip `gcal` to `default_config: { enabled: true }` in `reader.yaml` and set `GOOGLE_CALENDAR_MCP_URL`. Without calendar, the reader uses the profile's steering cadence to estimate the next date and flags `profile_estimate` in the JSON.
- **Set the Slack channel.** Set **steering-prep-alerts** in the practice profile before the first scheduled run or the handoff will dead-letter.
- **Tune prep lead time.** Default is 5 days before steering. Record your lead time in the practice profile so compute opens the window at the right time.
- **Confirm the work-product header.** The headless append in `agent.yaml` instructs the agent to prepend your profile's work-product header. Verify the language with your sponsor before turning this on.
- **Cadence.** Daily is the default (09:00 check). The cadence lives in your workflow engine — the cookbook does not schedule itself.
