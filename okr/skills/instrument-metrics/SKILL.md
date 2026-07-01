---
name: instrument-metrics
description: >
  This skill should be used when the user asks to "instrument this KR,"
  "where does this metric actually come from," or needs each key result
  mapped to an exact, reproducible measurement spec — formula, source,
  owner, refresh cadence.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.3.0"
  owner: "okr practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Instrument Metrics

## When to use

Map each KR to a measurement spec precise enough two people calculate the same number — with cross-plugin handoff to `performance` when installed.

## What this skill does not do

- **Does not duplicate `performance:metrics-glossary`** when performance plugin installed — mapping only.
- **Does not set targets** — route to `/okr:set-targets` after baselines known.
- **Does not invent data sources** — flag unknowns for user input.

## Preconditions

| Input | If missing |
|---|---|
| KRs to instrument | Ask user to provide |
| Practice profile (performance plugin status, check-in frequency) | Detect performance plugin; flag `[PROVISIONAL]` on cadence match |

## Provisional mode

Ambiguous formulas: flag **AMBIGUITY FLAGS** — do not pick calculation method silently.

## Trust spine

- **Confidence bands** (`structured-aggregation`):
  - **High:** Every KR mapped; formula/source/owner/cadence complete or deferred to performance with explicit handoff.
  - **Medium:** Some ambiguities flagged; cadence mismatches noted.
  - **Low:** KRs without measurable spec — halt target-setting.
- **Failure modes:**
  - **Strategic advice vs. support:** Spec is draft for data owner validation.
  - **Client confidentiality:** Metric definitions may expose internal systems — CONFIDENTIAL header.
  - **Accountability gap:** Owner named per metric; ambiguities flagged not hidden.
  - **Analytical Rigor:** Completeness check — every KR has mapping or explicit gap.
  - **Incentive Gaming:** N/A — definition focus.
- **Escalation triggers:** Check-in frequency faster than metric refresh — flag mismatch blocking reliable pulse.

## Workflow

1. **Read practice profile** for `performance` plugin status.
2. **If performance installed:** KR-to-metric mapping only; defer definition to `performance:metrics-glossary`.
3. **If performance not installed or metric new:** full spec — formula, source, owner, refresh, caveats.
4. **Cadence match check** — check-in frequency vs. metric refresh.
5. **Flag ambiguous formulas** — do not pick silently.
6. **Completeness/source-tag check** before output.

## Output format

```
CONFIDENCE: [defensible recommendation | structured first pass]
KR: [text]

[If performance installed:]
  Mapped metric: [name] — full definition owned by performance:metrics-glossary
  Cadence match: [ok | mismatch — explain]

[If performance not installed, or metric is new:]
  Formula: [exact calculation]
  Source: [system/sheet/table]
  Owner: [name/role]
  Refresh: [cadence]
  Cadence match: [as above]
  Caveats: [...]

[repeat per KR]

AMBIGUITY FLAGS: [any KR where metric admits more than one calculation method]
```

## Worked example

**Input:** KR "Enterprise NPS ≥ 50." Performance plugin installed. Weekly check-ins. NPS refreshes monthly in CRM.

**Expected output (excerpt):**

```
KR: Enterprise NPS ≥ 50
  Mapped metric: Enterprise NPS — full definition owned by performance:metrics-glossary
  Cadence match: mismatch — weekly check-in vs. monthly refresh [review]

AMBIGUITY FLAGS: none
```

## Quality checks before delivering

- [ ] Performance handoff respected when plugin installed
- [ ] Full spec when performance not installed
- [ ] Cadence match checked per KR
- [ ] Ambiguities flagged, not silently resolved
- [ ] Every KR covered

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/okr/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/okr:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `performance:metrics-glossary`, `set-targets`, or resolve cadence mismatch.
