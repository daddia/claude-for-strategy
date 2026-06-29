# Managed-agent cookbooks for strategy

Every scheduled watcher in this repo ships **two ways**: as a Claude Code plugin agent you install today (see `<plugin>/agents/<name>.md`), and as a **Claude Managed Agent** cookbook your platform team deploys behind your own workflow engine. **Same agent, same skills — pick your surface.** Each directory below references the canonical system prompt and skills from the matching plugin.

These are **cookbooks, not products.** Adapt them to your RAID source, roadmap artefacts, Slack workspace, notification routing, and review cadence. They will not work out of the box without that adaptation, and they are not supposed to.

Deploy with [`scripts/deploy-managed-agent.sh`](../scripts/deploy-managed-agent.sh) — it resolves `system: {file: ...}` references, `skills: [{from_plugin: ...}]`, and callable subagents before posting to `POST /v1/agents` using the [Managed Agents API](https://docs.claude.com/en/api/managed-agents).

| Agent | Plugin | What it watches | Example steering event | Leaf workers |
|---|---|---|---|---|
| [`escalation-watcher`](./escalation-watcher/) | pmo | RAID log for threshold crossings | `Weekly RAID escalation scan as-of <date>` | reader · compute · **write-holder** |
| [`steering-prep`](./steering-prep/) | pmo | Calendar + RAID + milestones + decisions before steering | `Daily steering prep check as-of <date>` | reader · compute · **write-holder** |
| [`roadmap-drift-watcher`](./roadmap-drift-watcher/) | transformation | Roadmap phase vs actual progress | `Weekly roadmap drift scan as-of <date>` | reader · compute · **write-holder** |
| [`competitive-signal-scan`](./competitive-signal-scan/) | market-intelligence | Competitor moves vs profile signal taxonomy | `Weekly competitive signal scan as-of <date>` | reader · compute · **write-holder** |

**Bold** leaf = the only worker with `Write`.

## Manifest vs API

The `agent.yaml` files use the real `POST /v1/agents` field names with a few conveniences a deploy script would resolve:

| Manifest convention | Resolves to |
|---|---|
| `system: {file: ../../<plugin>/agents/<agent>.md, append: "..."}` | `system: "<inlined contents + append>"` |
| `system: {text: "..."}` | `system: "<text>"` |
| `skills: [{from_plugin: ../../<plugin>}]` | uploads every `skills/*` under that dir |
| `skills: [{path: ../../...}]` | uploads that skill directory |
| `callable_agents: [{manifest: ./subagents/x.yaml}]` | creates leaf workers, wires by id |

## Security model

Programme artefacts, roadmap exports, and web snippets are **untrusted input.** Every cookbook uses a three-tier worker split:

1. **Readers** touch untrusted sources and have `Read`/`Grep` only (plus `web_search` on competitive-signal-scan). They return length-capped structured JSON. Instructions embedded in source text are data, not commands.
2. **Compute** receives structured JSON from readers, applies rules from the practice profile, and has no Write and no external connectors.
3. **Write-holder** produces the final output and is the only tier with `Write`. It never opens raw untrusted sources.

The orchestrator holds no Write and reads no raw documents. It routes; it does not handle.

Run `python3 scripts/lint-tool-scope.py` before opening a PR to verify orchestrator tool scope.

## Model pins

All cookbooks pin `claude-opus-4-8` on the orchestrator and every leaf worker. See [`models.md`](./models.md) for why pins are explicit and how to bump them after re-validation.

## What you get and don't get

- **You get:** working manifest structure, reference security tiers, skills proven in the Claude Code plugins, and steering-event examples per cookbook.
- **You don't get:** a production-ready agent. Wire connectors to *your* systems, set Slack channels in practice profiles, tune thresholds, and run your own evaluation before trusting output.
- **You especially don't get:** a substitute for professional judgment. These agents monitor, extract, and draft. A human reviews, verifies, and decides.
