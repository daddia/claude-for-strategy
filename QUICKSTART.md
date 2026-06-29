# Quick Start

**60 seconds.** This gets you to your first slash command. Allow 10–20 minutes per plugin if you want a filled practice profile before serious work.

## Install in Claude Cowork

1. Open the **Cowork** tab.
2. Click **Customize** in the left sidebar.
3. Click **Browse plugins** and install what you need, **or** upload a plugin directory as a zip.

## Install in Claude Code

1. **Open Claude Code** (in your terminal) or **Claude Cowork** (the desktop app). Not sure which you have? If you have a terminal window open with Claude in it, that's Claude Code.

2. **Add the marketplace.** In Claude Code, type `/plugin marketplace add ` (with a space at the end), then **drag the unzipped `claude-for-strategy` folder onto the terminal window** — it'll fill in the path. Then press Enter.

   (Or type the full path: `/plugin marketplace add /Users/you/Projects/claude-for-strategy`)

3. **Install your plugin.** Pick the one that matches your work from the table below, then:
   ```
   /plugin install consulting@claude-for-strategy
   ```

4. **⚠️ Restart Claude Code.** Close and reopen. This step is not optional — the plugin isn't live until you restart.

5. **Run setup.** Takes 2 minutes (`--quick`) or 10–20 minutes (`--full`). The first plugin you set up also writes a shared org profile reused by the others.
   ```
   /consulting:practice-setup
   /consulting:practice-setup --quick
   /consulting:practice-setup --check-integrations
   ```
   Other flags: `--full`, `--redo`, `--resume` (continue a paused interview).

6. **Connect your tools.** Skills work without connectors, but scheduled agents and live-data skills need them. In Cowork: Settings → Connectors → add Slack, Google Workspace, or Atlassian (all plugins); add Linear, Asana, or Monday.com when your plugin uses `~~project tracker`; add Google Calendar for `change-management`, `corporate-strategy`, `transformation`, `balanced-scorecard`, `okr`, `pmo`, or `value-realisation`; add GitHub for `transformation` and `strategy-builder-hub`; add Miro for `consulting`, `balanced-scorecard`, `market-intelligence`, or `operating-model` when you use `~~whiteboard`. In Claude Code: each plugin lists its MCP servers in `.mcp.json`; you'll be prompted to authorize the first time a skill needs one.

## Install user-scoped, not project-scoped

When you run `/plugin install`, you may be asked whether to install for this project only or for all projects (user scope). **Pick user scope** unless you have a specific reason not to.

It's counterintuitive: project scope feels safer for client work. But project scope blocks the plugin from reading files outside the project folder — your deck outline in Downloads, your tracker in Documents, your RAID log in a shared drive. Most skills need to read files you point at. User scope doesn't give the plugin extra access — it can only read files you explicitly reference or that are in the current directory. It just means the plugin works from any folder instead of one.

**When project scope is right:** you're running an agency and each client repo must carry its own practice profile in `.claude/` with no leakage between engagements on the same machine. Install project-scoped from inside that client's repo.

If you already installed the wrong scope and want to switch: `/plugin uninstall <plugin>`, then `/plugin install <plugin>@claude-for-strategy` from the directory where you want the scope to apply (home directory for user scope, client repo for project scope).

## Which plugin is for me?

| You are a… | Install… | First command |
|---|---|---|
| Strategy consultant or narrative lead | `consulting` | `/consulting:practice-setup` |
| Corporate strategy or portfolio lead | `corporate-strategy` | `/corporate-strategy:practice-setup` — connect `~~chat` and `~~calendar` for portfolio-review reminders; pair with `transformation` when options narrow to initiative-level business cases |
| Competitive strategy or market intelligence lead | `market-intelligence` | `/market-intelligence:practice-setup` — `competitive-signal-scan` works with native web search; connect `~~chat` for weekly digests; pair with `corporate-strategy` when signals become portfolio decisions |
| Transformation or digital lead | `transformation` | `/transformation:practice-setup` — connect `~~chat` for Assumption-Decay and Roadmap-Drift watchers; pair with `pmo` for decision-log revisit triggers and `change-management` for adoption planning |
| Change lead or OCM practitioner | `change-management` | `/change-management:practice-setup` — pair with `transformation` when stakeholder impacts seed from TOM or roadmap output; pair with `pmo` when resistance escalates to governance decisions |
| Org design or operating-model lead | `operating-model` | `/operating-model:practice-setup` — connect `~~hris` for headcount and reporting-line data; pair with `transformation` when org design is one layer of a broader TOM |
| Performance or metrics lead | `performance` | `/performance:practice-setup` |
| Program or PMO lead | `pmo` | `/pmo:practice-setup` — then connect `~~chat` and `~~calendar` for scheduled watchers |
| Agency principal (multi-client delivery) | `performance` + `pmo` | `/performance:practice-setup` then `/pmo:practice-setup` |
| OKR cycle owner | `okr` | `/okr:practice-setup` |
| Balanced scorecard owner | `balanced-scorecard` | `/balanced-scorecard:practice-setup` |
| Benefits realisation or post-implementation review lead | `value-realisation` | `/value-realisation:practice-setup` — pair with `transformation` when benefits trace back to approved business cases; distinct from `performance`/`okr`/`balanced-scorecard` (those are forward-looking cadences) |
| Anyone extending the built-in plugins with community skills | `strategy-builder-hub` | `/strategy-builder-hub:practice-setup` — install alongside your practice-area plugin; recommends a starter pack by engagement type |

After setup, run the agent that matches your job — see the [Agents table in README.md](./README.md#agents). Examples: `/consulting:narrative-builder`, `/transformation:roadmap-builder`, `/change-management:stakeholder-impact-map`, `/pmo:status-report`.

## What you're installing

Each plugin learns your playbook through a practice setup. Organisation-wide facts go to `~/.claude/plugins/config/claude-for-strategy/org-profile.md` (written once, shared across plugins). Plugin-specific conventions go to `~/.claude/plugins/config/claude-for-strategy/<plugin>/CLAUDE.md`. Every skill reads both. Edit either file directly, re-run setup (`--redo` for a full refresh), or accept a **propose profile update** when a skill surfaces a stable convention (it shows the diff and asks before writing).

**Every output is a draft for your review.** The plugins flag what they're unsure about, tag market figures and dollar amounts by source, surface load-bearing assumptions, and gate board- or exec-facing finals. You review, verify, and take responsibility. They make that review faster; they don't replace it.

## What's in the box

Twelve first-party plugins — eleven practice areas plus the Strategy Builder Hub for discovering and installing community skills — scheduled watch agents across PMO/performance/transformation/OKR/scorecard/corporate-strategy/market-intelligence/value-realisation, and connectors (Slack, Google Workspace, Atlassian, Linear, Asana, Monday.com, and plugin-specific GitHub/Miro/observability/hosting). The full reference is in [README.md](./README.md).

## Stuck?

- **Plugin not visible after install** → confirm the marketplace registered: `/plugin marketplace list` should show `claude-for-strategy`. If not, re-run step 2. Then check `/plugin` — your plugin (e.g. `consulting@claude-for-strategy`) should appear. In Cowork: Customize → Browse plugins. Still missing? You forgot step 4 — restart Claude Code.
- **"Command not found"** or **slash command not found** after install → you forgot step 4. Restart Claude Code.
- **"Run setup first"** or **practice profile not loading** → run `/<plugin>:practice-setup` before any other command. Profiles live at `~/.claude/plugins/config/claude-for-strategy/org-profile.md` and `~/.claude/plugins/config/claude-for-strategy/<plugin>/CLAUDE.md` — if missing or empty, re-run setup (`--redo` to overwrite).
- **Skill wants to update my profile** → that's the living-profile flow. It should show the exact text change and ask for confirmation before writing. Say yes to apply, no to skip, or edit `~/.claude/plugins/config/claude-for-strategy/<plugin>/CLAUDE.md` yourself.
- **Numbers look invented** or missing `[sourced:]` / `[unverified —]` tags → connect your data connectors (step 6). Without live sources, every figure is from training data. Run a consequential skill (`business-case`, `performance-narrative`, `deck-outline`, …) and verify the trust spine on the output.
- **"I can't read [file]"** → most often this means the plugin is project-scoped and the file is outside the project folder. See "Install user-scoped, not project-scoped" above — reinstall user-scoped or move the file into the project folder.
- **Scheduled agent never posts** → no `~~chat` connector configured. The agent still runs its read side — check the agent file for a file or conversation fallback.
- **Calendar-driven agent wrong cadence** → `~~calendar` not connected. Set the schedule in the agent frontmatter or practice profile to match your real cadence.
- **The plugin doesn't do X** → see the role table above or the [Agents table in README.md](./README.md#agents); check the plugin's README for what it does not do.

Updates: `/plugin update`.
