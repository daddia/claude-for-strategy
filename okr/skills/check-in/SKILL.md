---
name: check-in
description: >
  This skill should be used when the user asks to "do a check-in on our
  KRs," "what's our confidence on this objective," "update our OKR
  status," or needs a confidence-based pulse logged for one or more key
  results — distinct from a project status report, which this is not.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Check-In

A confidence pulse, not a status update. The difference matters: a status update reports what happened ("we shipped X"); a confidence check asks the owner to commit to a number — "given everything you know right now, what's your honest percentage chance of hitting this target by cycle end?" — which surfaces doubt early, before it becomes a missed target. This skill also persists an append-only log, the same convention as `pmo:raid-log` and `pmo:decision-log`.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for check-in frequency and the scoring scale.

2. **Get the current check-in log** (file or pasted content) if one exists — this skill appends, it doesn't restart the log each cycle.

3. **For each KR due for a check-in, get**:
   - A confidence rating (default scale: 0-100% likelihood of hitting target by cycle end, unless the profile records a different convention).
   - A one-line "what changed since last check-in" note — required, not optional; a confidence number with no explanation of *why* it moved (or didn't) is hard to act on later.

4. **Flag staleness**: any KR with no logged check-in for more than one cycle past the practice profile's frequency.

5. **Flag flat confidence**: a KR whose confidence rating hasn't moved across 3+ consecutive check-ins. This usually means one of two things — either no real progress is happening, or nobody's actually engaging with the question and just re-entering the same number. Flag it as worth a direct conversation either way, don't guess which.

6. **Flag sharp drops**: a confidence rating that falls significantly since the last check-in is the earliest possible warning a target is in trouble — surface it prominently, don't bury it in the log update.

7. **Output the full updated log**, appending new entries — same append-only discipline as the rest of this repo's persisted logs.

## Output format

```
[Full check-in log, existing entries unchanged]
NEW ENTRIES:

KR: [text]

Confidence: [X%] (previous: [Y%])

What changed: [one line]

Flag: [none] or [stale — no check-in logged for N cycles] or

[flat — unchanged across 3+ check-ins] or

[sharp drop — escalate]
[repeat per KR checked in this round]

```

## Note

This skill's logic is also shipped as a scheduled agent — see `agents/check-in-nudge.md` — so check-ins can happen on a cadence without someone remembering to ask for them.