# 🧭 Addendum — AI Journey, Part 2  ·  ⚠️ PLANNING SUPERSEDED

> ## 📍 This folder is now a CONTENT LIBRARY, not a plan.
> The governing plan for the whole journey is **[`../MasterPlan/`](../MasterPlan/README.md)** (v2.0,
> July 2026). It merged this Addendum's plan with the July-2026 second review pass. **Read the
> MasterPlan first; it wins over anything in this file.**
>
> What changed and why (details in `../MasterPlan/1-PROGRAM-MAP.md` §1):
> - The **START GATE below is REPEALED** — replaced by 3 parallel tracks
>   (`../MasterPlan/2-EXECUTION-PLAN.md` §2). Market-critical work no longer waits a year.
> - **Status is tracked ONLY in `../MasterPlan/6-MASTER-CHECKLIST.md`** — this folder's CHECKLIST.md
>   is deprecated.
> - Main-course weeks 14–20 are **absorbed into Addendum weeks G–M** (no separate main-course build).
> - The **lesson files in this folder are still the real content** — Modules 1–5 (weeks A–M) are built
>   and used as-is; Modules 6–9 (weeks N–U) get built into new sibling folders per
>   `../MasterPlan/4-MODULE-SPECS/`.
> - Modules 4–5 still need the light revision pass — now scoped in
>   `../MasterPlan/4-MODULE-SPECS/spec-module4-5-revision.md`.

<details>
<summary>📜 Original Addendum plan (historical — superseded by MasterPlan)</summary>

This addendum extends the main `aijourney_python` curriculum. It was derived from the
[full project analysis](aijourney_project_analysis.html) (June 2026).

> ## ⛔ START GATE (REPEALED — see MasterPlan)
> Originally: nothing in this Addendum starts until the main course is 100% finished.
> Now replaced by the 3-track system in `../MasterPlan/2-EXECUTION-PLAN.md`.

**Format law (learned from Weeks 10–11 of the main course):**
- Every lesson is a pair: `N.0.<topic>.md` (theory, written up-front) + `N.1.<topic>.py` (practice, filled in when we study it)
- Every lesson md opens with Topics + measurable Learning Goals, ends with Common Mistakes + Connections
- Every module ends with a capstone or mini-defense
- Mechanics first: math/intuition from scratch before any library call

**Rule:** start a module only when the previous one is ✅. Within a week, go day by day, in order.

---

## 📜 Program Overview

| Order | Module | Week | Topic | Days | Status |
|-------|--------|------|-------|------|--------|
| 0 | [0-Prerequisites](0-Prerequisites/) | — | Finish the ENTIRE main course (Week 12 + Phases 5–6), then revise Modules 4–5 | — | 🚧 |
| 1 | [1-ConsolidationPack](1-ConsolidationPack/) | — | Question banks (wk 3–12), cheat sheets, revision sheets | flexible | 📅 |
| 2 | [2-ClassicalML_Completion](2-ClassicalML_Completion/) | A | Decision trees, bagging, boosting, XGBoost | 7 | 📅 |
| 2 | | B | Interpretability: SHAP, LIME, PDP, calibration, fairness | 5 | 📅 |
| 3 | [3-Unsupervised_MathSpine](3-Unsupervised_MathSpine/) | C | Clustering, PCA, t-SNE/UMAP, anomaly detection | 7 | 📅 |
| 3 | | D | Math spine: probability, statistics, Bayes, linear algebra, SVD | 6 | 📅 |
| 4 | [4-AppliedAI](4-AppliedAI/) ⚠️ DRAFT | E | NLP foundations: tokenization → embeddings → RNN/LSTM | 7 | 🔧 revise first |
| 4 | | F | Transformers & LLMs: attention math → tiny transformer → HF → RAG | 7 | 📅 |
| 4 | | G | Computer vision: transfer learning + DL training toolkit | 7 | 📅 |
| 4 | | H | Time series: decomposition → ARIMA → ML → LSTM | 7 | 📅 |
| 4 | | I | Applied AI mini-capstone | 5 | 📅 |
| 5 | [5-Deployment_MLOps](5-Deployment_MLOps/) ⚠️ DRAFT | J | Software engineering for ML: pytest, structure, SQL | 5 | 🔧 revise first |
| 5 | | K | Deployment: serialization → FastAPI → Docker → monitoring | 6 | 📅 |
| 5 | | L | MLOps: MLflow, registries, data versioning, orchestration | 5 | 📅 |
| 5 | | M | Final capstone: end-to-end, deployed, monitored, defended | 7 | 📅 |

Legend: ✅ Completed · 🚧 In progress · 📅 To do · 🔧 Draft — revise against finished main course before starting

---

## 🔄 Suggested cadence

The main course averaged ~1 week of content per calendar month. At that pace:

| Module | Estimated calendar time |
|--------|------------------------|
| 0 + 1  | 1–1.5 months (light, good warm-down after Week 12) |
| 2      | 1.5–2 months |
| 3      | 1.5–2 months |
| 4      | 4–5 months (the big one) |
| 5      | 3–4 months |

Total: roughly 12–15 months — a natural "Year 2" of the journey.

---

## 🧩 Why these modules, in one paragraph each

**0 — Prerequisites.** Week 12 of the main course is scaffolded but empty (13 zero-byte files). Nothing
here makes sense until that capstone is done, because Modules 4 and 5 reuse its model, its workflow, and
its defense format. The errata file records known typos/path issues in the frozen main repo.

**1 — Consolidation.** The main repo's best retention tool — question banks with "my attempt vs reference"
answers — stopped at week 2. This module backfills weeks 3–12, then harvests the cheat sheets and one-page
revision sheets the repo never had. Do it right after Week 12 while everything is fresh: it is revision
disguised as authoring.

**2 — Classical ML completion.** Random Forests and Gradient Boosting were *used* in Week 8 but never
*understood* — contrary to the project's own philosophy. Week A opens the black box (split math, bagging
variance argument, boosting as gradient descent in function space). Week B extends the "model defense"
ritual with SHAP and friends, so future defenses can explain individual predictions.

**3 — Unsupervised + math spine.** Zero coverage so far of clustering, PCA, or anomaly detection. PCA
requires eigenvectors/SVD, which the math spine supplies — and those same tools power embeddings and
attention in Module 4. Statistics (distributions, hypothesis testing, Bayes) formalizes what Weeks 6–7
used implicitly.

**4 — Applied AI.** The main README planned NLP/CV/time-series (weeks 13–16). This upgrades that plan for
2026: NLP gets a second week for attention/transformers/LLM tooling (the analysis's biggest gap), CV is
built around transfer learning plus the missing DL toolkit (dropout, batch norm, augmentation, schedulers),
and time series includes the RNN→LSTM bridge that makes the transformer motivation land mechanically.

**5 — Deployment & MLOps.** The planned Phase 6, made concrete: test and structure ML code properly, pull
data from SQL instead of CSVs, serve the Week-12/Module-4 models with FastAPI + Docker, track experiments
with MLflow, then a final capstone that is framed, built, deployed, monitored, and defended.

---

## 🗂 Repository conventions for this addendum

```
Addendum/
  <module>/README.md          ← module index: day order, status checkboxes, deliverables
  <module>/week<X>-<topic>/
      N.0.<topic>.md          ← theory & plan (already written — read first)
      N.1.<topic>.py          ← placeholder; fill while studying (keep the header docstring)
```

- Update the Status column in this README as modules complete (mirror the main repo habit).
- Each week's final day produces a written artifact (comparison table, defense, or retrospective).
- Datasets: prefer small, cacheable, seeded — same reproducibility discipline as Week 8.

</details>

---
*Status and sequencing are now governed by [`../MasterPlan/`](../MasterPlan/README.md). This file is kept
for its module descriptions and conventions only.*
