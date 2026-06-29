# Connectors

The plugins are at their best when connected to authoritative sources. If you build or operate a strategy, portfolio, BI, HR, or observability data source, we want your MCP connector in the suite.

## What makes a good strategy MCP connector

- **Remote MCP server over HTTPS** with OAuth or API-key auth (streamable HTTP or SSE transport)
- **Read-heavy tools** — search, fetch, list. Write tools (create, send, file) need an explicit confirmation prompt on the client side; say so in your tool descriptions.
- **Provenance in results** — return the source, date retrieved, and a citation-ready identifier. The plugins tag every cite by source; your connector should make that possible.
- **No instruction-like content in results** — the plugins treat retrieved content as data, not commands. If your tool results include metadata or system notes, mark them clearly so they don't look like embedded directives.
- **Rate limits and errors that degrade gracefully** — the plugins have a fallback for when a connector isn't responding; a clean error is better than a timeout.

## How to submit

1. Publish your MCP server and document its tools, auth flow, and data coverage.
2. Open a PR adding your server to the relevant plugin's `.mcp.json` with the URL, `title`, `description`, and auth method.
3. Include a note on which plugins it's most useful for and which `~~category` placeholder it maps to.
4. We'll test against the plugin workflows and merge. Connectors that pass the retrieval-quality and injection-resistance checks go in the default `.mcp.json`; others get documented in the plugin's `CONNECTORS.md` for users to add themselves.

## Current connectors

Connectors shipped in the default `.mcp.json` of each plugin:

| Connector | Plugins | Category placeholder |
|---|---|---|
| **Slack** | all eleven first-party plugins | `~~chat` |
| **Gmail** | all eleven first-party plugins | `~~email` |
| **Google Drive** | all eleven first-party plugins | `~~documents`, `~~spreadsheet` |
| **Google Calendar** | corporate-strategy, transformation, balanced-scorecard, okr, pmo, value-realisation | `~~calendar` |
| **Atlassian (Rovo)** | all eleven first-party plugins | `~~project tracker`, `~~knowledge base` |
| **Linear** | all eleven first-party plugins | `~~project tracker` |
| **Asana** | all eleven first-party plugins | `~~project tracker` |
| **Honeycomb** | transformation, performance | `~~observability` |
| **Vercel** | transformation | `~~hosting` |

See the `.mcp.json` in each plugin directory for the authoritative list, including `title` and `description` on every entry.

## Wanted connectors

These would make specific plugins significantly more useful. If you build or operate one, see "How to submit" above.

| Category | Examples | Most useful for |
|---|---|---|
| Slides | Google Slides, PowerPoint/OneDrive | consulting (`deck-outline`), corporate-strategy, pmo (`steering-prep`) |
| Whiteboard | Miro, FigJam, Lucid | consulting (`hypothesis-tree`), balanced-scorecard (`build-strategy-map`), market-intelligence (`map-strategic-groups`), operating-model |
| Enterprise architecture | LeanIX, Ardoq | transformation (`target-operating-model`, `tech-strategy-brief`), corporate-strategy |
| Portfolio/PPM | Jira Align, Planview, Aha!, Productboard | corporate-strategy (`allocate-resources`), pmo, transformation (`roadmap-builder`) |
| BI/metrics | Looker, Tableau, Power BI, Mode | performance (`performance-narrative`, `tracker-builder`), corporate-strategy (`allocate-resources`), balanced-scorecard |
| Finance | Adaptive, Anaplan, Netsuite | corporate-strategy (`evaluate-strategic-option`, `synergy-stress-test`), transformation (`business-case`) |
| HR/org | Workday, HiBob, BambooHR | operating-model (`check-span-and-layers`, `align-rewards-and-incentives`) |
| Observability/product | Datadog, New Relic, Honeycomb, Amplitude, GA4 | performance, transformation (`tech-strategy-brief`, `maturity-assessment`) |

## Questions

Open an issue on this repo.

---

## For contributors

This section documents the `~~category` placeholder convention used across plugin skills and agent files in this repo. **End users should read the `CONNECTORS.md` inside each plugin they install** — that file lists the categories relevant to that plugin and what's pre-wired in its `.mcp.json`.

### The placeholder convention

Plugin markdown uses `~~category` as a stand-in for whatever MCP-backed tool the user connects in that category — e.g. `~~chat` for Slack or Teams, `~~project tracker` for Jira, Linear, or Asana. Skills describe workflows in terms of categories, not products, so the repo stays fork-friendly.

**Human placeholders vs machine categories.** Prose and skills use human-readable placeholders (`~~knowledge base`). Each plugin's `.mcp.json` `recommendedCategories` uses machine slugs (`knowledge-base`). The canonical mapping lives in [`references/connector-taxonomy.json`](./references/connector-taxonomy.json); `python3 scripts/check-connector-taxonomy.py --check` enforces it.

| Human placeholder | Machine category |
|---|---|
| `~~chat` | `chat` |
| `~~email` | `email` |
| `~~calendar` | `calendar` |
| `~~knowledge base` | `knowledge-base` |
| `~~project tracker` | `project-tracker` |
| `~~documents` | `documents` |
| `~~spreadsheet` | `spreadsheet` |
| `~~observability` | `observability` |
| `~~hosting` | `hosting` |
| `~~hris` | `hris` |

Extension categories (plugin-specific; same placeholder/slug rules):

| Human placeholder | Machine category |
|---|---|
| `~~whiteboard` | `whiteboard` |
| `~~bi analytics` | `bi-analytics` |
| `~~source control` | `source-control` |
| `~~web monitoring` | `web-monitoring` |
| `~~strategy skills registry` | `strategy-skills-registry` |

Rules when authoring skills:

1. Use the category placeholders from the taxonomy and the plugin's own `CONNECTORS.md`, not product names (no "post to Slack" — use `~~chat`).
2. Skills must produce usable output (markdown, files, chat) when no connector in that category is configured — connectors are enhancements, not hard dependencies unless explicitly documented.
3. When a skill is described as writing to a connector, the V1 fallback is always "produce the same content as a draft the user places manually."

### Per-plugin connector docs

Each first-party plugin ships its own connector reference:

| Plugin | File |
|---|---|
| consulting | [consulting/CONNECTORS.md](./consulting/CONNECTORS.md) |
| corporate-strategy | [corporate-strategy/CONNECTORS.md](./corporate-strategy/CONNECTORS.md) |
| market-intelligence | [market-intelligence/CONNECTORS.md](./market-intelligence/CONNECTORS.md) |
| transformation | [transformation/CONNECTORS.md](./transformation/CONNECTORS.md) |
| operating-model | [operating-model/CONNECTORS.md](./operating-model/CONNECTORS.md) |
| performance | [performance/CONNECTORS.md](./performance/CONNECTORS.md) |
| balanced-scorecard | [balanced-scorecard/CONNECTORS.md](./balanced-scorecard/CONNECTORS.md) |
| okr | [okr/CONNECTORS.md](./okr/CONNECTORS.md) |
| pmo | [pmo/CONNECTORS.md](./pmo/CONNECTORS.md) |
| value-realisation | [value-realisation/CONNECTORS.md](./value-realisation/CONNECTORS.md) |
| strategy-builder-hub | [strategy-builder-hub/CONNECTORS.md](./strategy-builder-hub/CONNECTORS.md) |

The per-plugin file is authoritative for which categories that plugin uses, which MCP servers are pre-configured in `.mcp.json`, and plugin-specific notes.

### Adding or changing connectors

When contributing:

1. **Category name** — add human placeholder and machine slug to `references/connector-taxonomy.json` when introducing a new category; reuse an existing pair when the semantic meaning is the same. Run `python3 scripts/check-connector-taxonomy.py --check` before opening a PR.
2. **`.mcp.json`** — add the HTTP MCP server URL when there's a well-known public endpoint; include `title` and `description` on every entry; add the category to `recommendedCategories` when relevant. Leave account-specific categories as "add your own" in the plugin's `CONNECTORS.md`.
3. **`CONNECTORS.md`** — update the plugin's file, not this one, unless you're documenting a new cross-repo convention or updating the wanted-connectors table.
4. **Skills** — reference a category in prose only where the skill actually uses it; don't wire every skill to every connector.

### Cross-plugin seams (no connector implication)

Some plugins defer to each other for canonical data without sharing connectors:

- `okr:instrument-metrics` → `performance:metrics-glossary` for metric definitions
- `balanced-scorecard:select-measures` → `performance:metrics-glossary` for metric definitions
- `value-realisation:benefits-map` → `transformation:business-case` or `corporate-strategy:evaluate-strategic-option` for seed business cases
- `value-realisation:benefits-register` → `performance:metrics-glossary` for formal metric definitions
- `value-realisation:benefits-recovery` → `pmo:decision-log` for continue-or-write-down governance decisions
- `value-realisation:realisation-review` → `transformation:business-case` / `corporate-strategy:evaluate-strategic-option` for optimism-bias calibration on future cases
- `corporate-strategy:evaluate-strategic-option` → `transformation:business-case` for initiative-level cases once a strategic direction is set — see `corporate-strategy/README.md`
- `market-intelligence:map-incentives` → `operating-model:align-rewards-and-incentives` when the incentive problem is internal — see `market-intelligence/README.md`
- `market-intelligence` competitive findings → `corporate-strategy:evaluate-strategic-option` when a signal becomes a portfolio decision
- BSC sets multi-year strategic themes; OKR cascades quarterly execution — see each plugin's README before running both cascades on the same objective set

### What these plugins don't do by default

None of these skills write directly into your tools out of the box — each produces a draft for review. Where a skill mentions posting or wiring to a connector, that's the path once you've connected one; without a connector, the skill falls back to file or chat output.
