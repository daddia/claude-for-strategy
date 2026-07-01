# Transformation-Programme Health Watcher — managed-agent cookbook

Combined RAID, milestone, and roadmap phase RAG digest for transformation sponsors. Plugin agent: [`transformation-programme-health-watcher.md`](../../transformation/agents/transformation-programme-health-watcher.md).

## Deploy

```bash
../../scripts/deploy-managed-agent.sh transformation-programme-health-watcher
```

## Security & handoffs

| Tier | Touches untrusted docs? | Tools | Connectors |
|---|---|---|---|
| **`reader`** | **Yes** | `Read`, `Grep` | atlassian / linear (optional on reader) |
| `compute` / Orchestrator | No | `Read`, `Grep`, `Glob`, `Agent` | None |
| **`write-holder`** | No | `Read`, `Write` | None |

Set **programme-health-alerts** in the transformation practice profile before scheduling.
