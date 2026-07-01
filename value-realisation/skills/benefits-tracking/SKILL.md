---
name: benefits-tracking
description: >
  This skill should be used when the user asks to "track this period's
  benefits," "update the register against actuals," "are we actually
  getting the savings we claimed," or needs a periodic remeasurement
  against baseline with an explicit attribution call — distinct from a
  status report, which tracks delivery progress, not realised value.
allowed-tools: Read, Grep, Glob, Write
metadata:
  version: "0.3.0"
  owner: "value-realisation practice"
  review_cadence: "quarterly"
  work_shape: "governance-tracking"
  permission_tier: artefact-writer
  output_class: "tracking-update"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Benefits Tracking

## When to use

Periodic remeasurement with explicit attribution call — not delivery status reporting.

## What this skill does not do

- **Does not fix at-risk benefits** — route AT-RISK/LAPSED to `benefits-recovery`.
- **Does not default to FULLY ATTRIBUTABLE** when data insufficient.

## Preconditions

| Input | If missing |
|---|---|
| Benefits register | Halt |
| Prior tracking log | Start new; note first period |

## Provisional mode

Attribution per profile convention; UNKNOWN when data insufficient.

## Trust spine

Governance-tracking bands; gaming-pattern check on claimed-but-not-remeasured; append-only log.

## Workflow

1. **Read the practice profile** — `~/.claude/plugins/config/claude-for-strategy/org-profile.md` and `~/.claude/plugins/config/claude-for-strategy/value-realisation/CLAUDE.md` — for the attribution convention and tracking cadence, the benefits register, and the prior tracking log if one exists — this skill appends, it doesn't restart the log each cycle.

2. **For each benefit due for tracking, get the current measured value** against its registered baseline and target. When the value comes from `~~bi analytics`, `~~spreadsheet`, or ERP MCP connectors, tag `[sourced: <connector>, <report/metric>, <as-of>]` on the measured figure before attribution.

3. **Run the attribution call, explicitly, before declaring status.** Ask whether a known external or market factor could explain some or all of the movement — a price change, unrelated attrition, a seasonal swing, a separate initiative touching the same number. State one of:
   - **FULLY ATTRIBUTABLE** — no material external factor identified; the movement plausibly reflects the initiative's business change.
   - **PARTIALLY ATTRIBUTABLE** — state the estimated discount and why (e.g. "roughly half the improvement; the other half coincides with a seasonal pattern visible in two prior years' data").
   - **NOT ATTRIBUTABLE** — an external factor plausibly explains the movement; this is not evidence of the benefit realising, regardless of which direction the number moved.
   - **UNKNOWN — DATA INSUFFICIENT** — say so rather than defaulting to fully attributable because that's the more flattering answer.

4. **Flag "claimed but not remeasured"** — any benefit marked on-track or realised this period with no fresh measurement actually taken. This is the most common way a register goes stale: a number gets carried forward by assumption rather than re-checked, and nobody notices until a review much later finds it was wrong for several cycles running.

5. **Status each benefit**: REALISED / ON-TRACK / AT-RISK / LAPSED. A benefit can be ON-TRACK numerically while being FULLY ATTRIBUTABLE, or AT-RISK precisely because this period's movement turned out NOT ATTRIBUTABLE even though the raw number looked fine — state both the number and the attribution call, since either one alone can mislead.

6. **Flag any status transition since last period** (e.g. ON-TRACK → AT-RISK, or the reverse) explicitly — a trend matters more than a single snapshot, and a quiet downgrade buried in a long log is easy to miss.

7. **Route AT-RISK and LAPSED benefits to `benefits-recovery`** rather than just logging the number and moving on — this skill's job ends at an honest status and attribution call, not a fix.

8. **Output the full updated log**, appending new entries — same append-only discipline as the rest of this repo's persisted logs.

## Output format

```
[Full tracking log, existing entries unchanged]
NEW ENTRIES — period: [date/cycle]

BENEFIT: [name]
  Current value: [value] (baseline: [value], target: [value])
  Attribution: [FULLY ATTRIBUTABLE | PARTIALLY ATTRIBUTABLE — discount: ... | NOT ATTRIBUTABLE | UNKNOWN]
  Status: [REALISED | ON-TRACK | AT-RISK | LAPSED]
  Transition: [none] or [changed from [prior status] — flag]
  Remeasurement: [fresh this period] or [FLAG — claimed but not remeasured]

[repeat per benefit tracked this round]

ROUTED TO benefits-recovery: [list of AT-RISK/LAPSED benefits, or "none"]
```

## Worked example

**Input:** Number improved but seasonal pattern explains movement.

**Expected output:** Attribution: NOT ATTRIBUTABLE; Status may be AT-RISK despite favorable number.

## Quality checks before delivering

- [ ] Attribution call before status
- [ ] Remeasurement freshness checked
- [ ] Log appended not overwritten
- [ ] AT-RISK/LAPSED routed to recovery

## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/value-realisation/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/value-realisation:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `benefits-recovery` or next tracking period.
