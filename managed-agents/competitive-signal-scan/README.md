# Competitive Signal Scan — managed-agent cookbook

## Overview

Scans for competitor moves matching what the practice profile defines as a meaningful signal, and flags anything that would change the strategic-group map or incentive map. Same source as the [`competitive-signal-scan`](../../market-intelligence/agents/competitive-signal-scan.md) Claude Code agent — this directory is the Managed Agent cookbook for `POST /v1/agents`.

This is a **cookbook, not a product.** It works with native `web_search` on the reader tier — no MCP connector required for a first deployment. Teams running serious ongoing monitoring should add a news/search MCP (Exa, Tavily, etc.) on the reader leaf for more reliable coverage.

## Before you deploy

- **Web snippets and aggregator headlines can be wrong or stale.** Verify primary sources before updating maps or briefing exec. The digest tags source quality; it does not certify accuracy.
- **Quiet weeks are not clean markets.** No map-changing signals may mean competitors were quiet, your signal taxonomy is too narrow, or search coverage missed the story. The quiet-week footer means the agent ran.
- **Map impact is modeled against artefacts on disk.** If strategic-group or incentive maps have not been built yet, compute notes `maps_not_available` and surfaces watchlist-grade signals only.

## Deploy

```bash
export ANTHROPIC_API_KEY=sk-ant-...
# Optional — enable exa on reader.yaml for curated search
export EXA_MCP_URL=...
# When deploy script ships:
# ../../scripts/deploy-managed-agent.sh competitive-signal-scan
```

Until `scripts/deploy-managed-agent.sh` lands in this repo, post the resolved manifest from this directory to `POST /v1/agents` using the Managed Agents API.

## Steering events

See [`steering-examples.json`](./steering-examples.json). The default weekly sweep uses the first example. The other two cover competitor-scoped runs and post-map-refresh checks.

## Security & handoffs

Web results, press releases, and competitor claims are **untrusted input.** Three-tier isolation:

| Tier | Touches untrusted docs? | Tools | Connectors |
|---|---|---|---|
| **`reader`** | **Yes** | `Read`, `Grep`, `web_search` | exa (optional, off by default) |
| `compute` / Orchestrator | No | `Read`, `Grep`, `Glob`, `Agent` | None |
| **`write-holder`** (Write-holder) | No | `Read`, `Write` | None |

`reader` returns length-capped, schema-validated JSON. `compute` is pure computation over that JSON plus the practice profile and map artefacts on disk — no web. `write-holder` produces `./out/competitive-signals-<date>.md` and emits a `handoff_request` for Slack delivery.

**Handoffs:** the orchestrator routes the `handoff_request` from `write-holder` to a Slack send worker using the channel from the practice profile's **signal-digest-alerts** field. The agent never sends Slack messages itself.

**Related agents:** a `handoff_request` can route into [`map-competitive-landscape`](../../market-intelligence/skills/map-competitive-landscape/SKILL.md) or [`map-incentives`](../../market-intelligence/skills/map-incentives/SKILL.md) when a signal warrants map updates, or into corporate-strategy when materiality thresholds are crossed. Named agents never call each other directly — routing is the orchestrator's job.

**Not guaranteed:** this agent surfaces leads; the CI lead decides what reaches exec or corp strategy.

## Adaptation notes

Before you trust the output on your workflow:

- **Name your competitors and signal types in the profile.** The reader tier reads `Known competitor set`, `Meaningful signal`, and `Signal taxonomy` from the market-intelligence practice profile. Vague definitions produce noisy or empty digests.
- **Set the Slack channel.** Set **signal-digest-alerts** in the practice profile before the first scheduled run or the handoff will dead-letter.
- **Add a news MCP when ready.** Flip `exa` (or your connector) to `default_config: { enabled: true }` on `reader.yaml` only — never on compute or write-holder.
- **Point at your maps.** Record paths to strategic-group and incentive map artefacts in seed documents or the workspace so compute can test mobility-barrier and incentive predictions.
- **Tune materiality.** Confirm exec-escalation thresholds in the profile match your response process before enabling scheduled runs.
- **Cadence.** Weekly is the default. The cadence lives in your workflow engine — the cookbook does not schedule itself.
