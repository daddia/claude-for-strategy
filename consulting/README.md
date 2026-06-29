# consulting

Strategic narrative, hypothesis-driven problem solving, and deliverable craft. The craft layer the other `claude-for-strategy` plugins write in — standalone by design, so it works whether or not you've installed anything else.

## Agents

Job-style names in the table map to slash commands — run the command to invoke the skill. This plugin has no scheduled agents under `agents/`.

| Agent | What it does | Command |
|---|---|---|
| **Narrative Architect** | Raw notes/findings → governing thought + MECE key line + support | `/consulting:narrative-builder` |
| **Deck Storyliner** | Narrative or brief → action-titled, slide-by-slide outline | `/consulting:deck-outline` |
| **Reviewing Partner** | Existing deck/memo → structural critique against pyramid discipline | `/consulting:doc-reviewer` |
| **So-What Sharpener** | Observations → implication → insight, point by point | `/consulting:so-what-sharpener` |
| **Workplan Architect** | Hypothesis tree → owned, timed workplan with expected so-what per row | `/consulting:workplan-builder` |

## What this plugin does NOT do

- **Replace your analysis or client judgment** — it structures and sharpens; you own the recommendation.
- **Build finished slides or Word documents** — `deck-outline` and `exec-memo` produce markdown skeletons; hand off to your presentation or doc toolchain.
- **Run market research or source verification automatically** — figures need `[sourced:]` tags you supply; untagged claims are flagged `[unverified —]`.
- **Install community skills from arbitrary registries** — use the [`strategy-builder-hub`](../strategy-builder-hub) plugin for trust-gated browse, install, and skill QA alongside first-party marketplace plugins.

## Getting started

Run `/consulting:practice-setup` first. It writes your practice profile to `~/.claude/plugins/config/claude-for-strategy/consulting/CLAUDE.md`, which every other skill reads before producing output. A quick-start (4 questions) or full interview (with 2–3 seed documents) are both supported.

### Living profile

- **Practice setup** — writes the full profile after you confirm the interview summary.
- **Any other skill** — when a stable convention surfaces (tone, pyramid style, deck rules), skills **propose a profile update**: show the exact change, ask for confirmation, write only if you say yes.
- **Edit directly** — small fixes without re-running setup.
- **Convention Monitor** (planned V1.2) — will propose the same kind of update when delivered decks/memos diverge from the profile repeatedly.

No environment variables or connectors are required for V1 — everything is markdown in, markdown out. Optional MCP servers are listed in [CONNECTORS.md](./CONNECTORS.md).

## Usage

Each skill works standalone (e.g. paste a memo and ask for a `doc-reviewer` pass) or chained:

```
hypothesis-tree → workplan-builder
narrative-builder → deck-outline
narrative-builder → exec-memo
```

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/consulting:practice-setup` | practice-setup | Learns narrative/deck/memo conventions; writes practice profile |
| `/consulting:narrative-builder` | narrative-builder | Raw notes → governing thought + MECE key line + support |
| `/consulting:hypothesis-tree` | hypothesis-tree | Problem statement → root hypothesis + falsifiable MECE sub-hypotheses |
| `/consulting:workplan-builder` | workplan-builder | Hypothesis tree → owned, timed workplan |
| `/consulting:deck-outline` | deck-outline | Narrative → action-titled, slide-by-slide outline |
| `/consulting:exec-memo` | exec-memo | Narrative or raw notes → BLUF one-pager |
| `/consulting:so-what-sharpener` | so-what-sharpener | Observations → implication → insight |
| `/consulting:doc-reviewer` | doc-reviewer | Existing deck/memo → structural critique |

## Reference material

`references/minto-pyramid.md`, `references/hypothesis-driven-approach.md`, `references/bluf-conventions.md`, `references/mece.md`, and `references/trust-conventions.md` ship with the plugin. Skills cite them plugin-relative (e.g. `../../references/minto-pyramid.md` from `skills/<name>/`). Repo-root `references/` mirrors the consulting copies for contributors — keep them in sync with `python3 scripts/sync-references.py --check`.

Consequential skills — `deck-outline`, `exec-memo`, and `doc-reviewer` — inline the condensed trust-spine block and link to `trust-conventions.md` for the full rules.

## Customization

See [CONNECTORS.md](./CONNECTORS.md) for optional connector categories and what's pre-wired in `.mcp.json`. V1 skills work without any connectors — markdown in, markdown out.
