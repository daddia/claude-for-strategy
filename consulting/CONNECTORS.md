# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that category. For example, `~~knowledge base` might mean Confluence, Notion, or any other knowledge base with an MCP server.

Plugins are tool-agnostic — they describe workflows in terms of categories rather than specific products. The `.mcp.json` in this plugin pre-configures the servers listed below as "Included servers"; any MCP server in that category works just as well.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|---|---|---|---|
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Email | `~~email` | Google Mail | Microsoft 365 |
| Productivity suite | `~~productivity suite` | Google Workspace (Drive) | Microsoft 365 |
| Project tracker | `~~project tracker` | Atlassian (Jira) | Asana, Linear, Monday |
| Knowledge base | `~~knowledge base` | Atlassian (Confluence), Notion | Guru, Slite |
| Whiteboard | `~~whiteboard` | — | Miro, Figma, Lucidchart, Mural |

## Notes

- **Atlassian** is a single connector (Rovo) covering both Jira (`~~project tracker`) and Confluence (`~~knowledge base`) — one entry in `.mcp.json`, two categories.
- **Notion** has no fixed server URL — it's workspace-specific. It's listed as a knowledge base option but not pre-wired in `.mcp.json`; add your own server entry if you use it.
- **Whiteboard** has nothing pre-wired — useful for sketching a hypothesis tree or pyramid visually with `hypothesis-tree` or `narrative-builder` output, but optional.
- `workplan-builder` output is the thing most likely to land in `~~project tracker`; `deck-outline` / `exec-memo` output is the thing most likely to land in `~~productivity suite` or get sent via `~~email`.