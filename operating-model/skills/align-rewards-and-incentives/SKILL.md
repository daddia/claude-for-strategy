---
name: align-rewards-and-incentives
description: >
  This skill should be used when the user asks "will this reorg actually
  stick," "does our reward system support the structure we want," "why are
  people still behaving the old way after the reorg," or needs the
  proposed or current structure checked against rewards, process, and
  people capability for genuine alignment — the Star Model integration
  check.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Align Rewards and Incentives

Structure is the cheapest of the four things that actually determine how an org behaves — drawing new boxes is easy. This skill checks the three things that are harder to change and that determine whether the new boxes mean anything: whether the reward system reinforces the structure's intent, whether existing processes still assume the old structure, and whether the org has people with the capabilities the new structure assumes.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for how people are actually measured and paid.

2. **State the structure's intent plainly** — what behavior is the new or current structure meant to produce (e.g., cross-functional collaboration, faster local decisions, deeper specialization).

3. **Check the reward system against that intent.** Apply the same incentive logic as `market-intelligence:map-incentives`, pointed internally: if the structure is meant to produce cross-functional collaboration but individual metrics and bonuses remain entirely siloed, predict — explicitly — that people will keep behaving like the old structure regardless of the new chart, because the reward system still pays them to. Don't soften this into "may face some friction"; if the incentive misalignment is real, state plainly that the reorg will likely fail to change behavior without a reward change.

4. **Check process fit** — do existing approval chains, planning cycles, or systems still assume the old structure (e.g., a budget process that only knows how to allocate by the old divisional lines)? Name specific processes that would create friction against the new structure if left unchanged.

5. **Check people/capability fit** — does the org currently have people with the skills the new structure assumes (e.g., a move to a more autonomous team structure assumes managers who can coach rather than direct — does that capability exist, or is it assumed)? Flag the gap rather than assuming capability will simply appear because the structure now requires it.

6. **Recommend the specific reward, process, or capability changes needed** to make the structure change real — a structure recommendation with no corresponding changes here should be flagged as incomplete, not shipped as if structure alone will do the work.

## Output format

```
STRUCTURE'S INTENT: [what behavior this is meant to produce]

REWARD FIT: [supports / undermines] — [specific mechanism, and predicted behavior if unchanged]
PROCESS FIT: [specific processes still assuming the old structure, if any]
PEOPLE/CAPABILITY FIT: [capability the new structure assumes — present / gap]

RECOMMENDED CHANGES (beyond the org chart): [reward, process, capability — specific]

VERDICT: [structure change alone is sufficient] or [structure change will likely NOT
  produce the intended behavior without the changes above — be direct about this]
```
