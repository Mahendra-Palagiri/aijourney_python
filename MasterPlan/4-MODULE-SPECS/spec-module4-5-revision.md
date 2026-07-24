# Spec — Revision passes (Module 1 addition + Modules 4–5 alignment)

> These are the only maintenance tasks on already-built content. Everything else in `4-MODULE-SPECS/`
> is net-new construction.

## R1 — Module 1 addition: the SRS system (do in M1)

**Why:** Module 1 builds retention *artifacts* but no retrieval *schedule* (Gap 19).

**Deliverables (in `Addendum/1-ConsolidationPack/srs/`):**
1. `srs-scheduler.py` — plain-text SM-2 scheduler (~100 lines: parse `Q;A` lines + per-card ease/interval
   state in a JSON sidecar; `review` command shows due cards, records 0–5 grade, reschedules). Building it
   is a Week-1-skills exercise. (Alternative: use Anki and skip the script — learner's choice; the card
   FORMAT is not optional.)
2. `srs-week<X>.txt` for every completed week (3–13 now; every new week on completion) per
   `3-CONVENTIONS.md` §7. Generate with the prompt in `5-AI-WORKFLOW.md` §4.
3. Interview-mode pass over existing question banks: add `⏱️` tags (see conventions §6).
4. Rule added to Module 1 README: *"A week is not Done until its SRS cards exist and are in rotation."*

## R2 — Weeks E–F revision vs completed Week 13 (do at the start of M2)

**Why:** Weeks E–F were drafted before Week 13 was finished; overlap must be cut, not studied twice.
(The original Addendum instruction said "revise Modules 4–5 vs main-course weeks 13–20"; since weeks
14–20 are now absorbed INTO the Addendum — see `1-PROGRAM-MAP.md` §1 — only Week 13 remains to
reconcile, and only weeks E–F touch its territory.)

**Procedure (prompt in `5-AI-WORKFLOW.md` §3):** walk weeks E and F lesson by lesson against the actual
completed Week 13 content; verdict each lesson **KEEP** (pure gap) / **TRIM** (overlap — list surviving
learning goals) / **DROP** (duplicate). Expected outcome: weekE days 1–2 (preprocessing/tokenization,
BoW/TF-IDF) largely TRIM to fast-review status; embeddings onward KEEP. Rewrite the two week READMEs
with verdicts + new day counts. Update `6-MASTER-CHECKLIST.md`.

## R3 — Weeks G–M sanity pass (do lazily, as each week starts)

Weeks G–M no longer collide with a main-course twin, but each was written in June 2026. On starting a
week: 15-minute currency check — are named tool versions still right? do datasets still exist? Fix
in-place, note changes in `Addendum/0-Prerequisites/errata.md`.
