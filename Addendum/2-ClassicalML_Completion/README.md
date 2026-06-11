# 🌲 Module 2 — Classical ML Completion

Closes the two gaps the analysis flagged in your classical-ML coverage: ensembles were **used but never
understood** (Week 8 treated RF/GBM as black boxes), and model defenses couldn't yet **explain individual
predictions**.

## Week A — Trees & Ensembles (7 days)
| Day | Lesson | Output |
|---|---|---|
| 1 | Decision tree split math (Gini/entropy/gain) | impurity + best-split from scratch |
| 2 | Overfitting & pruning (ccp_alpha) | depth/α tuning experiments |
| 3 | Bagging & Random Forests (variance argument, OOB) | hand-rolled bagger vs RF |
| 4 | Boosting mechanics (AdaBoost → GBM as functional GD) | hand-rolled GBM |
| 5 | XGBoost & LightGBM practice | Week-8 table + 2 rows |
| 6 | Tabular benchmark across datasets | league table + cost columns |
| 7 | Mini-project & defense | `weekA_defense.md` |

## Week B — Interpretability (5 days)
| Day | Lesson | Output |
|---|---|---|
| 1 | Global importance (impurity bias, permutation) | importance_report() |
| 2 | Shapley values — the fair-credit math | exact Shapley by hand |
| 3 | SHAP practice + LIME contrast | waterfall/beeswarm/dependence reads |
| 4 | PDP, ICE & calibration | reliability curves + calibrated model |
| 5 | Fairness & the upgraded defense | fairness_report() + model card |

## Status
- [ ] Week A days 1–7 · - [ ] Week B days 1–5 · - [ ] Defense + model card merged · - [ ] Flip ✅ in Addendum README

New packages: `xgboost`, `lightgbm`, `shap`, `lime` (add to a new addendum-requirements.txt as you go).
