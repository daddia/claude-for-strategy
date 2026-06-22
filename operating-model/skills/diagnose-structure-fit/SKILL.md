---
name: diagnose-structure-fit
description: >
  This skill should be used when the user asks "is our structure right for
  our strategy," "should we reorganize," "why does coordination feel so
  slow," or needs the current or proposed structure tested against the
  actual coordination need the strategy requires.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Diagnose Structure Fit

A structure is only "right" relative to a specific coordination need — there's no universally best org chart. This skill tests fit against what the strategy actually requires, and separately flags the most common reason structures drift away from that: being shaped by who currently reports to whom rather than by the work itself.

## Process

1. **Read the practice profile** (`../../CLAUDE.md`) for what the structure is meant to optimize for.

2. **State the coordination need precisely** — does the strategy require fast cross-functional decisions, deep functional expertise concentrated in one place, tight local responsiveness across markets, or centralized control for consistency? Most real strategies need more than one of these in different places; identify where each applies rather than picking one for the whole org.

3. **Test the current/proposed structure against that need, by area.** A strict functional hierarchy with no integrating mechanism is a mismatch for an area needing fast cross-functional decisions — name the specific mismatch, don't just assert "the structure feels wrong."

4. **Run the blank-page test on the structure itself**: if this org were designed today from scratch around the actual work and coordination needs — with no regard for who currently holds which title — would it look like this? If a structure persists mainly because it mirrors the current leadership team's personalities or political balance rather than the work, name that directly. This is uncomfortable to say plainly and is exactly why it's worth saying plainly.

5. **Recommend specific structural changes** where mismatches were found — not a full redesign by default, targeted fixes to the areas where fit actually breaks down.

## Output format

```
STRATEGIC PRIORITY: [what the structure should optimize for]

AREA: [function/business line] — Coordination need: [...]
  Current structure: [...] — Fit: [match / mismatch — specifics]

[repeat per area]

BLANK-PAGE TEST: [would this look the same designed fresh around the work? yes/no — if
  no, name what's actually driving the current shape]

RECOMMENDED CHANGES: [targeted, by area]
```
