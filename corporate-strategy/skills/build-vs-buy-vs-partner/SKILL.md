---
name: build-vs-buy-vs-partner
description: >
  This skill should be used when the user asks "should we build this,
  acquire it, or partner for it," has a capability gap that needs a
  build/buy/partner decision, or wants that decision checked against the
  known failure pattern each path tends toward.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
---

# Build vs. Buy vs. Partner

Each path has a well-known way it tends to go wrong, and the failure pattern is rarely the one being discussed when the decision is made. This skill forces each path's specific risk into the conversation rather than letting the decision get made on cost comparison alone.

## Process

1. **State the capability gap precisely** — what's missing, and why it matters to the strategy (if it doesn't clearly connect to a strategic priority, question whether it's worth closing at all before evaluating how).

2. **Test whether this is core or commodity.** A genuinely differentiating capability that competitors can't easily replicate is a stronger build case; a commodity capability available externally at good quality is a weaker one — name which this looks like, and don't let "we could probably build it" substitute for "we should."

3. **Evaluate Build** against its known failure pattern: building systematically underestimates both time and cost, especially outside the org's core competency. Ask for the team's track record on past build estimates — if there's a history of overrun, apply a haircut to this estimate too rather than treating it as independent.

4. **Evaluate Buy** against its known failure pattern: acquisitions systematically overestimate synergy capture and underestimate integration cost and culture risk. If this path is live, hand off to `synergy-stress-test` for the synergy case specifically rather than re-deriving that discipline here.

5. **Evaluate Partner** against its known failure pattern: partnerships underestimate governance complexity while running and exit difficulty when they end. Ask directly: what happens when this partnership needs to end — is there an exit mechanism, or is the assumption that it'll just continue indefinitely?

6. **Recommend**, stating which failure pattern is most likely to bite for this specific case and what would mitigate it if the recommended path is chosen anyway.

## Output format

```
CAPABILITY GAP: [what's missing, strategic relevance]
CORE OR COMMODITY: [which, and why]

BUILD: [time/cost estimate] — Failure pattern risk: [org's build track record] — Haircut applied: [if any]
BUY: [headline terms] — Failure pattern risk: [defer to synergy-stress-test if live]
PARTNER: [structure] — Exit mechanism: [exists / does not exist — flag if not]

RECOMMENDATION: [build | buy | partner] — [most likely failure pattern for this path, and mitigation]
```
