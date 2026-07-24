# Spec — Module 9: Recommender Systems (week U)

> Closes Gap 8: recsys is absent yet is a top-3 ML system-design interview domain and a whole industry.
> Build at `Addendum/9-Recommenders/weekU-recsys/`. Prereqs: weekD-5 (SVD), Week 6 (SGD), weekC-6
> (t-SNE), weekP-3 (ANN/vector search). Dataset: MovieLens (100k for speed, 1M if the machine allows).
> New packages: none beyond existing (numpy/pandas/torch); optionally `implicit` for verification only.
> Cut-line note (from `2-EXECUTION-PLAN.md` §3): if M11 slips, Day 5 folds into Day 4's defense.

## Week U — RecSys End-to-End (5 days) → `weekU-recsys/`

**Day 1 — The matrix view & the embarrassing baseline** (`1.0.matrix-view-baselines.md`)
- Topics: user×item interaction matrices; sparsity arithmetic (MovieLens is ~95% empty — compute it);
  explicit ratings vs implicit feedback (clicks/watches — the real world is implicit); the popularity
  baseline and why it's humiliatingly strong; train/test splitting in recsys (leave-last-out, time-aware —
  random splits leak the future, Week 7's lesson in new clothes).
- Goals: (1) load MovieLens into a sparse matrix and compute density, user/item activity distributions
  (both long-tailed — plot them); (2) explain implicit-vs-explicit and what "negative" even means when
  feedback is implicit (non-interaction ≠ dislike); (3) implement the popularity recommender and a
  time-aware split; (4) state why random splitting lies here.
- Build: sparsity + long-tail plots · time-aware split utility (reused all week) · popularity baseline
  scored (recall@10 — implemented Day 3 but a simple hit-count preview today) · one paragraph: "what the
  long tail means for everything downstream".
- Mistakes: random splits (future leakage) · dropping cold users/items from test (that's the hard part,
  don't delete it) · treating non-interaction as explicit dislike.
- Connects: Week 7 (leakage/time-series splits), weekS-6 (point-in-time correctness — same disease).

**Day 2 — Matrix factorization from scratch** (`2.0.matrix-factorization-sgd.md`)
- Topics: MF as learned embeddings — user vector · item vector ≈ affinity; the masked-SGD objective
  (only observed entries + regularization); biases (global/user/item) and why they eat most of the signal;
  relationship to weekD-5's SVD (and why plain SVD doesn't fit sparse+missing data).
- Goals: (1) write the MF loss and derive the SGD updates by hand (it's Week 6's gradient descent on two
  matrices); (2) implement MF in NumPy (~80 lines): biases first, then factors; (3) show bias-only vs
  bias+factors performance (the humbling ablation); (4) visualize item embeddings with weekC-6's t-SNE and
  find 3 interpretable neighborhoods (genres emerge — nobody told the model about genres).
- Build: derivation in comments + the implementation + RMSE ablation table (global / +user,item bias /
  +factors at k∈{8,32,64}) + the t-SNE with annotated neighborhoods.
- Mistakes: updating on unobserved zeros (that's what "masked" means) · skipping biases then blaming
  factors · k as big as memory allows (overfitting, Week 7 knows).
- Connects: Week 6 (SGD), weekD-5 (SVD), weekE-3 (word embeddings — same trick, different co-occurrence).

**Day 3 — Ranking metrics that lie less** (`3.0.ranking-metrics.md`)
- Topics: from rating prediction to top-k ranking (the business never wanted RMSE); recall@k,
  precision@k, MRR, NDCG derived by hand (compute NDCG for one worked example on paper); offline-online
  divergence — position bias, exposure bias, feedback loops (you trained on what the OLD recommender
  showed people).
- Goals: (1) hand-compute NDCG@5 for a worked ranking, every term; (2) implement recall@k / precision@k /
  NDCG@k and evaluate Day 1–2's models properly (popularity vs MF as *rankers*); (3) explain why offline
  metrics diverge from online reality, mechanically (position bias + exposure bias + loop); (4) connect to
  weekT: the offline metric selects candidates to A/B test, never replaces the test.
- Build: the paper NDCG + metrics module (~60 lines, tested against a hand case) + the leaderboard table +
  the divergence essay (½ page, mechanism-level).
- Mistakes: averaging NDCG over users with zero test items (silent inflation) · comparing models at
  different k · believing a 2% offline gain survives contact with position bias.
- Connects: weekO-1 (golden-set thinking), weekT-2 (the online experiment this feeds), Day 1's split.

**Day 4 — Two-tower & the retrieval→ranking cascade** (`4.0.two-tower-cascade.md`)
- Topics: THE production architecture — candidate generation (fast, approximate, thousands→hundreds) then
  ranking (slow, feature-rich, hundreds→ten); two-tower networks (user tower, item tower, dot-product
  affinity — trained with in-batch negatives); serving = item embeddings in an ANN index (weekP-3
  returns); where features go (ranking stage) vs can't go (retrieval towers can't cross user×item).
- Goals: (1) draw the cascade with honest latency/candidate-count budgets per stage; (2) build a small
  two-tower in PyTorch on MovieLens implicit data (in-batch negatives — explain why they're a biased but
  effective trick); (3) serve retrieval via the weekP vector index and measure recall@100 of the retrieval
  stage alone (its only job: don't lose the good stuff); (4) explain why the two towers can't see each
  other until the dot product (that independence IS what makes precompute+ANN possible).
- Build: cascade diagram + two-tower training (Week 10's loop, new head) + ANN-served retrieval +
  stage-wise metrics (retrieval recall@100, then final NDCG@10 after a simple ranker).
- Mistakes: features that need user×item interaction inside a tower (breaks precompute) · evaluating the
  cascade only end-to-end (measure stages separately — weekP-4's lesson) · in-batch negatives with tiny
  batches (nothing to contrast).
- Connects: weekP-3 (ANN), Week 10 (training loop), weekN/O habit (stage-wise evals).

**Day 5 — Cold start, feedback loops + the interview defense** (`5.0.coldstart-bias-defense.md`)
- Topics: cold-start strategies (content features, popularity fallback, explore quota); popularity bias
  and feedback loops (the doom-scroll mechanics: today's recs → tomorrow's training data → narrower recs);
  exploration as the antidote (ε-greedy taste of bandits — elective E1 hook); fairness surface (creator
  exposure, filter bubbles — weekB-5's thread).
- Goals: (1) implement one cold-start fallback and measure recs quality for zero-history users vs the
  cascade's (embarrassing) default; (2) simulate a feedback loop: retrain on your own recommendations ×3
  rounds, measure catalog coverage shrinking (plot it — this is the most underrated demo in recsys);
  (3) add an exploration quota and show coverage recover at a small NDCG price; (4) write the trade-off
  paragraph: relevance vs coverage vs freshness.
- Build: cold-start eval + the 3-round loop simulation with coverage curve + exploration ablation.
- Deliverable: `weekU_defense.md` in **interview format** — a full 45-minute-style answer to "Design
  recommendations for a streaming service": requirements → data → cascade architecture → features →
  training → offline evals → online experiment (weekT!) → cold start → feedback-loop guards → cost/latency
  → monitoring. Every section backed by something you built this week.
- Mistakes: cold-start as afterthought (it's most new users!) · optimizing engagement and calling it
  satisfaction · never measuring catalog coverage.
- Connects: weekT (the online half), weekB-5 (fairness), weekO/K (evals+monitoring), elective E1 (bandits).
