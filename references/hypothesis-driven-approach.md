# Hypothesis-Driven Approach — Condensed Reference

The governing convention behind `hypothesis-tree` and `workplan-builder`.

## Core principle

Don't start analysis by gathering all available data and seeing what it says. Start by proposing the most likely answer (a hypothesis), then design the minimum analysis needed to prove or disprove it. This is faster than exhaustive analysis and forces clarity about what would actually change the recommendation.

A hypothesis is **falsifiable**: a specific, testable claim about the answer — not a topic or a question.

- Weak (a topic): "Look into pricing."
- Weak (a question): "Is pricing a problem?"
- Strong (a hypothesis): "Churn is driven primarily by price increases in the mid-tier, not by competitor switching."

## Building the hypothesis tree

1. **Root hypothesis** — the proposed answer to the overall question, stated as a single falsifiable claim.
2. **Sub-hypotheses** — break the root into the 3-5 MECE claims that, if each were tested, would collectively prove or disprove the root. Same grouping discipline as the Minto key line — see `mece.md` and `minto-pyramid.md`.
3. **Evidence needed** — for each sub-hypothesis, name the smallest piece of evidence that would meaningfully move it toward "true" or "false." Favor evidence that's fast and cheap to get over evidence that's merely thorough.
4. **So-what per branch** — for each sub-hypothesis, state what changes about the recommendation if it turns out true vs. false. If the answer is "nothing changes either way," the branch doesn't belong in the tree — cut it.

## From tree to workplan

A hypothesis tree describes *what* needs to be tested. A workplan describes *how* and *by whom*. The translation is mechanical:

| Tree element | Workplan column |
|---|---|
| Sub-hypothesis | Hypothesis |
| Evidence needed | Analysis / data source |
| — | Owner |
| — | Timeline |
| So-what per branch | Expected so-what (stated *before* doing the analysis, so you can check afterward whether the result actually changed anything) |

Writing the expected so-what before the analysis is the discipline that prevents "interesting but inconclusive" workstreams — if you can't articulate in advance what a result would mean, the analysis isn't ready to start.

## Common failure modes to flag

- **Hypotheses that are really just topics** — "investigate competitive dynamics" is not falsifiable; "we are losing share specifically to Competitor X's bundle pricing" is.
- **Evidence requests bigger than the question warrants** — defaulting to a full market study when a back-of-envelope estimate would settle the sub-hypothesis.
- **Missing or vague so-what** — a workstream with no stated consequence for either outcome is busywork, not analysis.
- **Non-MECE branches** — sub-hypotheses that overlap, or a root hypothesis that doesn't logically follow from disproving/proving all its branches.

## Quick self-check

1. Is every node a falsifiable claim, not a topic or a question?
2. Are sub-hypotheses MECE relative to the root?
3. Does each branch have a stated "expected so-what" for both outcomes?
4. Is the evidence requested the *smallest* thing that would move the needle, not the most thorough?
