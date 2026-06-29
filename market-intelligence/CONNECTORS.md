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
| Source control | `~~source control` | GitHub | GitLab, Bitbucket |
| Whiteboard | `~~whiteboard` | — | Miro, Figma, Lucidchart, Mural |
| Web & news monitoring | `~~web monitoring` | — | Exa, Tavily, NewsAPI, Feedly |

## Notes

- **No project tracker listed** — this plugin produces analysis, not tracked work items; if a finding needs follow-up action, hand off to whichever plugin owns that action (a competitive threat might become a `corporate-strategy:evaluate-strategic-option`, an incentive misalignment might become an `operating-model:align-rewards-and-incentives` review). **Linear**, **Asana**, and **Monday.com** are pre-wired in `.mcp.json` if your team tracks competitive follow-ups there.
- **Whiteboard** matters here — strategic-group maps are genuinely visual (clusters with mobility-barrier arrows between them); a table is a lossy representation. Worth adding if you do this work often.
- **Web & news monitoring** has nothing pre-wired *as an MCP connector*, but the `competitive-signal-scan` agent doesn't strictly need one — this environment's native web search is sufficient for most competitive-signal scanning out of the box. A dedicated connector (Feedly-style curated feeds, or a structured news API) would give more reliable recurring coverage than ad hoc search, which is why it's still listed as an option worth adding for serious ongoing use.
