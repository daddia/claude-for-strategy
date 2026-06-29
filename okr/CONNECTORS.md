# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that category. For example, `~~chat` might mean Slack, Microsoft Teams, or any other chat tool with an MCP server.

Plugins are tool-agnostic — they describe workflows in terms of categories rather than specific products. The `.mcp.json` in this plugin pre-configures the servers listed below as "Included servers"; any MCP server in that category works just as well.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|---|---|---|---|
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Email | `~~email` | Google Mail | Microsoft 365 |
| Documents | `~~documents` | Google Workspace (Drive) | Microsoft 365 |
| Project tracker | `~~project tracker` | Atlassian (Jira), Linear | Asana, Monday |
| Knowledge base | `~~knowledge base` | Atlassian (Confluence), Notion | Guru, Slite |
| Calendar | `~~calendar` | Google Calendar | Microsoft 365 |

## Notes

- **Calendar** matters more here than in most plugins — `check-in` and the scheduled `check-in-nudge` agent are cadence-driven (weekly/biweekly confidence pulses, quarterly cycle boundaries), and `~~calendar` is the source of truth for when those land.
- **Chat** is the primary surface for `check-in-nudge` — see the agent's own notes for what happens with no `~~chat` connected.
- **Atlassian** (Rovo) covers both `~~project tracker` and `~~knowledge base`.
- **Linear** covers `~~project tracker` only — issues, projects, initiatives, and milestones. Use Atlassian when you also need `~~knowledge base`.
- This plugin has a real dependency relationship with `performance`: `instrument-metrics` hands off to `performance:metrics-glossary` for canonical metric definitions if that plugin is installed. No connector implication either way — noted here because it's the one cross-plugin seam in this plugin.
- If [`balanced-scorecard`](../balanced-scorecard) is also installed, see that plugin's README before running `okr:cascade` and `balanced-scorecard:cascade-to-scorecards` on the same objective set — they're meant to operate at different layers.