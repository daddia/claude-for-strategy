# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that category. For example, `~~spreadsheet` might mean Google Sheets, Excel, or any other spreadsheet tool with an MCP server.

Plugins are tool-agnostic — they describe workflows in terms of categories rather than specific products. The `.mcp.json` in this plugin pre-configures the servers listed below as "Included servers"; any MCP server in that category works just as well.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|---|---|---|---|
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Email | `~~email` | Google Mail | Microsoft 365 |
| Spreadsheet | `~~spreadsheet` | Google Workspace (Sheets via Drive) | Microsoft 365 (Excel), Airtable |
| Project tracker | `~~project tracker` | Atlassian (Jira), Linear, Asana | Monday |
| Knowledge base | `~~knowledge base` | Atlassian (Confluence), Notion | Guru, Slite |
| Observability | `~~observability` | Honeycomb | Datadog, New Relic |
| BI / analytics | `~~bi analytics` | — | Looker, Tableau, Power BI, Mode |

## Notes

- **Spreadsheet** is the primary file surface for this plugin — `tracker-builder` writes directly into a spreadsheet, so this is the category that matters most here specifically.
- **Atlassian** (Rovo) covers both `~~project tracker` and `~~knowledge base`.
- **Linear** and **Asana** cover `~~project tracker` only — issues, projects, initiatives, and milestones (Linear) or tasks, projects, portfolios, and goals (Asana). Use Atlassian when you also need `~~knowledge base`.
- **Observability** (Honeycomb) is here because your B2/B3 categories include Digital Product Performance — if any tracked metric is really a system/product telemetry number rather than a manually-logged one, `kpi-tree-builder`, **KPI Breach Watcher**, and **Cadence Reporter** are better grounded pulling it from `~~observability` than from a manually maintained Daily Log column. KPI Breach Watcher and Cadence Reporter also post summaries via `~~chat` when configured.
- **BI/analytics** has nothing pre-wired — relevant once `performance-narrative` needs to pull from a dashboard tool rather than the tracker spreadsheet directly, optional for now.
- **Notion** — no fixed server URL, add your own if used.
- This plugin has real cross-plugin seams with [`okr`](../okr) and [`balanced-scorecard`](../balanced-scorecard): `metrics-glossary` is the canonical home for metric definitions that `okr:instrument-metrics` and `balanced-scorecard:select-measures` defer to, if those plugins are installed. No connector implication either way.