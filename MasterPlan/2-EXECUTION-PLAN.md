# 📆 2 — Execution Plan: tracks, schedule, cadence, flagships, branches

> The "what do I do today" document. Map/dependencies: `1-PROGRAM-MAP.md`. Status ledger:
> `6-MASTER-CHECKLIST.md`. Rationale for every choice: `7-APPENDIX-GAP-ANALYSIS.md`.

---

## §1 Goal and definition of victory

**Goal:** interview-ready, top-decile candidate by **July 2027** (12 months from July 2026), role-agnostic
core with a branch chosen at month 11 (§4).

**Victory =** all of: ① 3 flagship projects public and deployed (§5) · ② 6+ published write-ups ·
③ one cloud cert · ④ DSA: 75 problems done, medium in ≤25 min consistently · ⑤ 10 system designs
practiced to rubric · ⑥ 10-story behavioral bank road-tested in ≥4 mock loops · ⑦ every checklist
phase ①–⑥ ticked.

## §2 The three-track system (replaces the old start-gate)

| Track | What | Time budget | Rules |
|---|---|---|---|
| **A — Deep spine** | The curriculum weeks, in dependency order | ~60% (mornings / long sessions) | Mechanics-first law applies fully. One week at a time, day order fixed |
| **B — Market-critical** | Modules 6–7 (weeks N–R) + cert study | 1–2 sessions/week | Starts the moment weekF is ✅. Pauses during math-heavy Track-A weeks (never two new-theory streams at once) |
| **C — Drip** | SRS 15 min/day · DSA 30 min/day (from M4) · publishing 2 h/week · weekly review 30 min | ~1 h/day | **Never pauses. Not even capstone weeks.** Streaks are tracked in the checklist |

Conflict rule: if a day is short, order is C → A → B (drip protects retention; depth beats breadth;
market work is chunkier and survives postponement best).

## §3 The 12-month schedule

Each month has one **named outcome** (the thing that must exist on the last day) and **cut-lines**
(what to drop first if slipping — scope bends, deadlines don't).

| Month | Track A | Track B | Track C adds | 📦 Named outcome (public) |
|---|---|---|---|---|
| **M1** Jul 2026 | Finish Week 13 · Module 1 harvest (QBs 3–12 → SRS deck) | — | SRS starts · GitHub cleanup | Repo repositioned "learning in public"; SRS live |
| **M2** Aug | Week E (NLP foundations; revision pass vs Week 13 first) | — | Blog post 1: Week-12 "baseline beat the CNN" retro | Post 1 live |
| **M3** Sep | Week F (attention→tiny GPT→LoRA) | — | Post 2: attention-by-hand notes | Tiny-GPT public repo + post 2 |
| **M4** Oct | Week H (time series) | **Week N (agents)** | DSA drip starts | Week N built+studied; agent traces public |
| **M5** Nov | Week G (CV transfer learning) | **Week O (evals/guardrails)** | — | Flagship 1 v0 local, with eval harness |
| **M6** Dec | Week A (trees/boosting) | **Week P (adv RAG/inference)** | — | Flagship 1 deployed, eval-gated |
| **M7** Jan 2027 | Week B (interpretability) + Week C (unsupervised) | **Week Q (cloud)** | Post 3: eval-harness write-up | All capstones on live cloud URLs |
| **M8** Feb | Week D (math spine) | *B pauses (math month)* | — | Week D done; SRS deck ≥1000 cards |
| **M9** Mar | Week J + Week K (SE-for-ML, serving) | **Week R (scale/chaos)** | Breadth drills start (10 min/day) | Chaos-day postmortems published (post 4) |
| **M10** Apr | Week L (MLOps) + Week S (data eng) | Cloud cert study (2 wks) → exam | System-design drills start (1/wk) | Flagship 2 deployed + monitored · cert passed |
| **M11** May | Week T (experiments) + Week U (recsys) | **Flagship 3 build** (role branch, §4) | Mock interviews (1/wk) | Flagship 3 public · post 5 |
| **M12** Jun | Week M = integrate flagships into one story | **Weeks X/Y/Z full-time** (gauntlet peak) | Applications live | Resume/LinkedIn final · talk delivered · post 6 · APPLYING |

Cut-lines, in drop order: electives (already deferred) → Week U day 5 → Week S days 5–6 → Week I
(fold into Flagship 2 defense) → reduce posts 5–6 to one. **Never cut:** Track C, defenses, flagship
deployment, the revision passes.

Weeks E–M were sized by Opus at 5–7 days each; the schedule allots each ~2–3 calendar weeks of Track-A
time — realistic at the historical pace *because* Track B/C absorb the non-deep work that used to stretch
weeks (question banks, polishing, tooling).

## §4 Role branch (decided end of M10; default = AI/ML Engineer)

| | AI/ML Engineer (default) | LLM/GenAI App Engineer | Data Scientist |
|---|---|---|---|
| Flagship 3 | RecSys or CV system, deployed + monitored | Multi-agent product, eval-gated CI | Experimentation platform / causal study on public data |
| M11 extra depth | Week R++, Week S++ | Weeks O/P second pass at depth; elective E1 (DPO) | Week T second pass; elective E7 (Kaggle) |
| Gauntlet weighting | design 40 / DSA 30 / breadth 30 | product+evals 40 / design 30 / DSA 30 | stats+causal 40 / SQL+case 30 / breadth 30 |
| Resume verbs | shipped, scaled, monitored, cut latency | built agents, eval-gated, cut cost/token | designed experiments, measured lift, informed decision X |

Branch decision inputs: which flagship was most fun · which interviews felt strongest in M9–10 drills ·
local market postings (check at M10, not before — don't chase a moving target early).

## §5 The three flagship projects

**The public bar (applies to every flagship, and to weeks I/M capstones):** standalone public repo ·
real/messy data (no Iris/MNIST/toy) · deployed or live-demo · versioned eval set with ONE headline number ·
monitoring or regression alarm · README-as-case-study (problem → approach → eval number → cost → limits,
all on the first screen) · written defense published as a post · AI-assistance log (where AI helped,
where it failed, how output was verified).

**Flagship 1 — "Repo Butler": RAG + agent over this curriculum** (M5–M7; evolves with N→O→P):
chunk/embed all `docs/` + `Addendum/` markdown → hybrid retrieval (BM25+dense, RRF) + reranker →
tool-using agent (search, read-file, run-python tools; answers "when did I learn Cook's distance?", runs
exercises) → guardrails with documented injection attacks/defenses → eval: 50-question golden set,
retrieval hit-rate separated from answer faithfulness, regression gate in CI → deployed (weekQ) with
tracing + cost-per-query ledger. *Weaponizes weekF-6's exercise into a product.*

**Flagship 2 — Boring-domain tabular system** (M9–M10): one messy public dataset with a real decision
attached (loan default / readmission / energy demand) → weekA boosting + weekB SHAP & calibration +
weekT-style decision framing → FastAPI + Docker + cloud → drift monitor + one simulated data shift +
written incident postmortem. *Proves the classical spine in production terms.*

**Flagship 3 — role branch** (M11): per §4 table.

## §6 Daily & weekly cadence (Track C mechanics)

- **SRS, 15 min/day**: deck built from every week's Learning Goals + Common Mistakes (format:
  `3-CONVENTIONS.md` §7). Missed day = do double next day, never skip two.
- **DSA, 30 min/day from M4**: schedule in `4-MODULE-SPECS/spec-module11-interviews.md` §2.
- **Publishing, 2 h/week**: pipeline = pick artifact → strip to case study → publish → log in
  `Career/publishing-log.md`.
- **Weekly review, 30 min, same weekday**: run the prompt in `5-AI-WORKFLOW.md` §7. Outputs: shipped vs
  plan, cut-or-carry per slip, streak check, one process change. Update checklist.
- **Monthly close**: named-outcome audit — if the outcome isn't public, the month isn't closed; apply
  cut-lines and re-plan before opening the next month.
