# 📑 Week 8 Question Bank — ML Mini-Capstone (workflow defense)
> Covers: end-to-end workflow, leakage-safe pipelines, baseline vs candidates, CV protocol, single-use holdout, model defense
> Answers: work in `qb-week8_challenges.py`. Many questions reference your own `3-MLFoundations/week8/` code — that's the point.

## 🟢 Easy (10)
1. Why does the capstone delete the `alive` column from Seaborn Titanic? Name the failure mode.
2. Why is the test split used exactly once? What dies the moment you peek twice?
3. What's in `config.py` and why freeze the dataclass?
4. Why cache the dataset CSV locally instead of downloading each run?
5. What is the baseline model and why must every project have one?
6. Why ROC-AUC as primary metric for this problem instead of accuracy?
7. What does `infer_basic_schema` do, and why infer instead of hard-coding columns?
8. Why does the preprocessor live inside the Pipeline rather than running before the split?
9. What two numbers does the model comparison table report per model, and why both?
10. List the sections every "model defense" document must contain (from memory).

## 🟡 Medium (10)
1. Trace one CV fold through the pipeline: exactly where does the imputer fit, on which rows?
2. The capstone compares LogReg / RandomForest / GradientBoosting under one protocol. What makes a comparison "fair"? List the controls.
3. LogReg scored 0.864 ± 0.022 in CV. What would make you prefer it over a GBM at 0.871 ± 0.05?
4. Why is `handle_unknown='ignore'` essential in a CV setting specifically?
5. Where would per-class weights enter this codebase if survival classes were 95/5 instead of ~60/40?
6. What would change in the protocol if rows were families (groups)? Which sklearn splitter?
7. Defend median imputation over mean for `age` on Titanic with a distributional argument.
8. The defense lists "risks + next steps". Write three honest risks of the current capstone.
9. Why might the holdout score differ from CV mean even with zero bugs? Two statistical reasons.
10. How would you add probability calibration to this pipeline without breaking CV honesty?

## 🔴 Tricky (5)
1. `train_test_split(..., stratify=y, random_state=42)` — enumerate everything that silently changes if a teammate removes each argument.
2. Suppose feature engineering created `fare_per_family_member` using a statistic computed on the FULL dataframe before splitting. Is that leakage? Under what condition exactly?
3. Your tuned GBM beats LogReg in CV but loses on the holdout. Give the decision procedure: what do you report, what do you ship, what do you NOT do?
4. Why does refitting the chosen pipeline on train+val (not train alone) before the final test evaluation remain honest?
5. Design the next capstone's "pre-registration": what must be written down BEFORE seeing any scores, to keep yourself honest?

## 🧪 Coding Challenges (5) — implement in `qb-week8_challenges.py`
1. Re-run the Week-8 protocol end to end with a different seed; quantify how much the holdout ROC-AUC moves (stability check).
2. Add a fourth candidate (HistGradientBoosting or SVM-with-scaling) under the identical protocol; extend the comparison table.
3. Write a leakage unit test: assert the pipeline's imputer statistics differ across folds (proof it fits per-fold).
4. Add per-fold timing + memory notes to the comparison (cost column) and re-argue model choice including cost.
5. Produce a one-page automated "defense skeleton" generator: script that renders metric tables from `final_eval.py` outputs into markdown.
