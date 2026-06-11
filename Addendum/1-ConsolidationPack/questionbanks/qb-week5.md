# 📑 Week 5 Question Bank — Classification Deep Dive (Logistic Regression)
> Covers: sigmoid, odds/log-odds, coefficient interpretation, metrics, thresholds, ROC/AUC, L1/L2, tuning
> Answers: work in `qb-week5_challenges.py`.

## 🟢 Easy (10)
1. Why can't we use plain linear regression for binary classification? Two distinct reasons.
2. Write the sigmoid formula. What are σ(0), σ(+∞), σ(−∞)?
3. What are odds? Convert p = 0.8 to odds, and odds = 3 to p.
4. What quantity is linear in the features in logistic regression?
5. What does `model.coef_` mean on the log-odds scale?
6. Why is 0.5 the "default" threshold, and why is it not sacred?
7. Define sensitivity and specificity in confusion-matrix terms.
8. What loss does logistic regression minimize (name and formula)?
9. What do L1 and L2 penalties add to the loss, respectively?
10. In sklearn's LogisticRegression, what does `C` control, and is bigger C more or less regularization?

## 🟡 Medium (10)
1. Show that the log-odds (logit) of σ(z) equals z. Why does this make coefficients interpretable?
2. A coefficient of 0.7 on `Sex_female`: interpret it as an odds ratio (e^0.7 ≈ 2). Say it in one sentence.
3. Why is squared error a bad loss for probabilities (think gradient when very wrong + non-convexity)?
4. Derive the gradient of log-loss for one sample: (p − y)·x. What's elegant about it?
5. Why does L1 zero out coefficients while L2 only shrinks? Geometric argument (diamond vs circle).
6. When recall matters more than precision, which direction do you move the threshold and why? Give a real scenario.
7. Class weights vs resampling vs threshold-moving for imbalance — mechanics and trade-offs of each.
8. Why must regularized logistic regression have scaled features for the penalty to be fair?
9. What does `predict_proba` calibration mean? How would you check it (reliability curve)?
10. Why can perfect separation make unregularized logistic-regression coefficients blow to infinity?

## 🔴 Tricky (5)
1. Prove the decision boundary of logistic regression is linear in feature space, despite the nonlinear sigmoid.
2. Two models, same accuracy, different log-loss. What does the lower log-loss model do better? Construct a tiny example.
3. AUC is unchanged by any monotonic transform of scores — why? What does that say about AUC and calibration?
4. With L1 and two perfectly correlated features, what does the solver do? Is the chosen feature meaningful?
5. Odds-ratio interpretation breaks for a feature that also appears in an interaction term — explain why.

## 🧪 Coding Challenges (5) — implement in `qb-week5_challenges.py`
1. Implement logistic regression from scratch (sigmoid + gradient descent on log-loss); match sklearn coefficients on synthetic data.
2. Plot how the sigmoid output and decision boundary shift as w and b vary (small interactive grid of subplots).
3. Sweep thresholds 0→1 on the Titanic model; plot precision, recall, F1 vs threshold; mark the F1-optimal point.
4. Fit L1 paths: coefficients vs C on a log scale (`np.logspace`), reproduce the "features entering one by one" plot.
5. Build a reliability (calibration) curve for your Week-5 model; compare raw vs `CalibratedClassifierCV`.
