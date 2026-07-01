# Board-Cycle Prep — managed-agent cookbook

Roadmap **X4** entry point. Same behaviour as [`steering-prep`](../steering-prep/) — assembles calendar, RAID, milestones, and decisions before a governance meeting. Canonical plugin agent: [`steering-prep.md`](../../pmo/agents/steering-prep.md).

## Deploy

```bash
../../scripts/deploy-managed-agent.sh board-cycle-prep
```

## Security & handoffs

| Tier | Touches untrusted docs? | Tools | Connectors |
|---|---|---|---|
| **`reader`** | **Yes** | `Read`, `Grep` | google-calendar (optional on reader leaf) |
| `compute` / Orchestrator | No | `Read`, `Grep`, `Glob`, `Agent` | None |
| **`write-holder`** | No | `Read`, `Write` | None |

See [`steering-prep/README.md`](../steering-prep/README.md) for full adaptation notes.
