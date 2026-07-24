# 🗺️ 1 — Program Map: the unified curriculum

> Every stage, module, and week of the entire journey in one place: what it covers, where its content
> lives, whether it exists yet, and what it depends on. Statuses are mirrored in `6-MASTER-CHECKLIST.md`
> (that file is the ledger; this one is the map).

---

## §1 How the old plans merge into this one

The journey previously had three overlapping plans. They merge as follows — **this table resolves every
conflict**:

| Old plan element | Fate | Where it went |
|---|---|---|
| Main README weeks 1–13 | ✅ Kept as history | `docs/curriculum/` (Week 13 still to finish — Stage 0) |
| Main README week 14 (CV) | **Absorbed** | Week G (`Addendum/4-AppliedAI/weekG-computer-vision/`) — richer superset (transfer learning, DL toolkit, augmentation) |
| Main README week 15 (Time series) | **Absorbed** | Week H (`Addendum/4-AppliedAI/weekH-time-series/`) — superset (ARIMA→ML→LSTM) |
| Main README week 16 (capstone) | **Absorbed** | Week I (`Addendum/4-AppliedAI/weekI-applied-capstone/`) |
| Main README weeks 17–18 (deploy/MLOps) | **Absorbed** | Weeks J, K, L (`Addendum/5-Deployment_MLOps/`) — superset |
| Main README weeks 19–20 (final capstone) | **Absorbed** | Week M (`Addendum/5-Deployment_MLOps/weekM-final-capstone/`) + the three flagship projects (`2-EXECUTION-PLAN.md` §5) |
| Addendum START GATE (serial ordering) | **Repealed** | Replaced by 3-track system (`2-EXECUTION-PLAN.md` §2) |
| Addendum "revise Modules 4–5 after main course" | ✅ Kept (adapted) | Now: revise weeks E–F against completed Week 13 only (weeks G–M no longer have a main-course twin to collide with) — `4-MODULE-SPECS/spec-module4-5-revision.md` |
| Addendum CHECKLIST.md | **Superseded** | `6-MASTER-CHECKLIST.md` |
| MasterclassPlan (July 2026 review) | **Merged** | Gap analysis → `7-APPENDIX-GAP-ANALYSIS.md`; roadmap → `2-EXECUTION-PLAN.md`; prompts → `5-AI-WORKFLOW.md`; module specs → `4-MODULE-SPECS/` |

**Consequence:** there is now exactly ONE path. Nobody builds main-course weeks 14–20; the main README
gets a pointer to this plan (see §5 below).

---

## §2 The unified curriculum, stage by stage

### Stage 0 — Close the main course (July 2026)

| Item | Content location | Status | Notes |
|---|---|---|---|
| Week 13 — NLP intro | `docs/curriculum/5-AppliedAI/13.week13.md` | 🚧 finish it | Last main-course item. Keep scope as written; Week E deepens it later |
| Week 12 closure checklist | `Addendum/0-Prerequisites/week12-closure-checklist.md` | verify | 13 zero-byte files issue |
| Errata pass | `Addendum/0-Prerequisites/errata.md` | verify | known typos/path fixes |

### Stage 1 — Existing Addendum modules (content already written)

| Module | Week | Topic (days) | Content location | Built? | Depends on |
|---|---|---|---|---|---|
| 1 Consolidation | — | QBs wk3–12, cheat sheets, revision sheets + **SRS conversion (new, spec-m1)** | `Addendum/1-ConsolidationPack/` | ✅ + small addition | Week 12 |
| 2 Classical ML | A | Trees, bagging, boosting, XGBoost (7) | `Addendum/2-ClassicalML_Completion/weekA-…` | ✅ | Wk 5–8 |
| 2 | B | SHAP, LIME, PDP, calibration, fairness (5) | `…/weekB-interpretability/` | ✅ | A |
| 3 Unsupervised+Math | C | Clustering, PCA, t-SNE, anomaly (7) | `Addendum/3-Unsupervised_MathSpine/weekC-…` | ✅ | Wk 3–8 |
| 3 | D | Probability, CLT, Bayes, linalg, SVD, calculus (6) | `…/weekD-math-foundations/` | ✅ | none |
| 4 Applied AI | E | NLP: tokens→embeddings→RNN/LSTM (7) | `Addendum/4-AppliedAI/weekE-…` | ✅ needs revision pass | Wk 13, D-4 |
| 4 | F | Transformers: attention→tiny GPT→HF→LoRA→RAG day (7) | `…/weekF-transformers-llms/` | ✅ needs revision pass | E, D-4/5 |
| 4 | G | CV: transfer learning + DL toolkit (7) | `…/weekG-computer-vision/` | ✅ | Wk 11–12 |
| 4 | H | Time series: ARIMA→ML→LSTM (7) | `…/weekH-time-series/` | ✅ | Wk 6–7, E-5 |
| 4 | I | Applied mini-capstone (5) | `…/weekI-applied-capstone/` | ✅ | E–H |
| 5 Deploy+MLOps | J | pytest, structure, SQL, git/CI (5) | `Addendum/5-Deployment_MLOps/weekJ-…` | ✅ | Wk 8 |
| 5 | K | FastAPI, Docker, batch/online, drift (6) | `…/weekK-deployment/` | ✅ | J |
| 5 | L | MLflow, registry, versioning, orchestration (5) | `…/weekL-mlops/` | ✅ | K |
| 5 | M | Final capstone: deployed, monitored, defended (7) | `…/weekM-final-capstone/` | ✅ | J–L + flagships |

### Stage 2 — New modules (specs written, content TO BE BUILT from `4-MODULE-SPECS/`)

| Module | Week | Topic (days) | Target location (create) | Spec file | Depends on |
|---|---|---|---|---|---|
| 6 LLM Engineering | N | Agents & tool use (7) | `Addendum/6-LLM_Engineering/weekN-agents-tools/` | `spec-module6` | F |
| 6 | O | Evals, guardrails & LLMOps (7) | `…/weekO-evals-guardrails/` | `spec-module6` | N |
| 6 | P | Advanced RAG & inference (7) | `…/weekP-rag-inference/` | `spec-module6` | N, O |
| 7 Cloud & Scale | Q | One cloud, for real (6) | `Addendum/7-Cloud_Scale/weekQ-cloud/` | `spec-module7` | K |
| 7 | R | Scale & reliability (5) | `…/weekR-scale-reliability/` | `spec-module7` | Q, G-5 |
| 8 Data & Decisions | S | Data engineering (6) | `Addendum/8-Data_Decisions/weekS-data-engineering/` | `spec-module8` | J-3/4 |
| 8 | T | Experimentation & causal (6) | `…/weekT-experiments-causal/` | `spec-module8` | D-2 |
| 9 Recommenders | U | RecSys end-to-end (5) | `Addendum/9-Recommenders/weekU-recsys/` | `spec-module9` | D-5, Wk 6, C-6 |
| 10 Portfolio Engine | V | Flagship builds + GitHub overhaul (ongoing) | `Career/` + external repos | `spec-module10` | rolling |
| 10 | W | Publishing: posts, resume, talk (ongoing) | `Career/` | `spec-module10` | rolling |
| 11 Interview Gauntlet | X | DSA drip: 75 problems (10–12 wks, 30 min/day) | `Career/dsa/` | `spec-module11` | none |
| 11 | Y | ML breadth + system design drills (3 wks drip) | `Career/system-design/` | `spec-module11` | most modules |
| 11 | Z | Mock loops, story bank, negotiation (2 wks) | `Career/` | `spec-module11` | X, Y |
| Electives | E1–E8 | RL/DPO · diffusion · speech · graph · edge · governance · Kaggle · OSS (≤1 wk each) | `Addendum/Electives/` | `spec-electives` | post-core |

---

## §3 Dependency graph (what unlocks what)

```
Week 13 ──► weekE ──► weekF ──► weekN ──► weekO ──► weekP ─┐
                        │                                   ├─► Flagship 1 (RAG+agent)
Wk 11–12 ──► weekG ─────┤          weekK ──► weekQ ──► weekR┘
Wk 6–7  ──► weekH ──────┴─► weekI
Wk 5–8  ──► weekA ──► weekB ─────────────┐
Wk 3–8  ──► weekC ─┐                     ├─► Flagship 2 (tabular, real data)
(none)  ──► weekD ─┴─► (feeds E/F/U math)│
Wk 8    ──► weekJ ──► weekK ──► weekL ───┘
weekJ-3/4 ──► weekS ─┐
weekD-2  ──► weekT ──┼─► Flagship 3 (role branch)
weekD-5+Wk6 ─► weekU ┘
All ──► weekM (final integration) ──► weeks X/Y/Z peak ──► applications
Track C (Module 1 SRS · weekX DSA · weekV/W publishing) runs parallel to everything, always.
```

Rule: a week may start when its dependencies are ✅ — regardless of module numbering.

---

## §4 What "built" vs "done" means (for models and humans)

- **Built** = all lesson pairs + week README exist per `3-CONVENTIONS.md`. (AI can do this from specs.)
- **Studied** = learner filled every `N.1.py`, appended the "what I learned" note.
- **Done** = studied + the week's defense artifact written + (for capstone weeks) the public bar met
  (`2-EXECUTION-PLAN.md` §5) + checklist box ticked.

## §5 Required edits to older files (do once, small)

1. Main `README.md`: under the Program Overview table, add: *"⚠️ Weeks 14–20 are superseded — the journey
   continues in [MasterPlan/](MasterPlan/README.md); weekly statuses now live in
   [MasterPlan/6-MASTER-CHECKLIST.md]."* Do not delete the table (it's history).
2. `Addendum/README.md` and `Addendum/CHECKLIST.md`: replaced by deprecation pointers (done in v2.0).
3. requirements: new packages land in `Addendum/addendum-requirements.txt` as modules start (per-module
   lists are in each spec file).
