# Spec — Module 10: Portfolio Engine (weeks V, W — ongoing tracks, not calendar weeks)

> Closes Gap 3: the program's work is invisible. This module is PROCESS, not lessons — it runs on
> Track C from M1 to M12. Artifacts live in `Career/` (create it) and in standalone public repos.
> Flagship project specs live in `2-EXECUTION-PLAN.md` §5 (the public bar + Flagships 1–3) — this file
> covers everything AROUND them.

## Week V — Build in public (starts M1, never ends)

### V.1 GitHub overhaul (M1, one session)
- This repo: rewrite the top of the main README to present the journey as its strongest asset — a
  20-week self-built curriculum with defenses and honest negative results. Add the MasterPlan pointer
  (`1-PROGRAM-MAP.md` §5). Pin: this repo + flagships as they appear.
- Profile README: 3 lines — who, what's being built, links to top artifacts. No skill-badge walls.
- Hygiene standards from now on: meaningful commit messages (the repo's git log is read by hiring
  managers); no giant "misc updates" commits; CI badges on flagships once weekJ-5/O-3 exist.

### V.2 Standalone repo standard (applies to tiny-GPT repo M3, all flagships)
Every public repo ships: README-as-case-study (problem → approach → headline eval number → cost →
limits, first screen — see the public bar) · `Makefile` or `justfile` with `setup/run/eval` targets ·
pinned requirements · license · the defense doc · AI-assistance log (Law 6's companion: where AI helped,
where it failed, how output was verified — interviewers ask about exactly this now).

### V.3 The publishing pipeline (2 h/week, tracked in `Career/publishing-log.md`)
Pipeline: pick an existing artifact → strip to case study → publish (personal blog or Medium-class
platform — choose in M2 and stop deliberating) → log it.
Post schedule (from `2-EXECUTION-PLAN.md` §3): M2 post 1 = Week-12 "the baseline beat the CNN"
retrospective (honest negative results are rare, memorable content) · M3 post 2 = attention-by-hand
notes · M7 post 3 = the eval-harness/ship-gate write-up · M9 post 4 = chaos-day postmortems ·
M11 post 5 = Flagship 3 case study · M12 post 6 = the journey retrospective (career-switch narrative).
Rule: posts are REPURPOSED defenses, never written from scratch — the defense ritual already produced
the content; publishing is editing.

## Week W — Presence & network (starts M6, peaks M12)

### W.1 Resume & LinkedIn (draft M10, final M12, in `Career/resume/`)
- Translation table (maintain as you go — this is the file other models use to write bullets):
  program vocabulary → market vocabulary. Examples: "model defense" → "evaluation methodology &
  model documentation"; "leakage proofs" → "reproducible pipelines with leakage-safe CV";
  "ship gate" → "eval-driven CI gates for LLM systems"; "chaos day" → "production incident response".
- Bullet law: every bullet = verb + thing + measured outcome ("built eval-gated RAG assistant;
  50-case golden set; +23pt faithfulness over baseline at $0.004/query"). No responsibilities, only
  evidence. Numbers come from defenses — another reason defenses are never cut.
- One resume per branch (§4 verbs table in the execution plan), same evidence base.

### W.2 Network (light but non-zero, from M6)
- Join ONE community (ML Discord / local meetup) and be visible weekly (answer questions — teaching
  is the program's native skill).
- M11: deliver one talk — a meetup lightning talk or recorded walkthrough of Flagship 1 (the talk is
  post material AND interview practice AND network in one artifact).
- Accountability: one person who sees the checklist monthly (even a peer learner).

### W.3 External validation checkpoints (Gap 20)
- M10: one cloud cert (AWS ML Engineer Associate or equivalent) — 2 weeks of Track-B study max; it's
  an HR-legibility token, not education; the program already over-covers the content.
- Optional (elective E7): one Kaggle tabular competition with weekA skills — a leaderboard position is
  external proof the benchmark discipline works.

## Definition of done (checked monthly, M12 = all true)
- [ ] 3 flagships public, deployed, defended (public bar met)
- [ ] 6 posts live · [ ] talk delivered · [ ] cert passed
- [ ] Resume(s) final, every bullet evidence-backed · [ ] LinkedIn mirrors it
- [ ] GitHub: pinned, hygienic, CI-badged · [ ] publishing-log.md complete
