# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that category. For example, `~~project tracker` might mean Jira, Asana, Linear, or any other project tracker with an MCP server.

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

## Notes

- **Atlassian** (Rovo) covers both `~~project tracker` and `~~knowledge base` — the natural eventual home for the RAID log, milestone plan, and decision log once you move them off pasted markdown (see the plugin README's V1 limitation note on this).
- **Linear** and **Asana** cover `~~project tracker` only — issues, projects, initiatives, and milestones (Linear) or tasks, projects, portfolios, and goals (Asana). Use Atlassian when you also need `~~knowledge base`.
- **Calendar** is here for steering cadence — `steering-prep` reads the next steering committee date from `~~calendar`; scheduling/checking the next steering date is the most calendar-relevant thing this plugin does.
- **Chat** is the delivery surface for scheduled watchers (`escalation-watcher`, `slippage-watcher`, `steering-prep`) — see each agent file for file fallback when no chat connector is configured.
- **Notion** — no fixed server URL, add your own if used.
- No incident-management connector (PagerDuty, Opsgenie) — RAID/escalation here is governance-level, not ops-incident-level; left out to avoid scope creep, easy to add later if that changes.
