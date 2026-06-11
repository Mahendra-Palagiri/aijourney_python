# 🔭 Module 3 — Unsupervised Learning + the Math Spine

Fills the two foundational holes from the analysis: **zero unsupervised coverage** (clustering, PCA,
anomaly detection) and the **implicit-only math** (probability, statistics, Bayes, linear algebra, SVD).
Sequenced so the math (Week D) powers the methods (Week C Day 4 especially) — if eigen-intuition is rusty,
do D-4/D-5 BEFORE C-4.

## Week C — Unsupervised (7 days)
| Day | Lesson | Output |
|---|---|---|
| 1 | k-means math & Lloyd's algorithm | from-scratch k-means |
| 2 | Choosing k & validation without labels | stability protocol |
| 3 | DBSCAN & hierarchical | 9-panel shootout |
| 4 | PCA — the math | PCA from scratch (eigen + SVD routes) |
| 5 | PCA in practice & pipelines | eigen-digits, CV over n_components |
| 6 | t-SNE & UMAP, honest reading | the noise-cluster cautionary plot |
| 7 | Anomaly detection + mini-project | `weekC_writeup.md` |

## Week D — Math Foundations (6 days)
| Day | Lesson | Output |
|---|---|---|
| 1 | Probability & distributions | zoo simulations; log-loss = Bernoulli NLL |
| 2 | Sampling, CLT, hypothesis testing | CI coverage experiment; bootstrap AUC |
| 3 | Bayes | grid-Bayes coin; Naive Bayes from scratch |
| 4 | Linear algebra core | transformation zoo; nn.Linear in NumPy |
| 5 | Eigenvectors & SVD | power iteration; SVD image compression |
| 6 | Calculus, gradients & THE MAP | gradient checker; the synthesis diagram |

## Status
- [ ] Week C 1–7 · - [ ] Week D 1–6 · - [ ] The Map drawn · - [ ] Flip ✅ in Addendum README

New packages: `umap-learn` (scipy/sklearn already present).
