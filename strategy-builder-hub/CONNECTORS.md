# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool you connect in that category. For example, `~~chat` might mean Slack, Microsoft Teams, or any other chat tool with an MCP server.

This plugin discovers and installs community strategy skills — it does not produce strategy work product. Connectors here support registry browsing, update notifications, and optional delivery of install/QA summaries.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|---|---|---|---|
| Strategy skills registry | `~~strategy skills registry` | GitHub | Other GitHub-based registries you configure in the practice profile |
| Source control | `~~source control` | GitHub | GitLab, Bitbucket |
| Chat | `~~chat` | Slack | Microsoft Teams, Discord |
| Documents | `~~documents` | Google Drive | Microsoft 365 |

## Notes

- **GitHub** covers both `~~source control` and the default path for `~~strategy skills registry` — browse registry repos, read skill manifests, and run `registry-browser` / `skills-qa` against live GitHub content after OAuth.
- **Chat** is optional but useful for proactive new-skill and update notifications when `auto-updater` or registry sync finds something worth surfacing before the next manual browse.
- **Documents** is a convenience surface for saving QA verdicts or install manifests — not required for core hub workflows.
