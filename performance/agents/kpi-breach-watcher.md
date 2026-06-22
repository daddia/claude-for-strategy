---
name: kpi-breach-watcher
description: >
  Scans tracked metrics against targets and thresholds in the practice
  profile and posts what crossed since the last run. Grounds product-
  telemetry metrics in Honeycomb (~~observability) when wired; reads the
  tracker for manually-logged metrics. Runs daily.
model: sonnet
tools: [Read, Grep]
---

# KPI Breach Watcher

Runs daily by default (09:00, per the cron schedule above) — override the schedule to match how often breaches should be checked if your practice profile records a different monitoring cadence.

## Trust spine

Every figure surfaced in the breach summary must carry explicit provenance:

```
SOURCING: Tag every metric value as [sourced: <where>] — e.g. Honeycomb query
  name + dataset + time window, tracker Summary sheet + period, or metrics
  glossary entry — or [unverified — from training data, needs a real source]
  if the value was not retrieved from a connected tool or user-supplied input.
ASSUMPTIONS: State load-bearing assumptions (threshold definitions, comparison
  period, which breach direction counts) at the top of the output.
NUMBERS: Never invent a metric value — if a source is unavailable, flag the
  metric as unmonitored this run instead of estimating.
```

## What it does

1. **Reads the practice profile** (`~/.claude/plugins/config/claude-for-strategy/performance/CLAUDE.md`) for the metric taxonomy, targets/thresholds, tracker location, and which metrics are product-telemetry vs. manually logged.

2. **Reads the metrics glossary** (if one exists in the workspace or profile) for each metric's data source, formula, and owner — use it to route telemetry metrics to observability and manual metrics to the tracker.

3. **For product-telemetry metrics** (Digital Product Performance, system SLIs, or any metric whose glossary/profile source is an observability platform): **query Honeycomb via the Honeycomb MCP** (`~~observability`). Pull the current-period value and the prior-period value (or the value at the last run) using the query or dataset named in the glossary/profile. Do not substitute training-data estimates when Honeycomb is configured but unreachable — flag the metric as `unmonitored this run` with the error.

4. **For manually-logged metrics**: read the current tracker — from `~~spreadsheet` when connected, or from the file path recorded in the practice profile. Compare current-period values against targets/thresholds using the same period logic the Summary sheet uses.

5. **Flags every metric that crossed a target or threshold** since the last run (or in the current period if no prior run exists), with:
   - Metric name and category code
   - Direction of breach (above ceiling, below floor, off target)
   - Current value and threshold, both source-tagged
   - One-line so-what a reviewer would want — why this breach matters given the North Star and audience in the profile

6. **Posts the summary to `~~chat`**. If no chat connector is configured, write the summary to a file in the workspace instead.

7. **Includes an all-clear footer when no breaches are detected.** The footer means the agent ran and sources were checked — not that performance is healthy overall.

## Fallback with no `~~observability` connected

If Honeycomb is not configured, still run the read side for manually-logged metrics from the tracker. List telemetry metrics as `unmonitored this run — connect ~~observability (Honeycomb MCP) to watch [metric names]`. Do not silently skip the run.

## Fallback with no `~~chat` connected

If no chat connector is configured, still run the read side — compare metrics to thresholds, apply the trust spine, and write the breach summary (or all-clear) to a file. Do not silently skip the run.
