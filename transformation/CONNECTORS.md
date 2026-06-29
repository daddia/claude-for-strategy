# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that category. For example, `~~observability` might mean Honeycomb, Datadog, or any other observability platform with an MCP server.

Plugins are tool-agnostic — they describe workflows in terms of categories rather than specific products. The `.mcp.json` in this plugin pre-configures the servers listed below as "Included servers"; any MCP server in that category works just as well.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|---|---|---|---|
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Email | `~~email` | Google Mail | Microsoft 365 |
| Documents | `~~documents` | Google Workspace (Drive) | Microsoft 365 |
| Project tracker | `~~project tracker` | Atlassian (Jira), Linear, Asana | Monday |
| Knowledge base | `~~knowledge base` | Atlassian (Confluence), Notion | Guru, Slite |
| Calendar | `~~calendar` | Google Calendar | Microsoft 365 |
| Source control | `~~source control` | — | GitHub, GitLab, Bitbucket |
| Observability | `~~observability` | Honeycomb | Datadog, New Relic, Grafana |
| Hosting / deployment | `~~hosting` | Vercel | Netlify, AWS, Cloudflare |

## Notes

- **Atlassian** (Rovo) covers both `~~project tracker` and `~~knowledge base` in one connector.
- **Linear** and **Asana** cover `~~project tracker` only — issues, projects, initiatives, and milestones (Linear) or tasks, projects, portfolios, and goals (Asana). Use Atlassian when you also need `~~knowledge base`.
- **Calendar, observability, and hosting** are the additions specific to this plugin — `tech-strategy-brief` and `target-operating-model` are meaningfully better grounded when they can check real system behavior (`~~observability`) or real deployment context (`~~hosting`) instead of relying only on what you describe.
- **Chat** is the delivery surface for scheduled watchers (`assumption-decay-watcher`, `roadmap-drift-watcher`) — see each agent file for file fallback when no chat connector is configured. Assumption-Decay also reads revisit triggers from the PMO decision log when `pmo` is installed.
- **Source control** has nothing pre-wired — useful for `tech-strategy-brief` and `maturity-assessment` to read actual architecture/config rather than working from your description of it, but optional and account-specific, so it's left to you to add.
- **Notion** — same note as `consulting`: no fixed server URL, add your own.
