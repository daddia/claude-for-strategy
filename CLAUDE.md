# CLAUDE.md

Guidance for working on this repo. `claude-for-strategy` is a Claude Code plugin marketplace — eleven first-party strategy plugins, vendor plugins (future), and managed-agent cookbooks. Most work here is editing prompt content (skills), plugin metadata, or reference material — not application code.

## Layout

```
.claude-plugin/marketplace.json   # the marketplace manifest — one entry per plugin
<plugin>/                         # 11 first-party plugins (consulting, corporate-strategy, market-intelligence, transformation, operating-model, performance, balanced-scorecard, okr, pmo, value-realisation, strategy-builder-hub)
  .claude-plugin/plugin.json      # plugin manifest (name, version, description, author)
  .mcp.json                       # MCP servers the plugin connects to
  CLAUDE.md                       # practice-profile TEMPLATE (see "Plugin CLAUDE.md" below)
  README.md                       # per-plugin docs
  skills/<name>/SKILL.md          # one skill per directory
  references/                     # consulting: method refs; all plugins: cold-start-framework + org-profile-template
  agents/<name>.md                # scheduled/background watcher definitions only (if any)
  hooks/hooks.json                # hook config (most plugins ship an empty stub)
  .gitignore
external-plugins/<vendor>/        # vendor plugins
managed-agents/<name>/   # agent.yaml + subagents/ + steering-examples.json
scripts/                          # validate.py, lint-tool-scope.py, check-marketplace-sync.py,
                                  # validate-skills.py, sync-skill-permission-tiers.py,
                                  # validate-connectors.py, sync-references.py,
                                  # deploy-managed-agent.sh
references/                       # repo-root mirror of consulting/references/ (see sync script);
                                  # connector-taxonomy.json (canonical ~~ placeholder map)
```

## Validation — run before opening a PR

Optional Python deps for `scripts/lint-tool-scope.py` and `scripts/validate.py`
(managed-agent cookbooks): `python3 -m venv .venv && source .venv/bin/activate &&
pip install -r requirements.txt`. Other checks use the stdlib only.

This repo follows the same conventions `anthropics/claude-plugins-official`
enforces in CI. Run the equivalent checks locally:

```bash
# 1. Marketplace + per-plugin schema validation (source of truth)
claude plugin validate .claude-plugin/marketplace.json
for d in */; do [ -f "$d/.claude-plugin/plugin.json" ] && claude plugin validate "$d"; done

# 2. JSON sanity
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"

# 3. consulting reference mirrors
python3 scripts/sync-references.py --check

# 4. managed-agent orchestrator tool scope
python3 scripts/lint-tool-scope.py

# 5. marketplace ↔ plugin.json field sync (name, description, author)
python3 scripts/check-marketplace-sync.py --check

# 6. skill frontmatter, permission tiers, and required headings (skill-design-framework.md)
python3 scripts/validate-skills.py --check

# 7. connector placeholder taxonomy (references/connector-taxonomy.json)
python3 scripts/validate-connectors.py --check
```

Install the optional pre-commit hook to run step 6 on staged `SKILL.md` files only:

```bash
pre-commit install
```

### Marketplace invariants (I1–I11)

`claude-plugins-official` layers these on top of the schema check. They apply
here too — the ones most likely to trip a contributor:

- **I1** — `plugins[]` should be alpha-sorted by name (case-insensitive).
  *Currently a known warning: the array is in a curated display order. If you
  add a plugin, ask before re-sorting the whole array.*
- **I2** — no duplicate plugin names.
- **I3** — `description` 10–2000 chars, no leading/trailing whitespace.
- **I8** — every vendored `source` (`"./<dir>"`) must point at a directory that
  contains `.claude-plugin/plugin.json`.
- **I9** — `source` paths/URLs must contain no shell metacharacters or `..`.
- **I10** — no hidden Unicode (zero-width chars, bidi controls) in
  `name`/`description`.
- **I11** — `name` must match `^[a-z0-9][a-z0-9-]{1,63}$`.

### Frontmatter requirements

Every `skills/<name>/SKILL.md` needs `description`. Multi-line descriptions use
`>` block scalars and that's fine — `claude plugin validate` parses them correctly.

## Conventions

### Keep `marketplace.json` in sync with `plugin.json`

For first-party plugins, `marketplace.json`'s `name`, `description`, and
`author` should match the corresponding fields in the plugin's own
`.claude-plugin/plugin.json`. If you change a plugin's description in one place, change it in the
other.

### Plugin agents vs job-style names

`agents/<name>.md` files are scheduled/background watcher definitions only.
Job-style on-demand agents are README labels that map to slash commands under
`skills/` — do not add duplicate files under `agents/`.

### Skill names in prose must be canonical

When a `SKILL.md` (especially `customize` or `cold-start-interview`) tells the
user "run `/foo`," `foo` must be the actual `skills/<foo>/` directory name.
Short forms like `/deck` for `/deck-outline` look right in prose but are
dead commands — the user types them and nothing happens. Refs to Claude Code
built-ins (`/mcp`, `/plugin`) and to other plugins (`/<other-plugin>:<skill>`)
are fine.

### Plugin CLAUDE.md is a template, not project context

Each `<plugin>/CLAUDE.md` is a practice-profile template that the
`cold-start-interview` skill copies to `~/.claude/plugins/config/claude-for-strategy/<plugin>/CLAUDE.md`
on the user's machine. Organisation-wide facts live once in
`~/.claude/plugins/config/claude-for-strategy/org-profile.md` (template:
`consulting/references/org-profile-template.md`). It is *not* loaded as project context when the plugin is
installed — `claude plugin validate` warns about this and the warning is
expected. Don't "fix" it by moving the content into a skill.

**Living profile.** `cold-start-interview` is the only skill that auto-applies a
full profile write (after the user confirms the interview summary). Every other
skill must use **propose profile update** — show the exact change, ask, then
write only on confirmation. All eleven plugins share the cold-start framework in
`references/cold-start-framework.md` (canonical under `consulting/references/`,
copied to each plugin's `references/`). Documented in each plugin's `cold-start-interview`
skill and in user-facing README/QUICKSTART.

### `external-plugins/` is vendor-authored

Plugins under `external-plugins/` are built and maintained by the vendor
(README.md has the policy). Don't change vendor-authored content without
checking with them first; whitespace normalization and formatting are usually
fine since the vendor lands changes via PR rather than mirroring a fork.

### `references/` ships with `consulting`, mirrored at repo root

The method and trust reference files (`minto-pyramid`, `hypothesis-driven-approach`,
`bluf-conventions`, `mece`, `trust-conventions`) plus shared setup refs
(`cold-start-framework`, `org-profile-template`) live in `consulting/references/`
so they ship when the consulting plugin is installed. Other plugins carry copies
of the two setup refs in their own `references/` for standalone install. Skills
cite them plugin-relative (`../../references/<file>.md` from `skills/<name>/`).
Repo-root `references/` holds identical copies for contributors browsing the
monorepo — run `python3 scripts/sync-references.py --check` before opening a PR
(or `python3 scripts/sync-references.py` to copy canonical → mirror and plugin
copies after editing the consulting copies).

### Formatting

- 2-space indent in all JSON and `.mcp.json` files.
- Final newline at end of every text file.
- No trailing whitespace.
- Markdown tables: pipe-aligned columns are nice but not required; just keep
  the column count consistent.

## Cookbooks

Each `managed-agents/<name>/` has `agent.yaml` (the orchestrator),
`subagents/*.yaml` (the leaves), `steering-examples.json`, and `README.md`. Two
rules that `scripts/lint-tool-scope.py` enforces:

1. The orchestrator gets local-only tools (`read`, `grep`, `glob`,
   `agent_toolset`); MCP and write tools belong to specific subagent leaves.
2. The README's security table and the `agent.yaml` comments must match what
   the YAML actually grants. Don't claim a tool a subagent doesn't have.

## Things to leave alone

- Per-plugin `.gitignore` files differ slightly across plugins. Probably
  intentional; ask before unifying.
- `hooks/hooks.json` stubs are empty in every first-party plugin. Hooks are
  optional; the empty stubs are not a bug.