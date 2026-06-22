# MECE — Condensed Reference

The grouping discipline behind every leveled structure in this plugin set — Minto key lines, hypothesis trees, BLUF "why" sections, KPI driver trees, and structural review. See `minto-pyramid.md` for how MECE fits inside the pyramid; this file is the full version of the grouping rule itself.

## What it means

**MECE** = **Mutually Exclusive, Collectively Exhaustive**.

A set of sibling items at one level is MECE when:

1. **Mutually exclusive** — no two items cover the same ground. If a fact or sub-issue could plausibly sit under more than one item, the items overlap and the structure is wrong — merge, split, or redraw the boundary.
2. **Collectively exhaustive** — together, the items account for everything that matters at that level relative to their parent. If the reader can think of a material factor that doesn't fit any item, something is missing — add a bucket or explicitly mark it as out of scope.

MECE applies **relative to a parent**: the key line is MECE relative to the governing thought; support under each key line point is MECE relative to that point; sub-hypotheses are MECE relative to the root hypothesis.

## Why it matters

Non-MECE structures look organized but aren't. Overlapping points make the argument feel repetitive without adding proof; gaps leave the reader unsure whether you've considered what they care about. MECE forces explicit choices about what belongs where — which is most of the work in structuring strategy work.

MECE is a **design constraint**, not a claim of perfect completeness. "Collectively exhaustive" means exhaustive **for the purpose at hand** given what the reader needs to decide. It's fine to scope a parent narrowly ("reasons to act *this quarter*") as long as the scope is stated and the key line covers that scope.

## The two tests (run separately)

### Mutual exclusivity test

For each pair of sibling items A and B, ask: **could the same fact, risk, driver, or sub-claim legitimately belong under both?**

- **Yes → overlap.** Fix by merging the items, splitting one into finer points, or redrawing the grouping dimension (e.g. you mixed "by stakeholder" and "by time horizon" in one list).
- **Borderline → suspicious.** Items that are "different in wording but same in substance" fail too — "cost pressure" and "margin compression" are often one point.

### Collective exhaustiveness test

Ask: **relative to the parent, is there a material factor a skeptical reader would expect to see that doesn't fit any sibling?**

- If yes, add a bucket, expand scope, or **explicitly call out the gap** ("we are not addressing X in this memo because..."). Unmarked gaps read as blind spots.
- If you're adding a catch-all ("other," "miscellaneous," "various"), the structure probably isn't MECE — you've given up on grouping. Revisit the dimension.

## Practical grouping dimensions

Pick **one primary dimension per sibling set**. Common choices:

| Dimension | Example parent | MECE siblings |
|---|---|---|
| Causal drivers | "Why revenue is down" | Volume, price, mix, churn — not "competitors" and "pricing" if pricing is already a driver |
| Options | "How to close the gap" | Build, buy, partner — each exclusive, cover the decision space |
| Time | "What happens next" | Now, next quarter, beyond — boundaries explicit |
| Stakeholder | "Who is affected" | Customer, employee, shareholder — watch for overlap across groups |
| Geography / segment | "Where the problem shows up" | Regions or segments that partition the whole |

When 3-5 items don't come cleanly MECE on one dimension, you may have two problems jammed together at the parent level — split the parent before forcing MECE on the children.

## Common failure modes to flag

- **Same point, different words** — two siblings restate each other; merge.
- **One sibling is really two** — "pricing and product quality" is two points; split or pick the dimension.
- **Mixed dimensions in one list** — three causes and one random recommendation at the same level.
- **Catch-all bucket** — "other risks" instead of naming what "other" contains.
- **False exhaustiveness** — list looks complete but omits the factor the audience cares most about (often cost, risk, or timing).
- **Over-splitting** — six near-identical points that should be three; MECE doesn't require maximizing count, it requires clean boundaries. **3-5 siblings** is the usual sweet spot.

## Quick self-check

1. Can I state the **one grouping dimension** this sibling set uses?
2. Does **every pair** pass the mutual exclusivity test — no shared substance?
3. Would a **skeptical reader** name a material missing bucket? If yes, is it added or explicitly scoped out?
4. Are there **3-5 siblings** (or fewer with good reason), not a laundry list?
5. At the next level down, is **each subtree** MECE relative to its own parent (not just the top level)?

## Where this shows up

- **`narrative-builder` / `deck-outline` / `exec-memo`** — MECE key line and BLUF "why" sections (`minto-pyramid.md`, `bluf-conventions.md`)
- **`hypothesis-tree` / `workplan-builder`** — MECE sub-hypotheses (`hypothesis-driven-approach.md`)
- **`doc-reviewer`** — explicit MECE test on the supporting structure
- **Other plugins** — condensed inline MECE (e.g. `performance:kpi-tree-builder`, `transformation:tech-strategy-brief`) when `consulting` isn't installed
