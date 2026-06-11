# 📑 Week 7 Question Bank — Model Selection & Validation
> Covers: bias-variance, splits & leakage, k-fold/stratified/repeated/nested CV, time-series split, tuning with pipelines, model comparison
> Answers: work in `qb-week7_challenges.py`.

## 🟢 Easy (10)
1. Model selection vs model assessment — what do you tune vs what do you report?
2. Define bias and variance in terms of what happens across different training samples.
3. Symptoms checklist: how do train/val scores look under underfitting? Overfitting?
4. Why does the validation set get "used up" during tuning?
5. Describe k-fold CV in 4–5 steps from memory (Week-7 Day-3 drill).
6. What does stratified k-fold guarantee, and for which problem type is it the default?
7. What is data leakage in one sentence? Give two concrete examples from earlier weeks.
8. Why must preprocessing live *inside* the CV loop (pipeline), not before it?
9. GridSearchCV vs RandomizedSearchCV — when is random search clearly better?
10. Why can't you shuffle time-series data for CV?

## 🟡 Medium (10)
1. Explain the bias-variance decomposition of expected error conceptually (bias² + variance + noise). What does each term respond to?
2. Small k (3) vs large k (10): trade-offs in estimate bias, variance, and compute. Why is LOOCV high-variance?
3. Nested CV: draw the loop structure in pseudo-code. What question does the *outer* loop answer that plain GridSearchCV cannot?
4. CV mean 0.85 ± 0.02 vs 0.87 ± 0.09 — which model do you ship and what's the argument?
5. Repeated CV: what source of noise does it average away, and what does it NOT fix?
6. Why is tuning on CV scores and then reporting the best CV score optimistically biased? (Winner's curse.)
7. Learning curves: sketch the train/val curves for (a) high bias, (b) high variance. What action does each suggest?
8. TimeSeriesSplit mechanics: how do folds grow, and why is the test fold always "in the future"?
9. A teammate standardizes the full dataset, then runs CV. Quantify the kind of leakage and when it's most damaging (small n, why?).
10. Why is accuracy "a trap" for imbalanced problems even within CV? Which scoring strings do you pass to sklearn instead?

## 🔴 Tricky (5)
1. Prove every row is validated exactly once in k-fold CV, and trained on k−1 times. What property of the estimate does this give?
2. The CV folds' scores are not independent (shared training data). Why does this make the naive std an imperfect uncertainty measure?
3. Construct a leakage scenario where CV score is perfect but production fails (hint: duplicate/near-duplicate rows across folds, or group leakage).
4. Why does selecting the best of 50 models by CV inflate the expected reported score even with honest folds? Connect to multiple comparisons.
5. When would you deliberately accept a higher-bias model? Give a stability/maintainability argument like Week-8's defense.

## 🧪 Coding Challenges (5) — implement in `qb-week7_challenges.py`
1. Empirically show bias-variance: fit polynomial degrees 1–15 over 100 bootstrap samples; plot avg prediction vs truth (bias) and spread (variance).
2. Implement stratified k-fold by hand (preserve class ratios per fold); verify ratios.
3. Run nested CV (inner GridSearch, outer 5-fold) and compare its honest estimate vs naive best-CV-score on the same data.
4. Build group-aware CV: synthetic data where rows share a `group_id`; show GroupKFold vs KFold score gap.
5. Plot learning curves for LogisticRegression vs RandomForest on Titanic; diagnose which is bias- vs variance-limited.
