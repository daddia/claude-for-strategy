# OKR Drift Detector — managed-agent cookbook

Weekly drift digest for confidence drops, stale KRs, and coverage gaps. Plugin agent: [`okr-drift-detector.md`](../../okr/agents/okr-drift-detector.md).

## Deploy

```bash
../../scripts/deploy-managed-agent.sh okr-drift-detector
```

## Security & handoffs

| Tier | Touches untrusted docs? | Tools | Connectors |
|---|---|---|---|
| **`reader`** | **Yes** | `Read`, `Grep` | None |
| `compute` / Orchestrator | No | `Read`, `Grep`, `Glob`, `Agent` | None |
| **`write-holder`** | No | `Read`, `Write` | None |

Set **okr-drift-alerts** in the OKR practice profile before scheduling.
