# Competitor-Move Monitor — managed-agent cookbook

Roadmap **X4** entry point. Same behaviour as [`competitive-signal-scan`](../competitive-signal-scan/) — scans named competitors for map-changing signals. Canonical plugin agent: [`competitive-signal-scan.md`](../../market-intelligence/agents/competitive-signal-scan.md).

## Deploy

```bash
../../scripts/deploy-managed-agent.sh competitor-move-monitor
```

## Security & handoffs

| Tier | Touches untrusted docs? | Tools | Connectors |
|---|---|---|---|
| **`reader`** | **Yes** | `Read`, `Grep`, `web_search` | exa (optional, off by default) |
| `compute` / Orchestrator | No | `Read`, `Grep`, `Glob`, `Agent` | None |
| **`write-holder`** | No | `Read`, `Write` | None |

See [`competitive-signal-scan/README.md`](../competitive-signal-scan/README.md) for full adaptation notes.
