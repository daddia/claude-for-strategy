# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that category. For example, `~~chat` might mean Slack, Microsoft Teams, or any other chat tool with an MCP server.

Plugins are tool-agnostic — they describe workflows in terms of categories rather than specific products. The `.mcp.json` in this plugin pre-configures the servers listed below as "Included servers"; any MCP server in that category works just as well.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|---|---|---|---|
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Email | `~~email` | Google Mail | Microsoft 365 |
| Spreadsheet | `~~spreadsheet` | Google Workspace (Sheets via Drive) | Microsoft 365 (Excel), Airtable |
| Project tracker | `~~project tracker` | Atlassian (Jira), Linear, Asana, Monday.com | — |
| Knowledge base | `~~knowledge base` | Atlassian (Confluence), Notion | Guru, Slite |
| Calendar | `~~calendar` | Google Calendar | Microsoft 365 |

## Notes

- **Calendar** matters here for the same reason it matters in `okr`: realisation windows and tracking cadences are date-driven, and `~~calendar` is the source of truth for when a benefit's go-live, baseline cutoff, or review date actually lands.
- **Chat** is the primary surface for `realisation-checkpoint-reminder` — see the agent's own notes for what happens with no `~~chat` connected.
- **Atlassian** (Rovo) covers both `~~project tracker` and `~~knowledge base` — the natural home for the benefits register once it moves off pasted markdown.
- **Linear**, **Asana**, and **Monday.com** cover `~~project tracker` only — issues, projects, initiatives, and milestones (Linear); tasks, projects, portfolios, and goals (Asana); or boards, items, columns, and users (Monday.com). Use Atlassian when you also need `~~knowledge base`.
- **Notion** — no fixed server URL, add your own if used.
- This plugin has real cross-plugin seams with [`performance`](../performance) (`benefits-register` defers to `performance:metrics-glossary` for metric definitions), [`pmo`](../pmo) (`benefits-recovery` decisions belong in `pmo:decision-log`), and [`transformation`](../transformation) (`benefits-map` seeds from `transformation:business-case`). No connector implication in any of these — noted here because they're the seams that matter most for this plugin specifically.
