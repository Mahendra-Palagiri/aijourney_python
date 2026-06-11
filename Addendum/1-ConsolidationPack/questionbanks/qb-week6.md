# 📑 Week 6 Question Bank — Regression Deep Dive
> Covers: ŷ=wx+b from scratch, MSE/gradient descent, MAE/RMSE/R², OLS inference, diagnostics, leverage/Cook's, VIF, Ridge/Lasso/ElasticNet
> Answers: work in `qb-week6_challenges.py`.

## 🟢 Easy (10)
1. Write the simple linear model and name every symbol. What does b mean geometrically?
2. MSE formula — why square the residuals at all? Two reasons.
3. What do dw and db represent in gradient descent, in plain words?
4. What happens with a learning rate that's too big? Too small? Describe the loss curve in each case.
5. MAE vs RMSE: which punishes large errors more, and why?
6. Define R². What does R² = 0 mean? Can it be negative — when?
7. In statsmodels OLS output: what is a coefficient's p-value testing, exactly?
8. What is a residual plot, and what does a "good" one look like?
9. Define leverage in one sentence. High leverage ≠ outlier — why?
10. Ridge vs Lasso: which penalty does each use, and what's the headline behavioral difference?

## 🟡 Medium (10)
1. Derive dL/dw and dL/db for MSE on ŷ = wx + b. Show every step.
2. Why does multiplying X by 100 wreck gradient descent unless you shrink the learning rate? Connect to the gradient formula.
3. Adjusted R² vs R²: what is being penalized, and why does plain R² never decrease when adding features?
4. A confidence interval for a coefficient contains 0 — what does that mean for interpretation?
5. Heteroskedasticity: what does it look like in a residual plot, what does it break (predictions or inference?), and one fix.
6. Cook's distance combines residual size and leverage — explain why both are needed to flag influence.
7. Why might removing an influential point be worse than using Ridge? When is each appropriate?
8. Polynomial features can fit non-linearity but explode variance — connect this to Week 7's bias-variance language.
9. Why does Lasso struggle when features are highly correlated, and how does ElasticNet patch this?
10. OLS assumptions: list them and say which matter for prediction vs which matter for p-values/CIs.

## 🔴 Tricky (5)
1. Show that the OLS solution minimizes MSE by setting the gradient to zero → normal equations (matrix form OK).
2. R² on train always improves with more features; design a CV experiment proving test R² doesn't. Predict the curve shape.
3. A single high-leverage point can give a significant slope to pure noise. Construct such a dataset on paper.
4. Why is interpreting individual coefficients dangerous under multicollinearity even when predictions are stable? Use the variance-inflation argument.
5. Log-transforming y changes the error structure: what does the model now assume about errors, and how do you back-transform predictions honestly?

## 🧪 Coding Challenges (5) — implement in `qb-week6_challenges.py`
1. Re-implement Week-6 Day-1 gradient descent, but vectorized for multiple features; verify against sklearn on synthetic data.
2. Implement R² and adjusted R² by hand; reproduce statsmodels' values on the Week-6 dataset.
3. Build the four classic diagnostic plots (residual vs fitted, QQ, scale-location, leverage) without statsmodels' built-ins.
4. Compute Cook's distance manually via the leave-one-out refit definition for a small dataset; compare to statsmodels.
5. Ridge coefficient paths vs alpha (log scale) on correlated synthetic features; show Lasso zeroing vs Ridge shrinking on the same plot.
