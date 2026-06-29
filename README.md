# Claude for Strategy

Reference agents, skills, and data connectors for the strategy and transformation workflows we see most — consulting craft, corporate strategy, market intelligence, digital transformation, org design, performance management, program PMO, balanced scorecards, OKRs, value realisation, and a Strategy Builder Hub for discovering community skills.

> **New here?** Start with [QUICKSTART.md](QUICKSTART.md) — install in 60 seconds. This README is the full reference.

Everything here ships as [Claude Cowork](https://claude.com/product/cowork) or [Claude Code](https://claude.com/product/claude-code) plugins **and** as [managed-agent cookbooks](./managed-agents/) for headless deployment through the [Claude Managed Agents API](https://docs.claude.com/en/api/managed-agents) — same skills and prompts, two surfaces from one source.

> [!IMPORTANT]
> **Every output from these plugins is a draft for your review — not a certified methodology, not a board-ready recommendation, not a substitute for your analysis and professional judgment.** They are built with guardrails that reflect that: source tagging on market figures and dollar amounts, load-bearing assumptions surfaced, conservative defaults on invented inputs, confidence labeling, and explicit gates before board- or exec-facing finals. You review, verify, and take responsibility for anything that leaves the building. These plugins make that review faster; they do not replace it.

What's in the repo:

- **Practice-area plugins** covering consulting craft, corporate strategy, market intelligence, transformation, org design, performance, PMO, balanced scorecards, OKRs, and value realisation — each built around a cold-start interview that learns your playbook, a living `CLAUDE.md` practice profile every skill reads from, and a **propose profile update** flow so conventions can be recorded mid-engagement without re-running setup.
- **Strategy Builder Hub** for discovering, installing, and QAing community strategy skills from trusted registries.
- **MCP connectors** across general productivity (Slack, Google Workspace, Atlassian) and strategy-specific categories (observability, hosting, spreadsheets).
- **[Named agents](#agents)** — job-style entry points (Narrative Architect, Roadmap Architect, RAID Logger, …) with a single command to run each one.
- **Scheduled agents** in `pmo`, `performance`, `transformation`, `okr`, `balanced-scorecard`, `corporate-strategy`, and `market-intelligence` — escalation/slippage/steering prep, KPI breach watching, cadence reporting, assumption-decay/roadmap-drift, check-in nudges, scorecard review reminders, portfolio review prompts, competitive signal scanning. Convention Monitor (`consulting`) is still planned for V1.2.

## Agents

Each agent is named for the job it does. They're the most common surface — start with the ones that match your work, then tune the underlying skill, the practice profile, and the connectors to how your team does it.

| Agent | What it does | Plugin | Command |
|---|---|---|---|
| **Narrative Architect** | Raw notes/findings → governing thought + MECE key line + support | `consulting` | `/consulting:narrative-builder` |
| **Deck Storyliner** | Narrative or brief → action-titled, slide-by-slide outline | `consulting` | `/consulting:deck-outline` |
| **Reviewing Partner** | Existing deck/memo → structural critique against pyramid discipline | `consulting` | `/consulting:doc-reviewer` |
| **So-What Sharpener** | Observations → implication → insight, point by point | `consulting` | `/consulting:so-what-sharpener` |
| **Workplan Architect** | Hypothesis tree → owned, timed workplan with expected so-what per row | `consulting` | `/consulting:workplan-builder` |
| **Maturity Assessor** | Interview notes/observations → maturity scorecard with binding-constraint analysis | `transformation` | `/transformation:maturity-assessment` |
| **Roadmap Architect** | Current state + ambition → phased Now/Next/Later roadmap | `transformation` | `/transformation:roadmap-builder` |
| **TOM Designer** | Current state + ambition → target operating model across capability/org/process/tech/data | `transformation` | `/transformation:target-operating-model` |
| **Structure Fit Diagnostician** | Tests whether org structure matches the coordination need the strategy requires | `operating-model` | `/operating-model:diagnose-structure-fit` |
| **Decision Rights Designer** | Builds RACI/RAPID with single-point accountability; flags zero-A and multi-A decisions | `operating-model` | `/operating-model:design-decision-rights` |
| **Span & Layers Checker** | Diagnoses span of control and layer count against over- and under-management patterns | `operating-model` | `/operating-model:check-span-and-layers` |
| **Matrix Reporting Stress Tester** | Forces explicit tie-breakers for dual-reporting relationships | `operating-model` | `/operating-model:stress-test-matrix-reporting` |
| **Rewards Alignment Checker** | Star Model check — structure, process, rewards, and people fit | `operating-model` | `/operating-model:align-rewards-and-incentives` |
| **Tech Decision Brief** | Platform/architecture decision → options + recommendation, BLUF-structured | `transformation` | `/transformation:tech-strategy-brief` |
| **Business Case Builder** | Initiative scope → problem, options, cost/benefit, sequencing, risk, ask | `transformation` | `/transformation:business-case` |
| **Assumption-Decay Watcher** | Business cases, roadmaps, decision log → assumptions with revisit-trigger dates now due | `transformation` | scheduled agent |
| **Roadmap-Drift Watcher** | Roadmap vs. actual progress → initiatives slipping phase, with knock-on effects | `transformation` | scheduled agent |
| **KPI Tree Builder** | North Star metric → MECE drivers → leading indicators | `performance` | `/performance:kpi-tree-builder` |
| **Tracker Builder** | Builds a `.xlsx` tracker wired to your Daily Log → Summary pattern | `performance` | `/performance:tracker-builder` |
| **Board Narrative Writer** | Metrics/results → BLUF-structured narrative for your stated audience | `performance` | `/performance:performance-narrative` |
| **OKR Cascader** | Maps company OKRs to team-level objectives with coverage checks | `performance` | `/performance:okr-cascade` |
| **KPI Breach Watcher** | Daily scan for metrics crossing targets/thresholds; Honeycomb for telemetry | `performance` | scheduled agent |
| **Cadence Reporter** | Assembles period performance narrative draft on reporting cadence | `performance` | scheduled agent |
| **RAID Logger** | Logs/updates a Risk, Assumption, Issue, or Dependency; flags escalation | `pmo` | `/pmo:raid-log` |
| **Status Reporter** | RAID log + milestones → audience-specific RAG status report | `pmo` | `/pmo:status-report` |
| **Steering Pack Builder** | Status + RAID + pending decisions → decision-led steering deck outline | `pmo` | `/pmo:steering-pack` |
| **Milestone Tracker** | Plan vs actual → critical-path status with slippage and knock-on effects | `pmo` | `/pmo:milestone-tracker` |
| **Decision Logger** | Appends a decision + rationale to a persisted, append-only audit log | `pmo` | `/pmo:decision-log` |
| **Escalation Watcher** | Weekly + post-`raid-log` scan for items crossing escalation threshold | `pmo` | scheduled agent |
| **Slippage Watcher** | Weekly critical-path milestone check against tolerance; flags knock-on effects | `pmo` | scheduled agent |
| **Steering Prep** | N days before steering (from `~~calendar`), assembles inputs for steering pack | `pmo` | scheduled agent |
| **Check-In Nudge** | Weekly confidence pulses to KR owners; flags staleness to the OKR lead | `okr` | scheduled agent |
| **Strategy Review Reminder** | Quarterly scorecard review prompt; separately tracks annual map-refresh cadence | `balanced-scorecard` | scheduled agent |
| **Portfolio Review Reminder** | Quarterly prompt to run `allocate-resources` and recheck `exit-or-double-down` holds past their re-rating date | `corporate-strategy` | scheduled agent |
| **Competitive Signal Scan** | Weekly scan for competitor moves that would change the strategic-group or incentive map; works with native web search, no connector required | `market-intelligence` | scheduled agent |

## Repository layout

```
consulting/               # narrative, hypothesis trees, workplans, decks, memos, doc review
corporate-strategy/       # growth vectors, resource allocation, portfolio calls, strategic options
market-intelligence/      # competitive landscape, incentives, positioning, information asymmetry
transformation/           # maturity, roadmaps, TOM, tech strategy, business cases
operating-model/          # structure fit, decision rights, span/layers, matrix reporting, rewards alignment
performance/              # KPI trees, trackers, glossary, performance narrative
pmo/                      # RAID, status reports, steering packs, milestones, decisions
balanced-scorecard/       # strategy maps, perspectives, measures, cascade, review
okr/                      # objectives, key results, targets, cascade, check-ins, scoring
strategy-builder-hub/     # community skill discovery, installation, QA, and update management
external-plugins/         # vendor plugins (future)
managed-agents/           # CMA cookbooks — escalation-watcher, steering-prep, roadmap-drift-watcher, competitive-signal-scan
scripts/                  # sync-references.py · check-marketplace-sync.py · check-connector-taxonomy.py · lint-tool-scope.py
references/               # repo-root mirror of consulting/references/ · connector-taxonomy.json
.claude-plugin/
  marketplace.json        # plugin registry
CONNECTORS.md             # contributor guide to the ~~ placeholder convention
QUICKSTART.md             # 60-second install path
```

Each plugin directory has the same shape:

```
<plugin>/
  .claude-plugin/plugin.json
  CLAUDE.md               # template practice profile — filled in by /<plugin>:cold-start-interview
  README.md
  skills/                 # skills — each is a /<plugin>:<skill> slash command
  agents/                 # scheduled/event-driven watchers only (if any)
  hooks/                  # pre- and post-tool hooks (if any)
```

## Getting started

### Claude Cowork

1. Open the **Cowork** tab.
2. Click **Customize** in the left sidebar.
3. Click **Browse plugins** and install the ones you want, **or** upload a custom plugin file (any plugin directory zipped up).

After install, skills fire automatically when relevant, slash commands are available via `/`, and scheduled agents run on the cadence set in their frontmatter.

### Claude Code

```bash
# Add the marketplace (use the absolute path to this repo or a GitHub URL)
/plugin marketplace add <path-to-this-repo>

# Install a plugin — pick the ones that match your practice
/plugin install consulting@claude-for-strategy
/plugin install corporate-strategy@claude-for-strategy
/plugin install market-intelligence@claude-for-strategy
/plugin install transformation@claude-for-strategy
/plugin install operating-model@claude-for-strategy
/plugin install performance@claude-for-strategy
/plugin install pmo@claude-for-strategy
/plugin install balanced-scorecard@claude-for-strategy
/plugin install okr@claude-for-strategy
/plugin install strategy-builder-hub@claude-for-strategy

# Restart Claude Code, then run setup for each plugin you installed.
# This writes org-profile.md (once) and per-plugin CLAUDE.md to ~/.claude/plugins/config/claude-for-strategy/
/consulting:cold-start-interview
/corporate-strategy:cold-start-interview
/market-intelligence:cold-start-interview
/transformation:cold-start-interview
/operating-model:cold-start-interview
/performance:cold-start-interview
/pmo:cold-start-interview
/balanced-scorecard:cold-start-interview
/okr:cold-start-interview
/strategy-builder-hub:cold-start-interview
```

**Run the cold-start interview first.** Every other skill in a plugin reads from the practice profile it writes. Skipping setup is the single most common reason a skill produces generic output. The interview takes 10–20 minutes per plugin and will ask you to point at seed documents. More seed material is better; a **quick start** option is available if you want to be productive in 2 minutes and refine later.

**Which plugin is for me?** See the [role routing table in QUICKSTART.md](QUICKSTART.md#which-plugin-is-for-me).

Updates: `/plugin update`.

## How it fits together

| | What it is | Where it lives |
|---|---|---|
| **Plugins** | Self-contained practice-area bundles — skills, agents, hooks, and a template practice profile. Install the ones you need. | `<plugin>/` |
| **Skills** | Domain expertise and step-by-step methods Claude draws on automatically when relevant — and slash actions you trigger explicitly: `/consulting:narrative-builder`, `/transformation:roadmap-builder`, `/pmo:status-report`. | `<plugin>/skills/<skill>/SKILL.md` |
| **Agents** | Scheduled or event-driven watchers (check-in nudge, scorecard reminder, escalation scan). Job-style names in each plugin's README map to slash commands; they do not live as separate files under `agents/`. | `<plugin>/agents/` |
| **Practice profile** | Two layers: shared `org-profile.md` (organisation, cadence, risk, financial conventions, escalation, house style) plus per-plugin `CLAUDE.md` (plugin-specific operating model, frameworks, thresholds, output formats, review gates). Every skill reads both. | `~/.claude/plugins/config/claude-for-strategy/org-profile.md` and `~/.claude/plugins/config/claude-for-strategy/<plugin>/CLAUDE.md` |
| **Connectors** | [MCP servers](https://modelcontextprotocol.io/) that wire Claude to your data — chat, calendar, project tracker, observability, spreadsheets. | `.mcp.json` (per plugin) |
| **Managed-agent cookbooks** | `agent.yaml` + depth-1 subagents + steering examples for headless deployment via the Managed Agents API. | [`managed-agents/<name>/`](./managed-agents/) |
| **Trust spine** | Sourcing tags, surfaced assumptions, numbers provenance, confidence labeling, board-ready gate — on consequential outputs. | [`references/trust-conventions.md`](references/trust-conventions.md) |

Everything is markdown and JSON. No build step.

### Claude Managed Agents

Four scheduled watchers ship as managed-agent cookbooks today — same system prompts and skills as their plugin agents, deployable headlessly behind your own workflow engine:

| Cookbook | Plugin agent | What it does |
|---|---|---|
| [`escalation-watcher`](./managed-agents/escalation-watcher/) | pmo | RAID threshold crossings |
| [`steering-prep`](./managed-agents/steering-prep/) | pmo | Pre-steering brief assembly |
| [`roadmap-drift-watcher`](./managed-agents/roadmap-drift-watcher/) | transformation | Roadmap phase slippage |
| [`competitive-signal-scan`](./managed-agents/competitive-signal-scan/) | market-intelligence | Competitor signal digest |

See [`managed-agents/README.md`](./managed-agents/README.md) for manifest conventions, security tiers, and steering-event examples. Post the resolved manifest from each directory to `POST /v1/agents` using the [Managed Agents API](https://docs.claude.com/en/api/managed-agents). A `deploy-managed-agent.sh` script is planned.

## Vertical plugins

Grouped by where the work sits. Each plugin's cold-start interview is what tailors it to your team — start there.

### Craft & delivery

| Plugin | What it adds |
|---|---|
| **[consulting](./consulting)** | Strategic narrative (Minto pyramid), hypothesis trees, hypothesis-driven workplans, deck outlines, exec memos, so-what sharpening, doc/deck review. The craft layer every deliverable should be written in. |
| **[transformation](./transformation)** | Digital maturity assessment, Now/Next/Later roadmaps, target operating model design, tech strategy briefs, transformation business cases. |
| **[operating-model](./operating-model)** | Org design and decision rights — structure-strategy fit, RACI/RAPID design, span and layers analysis, matrix-reporting stress tests, Star Model rewards alignment. |
| **[performance](./performance)** | KPI trees, metrics tracker builder, metrics glossary, performance narratives, OKR cascade helper. |
| **[pmo](./pmo)** | RAID logs, status reports, steering committee packs, milestone tracking, decision logs. |

### Corporate & portfolio strategy

| Plugin | What it adds |
|---|---|
| **[corporate-strategy](./corporate-strategy)** | Growth-gap diagnostics, resource allocation, exit-or-double-down portfolio calls, real-options-framed strategic decisions, build-vs-buy-vs-partner, synergy stress-testing. |
| **[market-intelligence](./market-intelligence)** | Strategic-group mapping with mobility barriers, incentive-driven behavior prediction, positioning trade-off discipline, information-asymmetry analysis, game-theory-grounded competitive response forecasting. |

### Measurement frameworks

| Plugin | What it adds |
|---|---|
| **[balanced-scorecard](./balanced-scorecard)** | Strategy maps and balanced scorecards — perspective design, causal strategy mapping, lead/lag measures, targets and initiatives, cascaded scorecards, and reviews that test the strategy's causal theory. |
| **[okr](./okr)** | Objectives and key results — drafting objectives, outcome-based key results, target calibration, cascading, confidence-based check-ins, and end-of-cycle scoring. |
| **[value-realisation](./value-realisation)** | Benefits mapping, baseline discipline, realisation tracking with attribution, at-risk recovery, and post-implementation review — closes the loop from approved business case to proven delivered value. |

**If you run both BSC and OKR:** a common pattern is BSC setting multi-year strategic themes and the causal map, with OKR cascading quarterly execution underneath specific BSC objectives. Don't run both cascades on the same objective set independently — pick which plugin owns which layer and record it in both practice profiles.

### Platform

| Plugin | What it adds |
|---|---|
| **[strategy-builder-hub](./strategy-builder-hub)** | Community strategy skill discovery, installation, QA, and update management. Browses GitHub registries, surfaces related community skills inside other plugins, and applies a four-layer security gate (allowlist, raw display, heuristic scan, human approval) before anything is written. The cold-start interview IS the starter pack recommender — ask your engagement type and it recommends what to install. |

**Planned, not yet built:** `change-management`, `thought-leadership`.

## MCP connectors

These plugins ship connectors for the systems strategy teams live in. A connector gives Claude the ability to read from and (where scoped) write to your data; the skills and commands use them. Skills produce usable output when no connector is configured — connectors are enhancements, not hard dependencies unless documented otherwise.

| Connector | What it gives Claude | Plugins | Notes |
|---|---|---|---|
| **Slack** | Read channels, search, send messages | all plugins | `~~chat` |
| **Google Workspace** | Drive, Sheets, Gmail, Calendar | all plugins | `~~documents`, `~~spreadsheet`, `~~calendar`, `~~email` |
| **Atlassian (Rovo)** | Jira issues, Confluence pages | all plugins | `~~project tracker`, `~~knowledge base` |
| **Honeycomb** | Product/system telemetry | `transformation`, `performance` | `~~observability` |
| **Vercel** | Deployment and hosting context | `transformation` | `~~hosting` |
| **HRIS** | Headcount and reporting-line data | `operating-model` | `~~hris` — Workday, BambooHR, Rippling, HiBob |
| **Notion** | Knowledge base (workspace-specific) | all plugins | Add your own MCP server URL |
| **Web & news monitoring** | Curated competitive/news feeds | `market-intelligence` | Exa, Tavily, NewsAPI, Feedly — optional; `competitive-signal-scan` works with native web search |

Per-plugin connector details: each plugin's [CONNECTORS.md](./CONNECTORS.md) (contributor index) links to `<plugin>/CONNECTORS.md`.

> Connectors marked "customer subscription" need your own account and API key. Configure them in each plugin's `.mcp.json` or via `claude mcp` in Claude Code.

## Making it yours

These are reference templates. They get better when you tune them to how your team works — and the customization mechanism is the plugin itself, not a config file buried in a repo.

- **Run the cold-start interview.** It **is** the customization mechanism. It asks how your practice works, reads your seed documents, and writes your practice profile after you confirm the summary. Every other skill reads from that profile.
- **Edit the practice profile.** Org-wide facts live at `~/.claude/plugins/config/claude-for-strategy/org-profile.md`; plugin-specific conventions at `~/.claude/plugins/config/claude-for-strategy/<plugin>/CLAUDE.md`. Edit either file directly for small fixes. They survive plugin updates.
- **Propose profile updates from any skill.** When a stable convention surfaces during work (repeated tone corrections, a new RAID threshold, tracker column names), skills show the exact profile change and ask before writing. Only `cold-start-interview` auto-applies a full profile write — everything else proposes first.
- **Re-run setup.** `/<plugin>:cold-start-interview` again for a full re-interview when your practice shifts materially.
- **Swap connectors.** Point `.mcp.json` at your project tracker, slides tool, observability platform, and data sources. Skills fall back gracefully when a connector isn't configured.
- **Bring your playbook and templates.** Drop your terminology, house style, and branded templates into the practice profile and `references/`. The skills will pick them up.
- **Fork skills for house style.** Every skill is a markdown file under `skills/`. Edit the steps, the gates, the output format.
- **Add watchers.** Scheduled agents live under `<plugin>/agents/` with their system prompt and cadence. Job-style names for on-demand work map to slash commands in each plugin's README — not to duplicate subagent files.

No build step. Everything is markdown and JSON.

## Skill & command reference

The full map across all plugins. The cold-start interview is the first thing to run in any plugin.

### consulting

| Command | Skill | What it does |
|---|---|---|
| `/consulting:cold-start-interview` | cold-start-interview | Learns narrative/deck/memo conventions; writes practice profile |
| `/consulting:narrative-builder` | narrative-builder | Raw notes → governing thought + MECE key line + support |
| `/consulting:hypothesis-tree` | hypothesis-tree | Problem statement → root hypothesis + falsifiable MECE sub-hypotheses |
| `/consulting:workplan-builder` | workplan-builder | Hypothesis tree → owned, timed workplan |
| `/consulting:deck-outline` | deck-outline | Narrative → action-titled, slide-by-slide outline |
| `/consulting:exec-memo` | exec-memo | Narrative or raw notes → BLUF one-pager |
| `/consulting:so-what-sharpener` | so-what-sharpener | Observations → implication → insight |
| `/consulting:doc-reviewer` | doc-reviewer | Existing deck/memo → structural critique |

### corporate-strategy

| Command | Skill | What it does |
|---|---|---|
| `/corporate-strategy:cold-start-interview` | cold-start-interview | Learns portfolio composition, growth ambition, capital allocation process, risk posture |
| `/corporate-strategy:assess-growth-vectors` | assess-growth-vectors | Categorizes initiatives core/adjacent/transformational; tests whether the portfolio sums to the stated growth target |
| `/corporate-strategy:allocate-resources` | allocate-resources | Maps spend/headcount/attention against strategic priority; flags misallocation |
| `/corporate-strategy:exit-or-double-down` | exit-or-double-down | Blank-page test per unit; surfaces sunk-cost reasoning; exit/hold/double-down call |
| `/corporate-strategy:evaluate-strategic-option` | evaluate-strategic-option | Real-options framing — staging, kill criteria, case against written by the skill |
| `/corporate-strategy:build-vs-buy-vs-partner` | build-vs-buy-vs-partner | Capability gap vs. build/buy/partner paths with failure priors |
| `/corporate-strategy:synergy-stress-test` | synergy-stress-test | Cost vs. revenue synergies; base-rate haircut; double-count check |
| scheduled | portfolio-review-reminder (agent) | Quarterly `allocate-resources` + hold-recheck prompt via `~~chat` |

### market-intelligence

| Command | Skill | What it does |
|---|---|---|
| `/market-intelligence:cold-start-interview` | cold-start-interview | Learns market definition, positioning, incentive context, signal-monitoring preferences |
| `/market-intelligence:map-competitive-landscape` | map-competitive-landscape | Strategic-group map with mobility barriers; white-space attractiveness test |
| `/market-intelligence:map-incentives` | map-incentives | Actual incentive structures vs. stated motivations; behavior prediction |
| `/market-intelligence:test-positioning` | test-positioning | Explicit trade-offs; stuck-in-the-middle check; alienation stress test |
| `/market-intelligence:map-information-asymmetry` | map-information-asymmetry | Informed vs. uninformed players; signaling/screening mechanisms |
| `/market-intelligence:forecast-competitive-response` | forecast-competitive-response | Competitor reaction prediction grounded in incentive structure |
| scheduled | competitive-signal-scan (agent) | Weekly competitor signal scan via native web search; optional `~~chat` digest |

### transformation

| Command | Skill | What it does |
|---|---|---|
| `/transformation:cold-start-interview` | cold-start-interview | Learns platform vocabulary, delivery model, maturity framework |
| `/transformation:maturity-assessment` | maturity-assessment | Observations → maturity scorecard with binding-constraint analysis |
| `/transformation:roadmap-builder` | roadmap-builder | Current state + ambition → phased roadmap |
| `/transformation:target-operating-model` | target-operating-model | Current state + ambition → TOM |
| `/transformation:tech-strategy-brief` | tech-strategy-brief | Architecture decision → options + recommendation |
| `/transformation:business-case` | business-case | Initiative scope → full business case |
| scheduled | assumption-decay-watcher (agent) | Weekly + post-update scan for due revisit-trigger assumptions via `~~chat` |
| scheduled | roadmap-drift-watcher (agent) | Weekly roadmap phase-slippage check via `~~chat` |

### operating-model

| Command | Skill | What it does |
|---|---|---|
| `/operating-model:cold-start-interview` | cold-start-interview | Learns current structure, strategic priority, decision-rights gaps, reward mechanics |
| `/operating-model:diagnose-structure-fit` | diagnose-structure-fit | Tests structure against strategy coordination needs; flags leader-centric charts |
| `/operating-model:design-decision-rights` | design-decision-rights | RACI/RAPID with single-point accountability; flags zero-A and multi-A decisions |
| `/operating-model:check-span-and-layers` | check-span-and-layers | Span of control and layer count vs. over- and under-management patterns |
| `/operating-model:stress-test-matrix-reporting` | stress-test-matrix-reporting | Explicit tie-breakers for dual-reporting; flags matrix-as-unresolved-compromise |
| `/operating-model:align-rewards-and-incentives` | align-rewards-and-incentives | Star Model check — structure, process, rewards, and people fit |

### performance

| Command | Skill | What it does |
|---|---|---|
| `/performance:cold-start-interview` | cold-start-interview | Learns KPI taxonomy, tracker structure, reporting cadence |
| `/performance:kpi-tree-builder` | kpi-tree-builder | North Star → MECE drivers → leading indicators |
| `/performance:tracker-builder` | tracker-builder | Builds `.xlsx` with Daily Log → Summary formulas |
| `/performance:metrics-glossary` | metrics-glossary | Metric list → single source-of-truth definitions |
| `/performance:performance-narrative` | performance-narrative | Metrics/results → BLUF narrative |
| `/performance:okr-cascade` | okr-cascade | Company OKRs → team-level objectives |
| scheduled | kpi-breach-watcher (agent) | Daily threshold breach scan via `~~chat`; Honeycomb for telemetry |
| scheduled | cadence-reporter (agent) | Period narrative draft on reporting cadence via `~~chat` |

### pmo

| Command | Skill | What it does |
|---|---|---|
| `/pmo:cold-start-interview` | cold-start-interview | Learns governance cadence, RAID/RAG definitions, escalation thresholds |
| `/pmo:raid-log` | raid-log | Log/update RAID item; flag escalation |
| `/pmo:status-report` | status-report | RAID + milestones → RAG status report |
| `/pmo:steering-pack` | steering-pack | Status + RAID + decisions → steering deck outline |
| `/pmo:milestone-tracker` | milestone-tracker | Plan vs actual → critical-path status |
| `/pmo:decision-log` | decision-log | Append decision + rationale to audit log |
| scheduled | escalation-watcher (agent) | Weekly + post-`raid-log` escalation scan via `~~chat` |
| scheduled | slippage-watcher (agent) | Weekly critical-path slippage check via `~~chat` |
| scheduled | steering-prep (agent) | Pre-steering brief from `~~calendar` + RAID/milestones/decisions |

### balanced-scorecard

| Command | Skill | What it does |
|---|---|---|
| `/balanced-scorecard:cold-start-interview` | cold-start-interview | Learns sector, perspective model, cadence, cascade structure |
| `/balanced-scorecard:define-perspectives` | define-perspectives | Perspective set and causal-chain top perspective |
| `/balanced-scorecard:build-strategy-map` | build-strategy-map | Objectives per perspective with explicit causal mechanisms |
| `/balanced-scorecard:select-measures` | select-measures | Lead/lag classification per measure |
| `/balanced-scorecard:set-targets-and-initiatives` | set-targets-and-initiatives | Targets plus named strategic initiatives |
| `/balanced-scorecard:cascade-to-scorecards` | cascade-to-scorecards | Cascade to BU/team scorecards via causal-mechanism test |
| `/balanced-scorecard:review-and-validate` | review-and-validate | Score measures; test causal links against outcomes |
| scheduled | strategy-review-reminder (agent) | Quarterly review prompt; annual map-refresh tracker |

### okr

| Command | Skill | What it does |
|---|---|---|
| `/okr:cold-start-interview` | cold-start-interview | Learns philosophy, scoring scale, cadence, cascade structure |
| `/okr:draft-objectives` | draft-objectives | Draft objectives; catch KR-disguised-as-objectives |
| `/okr:write-key-results` | write-key-results | Outcome-shaped KRs; catch vanity metrics |
| `/okr:set-targets` | set-targets | Commit vs aspirational labeling; sandbagging detection |
| `/okr:instrument-metrics` | instrument-metrics | Map each KR to an exact metric spec |
| `/okr:cascade` | cascade | Parent-contribution test; orphan/coverage check |
| `/okr:check-in` | check-in | Confidence-based pulse per KR |
| `/okr:score-and-retro` | score-and-retro | End-of-cycle grading; keep/kill/revise |
| scheduled | check-in-nudge (agent) | Weekly KR confidence nudges via `~~chat` |

### strategy-builder-hub

| Command | Skill | What it does |
|---|---|---|
| `/strategy-builder-hub:cold-start-interview` | cold-start-interview | Engagement profile → starter pack recommendation; asks engagement type and recommends community skills to install |
| `/strategy-builder-hub:registry-browser [query]` | registry-browser | Search watched registries for community strategy skills |
| `/strategy-builder-hub:skill-installer [skill]` | skill-installer | Allowlist-gate, fetch, raw display, heuristic scan, QA, and install a community skill |
| `/strategy-builder-hub:auto-updater` | auto-updater | Check for updates to installed skills; show full diff and trust review; apply only on explicit approval |
| `/strategy-builder-hub:related-skills-surfacer` | related-skills-surfacer | Surface related community skills based on what you've been doing |
| `/strategy-builder-hub:skills-qa [skill]` | skills-qa | Evaluate a skill against the Strategy Skill Design Framework (13 parameters + prompt-injection scan) before installing |
| `/strategy-builder-hub:disable [skill]` | disable | Disable an installed community skill without removing files; re-enable later |
| `/strategy-builder-hub:uninstall [skill]` | uninstall | Uninstall a community skill installed through the hub; refuses to touch first-party plugin skills |
| scheduled | registry-sync (agent) | Weekly scan of watched registries for new and updated skills; posts notifications per update preferences |

## Contributing

Everything here is markdown and JSON. Fork, edit, PR.

- **New skill** → add `<plugin>/skills/<skill-name>/SKILL.md` with `name` and `description` frontmatter. The skill is invokable as `/<plugin>:<skill-name>`.
- **New job-style name** → add the skill under `<plugin>/skills/<skill-name>/SKILL.md` and a row in the plugin README Agents table mapping the job title to `/<plugin>:<skill-name>`. Do not add a duplicate subagent file that preloads the skill.
- **New scheduled agent** → add `<plugin>/agents/<name>.md` with the system prompt (and schedule/cadence in the body or frontmatter). Add a matching `managed-agents/<name>/` cookbook when the agent should deploy headlessly (see [managed-agents/README.md](managed-agents/README.md)).
- **Validate before opening a PR** — see [CLAUDE.md](CLAUDE.md) for marketplace invariants and `claude plugin validate`.

## License

Licensed under the [MIT License](LICENSE).

Copyright 2026 Jonathan Daddia.
