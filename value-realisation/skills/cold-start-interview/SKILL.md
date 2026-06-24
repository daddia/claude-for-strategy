---
name: cold-start-interview
description: >
  This skill should be used when the user runs
  "/value-realisation:cold-start-interview", asks to "set up the
  value-realisation plugin," "teach Claude how we track benefits," or
  wants to redo that setup after the benefits framework, governance
  model, or realisation cadence changes materially.
tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.1.0"
---

# Cold-Start Interview — value-realisation

Writes the practice profile (`~/.claude/plugins/config/claude-for-strategy/value-realisation/CLAUDE.md`) every other skill in this plugin reads. Run this before `benefits-map`, `benefits-register`, `benefits-tracking`, `benefits-recovery`, or `realisation-review` produce tailored output. The baseline-discipline question below matters more than it sounds — get an honest answer before anything else.

## Process

1. **Offer quick vs. full setup** — quick is 4-5 questions with sensible defaults filled in elsewhere; full includes reviewing a seed business case and any existing benefits register or tracker.

2. **Ask about the benefits framework**:
   - Is there a named framework already in use (Cranfield Benefits Management, HM Treasury's five-case model, an internal house framework) — or none yet, in which case this plugin's default chain (enabler → business change → benefit → strategic objective) becomes the working model?
   - What's the benefit type taxonomy — cash-releasing, cash-releasable, non-cash/qualitative, or different labels? Get the org's own terms rather than imposing these three if they already have a convention.

3. **Ask about governance and accountability, directly**:
   - Who normally holds the benefit owner role today — and is it already distinguished from the delivery PM, or does the same person tend to hold both? If the same person holds both, say plainly that this is the most common reason benefits go unfollowed after go-live, and ask whether splitting them is feasible for this org.
   - Who decides whether an at-risk benefit gets more recovery investment versus a write-down? Steering committee, benefit owner alone, a finance gate?
   - Where do recovery decisions get recorded — `pmo:decision-log` if that plugin is installed, or somewhere else?

4. **Ask about baseline discipline, and don't accept a vague answer**:
   - Are baselines normally captured *before* a change goes live, or reconstructed afterward from whatever data exists? Most orgs answer "afterward" honestly if pushed — record this plainly rather than letting the user round up to "before." `benefits-register` needs the true answer to know how hard to flag retrofitted baselines going forward.
   - What's the default measurement source — system of record, manual extract, a survey?

5. **Ask about attribution convention** — does the org normally run anything like a formal counterfactual or control group, or is attribution handled by judgment-based discounting when external factors are in play? Most consultancies and internal teams do the latter; that's a fine answer, just record it so `benefits-tracking` calibrates its attribution language to match.

6. **Ask about cadence**:
   - Typical realisation window length post go-live (6/12/24 months, or varies by initiative).
   - Tracking cadence (monthly, quarterly).
   - What normally triggers a `realisation-review` — end of window, program closure, an annual portfolio cycle?

7. **Ask whether `transformation` and/or `corporate-strategy` are installed** — if so, `benefits-map` should seed directly from `transformation:business-case` or `corporate-strategy:evaluate-strategic-option` output rather than starting blank.

8. **Request seed documents** for the full interview — a prior business case with a benefits section, an existing register or tracker, a past post-implementation review if one exists. Read for vocabulary, taxonomy, and structure, not to copy specific numbers.

9. **Write the practice profile** to `~/.claude/plugins/config/claude-for-strategy/value-realisation/CLAUDE.md`, following the section structure in the in-repo template (`../../CLAUDE.md`). Do not modify the installed plugin's template file. Fill every section. Mark genuinely unanswered items as "no strong preference — will flag baselines and attribution conservatively by default" so downstream skills know to default to caution rather than optimism.

10. **Confirm and summarize**, and tell the user they can edit `~/.claude/plugins/config/claude-for-strategy/value-realisation/CLAUDE.md` directly for small corrections or re-run this interview for a full refresh.
