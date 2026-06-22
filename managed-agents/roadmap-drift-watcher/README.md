# Roadmap Drift Watcher — managed-agent cookbook

## Overview

Scans the transformation roadmap for initiatives slipping their planned phase and writes a summary with downstream knock-on effects. Same source as the [`roadmap-drift-watcher`](../../transformation/agents/roadmap-drift-watcher.md) Claude Code agent — this directory is the Managed Agent cookbook for `POST /v1/agents`.

This is a **cookbook, not a product.** It assumes the roadmap and progress signals live in the workspace (latest `roadmap-builder` output, seed documents, milestone exports). Teams that track delivery in Jira should wire a read connector on the reader tier or export before the run.

## Before you deploy

- **Phase tags and progress signals in planning artefacts can be stale.** Initiatives get re-baselined in conversation but not in the roadmap file; milestone actuals lag. Before acting on a drift flag, the transformation owner verifies against delivery reality.
- **Knock-on effects are modeled from the dependency graph; they are not commitments.** A blocked downstream id is a hypothesis to verify, not an automatic reschedule.
- **All-clear weeks are not clean weeks.** Initiatives on track within the planning horizon may still have local delays that do not constitute phase drift. The all-clear footer means the agent ran.

## Deploy

```bash
export ANTHROPIC_API_KEY=sk-ant-...
# When deploy script ships:
# ../../scripts/deploy-managed-agent.sh roadmap-drift-watcher
```

Until `scripts/deploy-managed-agent.sh` lands in this repo, post the resolved manifest from this directory to `POST /v1/agents` using the Managed Agents API.

## Steering events

See [`steering-examples.json`](./steering-examples.json). The default weekly sweep uses the first example. The other two cover Now-track-only checks and post-rebaseline scans.

## Security & handoffs

Roadmap rows, status comments, and milestone exports are **untrusted input.** Three-tier isolation:

| Tier | Touches untrusted docs? | Tools | Connectors |
|---|---|---|---|
| **`reader`** | **Yes** | `Read`, `Grep` only | None |
| `compute` / Orchestrator | No | `Read`, `Grep`, `Glob`, `Agent` | None |
| **`write-holder`** (Write-holder) | No | `Read`, `Write` | None |

`reader` returns length-capped, schema-validated JSON. `compute` is pure computation over that JSON plus the practice profile on disk — no MCP, no web. `write-holder` produces `./out/roadmap-drift-<date>.md` and emits a `handoff_request` for Slack delivery.

**Handoffs:** the orchestrator routes the `handoff_request` from `write-holder` to a Slack send worker using the channel from the practice profile's **roadmap-drift-alerts** field. The agent never sends Slack messages itself.

**Related agents:** a `handoff_request` can route into [`roadmap-builder`](../../transformation/skills/roadmap-builder/SKILL.md) when a re-baseline is needed, or into PMO [`milestone-tracker`](../../pmo/skills/milestone-tracker/SKILL.md) when actuals need refresh. Named agents never call each other directly — routing is the orchestrator's job.

**Not guaranteed:** this agent recommends attention; the transformation owner decides whether to re-baseline.

## Adaptation notes

Before you trust the output on your workflow:

- **Point at your roadmap source.** Record seed-document locations and the default track model in the transformation practice profile. The reader tier reads local files only by default.
- **Set the Slack channel.** Set **roadmap-drift-alerts** in the practice profile before the first scheduled run or the handoff will dead-letter.
- **Tune the planning horizon.** Now/Next/Later (or your named tracks) must match how `roadmap-builder` labels phases or compute will mis-classify drift.
- **Wire PMO milestone actuals when available.** If the PMO plugin is installed, export milestone actuals to a path the reader can grep, or add a read connector on the reader leaf only.
- **Confirm the work-product header.** Verify the header language with your sponsor before turning this on.
- **Cadence.** Weekly (Thursday 09:00) is the default. The cadence lives in your workflow engine — the cookbook does not schedule itself.
