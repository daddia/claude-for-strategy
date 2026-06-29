# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that category. For example, `~~chat` might mean Slack, Microsoft Teams, or any other chat tool with an MCP server.

This plugin discovers and installs community strategy skills — it does not produce strategy work product. Connectors here support registry browsing, update notifications, and optional delivery of install/QA summaries.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|---|---|---|---|
| Strategy skills registry | `~~strategy skills registry` | — | GitHub-based skill registries you configure in the practice profile |
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Documents | `~~documents` | Google Drive | Microsoft 365 |

## Notes

- **Strategy skills registry** has no fixed MCP server URL — registries are workspace- or firm-specific. Add your registry MCP entry in `.mcp.json` when you have one; until then, `/strategy-builder-hub:registry-browser` works from URLs in the practice profile.
- **Chat** is optional but useful for proactive new-skill and update notifications when `auto-updater` or registry sync finds something worth surfacing before the next manual browse.
- **Documents** is a convenience surface for saving QA verdicts or install manifests — not required for core hub workflows.
