# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that category. For example, `~~whiteboard` might mean Miro, Figma, or any other diagramming tool with an MCP server.

Plugins are tool-agnostic — they describe workflows in terms of categories rather than specific products. The `.mcp.json` in this plugin pre-configures the servers listed below as "Included servers"; any MCP server in that category works just as well.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|---|---|---|---|
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Email | `~~email` | Google Mail | Microsoft 365 |
| Documents | `~~documents` | Google Workspace (Drive) | Microsoft 365 |
| Project tracker | `~~project tracker` | Atlassian (Jira) | Asana, Linear, Monday |
| Knowledge base | `~~knowledge base` | Atlassian (Confluence), Notion | Guru, Slite |
| Calendar | `~~calendar` | Google Calendar | Microsoft 365 |
| Whiteboard | `~~whiteboard` | — | Miro, Figma, Lucidchart, Mural |

## Notes

- **Whiteboard** matters more here than anywhere else in the repo — `build-strategy-map`'s output is a causal diagram by nature (boxes and arrows across four perspectives), and a markdown table is a lossy way to represent it. Nothing pre-wired since it's account-specific; this is the strongest candidate in the whole repo for adding your own connector.
- **Calendar** drives two different cadences here, not one — `review-and-validate` runs quarterly (or whatever the profile records), but the strategy map itself (`build-strategy-map`) should be revisited far less often, typically annually or on a material strategy change. Don't let the quarterly cadence pull you into re-litigating the map every quarter — see the agent notes.
- **Atlassian** (Rovo) covers both `~~project tracker` and `~~knowledge base`.
- Cross-plugin seam: `select-measures` hands off to `performance:metrics-glossary` for formal metric definitions if that plugin is installed, same pattern as `okr:instrument-metrics`.
- If both `okr` and `balanced-scorecard` are installed: see the README's integration note before running `cascade-to-scorecards` and `okr:cascade` on the same objective set — they're meant to operate at different layers, not duplicate each other.
