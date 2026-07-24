# Spec — Module 8: Data & Decisions (weeks S, T)

> Closes Gaps 6 & 7: data engineering beyond `read_csv`, and experimentation/causal inference.
> Build at `Addendum/8-Data_Decisions/`. Prereqs: weekJ-3/4 (SQL) for S; weekD-2 (CLT/tests) for T.
> New packages: `duckdb`, `polars`, `pyarrow`; (T uses only numpy/pandas/scipy/statsmodels — already present).

---

## Week S — Data Engineering (6 days) → `weekS-data-engineering/`

**Day 1 — Columnar thinking & Parquet internals** (`1.0.columnar-parquet.md`)
- Topics: row vs column layout mechanics (why an analytical scan reads 1/20th of the bytes); Parquet
  anatomy — row groups, column chunks, dictionary encoding, predicate pushdown; file sizing.
- Goals: (1) explain, at the byte level, why `SELECT AVG(one_column)` loves columnar and `UPDATE one row`
  hates it; (2) convert the biggest available dataset (NYC-taxi-class, ≥1 GB CSV) to Parquet; (3) inspect
  the file with pyarrow (row groups, encodings, stats) and explain what predicate pushdown will skip;
  (4) produce the size/speed table.
- Build: the conversion + inspection notebook + table (CSV vs Parquet: size, full-scan time, one-column-agg
  time, filtered-read time).
- Mistakes: one giant row group (no skipping) · gzip-ing Parquet like it's CSV (codecs are per-column) ·
  benchmarking with the OS cache warm on one side only.
- Connects: weekQ-2 (Parquet on S3), Week 2 (Pandas — now you know what it was hiding).

**Day 2 — DuckDB & analytical SQL in anger** (`2.0.duckdb-analytical-sql.md`)
- Topics: embedded OLAP; window functions on real volume (extends weekJ-4); EXPLAIN as a habit; SQL-vs-
  Pandas judgment.
- Goals: (1) answer 8 provided analytical questions on the Day-1 dataset in pure SQL (top-k per group,
  rolling averages, sessionization, percent-of-total — each exercising a window pattern); (2) EXPLAIN every
  query and point at the pushdown/pruning in the plan; (3) rewrite 2 of them in Pandas and argue honestly
  which tool won and why.
- Build: the 8 queries + plans + the 2 rewrites + timing table.
- Mistakes: `SELECT *` then filtering in Pandas · window function where GROUP BY suffices · never reading
  a plan.
- Connects: weekJ-3/4 (SQL foundation), Day 3 (same queries, lazy engine).

**Day 3 — Larger-than-memory: Polars & the Spark boundary** (`3.0.polars-lazy-scale.md`)
- Topics: eager vs lazy execution; query optimization you get for free (projection/predicate pushdown);
  streaming execution; where single-node ends and Spark begins (honest paragraph, not a week).
- Goals: (1) port Day-2's pipeline to Polars lazy; read the optimized plan and name 2 optimizations it
  applied; (2) process a dataset larger than RAM via streaming and prove peak memory stayed flat;
  (3) write the Pandas-vs-Polars-vs-DuckDB decision paragraph with your own timings as evidence;
  (4) state the Spark boundary: what actually forces a cluster (data won't fit one machine's disk /
  shuffle across nodes) — and that you haven't crossed it.
- Build: the port + plan reading + memory-profile proof + the 3-way timing/memory table.
- Mistakes: `.collect()` early (kills laziness) · benchmarking lazy plan-build time as if it were execution ·
  cluster-envy (distributed adds failure modes; earn them).
- Connects: Day 1–2, weekR-2 (distributed *training* — same "earn it" logic).

**Day 4 — Transformation-as-code (dbt-style)** (`4.0.transformation-as-code.md`)
- Topics: staged modeling — source → staging → marts; tests on models (unique, not-null,
  accepted-values); lineage; why analysts version transformations like engineers version code.
- Goals: (1) structure the Day-1 dataset into staged SQL models with a tiny runner (~60 lines: execute
  `.sql` files in dependency order against DuckDB — building the runner teaches what dbt automates);
  (2) add ≥6 model tests and make one fail meaningfully; (3) draw the lineage graph; (4) map each piece
  to its dbt equivalent by name (so the resume word is earned).
- Build: `models/` tree + runner + tests + lineage diagram + the dbt-mapping table.
- Mistakes: business logic duplicated across models (staging exists so it lives once) · tests that can't
  fail · lineage in your head instead of on paper.
- Connects: weekJ (SQL+structure), weekL-4 (orchestration will schedule this), Flagship 2 (its data layer).

**Day 5 — Data quality gates & contracts** (`5.0.data-quality-contracts.md`)
- Topics: expectation-style checks as code (schema, ranges, nulls, freshness, referential integrity);
  schema evolution handling; where gates sit in a pipeline (fail loud, before training).
- Goals: (1) write a quality-gate module (~80 lines, expectations declared as data, results as a report)
  for Flagship 2's training data; (2) plant 3 corruptions (silent nulls, unit change, category typo) and
  prove the gate catches all 3; (3) decide-and-document per check: fail-hard vs warn; (4) connect to
  drift: quality gates catch *broken* data, weekK-5's monitors catch *shifted* data — different beasts.
- Build: the gate + corruption drill + the fail/warn policy table.
- Mistakes: validating only at ingest (validate before every training run) · gates so strict nothing ships ·
  logging violations nobody reads (fail loud or don't bother).
- Connects: weekK-5 (drift), weekJ-1 (it's just pytest for data), Flagship 2 (mandatory component).

**Day 6 — Feature stores, streaming concepts + mini-defense** (`6.0.features-streaming-defense.md`)
- Topics: offline/online skew (THE feature-store motivation); point-in-time correctness (leakage's
  production cousin — connect to Week 7's obsession); batch vs streaming ingestion concepts (a simulator
  suffices; no cluster).
- Goals: (1) compute the same feature (e.g., user's 7-day rolling average) offline-batch and
  online-incremental; find and explain the skew; (2) demonstrate a point-in-time-incorrect join creating
  leakage, then fix it; (3) simulate streaming (replay the dataset row-by-row through the online path)
  and reconcile end-state vs batch.
- Build: both feature paths + skew measurement + the leakage demo/fix + the replay reconciliation.
- Deliverable: `weekS_defense.md` = the **data architecture memo for Flagship 2**: formats, stores, models,
  gates, features — every choice justified; the interview-ready "walk me through your data layer" answer.
- Mistakes: computing features on data the model wouldn't have had at prediction time (leakage, again,
  always) · feature-store-the-product before feature-store-the-problem is felt.
- Connects: Week 7 (leakage), weekK-4 (batch vs online serving — same split, feature side), weekU (recsys
  features need exactly this).

---

## Week T — Experimentation & Causal Inference (6 days) → `weekT-experiments-causal/`

**Day 1 — Why correlation keeps lying** (`1.0.confounding-simpsons-dags.md`)
- Topics: confounding mechanics; Simpson's paradox CONSTRUCTED (not just shown); DAG literacy —
  confounder vs mediator vs collider; when controlling for a variable makes estimates WORSE
  (collider bias — the shocker).
- Goals: (1) build, in Pandas, a synthetic dataset where the aggregate correlation flips sign within every
  subgroup (choose the confounder weights yourself — if you can construct it, you understand it);
  (2) draw the 3 canonical DAGs and state the adjustment rule for each; (3) demonstrate collider bias
  numerically (condition on the collider → spurious association appears).
- Build: the Simpson constructor + the flip visualization + the collider demo + 3 real-world examples
  written in your own words.
- Mistakes: "control for everything" (colliders punish it) · DAGs as decoration instead of adjustment
  decisions · believing observational correlations after this day.
- Connects: Week 6 (regression coefficients were always conditional statements), weekB (interpreting ≠
  causal), Day 5.

**Day 2 — A/B mechanics from scratch** (`2.0.ab-testing-mechanics.md`)
- Topics: randomization as the confounder-killer (ties Day 1's knot); randomization units (user vs session
  vs request — and interference between them); the two-proportion z-test DERIVED from weekD-2's CLT;
  A/A tests as the trust ritual.
- Goals: (1) derive the z-test from the CLT, no formula memorization; (2) simulate 1,000 A/A tests and
  watch false-positive rate converge to α (the day p-values become mechanical, not mystical); (3) pick the
  randomization unit for 3 scenarios and name the interference risk in each (e.g., recsys experiments
  contaminate via shared trending items).
- Build: the derivation (comments) + A/A simulator + the α-convergence plot + one properly analyzed
  synthetic A/B with CI on the lift.
- Mistakes: session-randomizing a user-level effect · declaring victory on the point estimate without the
  CI · skipping A/A ("we trust the platform" — you are the platform here).
- Connects: weekD-2 (CLT cashes in), Day 3 (how long to run it).

**Day 3 — Power, MDE & the peeking problem** (`3.0.power-mde-peeking.md`)
- Topics: power analysis derived AND simulated; the MDE/sample-size/duration triangle; the peeking problem
  demonstrated (sequential looks inflate false positives); sequential-testing intuition (what alpha-spending
  fixes, concept level).
- Goals: (1) compute required sample size analytically, then CONFIRM by simulation (the program's
  derive-then-verify signature); (2) produce the MDE-vs-duration curve for a realistic traffic level and
  make a business call from it ("we cannot detect <2% lift in under 6 weeks — so we won't try");
  (3) simulate peeking (test daily, stop at first p<0.05) and report the actual false-positive rate
  (expect ~25–30% — feel it).
- Build: analytic + simulated power (matching!) + the curve + the peeking simulation + a 5-line experiment
  runbook (fix n in advance; look when done; or use sequential methods knowingly).
- Mistakes: powering for the effect you HOPE for, not the smallest worth acting on · peeking "just to
  check" · running underpowered tests and reading noise as insight.
- Connects: Day 2, Week 7 (variance of estimates — same statistics, business stakes).

**Day 4 — Metrics design & variance reduction (CUPED)** (`4.0.metrics-cuped.md`)
- Topics: driver vs guardrail metrics; ratio-metric pitfalls (users vs sessions denominators);
  novelty/primacy effects; CUPED demystified — it's regression adjustment with pre-period data
  (connect to Week 6 literally).
- Goals: (1) design the metric suite for a real feature change (1 driver, 2–3 guardrails, 1 do-no-harm),
  with the reasoning written; (2) show a ratio-metric paradox numerically (per-user vs per-session moving
  in opposite directions); (3) implement CUPED from scratch, derive why θ = cov/var is optimal, and
  measure the variance reduction (equivalently: how much less traffic you now need).
- Build: the metric design doc + the ratio paradox demo + CUPED implementation with before/after CI widths.
- Mistakes: shipping on a driver while a guardrail quietly tanks · CUPED with post-period covariates
  (bias! pre-period only) · 15 metrics and a significance fishing trip.
- Connects: Week 6 (regression adjustment), Day 3 (variance reduction = cheaper power).

**Day 5 — Causal inference without experiments** (`5.0.observational-causal.md`)
- Topics: when you can't randomize; diff-in-diff (parallel-trends assumption FIRST, plot before estimate);
  propensity scores — it's logistic regression! (Week 5 cashes in) — matching/weighting mechanics;
  uplift modeling concept (predicting the treatment effect, not the outcome); the honesty section: what
  each method assumes and cannot rescue.
- Goals: (1) implement diff-in-diff on a synthetic policy change with known ground truth; recover the
  effect; then BREAK parallel trends and watch the estimate lie; (2) build propensity scores with Week-5
  logistic regression, weight the sample, show covariate balance before/after; (3) explain uplift vs
  outcome modeling in one paragraph with a "who to target" example; (4) rank the evidence ladder: RCT >
  quasi-experiment > adjusted observational > raw correlation — with the assumptions each rung leans on.
- Build: DiD with trends plot + the broken-assumption demo + propensity weighting with balance table +
  the evidence-ladder write-up.
- Mistakes: DiD without plotting trends · propensity scores from a model that can't predict treatment
  (check AUC, then check overlap) · uplift claims from outcome models.
- Connects: Week 5 (logistic), Day 1 (DAGs say WHICH covariates), weekB (SHAP explains, doesn't cause).

**Day 6 — Mini-project + defense: the experiment design doc** (`6.0.experiment-design-defense.md`)
- Build: a COMPLETE experiment design for a real question on Flagship 1 — **"did weekP's reranker improve
  answer quality for users?"** — units (queries? sessions?), driver + guardrail metrics (incl. latency,
  cost/query), power calc from realistic traffic, duration, interference risks, decision rule
  (ship/iterate/kill thresholds pre-registered), and the analysis code stubbed and A/A-tested.
- Deliverable: `weekT_defense.md` = the design doc — this exact artifact is what DS interviews ask
  candidates to produce live; you'll have written a real one.
- Public bar: publishable as post material; feeds the DS branch of Flagship 3.
- Connects: everything this week + weekO (offline evals) — offline evals gate the ship, experiments
  measure the shipped; a candidate who can articulate that boundary is rare.
