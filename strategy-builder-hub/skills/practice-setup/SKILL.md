---
name: practice-setup
description: >
  Engagement-profile interview that recommends and installs a starter pack of
  community strategy skills. This IS the practice setup for the whole ecosystem — it
  asks what kind of strategist you are and recommends what to install first. Use
  on fresh install, when the user says "get me started" or "what should I
  install", or to re-run the integration-availability check after adding or
  removing an MCP connector.
argument-hint: "[--redo] [--check-integrations]"
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.3.0"
  owner: "strategy-builder-hub practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# /strategy-builder-hub:practice-setup

## When to use

Hub onboarding — engagement profile, integration check, starter pack recommendations. Explicit invocation only.

## What this skill does not do

- **Does not install without user picking skills** from recommendations.
- **Does not report integration ✓ without successful MCP probe.**

## Preconditions

Detect existing profile; offer `--redo` or `--check-integrations` per flags.

## Provisional mode

Partial profile → offer resume or fresh start.

## Trust spine

Structured-aggregation; integration table only ✓ on successful probe.

## Workflow

Read `~/.claude/plugins/config/claude-for-strategy/strategy-builder-hub/CLAUDE.md`:
- **Does not exist** → start the interview.
- **Contains `<!-- PAUSED -->`** → greet the user and offer to resume from that section.
- **Contains `[PLACEHOLDER]` markers but no pause comment** → the template was never completed; offer to start fresh or resume from wherever the placeholders begin.
- **Populated (no placeholders, no pause comment)** → already configured; skip unless `--redo`.

The template structure lives at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — use it as the section scaffold. Write the completed engagement profile to the config path, creating parent directories as needed.

## Check for the shared org profile

Look for `~/.claude/plugins/config/claude-for-strategy/org-profile.md`.

- **If it exists:** Read it. Show a one-line confirmation: "You're [name], [role], at [company], [industry], focusing on [areas]. Right? (Or say 'update' to change the shared profile.)" If confirmed, skip the org questions — go straight to the plugin-specific ones.
- **If it doesn't exist:** You'll be the first plugin this user set up. After the orientation and fork, ask the org questions and write them to the shared profile (per the template at `references/org-profile-template.md` in the plugin root), then continue with the plugin-specific questions. Tell the user: "I've saved your org profile — the other strategy plugins will read it and skip these questions."

The org questions that belong in the shared profile (and should NOT be re-asked if it exists): org name, industry, what-you-sell, size, key geographies, key stakeholders, risk appetite, escalation names. The plugin-specific questions (engagement type, methodology preferences, tooling comfort, playbook positions) stay per-plugin.

## Purpose

This plugin is the app store. The practice setup is the onboarding recommendation engine — asks what you do, recommends a starter pack, installs what you pick.

Unlike practice setup in the other plugins, this one is short. Five questions, a recommendation, done.

## Install scope check

Before the orientation, if you notice the working directory is inside a project (not the user's home directory), flag it. Say once:

> **Heads up — it looks like this plugin may be project-scoped, which means I can only read files in [current directory]. If you'll want me to read documents from elsewhere (Downloads, Documents, Dropbox), install user-scoped instead. You can continue with project scope, but you'll need to move files into this folder.**

Ask the user to confirm before proceeding: continue with project scope, or pause to reinstall user-scoped.

## Before the interview starts

Show this preamble first (3-4 short lines, nothing more):

> **`strategy-builder-hub` is for finding, installing, and managing community-contributed strategy skills.** Looking for a specific strategy workflow? Install one of the `strategy-*` or consulting plugins directly; run `/strategy-builder-hub:registry-browser` to see what's out there.
>
> **2 minutes** gets you role and engagement type(s) — plus working defaults for registry watchlist, update cadence, and a permissive-by-default allowlist. **15 minutes** adds a calibrated starter pack matched to your engagement type, a trusted-sources policy written to `allowlist.yaml`, update notification preferences, and your industry/team-size signal for recommendations.
>
> Quick or full? (Upgrade any time with `/strategy-builder-hub:practice-setup --full`.)

## After the user picks quick or full

Once the user has picked, orient them. Cover, in your own voice:

- **What this plugin maintains:** your engagement profile (trusted sources, update preferences, deployment context), an `allowlist.yaml` that gates installs, and an install log.
- **What this setup does:** helps the user discover, install, and evaluate community strategy skills — a profile-driven starter pack plus a design-quality check before anything touches their workflow. Learns the engagement profile and update preferences and writes them into a plain-text file the plugin reads from every time. Everything can be changed later.
- **Data sources:** setup builds a fresh engagement profile from the user's answers only. It does not read personal Claude history, other conversations, or the home-directory CLAUDE.md. If something relevant came up earlier in this conversation, ask before folding it in.

**Why this matters.** The hub's starter-pack recommendation and the auto-updater's filtering both read from the profile this interview writes. A generic profile gets a generic starter pack — skills that are plausibly useful but not matched to the user's actual work. Telling the hub what kind of strategist the user is and what they do most is what makes the difference between "here are all the skills other strategists have built" and "here's the set that matches your work."

### Quick start or full setup — branching

The user picked quick or full in the preamble. Branch:

**Quick start path:** ask only role and engagement type(s). Write the config with `[DEFAULT]` markers on everything else. Close with: "Done. You can start browsing and installing now. I've used sensible defaults for registry watchlist and update cadence. Run `/strategy-builder-hub:practice-setup --full` anytime to do the whole interview, or `/strategy-builder-hub:practice-setup --redo <section>` to re-do one part."

**Full setup path:** the existing interview flow below.

## Interview pacing

- **Assume the answer exists somewhere.** When a question asks for information that's probably written down — org description, engagement scope, escalation matrix, methodology guide — prompt for a link or a paste before asking the user to type it from memory.

Short as this interview is, the five questions vary — engagement type and industry are tap-through, but "what's the thing you do most" needs a real answer. When a question needs more than a quick tap:

- **Ask the question and wait.** Say explicitly: "This one needs a typed answer — I'll wait." Do not move to the next question until the user responds.
- **If anything gets skipped:** "Skip for now and I'll flag it in your profile — you can fill it in with `--redo` later." Then move on, but track the skip.
- **Before writing the profile and recommending a starter pack:** if any answer was skipped or left as a placeholder, list them and ask: "Want to fill any of these now, or leave them as placeholders? Your starter-pack recommendation is only as good as the profile." Then wait.
- **Never** write the profile with silent gaps — every placeholder should be a deliberate skip the user confirmed.
- **Batch size — count subparts.** "Never ask more than 2-3 questions in one turn" means 2-3 *answerable prompts*, counting subparts. Can the user answer without scrolling? If not, it's too many.
- **Pause and resume.** Tell the user up front: "If you need to stop, say 'pause' and I'll save your progress. Run `/strategy-builder-hub:practice-setup` again later and I'll pick up where you left off." When the user pauses, write a partial configuration with a `<!-- PAUSED -->` comment at the top and `[PENDING]` markers on unanswered fields. When setup re-runs and finds a paused config, greet the user: "Welcome back. You paused at [section]. Your earlier answers are saved. Pick up where we left off, or start over?"

## The interview

### Opening

> I'll help you find and install community strategy skills — things other strategists have built and shared. First, what kind of strategy work do you do? I'll recommend a starting pack.

### Part 0: Who's using this, and what's connected

Two quick questions before the engagement profile. These shape how the plugin works, not what it can do.

#### Who's using this?

> Who'll be using this plugin day to day? (This feeds the Role signal carried across every plugin you install — skills with non-strategist mode read from here instead of re-asking.)
>
> 1. **Strategy practitioner or consultant** — a strategist, management consultant, or strategy professional.
> 2. **Non-strategist with practitioner access** — a founder, product lead, operations manager, or business lead; you have a strategy team or consultant you can consult.
> 3. **Non-strategist working independently** — you're handling this yourself without direct access to a strategy professional.

If the answer is 2 or 3, say this once:

> This plugin discovers and installs skills. Skills you install will have their own guardrails based on your role — I'll carry your answer here forward so you don't have to answer it per plugin.

#### What's connected?

> This plugin can work with: Slack (for new-skill / update notifications). Let me check which connectors you have configured — features that need them will work, and features that don't have them will fall back to manual gracefully instead of failing silently.

**Check what's actually connected, not what's configured.** A connector listed in `.mcp.json` is *available*. A connector that's actually responding is *connected*. For each connector this plugin uses:

- If you can test the connection (call a simple MCP tool like a list or search), report ✓ only on a successful response.
- If you can't test (no way to probe from here), report ⚪ "configured but not verified" with a one-line how-to.
- Never report ✓ based on configuration alone.

Then report findings in this form:

> - ✓ [Integration] — connected (tested)
> - ⚪ [Integration] — configured but not verified.
> - ✗ [Integration] — not found. [Feature] will fall back to [manual alternative]. [How to connect.]

Write Part 0 answers to the plugin config under `## Who's using this` and `## Available integrations`.

Before the five questions: "Do you already have a list of community-skill registries you watch, or an allowlist / blocklist of skill sources your team uses? Paste the contents, share a file path, or say 'no' and I'll add the default. If you share one, I'll read it and add those registries plus your allowlist to the profile rather than making you re-type them."

**Deployment context.** After the allowlist question and before writing the file, ask:

> "How are you going to use the skills you install — just for yourself, shared across your firm, or embedded in a product or service you ship to others? (Personal / Firm-internal / Product-embedding.) This sets your license defaults."

Record the answer in the profile under `## Sources I trust` as `Deployment context: [personal | firm-internal | product-embedding]`.

**Write the allowlist to `allowlist.yaml`.** The installer's gate reads from `~/.claude/plugins/config/claude-for-strategy/strategy-builder-hub/allowlist.yaml`, not from CLAUDE.md.

1. Write `allowlist.yaml` at the config path, following the schema in `skill-installer/references/allowlist.md`:
   - `mode:` — the template default is `restrictive`. Offer `permissive` for Solo/small team. Keep `restrictive` for Midsize/large firm. Always confirm: "I'm setting the allowlist to [mode]. Restrictive refuses unknown sources until you add them. Permissive flags unknown sources and asks you before installing. Which do you want?" Never write permissive without explicit user consent.
   - `registries:` — what the user provided.
   - `publishers:` — GitHub owners/orgs the user named or that own the trusted registries.
   - `connectors:` — empty unless the user provided a list; in restrictive mode, prompt: "Restrictive mode needs a connector allowlist — paste approved MCP server URLs, or I'll leave it empty and skills declaring any connector will be refused."
   - `licenses:` — seed based on the deployment-context answer:
     - **Personal** → `MIT`, `Apache-2.0`, `BSD-2-Clause`, `BSD-3-Clause`, `ISC`, `CC0-1.0`.
     - **Firm-internal** → same as Personal plus `LGPL-2.1-only`, `LGPL-3.0-only`, `MPL-2.0`.
     - **Product-embedding** → same as Personal plus a top-of-file comment: `## License review required before shipping.`
2. Also summarize in the profile's `## Sources I trust` section.
3. Tell the user where it lives: "Your allowlist is at `~/.claude/plugins/config/claude-for-strategy/strategy-builder-hub/allowlist.yaml`. The installer reads it before fetching anything."

**Freshness reminders.** After the allowlist question, ask:

> "When a community skill bundles reference material — market frameworks, benchmarks, industry data — how long should it be trusted before I remind you to verify it's still current? (6 months is a common default for market/competitive content. 12 months for methodological/framework content. Set it tighter if you work in a fast-moving area.)"

Accept either a single number or per-category answers. Validate each answer shapes to `N days`, `N months`, or `N years` with `N` a positive integer ≤ 120.

Write the answer to a `## Freshness reminders` section in the profile:

```markdown
## Freshness reminders

| Content category | Max age before reminder | Rationale |
|---|---|---|
| market-data | 6 months | Markets and competitive landscapes shift quickly |
| methodology | 12 months | Frameworks and methodologies evolve slower |
| benchmarks | 6 months | Industry benchmarks update annually at most |
| unknown | 3 months | A skill that doesn't declare freshness is treated cautiously |
```

### The five questions

1. **Engagement type** — Corporate strategy, management consulting, market intelligence, transformation, operating model, performance management, OKR planning, PMO, something else? (This feeds /strategy-builder-hub:related-skills-surfacer — the engagement type is the primary key that maps to the starter pack.)

   **Engagement types that don't fit the boxes.** If the user's work doesn't match the options (public sector strategy, PE/VC portfolio support, academic research, non-profit strategy, or anything else the standard categories assume away), offer: "It sounds like your work doesn't fit my usual categories. Tell me about it in your own words — what you do, who for, what markets and contexts, what the work looks like — and I'll build your profile from that instead of forcing you into boxes that don't fit." Then build the profile from the free-form description, flagging which template fields were filled, adapted, or left empty.

2. **Industry** — Tech, healthcare, finance, consumer, industrials, other, doesn't matter? (This feeds /strategy-builder-hub:related-skills-surfacer and /strategy-builder-hub:registry-browser — industry narrows the starter pack and filters registry results.)

3. **Team size** — Solo consultant, small team (2-5), large strategy department? (This feeds the `allowlist.yaml` mode default — Solo/small gets permissive, Midsize/large gets restrictive.)

4. **What's the thing you do most?** — Market sizing, competitive analysis, strategic planning, business case development, operating model design, KPI frameworks, executive presentations, etc. (This feeds /strategy-builder-hub:related-skills-surfacer — the surfacer nudges you when you're doing something the community has a skill for.)

5. **Tooling comfort** — Builder (you write your own skills), tinkerer (you edit what's installed), just-make-it-work (you want it to work out of the box)? (This feeds /strategy-builder-hub:related-skills-surfacer — builders get the raw registries and /strategy-builder-hub:skills-qa framework; just-make-it-work gets a curated, working pack.)

### Recommend

Map the profile to registry skills:

| Profile | Starter pack |
|---|---|
| Corporate strategy, in-house | corporate-strategy plugin + any community strategic-planning skills |
| Management consulting | consulting plugin + community market-sizing or deck-building skills |
| Market intelligence | market-intelligence plugin + community competitive-research skills |
| Transformation lead | transformation plugin + community change-management skills |
| PMO / performance | pmo + performance plugins + community OKR or roadmap skills |
| Builder | the raw registries and the skills-qa framework — they'll build and validate their own |

For each recommended skill: show the SKILL.md description. Let them pick — don't install anything without a yes.

## Writing the engagement profile

Short. Profile + installed list + registry prefs. Per the template at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`.

## After writing

**Show what this plugin can do.** Before closing, offer:

> **Want to see what I can help with?**

If yes, show this tailored list:

> **Here's what I'm good at in strategy skill management:**
>
> - **Browse community strategy skills** — e.g., "See what other practitioners have built for your engagement type." Try: `/strategy-builder-hub:registry-browser`
> - **Install a skill from a registry** — e.g., "Add a community skill to your environment — license-gated and allowlist-checked before it runs." Try: `/strategy-builder-hub:skill-installer`
> - **Check for updates** — e.g., "See which installed skills have newer versions in their source registry." Try: `/strategy-builder-hub:auto-updater`
> - **Get skill recommendations** — e.g., "Based on recent activity in your other plugins, surface skills worth trying." Try: `/strategy-builder-hub:related-skills-surfacer`
> - **Evaluate a skill against the design framework** — e.g., "Run the Strategy Skill Design Framework on a skill — thirteen design parameters, three failure modes, a trust-surface check." Try: `/strategy-builder-hub:skills-qa`
>
> **My suggestion for your first one:** Browse the registry and pick one skill that matches a current engagement — install it and see how the allowlist gate feels. Or tell me what's on your plate and I'll pick.

Then close with the "you can change anything later" note:

> Done. Your configuration is at `~/.claude/plugins/config/claude-for-strategy/strategy-builder-hub/CLAUDE.md` — a plain text file you can read and edit directly. Anything you answered can be changed:
>
> - Edit the file directly for a quick change
> - Run `/strategy-builder-hub:practice-setup --redo` for a full re-interview
> - Run `/strategy-builder-hub:practice-setup --check-integrations` to re-check what's connected
>
> The things most commonly tweaked later: your watched registries (add or drop sources), your update preference (notify vs. manual), and the scope of your engagement profile (add an industry or a second engagement type as your work shifts). Your configuration will improve as you use the plugin — if recommendations feel off, the profile is usually the fix.

## Your engagement profile learns

After writing the engagement profile, close with this note:

> **Your engagement profile learns.** It gets better as you use the plugins:
>
> - When a skill's output feels off, that's usually a position to tune. The output will tell you which one.
> - You can always say "update my profile to prefer X" or "change my escalation threshold to Y" and the relevant skill will write the change.
> - Run `/strategy-builder-hub:practice-setup --redo <section>` to re-interview one part, or edit the config file directly.
>
> Ten minutes of setup gets you a working profile. A month of use gets you one that reads like you wrote it yourself.

## Registries watched by default

No default registries are pre-configured. Add registries you trust via `/strategy-builder-hub:registry-browser` or by editing your allowlist directly.

## Worked example

**Input:** Corporate strategist, mid-size firm, picks two registry skills from starter recommendations.

**Expected output:** Profile written to config path; installed table updated; integration table with probed statuses.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `registry-browser`, `skill-installer`, or `--check-integrations`.
