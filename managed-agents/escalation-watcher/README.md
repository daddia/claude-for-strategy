# Escalation Watcher — managed-agent cookbook

## Overview

Scans the RAID log for items crossing the escalation threshold in the practice profile and writes an alert report for human review. Same source as the [`escalation-watcher`](../../pmo/agents/escalation-watcher.md) Claude Code agent — this directory is the Managed Agent cookbook for `POST /v1/agents`.

This is a **cookbook, not a product.** It assumes the RAID log lives in the workspace (markdown table, spreadsheet export, or pasted content). Teams that keep RAID in Jira, Linear, Asana, or another tracker should wire a read connector on the reader tier or export to a local file before the run.

## Before you deploy

- **Severity tags and status fields in tracker exports can be stale.** RAID metadata drifts from ground truth — items get downgraded in conversation but not in the log, owners change without an update. Before acting on an escalation flag, the programme lead verifies context and decides whether to escalate now.
- **Thresholds follow the practice profile; they do not make the escalation judgment.** A flagged item may still be acceptable in context; an unflagged item may still need attention. The profile is a router, not a reviewer.
- **Quiet weeks are not clean weeks.** An item that isn't surfaced may be missing from the log, mis-tagged, or below the radar without the metadata reflecting that. The all-clear footer means the agent ran, not that nothing needs doing.

## Deploy

```bash
export ANTHROPIC_API_KEY=sk-ant-...
# When deploy script ships:
# ../../scripts/deploy-managed-agent.sh escalation-watcher
```

Until `scripts/deploy-managed-agent.sh` lands in this repo, post the resolved manifest from this directory to `POST /v1/agents` using the Managed Agents API.

## Steering events

See [`steering-examples.json`](./steering-examples.json). The default Monday-morning sweep uses the first example. The other two cover post-`raid-log` runs and ad-hoc pre-steering scans.

## Security & handoffs

RAID log rows, status comments, and tracker exports are **untrusted input.** Three-tier isolation:

| Tier | Touches untrusted docs? | Tools | Connectors |
|---|---|---|---|
| **`reader`** | **Yes** | `Read`, `Grep` only | None |
| `compute` / Orchestrator | No | `Read`, `Grep`, `Glob`, `Agent` | None |
| **`write-holder`** (Write-holder) | No | `Read`, `Write` | None |

`reader` returns length-capped, schema-validated JSON. `compute` is pure computation over that JSON plus the practice profile on disk — no MCP, no web. `write-holder` produces `./out/escalation-alerts-<date>.md` and emits a `handoff_request` for Slack delivery.

**Handoffs:** the orchestrator routes the `handoff_request` from `write-holder` to a Slack send worker using the channel from the practice profile's **escalation-alerts** field. The agent never sends Slack messages itself.

**Related skills:** a `handoff_request` can also route into [`status-report`](../../pmo/skills/status-report/SKILL.md) when a fuller narrative is needed for steering, or into [`steering-pack`](../../pmo/skills/steering-pack/SKILL.md) prep. Watchers never call each other directly — routing is the orchestrator's job.

**Not guaranteed:** this agent recommends an escalation; the programme lead or sponsor decides whether to act.

## Adaptation notes

Before you trust the output on your workflow:

- **Point at your RAID source.** The default reader tier reads local files only. If RAID lives in Jira via Atlassian MCP, Linear via Linear MCP, or Asana via Asana MCP, add an `mcp_toolset` for `atlassian`, `linear`, or `asana` on `reader.yaml` only — never on compute or write-holder.
- **Set the Slack channel.** The write-holder emits a `handoff_request` that names a Slack channel. Set **escalation-alerts** in the practice profile before the first scheduled run or the handoff will dead-letter.
- **Tune escalation thresholds.** The compute tier reads severity/impact rules from the practice profile. Confirm they match your governance model (what triggers escalation above the working level) before enabling scheduled runs.
- **Confirm the work-product header.** The headless append in `agent.yaml` instructs the agent to prepend your profile's work-product header. Verify the language with your sponsor before turning this on.
- **Cadence.** Weekly is the default (`0 9 * * 1`). High-volatility programmes may run daily; stable programmes may run monthly. The cadence lives in your workflow engine — the cookbook does not schedule itself.
