# Trust Conventions — Condensed Reference

Strategy outputs — business cases, performance narratives, board decks, roadmaps, status reports — often carry dollar figures, market claims, and recommendations that go out under someone's name. This reference is the repo-wide **trust spine**: how to tag what you know, surface what you assume, refuse to fabricate inputs, calibrate confidence honestly, and gate consequential finals.

This file is the canonical full version. Consequential skills carry a condensed inline block of the same five rules so each plugin works without depending on `consulting` being installed. See **Where this shows up** at the end.

**Not a certified methodology.** These conventions make outputs safer to rely on; they do not replace professional judgment, finance sign-off, or legal review where those apply.

---

## 1. Source and provenance tagging

Every market figure, benchmark, competitor claim, and financial number must carry explicit provenance — your equivalent of a citation. Untagged numbers read as verified when they may not be.

### Tags

| Tag | When to use |
| --- | --- |
| `[sourced: <where>]` | The figure or claim comes from a document, dataset, URL, interview, or other traceable input the user or a connected tool provided. `<where>` is specific enough to find again — file name, URL, report title + date, "user message 2026-06-22", not "industry research". |
| `[unverified — from training data, needs a real source]` | The figure or claim is plausible from general knowledge or model training but was **not** grounded in user-supplied or tool-retrieved evidence in this session. |

### Rules

- Tag **at the point of use** — inline on the number or claim, not only in a footnote section.
- One tag per material claim. A paragraph with three dollar figures needs three tags (or a single tag only if all three share the exact same source).
- **Do not upgrade** `[unverified — …]` to `[sourced: …]` without new evidence in the session. Re-stating a number more confidently is not sourcing it.
- Qualitative claims that would change a decision ("market leader," "regulatory risk is low," "competitor X is exiting") get the same treatment as numbers.

### Examples

- "TAM is ~$4.2B `[sourced: Gartner Market Guide for X, 2025, user-uploaded PDF]`."
- "Typical SaaS gross margin is 70-80% `[unverified — from training data, needs a real source]` — replace with your finance team's benchmark before the board pack."
- "Churn improved 2.1pp `[sourced: performance tracker Summary sheet, June 2026]`."

### Common failure modes

- **Naked numbers** — dollar amounts, percentages, or market sizes with no tag.
- **Vague sourcing** — `[sourced: internet]` or `[sourced: research]` with nothing to retrieve.
- **Implied verification** — "according to industry standards" without a real source when the figure is actually from training data.

---

## 2. Assumptions surfaced

Roadmaps, target operating models, business cases, and transformation plans rest on assumptions. Load-bearing ones must be visible **before** the reader reaches the recommendation — not buried in an appendix.

### Load-bearing assumptions

An assumption is **load-bearing** when the recommendation, timeline, or financial case would materially change if the assumption were wrong. Examples: adoption rate, cost of a platform migration, regulatory timeline, sponsor availability, baseline metric, discount rate, headcount for a new function.

### Required block

At the **top of the output** (immediately after the title or BLUF bottom line, before detailed analysis), include:

```
LOAD-BEARING ASSUMPTIONS:
- [assumption] — if wrong: [what changes in the recommendation]
- …
```

### Rules

- **Flag, don't fix** — if an assumption is unstated in the input, name it and its impact; do not silently pick a convenient value.
- Distinguish **confirmed** vs **unconfirmed** assumptions: "We assume Q3 budget approval `[unconfirmed — not stated in input]`."
- If there are no load-bearing assumptions (rare for consequential outputs), say so explicitly: `LOAD-BEARING ASSUMPTIONS: None identified — output is descriptive only, not a recommendation.`
- Revisit triggers belong here when relevant: "Assumption: vendor delivers API by March — revisit if not confirmed by [date]."

### Common failure modes

- **Hidden defaults** — a business case built on a 15% efficiency gain that was never discussed.
- **Appendix-only assumptions** — the reader has already accepted the recommendation before seeing what it rests on.
- **Generic assumption lists** — "change management will be hard" without tying assumptions to this initiative's numbers or sequencing.

---

## 3. Numbers provenance — flag, never invent

Never invent a plausible-looking input, placeholder metric, or fake precision. A fabricated TAM or a made-up baseline is the strategy equivalent of an unverified legal cite — it looks authoritative and fails under scrutiny.

### Rules

- If a number is **required** for the output and **not provided**, flag the gap and describe what is needed — do not fill with a round number, industry average, or "typical" value unless tagged `[unverified — …]` and clearly marked as a stand-in for discussion only.
- If a number is **optional** for the structure (e.g. a workplan row's data source), leave it blank or mark `TBD — [what to confirm]` rather than inventing.
- **Derived numbers** are only as good as their inputs. Show the math when material; if an input is unverified, the derived result inherits that uncertainty.
- **Precision honesty** — do not imply false accuracy ("$4,237,891") from rough inputs; use ranges or explicit rounding when appropriate.
- Tables and trackers: every metric column should trace to a **data source** field or an explicit flag that the source is missing.

### What to do instead

| Situation | Action |
| --- | --- |
| User asked for a business case but gave no cost figures | Structure the case; mark cost lines `INPUT NEEDED: [one-time / run-rate / by workstream]` |
| Tracker needs a daily input column | Flag: "Raw input for [metric] not specified — what field or system feeds this?" |
| Benchmark would strengthen the argument but isn't sourced | State the gap; offer `[unverified — …]` only as a discussion placeholder, not as the basis of the recommendation |

### Common failure modes

- **Placeholder realism** — "$2.5M implementation cost" with no source because "it sounds right."
- **Silent rounding** — changing user-provided 847 to 850 without noting it.
- **Invented categories** — new metric taxonomy codes when the practice profile already defines one.

---

## 4. Confidence calibration

Distinguish output the user can **defend as their own judgment** from output that is **structured first pass** — craft scaffolding that still needs their analysis, data, and sign-off.

### Labels

Use an explicit confidence line near the top of consequential outputs (after assumptions or integrated into the header block):

| Label | Meaning |
| --- | --- |
| **Defensible recommendation** | Grounded in user-provided or session-sourced evidence; assumptions are stated; material claims are tagged; a prepared reviewer could explain and support this with the cited inputs. |
| **Structured first pass** | Shape and logic are sound, but material numbers, market claims, or assumptions still depend on unverified or missing inputs — useful for working sessions, not for external distribution without further work. |

### Rules

- Default to **structured first pass** when any load-bearing number or claim is `[unverified — …]` or `INPUT NEEDED`.
- Do not use **defensible recommendation** for board/exec finals unless the user has confirmed they accept the sourcing state (see §5).
- When mixed, the overall label is the **weakest** link: one unverified load-bearing figure → **structured first pass**.
- Confidence is about **epistemic honesty**, not tone — a first pass can still be direct and well-structured.

### Common failure modes

- **False defensibility** — recommendation language ("we should invest $X") while key inputs are invented or unverified.
- **Hedging without labeling** — endless "may/might/could" instead of a clear structured-first-pass stamp.
- **Over-cautious labeling** — marking defensible work as first pass out of habit; if inputs are sourced and assumptions stated, say so.

---

## 5. Board-ready gate

The irreversible-ish action in strategy work is not "send" or "file" — it is **this went to the board, the sponsor, or the exec committee with my name on it.** Final exec- or board-facing versions require explicit confirmation and a reviewer note.

### When the gate applies

Before producing a **final** version of any of the following (or equivalent), stop and confirm:

- Board or exec committee deck or pre-read
- Signed-off business case or investment memo
- External performance or status report
- Steering pack or sponsor-facing roadmap/TOM intended for governance forums

Working drafts, internal iterations, and "for discussion" versions do **not** require the gate — but they should still carry assumptions, sourcing tags, and confidence labels.

### Gate flow

1. **Present a pre-final summary** — what the document recommends, what remains `[unverified — …]` or `INPUT NEEDED`, and the current confidence label.
2. **Ask explicitly** — e.g. "Confirm you want the board-ready final with the sourcing gaps noted below, or pause to fill inputs first?"
3. **Only after confirmation**, produce the final and stamp the **reviewer note** at the top (below title or BLUF):

```
REVIEWER NOTE (board-ready final):
- Confirmed by: [user / role if stated]
- Date: [session date]
- Confidence: [defensible recommendation | structured first pass]
- Not verified in this session: [bullet list of unverified claims, missing inputs, or assumptions marked unconfirmed]
- Reviewer action: [what a human should verify before circulation, if anything]
```

If the user confirms despite gaps, the reviewer note records that — it does not erase the gaps.

### Common failure modes

- **Skipping straight to polish** — beautiful final formatting on unverified numbers.
- **Empty reviewer note** — stamp present but no list of what wasn't verified.
- **Gate on everything** — blocking low-stakes drafts; reserve the gate for consequential external finals.

---

## Condensed inline block (for skills)

Skills that produce consequential output should include this block (or equivalent) in their process section:

```
SOURCING: Tag every market figure, benchmark, competitor claim, and dollar amount as
  [sourced: <where>] or [unverified — from training data, needs a real source].
ASSUMPTIONS: State load-bearing assumptions at the top of the output — flag, don't fix.
NUMBERS: Never invent an input — flag what's needed instead.
CONFIDENCE: Label output defensible recommendation vs structured first pass.
GATE: Before producing the board-/exec-facing final, confirm explicitly and stamp a
  reviewer note recording what wasn't verified.
```

Full rules: `../../references/trust-conventions.md` (consulting) or the repo-root `references/trust-conventions.md` mirror.

---

## Quick self-check

1. Does **every material number or external claim** have `[sourced: …]` or `[unverified — …]`?
2. Are **load-bearing assumptions** at the top, with impact if wrong?
3. Is anything in the output **invented** that should be `INPUT NEEDED` or explicitly unverified?
4. Is the **confidence label** honest given the sourcing state?
5. For a **board/exec final**, was confirmation obtained and a **reviewer note** stamped?

---

## Where this shows up

- **High-trust outputs (inline block required in REF01-02):** `business-case`, `performance-narrative`, `deck-outline`, `exec-memo`, `status-report`, `steering-pack`, `roadmap-builder`, `target-operating-model`, `tech-strategy-brief`, `doc-reviewer`
- **Numbers discipline already partial:** `workplan-builder`, `tracker-builder` — "flag, don't invent" promotes here to repo-wide convention
- **Review pass:** `doc-reviewer` should flag missing tags, hidden assumptions, invented inputs, and finals without a reviewer note
- **Watcher agents:** `market-intelligence:competitive-signal-scan` and other scheduled agents that emit tagged alerts depend on this spine being real
