# 📑 Week 3 Question Bank — Intro to ML Workflow
> Covers: sklearn workflow, Iris, KNN, train/test split, metrics, confusion matrix, ROC/AUC, CV, tuning
> Answers: work in `qb-week3_challenges.py`; write text answers below each question, then self-grade.

## 🟢 Easy (10)
1. What are the standard steps of a supervised ML workflow, from raw data to reported result?
2. Why do we split data into train and test sets? What question does the test set answer?
3. What does `fit()` do vs `predict()` in sklearn's API?
4. How does KNN classify a new point? What is the role of `k`?
5. What is accuracy, and when is it a misleading metric?
6. What are the four cells of a confusion matrix? Define each in plain words.
7. Define precision and recall. Which mistake does each one punish?
8. What does `random_state` control and why do we fix it?
9. What is stratification in `train_test_split` and when is it needed?
10. What is the difference between a model's parameters and its hyperparameters?

## 🟡 Medium (10)
1. Walk through what happens to the decision boundary of KNN as k goes 1 → N. Which end overfits?
2. Why must scaling be fit on train only, then applied to test? What goes wrong otherwise?
3. Derive F1 from precision and recall. Why harmonic mean instead of arithmetic?
4. Explain what the ROC curve plots, point by point, as the threshold moves from 1 to 0.
5. What does AUC = 0.5 mean mechanically? AUC = 1.0? AUC = 0.3?
6. Why is k-fold CV a better estimate of generalization than a single validation split?
7. When comparing two models with CV, why look at the std of fold scores, not just the mean?
8. GridSearchCV refits the best model on all training data at the end — why is that valid?
9. Precision–recall curves vs ROC: when is PR the better choice and why (think class imbalance)?
10. Your test accuracy is far below CV accuracy. List three distinct causes and how to check each.

## 🔴 Tricky (5)
1. KNN with k=1 has 100% train accuracy by construction. Prove it, and explain why that's a warning, not a win.
2. You tuned threshold on the test set to maximize F1. Why is the reported F1 now biased? Where should tuning have happened?
3. Accuracy paradox: build (on paper) a 95%-accurate classifier that is useless. What metric exposes it?
4. Why can ROC-AUC stay high while precision collapses when positives are rare? Reason from the definitions.
5. If two features are on scales 0–1 and 0–10,000, what happens to KNN distances? Show with a concrete pair of points.

## 🧪 Coding Challenges (5) — implement in `qb-week3_challenges.py`
1. Implement KNN from scratch (euclidean distance, majority vote) and match sklearn's predictions on Iris.
2. Write a function that computes precision, recall, F1 from a confusion matrix — no sklearn.
3. Plot ROC by hand: sort predicted probabilities, sweep thresholds, accumulate TPR/FPR. Compare to `roc_curve`.
4. Implement 5-fold CV manually (index slicing, no `cross_val_score`) and match sklearn's fold means.
5. Show scaling leakage: fit a scaler on full data vs train-only, report the test-accuracy difference on a synthetic dataset.
