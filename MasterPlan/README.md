# 🧭 MasterPlan — THE Single Source of Truth (v2.0, July 2026)

**This folder is the one and only governing plan for the entire AI journey from this point forward.**
It merges and supersedes: the main README's weeks 14–20 plan, `Addendum/README.md`'s module plan and
start-gate, `Addendum/CHECKLIST.md`, and the earlier `MasterclassPlan/` review (now Appendix here).
If any other document in this repo contradicts this folder, **this folder wins**.

## Who reads this and in what order

**If you are Mahi (the learner):**
1. `2-EXECUTION-PLAN.md` — what to do this month, this week, today.
2. `6-MASTER-CHECKLIST.md` — tick boxes as you go. The only status ledger.
3. Everything else is reference.

**If you are an AI model (Sonnet, Opus, Fable, GPT, …) asked to extend, build, review, or tutor:**
1. `1-PROGRAM-MAP.md` — the full curriculum: what exists, where it lives, what must be built, dependencies.
2. `3-CONVENTIONS.md` — the format law. Every file you generate MUST follow it exactly. Contains templates
   and a fully worked example.
3. `4-MODULE-SPECS/` — day-level specifications for every piece of unbuilt content. Build from these; do
   not invent scope.
4. `5-AI-WORKFLOW.md` — ready-made prompts and the standing rules for AI sessions in this repo.
5. `6-MASTER-CHECKLIST.md` — determine current position before doing anything.

## 📁 Folder contents

| File | Purpose |
|------|---------|
| `1-PROGRAM-MAP.md` | Unified curriculum map: every stage, module, week — status, location, dependencies, what supersedes what |
| `2-EXECUTION-PLAN.md` | The 12-month schedule, 3-track system, daily/weekly cadence, cut-lines, flagship projects, role branches |
| `3-CONVENTIONS.md` | Format law: file anatomy, templates (.md lesson, .py scaffold, week README, defense, question bank, SRS), quality gates |
| `4-MODULE-SPECS/` | One spec file per unbuilt module — day-by-day detail sufficient to generate every lesson pair without guessing |
| `5-AI-WORKFLOW.md` | The CONTEXT block + prompt library: build, revise, review, question banks, mock interviews, weekly review |
| `6-MASTER-CHECKLIST.md` | Single status ledger for the whole program |
| `7-APPENDIX-GAP-ANALYSIS.md` | The evidence: repo inventory vs 2026 market research; why every module exists. Read when you doubt the plan |

## The five laws (inherited, unchanged, non-negotiable)

1. **Mechanics first.** Math/intuition from scratch (hand or NumPy) before any framework call; then verify
   the from-scratch version matches the library.
2. **Paired files.** Every lesson = `N.0.<topic>.md` (theory, written up-front) + `N.1.<topic>.py`
   (practice scaffold, filled while studying).
3. **Defense ritual.** Every week ends with a written artifact: comparison table, model defense, or
   retrospective. Choices → evidence → risks → next steps.
4. **Evaluation honesty.** Baselines first. Holdout used once. Negative results are valid results.
5. **Connection threading.** Every lesson names the specific prior lessons it builds on.

## The three laws this plan adds (v2.0)

6. **Public by default.** Every capstone ships as a public artifact (deployed endpoint, public repo, or
   published write-up). "Done" = public and defensible, not "the last .py runs".
7. **Parallel tracks, not a gate.** Deep work (Track A), market-critical work (Track B), and daily drip
   (Track C) run concurrently under the rules in `2-EXECUTION-PLAN.md` §2. The old Addendum start-gate is
   repealed.
8. **Time-boxed months.** Every month has a named outcome and cut-lines. Scope bends; deadlines don't.

## Content library (where lesson material physically lives)

- `docs/curriculum/` — main course weeks 1–13 (history; complete except Week 13).
- `Addendum/1-…5-…` — modules 1–5 lesson pairs, weeks A–M (built by Opus, June 2026; Modules 4–5 need
  the revision pass in `4-MODULE-SPECS/spec-module4-5-revision.md`).
- `Addendum/6-…9-…` — modules 6–9, weeks N–U (**to be built** from `4-MODULE-SPECS/`).
- `Career/` — module 10–11 artifacts (**to be created**: story bank, resume, system-design notes, publishing log).
- Flagship projects — standalone public repos outside this one (specs in `2-EXECUTION-PLAN.md` §5).
