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
| Project tracker | `~~project tracker` | Atlassian (Jira), Linear, Asana, Monday.com | — |
| Knowledge base | `~~knowledge base` | Atlassian (Confluence), Notion | Guru, Slite |
| Calendar | `~~calendar` | Google Calendar | Microsoft 365 |

## Notes

- **Atlassian** (Rovo) covers both `~~project tracker` and `~~knowledge base` — the natural eventual home for stakeholder maps, comms plans, and readiness assessments once you move them off pasted markdown.
- **Linear**, **Asana**, and **Monday.com** cover `~~project tracker` only — use Atlassian when you also need `~~knowledge base`.
- **Calendar** supports go-live sequencing in `communications-plan` and sponsor checkpoint timing in `sponsor-roadmap`.
- **Chat** and **Email** are optional delivery surfaces for comms drafts — V1 skills produce markdown output; connectors enhance context gathering, not hard dependencies.
- **Notion** — no fixed server URL, add your own if used.
