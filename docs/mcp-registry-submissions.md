# MCP Registry submission checklist

Use this when publishing a **net-new** MCP server built for `claude-for-strategy` (not the bundled third-party endpoints already in each plugin's `.mcp.json`).

## Before you publish

1. **Prove ownership** — register under a reverse-DNS namespace via [MCP Registry](https://registry.modelcontextprotocol.io).
2. **Document tools** — list read vs write tools, auth method (OAuth vs API key), and data coverage.
3. **Provenance** — every numeric tool result should return source, as-of date, and a citation-ready identifier (see root `CONNECTORS.md`).
4. **Security** — no instruction-like content in tool payloads; clean errors on timeout/rate limit.

## Publish and claim

| Directory | Action |
|---|---|
| [MCP Registry](https://registry.modelcontextprotocol.io) | `mcp-publisher` submit `server.json` |
| [smithery.ai](https://smithery.ai) | CLI publish or claim hosted endpoint |
| [glama](https://glama.ai) | Claim server after registry crawl |
| [PulseMCP](https://www.pulsemcp.com) | Submit for hand review |
| [mcp.so](https://mcp.so) | Claim listing after registry index |

Optional bulk submit: [mcp-submit](https://github.com/modelcontextprotocol/mcp-submit) (10+ directories).

## After merge in this repo

1. Add the server to relevant plugin `.mcp.json` files (or run `python3 scripts/sync-priority-connectors.py` if added to `references/priority-mcp-servers.json`).
2. Map a `~~category` placeholder in `references/connector-taxonomy.json` if needed.
3. Update the plugin's `CONNECTORS.md` and root `CONNECTORS.md` table.
4. Run `python3 scripts/validate-connectors.py --check`.
