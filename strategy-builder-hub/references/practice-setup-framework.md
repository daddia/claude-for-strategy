# Practice setup framework — claude-for-strategy

Every first-party plugin's `practice-setup` skill follows this framework. Plugin skills add only **plugin-specific** questions on top; org-wide facts live once in the shared org profile.

## Invocation

| Command | Behaviour |
|---|---|
| `/<plugin>:practice-setup` | Detect existing setup; offer quick vs full if mode not specified |
| `/<plugin>:practice-setup --quick` | Short path: org gaps (if any) + 3–5 plugin questions; sensible defaults elsewhere |
| `/<plugin>:practice-setup --full` | Full org interview (when needed) + full plugin interview; review seed documents |
| `/<plugin>:practice-setup --redo` | Ignore existing profiles for this run; re-interview and overwrite on confirmation |
| `/<plugin>:practice-setup --check-integrations` | Report MCP connector status for this plugin; no interview unless user asks to continue |
| `/<plugin>:practice-setup --resume` | Continue a paused interview from the saved session file |

Combine flags when useful (e.g. `--redo --full`). If `--resume` is present, load the session first; other flags adjust what happens after resume.

## Config paths

| File | Purpose |
|---|---|
| `~/.claude/plugins/config/claude-for-strategy/org-profile.md` | Shared org facts — written once, read by every plugin |
| `~/.claude/plugins/config/claude-for-strategy/<plugin>/CLAUDE.md` | Plugin practice profile — plugin-specific conventions only |
| `~/.claude/plugins/config/claude-for-strategy/<plugin>/practice-setup-resume.json` | Paused interview state (questions answered, remaining steps, draft field values) |

**In-repo templates (read-only):** `../../references/org-profile-template.md` and the plugin's `../../CLAUDE.md`. Never modify installed plugin templates.

**Install scope:** User-scoped install (recommended) lets skills read files you reference anywhere on disk. Project-scoped install limits reads to the project folder — note this if the user reports "can't read [file]" during seed-document review. See QUICKSTART "Install user-scoped, not project-scoped."

## Startup — detect existing setup

Before asking questions:

1. **Read** `org-profile.md` if it exists. Note `Status` (`template` vs `complete`) and which sections are filled.
2. **Read** `~/.claude/plugins/config/claude-for-strategy/<plugin>/CLAUDE.md` unless `--redo` is set.
3. **If both exist and are complete** (not `template`, no major blanks): summarize what's on file and ask — refresh org profile, refresh plugin profile, both, or `--check-integrations` only? Do not re-interview unless the user chooses refresh or passed `--redo`.
4. **If only org profile exists:** say the org layer is done; run plugin-specific interview only.
5. **If only plugin profile exists** (legacy): offer to backfill org profile from plugin content where possible, then continue.
6. **If neither exists:** explain the two-layer model (org once, plugin per practice area) and proceed.

### Legacy migration

If an old practice profile at a non-standard path is found (e.g. project-scoped `.claude/CLAUDE.md` with strategy content), offer to copy normalized content into the standard paths above. Do not delete the legacy file without explicit confirmation.

## Org profile interview

Run when `org-profile.md` is missing, `Status` is `template`, `--redo` is set, or `--full` requires org refresh. **Skip sections already answered** in a complete org profile unless `--redo`.

Ask (quick: organisation + industry + planning cadence + default audiences + house tone; full: all):

1. **Organisation / client** — legal name, what you call it in prose, and whether this is internal strategy or client/advisory work.
2. **Industry / market** — market, geography, rough scale (revenue band or headcount if comfortable sharing).
3. **Strategic horizon** — planning window (e.g. 3-year strategy, annual operating plan, quarterly execution).
4. **Planning cadence** — annual strategy cycle, quarterly business reviews, OKR/BSC rhythm, budget cycle timing.
5. **Board cycle** — board meeting rhythm, annual strategy/budget board timing, materials due dates, standing agenda themes.
6. **Decision forums** — board, exec committee, investment committee, steering bodies; who decides what class of decision.
7. **Risk appetite** — conservative, balanced, or aggressive as a default; any hard constraints (regulatory, capital, political).
8. **Financial model conventions** — currency/units, planning basis, case time horizon, sensitivity conventions, who validates numbers.
9. **Default audiences** — who most outputs are for (board, C-suite, working team, external client).
10. **Data systems / source hierarchy** — systems of record (ERP, CRM, BI, Jira, HRIS); which source wins when numbers disagree; tool stack / connectors in use.
11. **Escalation / approval model** — working level → approver → exec triggers; dollar/impact thresholds if used.
12. **House writing style** — tone, person/tense, things to avoid, preferred structure (BLUF, pyramid, etc.).
13. **Preferred frameworks** — house methods (BSC, OKRs, McKinsey-style narrative, SAFe, etc.) and what to avoid.
14. **Terminology** — internal names for key concepts, banned generic substitutes.

**Write org profile** to `~/.claude/plugins/config/claude-for-strategy/org-profile.md` following `org-profile-template.md`. Set `Status: complete` when done. User confirmation on the org summary authorizes the write (same rule as plugin profile).

## Plugin profile interview

After org layer is satisfied:

1. **Read org profile** and **do not re-ask** facts already captured there (sector, cadence, risk appetite, audiences, etc.). Reference org profile in the plugin profile where relevant (e.g. "Default audiences: see org profile").
2. Run the **plugin-specific** questions defined in the skill (below the framework section in each `practice-setup/SKILL.md`).
3. **Quick mode:** plugin-specific essentials only; seed documents optional.
4. **Full mode:** request 2–3 seed documents listed in the plugin skill; read for tone, structure, and vocabulary — not to copy proprietary content.
5. **Write plugin profile** to `~/.claude/plugins/config/claude-for-strategy/<plugin>/CLAUDE.md`. Fill every section; use "no strong preference — will infer per task" or "see org profile" rather than leaving blanks.

## Integrations — `--check-integrations`

Read the installed plugin's `.mcp.json` (in-repo: `../../.mcp.json` from the skill). For each server, report:

| Server | Enables in this plugin |
|---|---|
| slack | Scheduled digests, nudges, team notifications |
| gmail | Email context, stakeholder comms |
| google-drive | Seed documents, shared decks/trackers |
| google-calendar | Steering prep, review reminders, cadence-driven agents |
| atlassian | Jira/Confluence status, RAID, decision logs |
| linear | Issues, projects, initiatives, milestones, cycle status |

For each: **connected** (user has authorized), **available but not connected**, or **not in this plugin's manifest**. Name which agents/skills are degraded without each connector. Offer to continue setup after the report.

## Pause and resume

**Pause:** If the user must stop mid-interview, write `practice-setup-resume.json` with: `plugin`, `mode` (quick/full), `started_at`, `org_complete` (bool), `answers` (object of field → value), `remaining_steps` (array), `last_step_completed`. Tell the user to run `/<plugin>:practice-setup --resume`.

**Resume:** Load the session file, summarize progress, continue from `remaining_steps`. Delete the session file after successful write of both profiles (or on `--redo` completion).

## Confirm and summarize

1. Show **org profile** changes (if any) and **plugin profile** changes in plain language.
2. Wait for explicit confirmation before writing.
3. After write: remind user they can edit files directly, use **propose profile update** from other skills, run `--check-integrations`, or `--redo` for a full refresh.
4. Mention `org-profile.md` is shared — other plugins will reuse it on their first practice-setup.

## Living profile rules

- **`practice-setup`** is the only skill that may **auto-apply** a full profile write (after confirmation above).
- **Every other skill** uses **propose profile update** for stable conventions — show exact diff, ask, write only on yes.
- Org-level stable facts discovered later → propose update to `org-profile.md`. Plugin-specific facts → propose update to the plugin `CLAUDE.md`.
