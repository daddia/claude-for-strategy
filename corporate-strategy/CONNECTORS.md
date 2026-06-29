# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that category. Plugins are tool-agnostic — the `.mcp.json` pre-configures the servers below as "Included servers"; any MCP server in that category works just as well.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|---|---|---|---|
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Email | `~~email` | Google Mail | Microsoft 365 |
| Documents | `~~documents` | Google Workspace (Drive) | Microsoft 365 |
| Project tracker | `~~project tracker` | Atlassian (Jira), Linear, Asana, Monday.com | — |
| Knowledge base | `~~knowledge base` | Atlassian (Confluence), Notion | Guru, Slite |
| Calendar | `~~calendar` | Google Calendar | Microsoft 365 |
| Source control | `~~source control` | GitHub | GitLab, Bitbucket |
| BI / analytics | `~~bi analytics` | — | Looker, Tableau, Power BI, Mode |

## Notes

- **Calendar** is here for the portfolio-review cadence — see `agents/portfolio-review-reminder.md`.
- **Linear**, **Asana**, **Monday.com**, and **Atlassian** (Jira) are all pre-wired for `~~project tracker`; Atlassian also covers `~~knowledge base` (Confluence).
- **BI/analytics** has nothing pre-wired — `allocate-resources` is meaningfully better grounded pulling actual spend/headcount-by-business-unit from a live BI tool than from a description of it, but that's account-specific and left to you.
- No market-data connector (Bloomberg, PitchBook, CB Insights) — would help `evaluate-strategic-option` and `synergy-stress-test` ground comparable-deal data, but nothing in this category has a broadly available MCP server yet.
- Cross-plugin seam: `evaluate-strategic-option` is the portfolio-level sibling of `transformation:business-case` — see this plugin's README for where the boundary sits.
