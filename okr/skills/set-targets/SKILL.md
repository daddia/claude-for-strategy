---
name: set-targets
description: >
  This skill should be used when the user asks to "set targets for these
  KRs," "what should our target be," "calibrate this OKR," or has key
  results that need a baseline, target, commit/aspirational label, and
  scoring formula attached.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Set Targets

The core failure mode: targets set without a stated commitment level, which makes scoring meaningless later — a KR scored at 60% reads as a miss if it was meant to be a commit, and as a healthy stretch if it was meant to be aspirational. Same number, opposite meaning. This skill won't let that ambiguity through.

## Trust spine

```
INCENTIVE GAMING: Guards against sandbagging — targets set so low that hitting
  1.0 is routine, or commit/aspirational labels smuggled to game the scoring
  curve. Sandbagging detection: compare each target to baseline and prior-cycle
  scores in seed data (consistent ~1.0 across KRs is named as a pattern, not
  praised); flag commits with aspirational stretch and aspirational KRs with
  trivial targets barely above baseline.
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent an input — flag what's needed instead.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

Full rules: repo-root `references/trust-conventions.md`.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for the org's philosophy (commit-only vs. mixed) and scoring scale/formula.

2. **For each KR, get an explicit commit-or-aspirational label** — don't infer it from the number. If the practice profile says commit-only, every KR is a commit by definition and the rest of this process is about realism, not stretch calibration.

3. **Set baseline and target explicitly.** If `write-key-results` flagged the baseline as unknown, stop here and route to `instrument-metrics` first — a target against an unknown baseline is a guess wearing a number.

4. **Apply the scoring formula** from the practice profile (default: linear interpolation, baseline = 0.0, target = 1.0) and state it alongside the KR so scoring isn't reverse-engineered later.

5. **Run the calibration check across the set**:
   - For **commits**: is the target realistically achievable with current resourcing, or is it aspirational language smuggled into a commit slot? Flag if so.
   - For **aspirational KRs**: is the target genuinely a stretch (meaningful chance of landing well below 1.0), or is it set just barely above baseline — i.e. dressed up as aspirational but actually trivial? Flag trivial targets explicitly.
   - **Across history** (if the practice profile's seed documents include prior-cycle scores): if this org has consistently scored ~1.0 on most KRs across past cycles, say so directly — that's a sandbagging pattern, not a track record to be proud of, and it's worth surfacing even though it's an uncomfortable thing to point out.

## Output format

```
KR: [text]
  Type: [commit | aspirational]
  Baseline: [value] → Target: [value]
  Scoring formula: [as recorded in practice profile]
  Calibration flag: [none] or [target looks trivial for an aspirational KR] or
                     [target looks unrealistic for a commit] or
                     [baseline unknown — route to instrument-metrics first]

[repeat per KR]

SET-LEVEL PATTERN CHECK: [any history of sandbagging or consistent overreach, if seed data exists]
```
