# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that category. Plugins are tool-agnostic — the `.mcp.json` pre-configures the servers below as "Included servers"; any MCP server in that category works just as well.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|---|---|---|---|
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Email | `~~email` | Google Mail | Microsoft 365 |
| Documents | `~~documents` | Google Workspace (Drive) | Microsoft 365 |
| Knowledge base | `~~knowledge base` | Atlassian (Confluence), Notion | Guru, Slite |
| HRIS / People system | `~~hris` | — | Workday, BambooHR, Rippling, HiBob |
| Whiteboard | `~~whiteboard` | — | Miro, Figma, Lucidchart |

## Notes

- **No project tracker** — this plugin diagnoses structure, it doesn't track tickets. If a diagnosis produces follow-up work (a reorg, a RACI rollout), that work belongs in whatever tracker the org already uses, outside this plugin's scope. **Linear**, **Asana**, and **Monday.com** are pre-wired in `.mcp.json` if you want live issue context during a diagnosis.
- **HRIS/People system** is the connector most worth adding here — `check-span-and-layers` is currently a manual-input skill; real headcount and reporting-line data turns it from a discussion exercise into an actual diagnostic.
- **No scheduled agent in this plugin.** Org design isn't calendar-driven the way OKRs or BSC reviews are — the natural trigger is event-driven (a reorg, an M&A integration, a leadership change, a strategy shift), not a recurring date. See the README.
