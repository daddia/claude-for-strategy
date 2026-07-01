# Market Signal Radar — managed-agent cookbook

Macro, regulatory, supply-chain, and category signals beyond named competitors. Plugin agent: [`market-signal-radar.md`](../../market-intelligence/agents/market-signal-radar.md).

## Deploy

```bash
../../scripts/deploy-managed-agent.sh market-signal-radar
```

## Security & handoffs

| Tier | Touches untrusted docs? | Tools | Connectors |
|---|---|---|---|
| **`reader`** | **Yes** | `Read`, `Grep`, `web_search` | exa (optional) |
| `compute` / Orchestrator | No | `Read`, `Grep`, `Glob`, `Agent` | None |
| **`write-holder`** | No | `Read`, `Write` | None |

Set **signal-digest-alerts** in the market-intelligence practice profile before scheduling.
