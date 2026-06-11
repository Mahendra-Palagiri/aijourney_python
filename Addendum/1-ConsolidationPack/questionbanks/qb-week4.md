# 📑 Week 4 Question Bank — Preprocessing & Feature Engineering
> Covers: missing data (MCAR/MAR/MNAR), outliers, scaling, encoding, feature selection, multicollinearity/VIF
> Answers: work in `qb-week4_challenges.py`.

## 🟢 Easy (10)
1. Define MCAR, MAR, MNAR with one concrete example each (not the ones from the lesson).
2. Why does mean imputation distort variance? What does it do to a histogram?
3. Median vs mean imputation — when does the difference matter most?
4. What is one-hot encoding, and why can't we just label-encode nominal categories for a linear model?
5. What is the dummy-variable trap?
6. StandardScaler vs MinMaxScaler — formula and effect of each.
7. Which model families need feature scaling, and which are indifferent? Why?
8. What is an outlier by the IQR rule? Write the bounds formula.
9. What does `handle_unknown='ignore'` solve in OneHotEncoder?
10. What is the difference between feature selection and feature extraction?

## 🟡 Medium (10)
1. Why is imputing before train/test split a form of leakage? What statistic leaks?
2. Z-score vs IQR outlier detection: when do they disagree, and which is robust to the outliers themselves?
3. Log transform: which shapes of distribution does it help, and why does it linearize multiplicative effects?
4. Target encoding of categories: what is it, and why does it leak catastrophically without CV-style fitting?
5. High-cardinality categorical (1,000 cities) — give three handling strategies and their trade-offs.
6. Explain correlation vs multicollinearity. Why can VIF be high when no pairwise correlation is?
7. Write the VIF formula in terms of R² of regressing one feature on the others. Interpret VIF = 10.
8. Why does multicollinearity inflate coefficient *variance* but not necessarily hurt *predictions*?
9. SelectKBest vs model-based importance vs RFE — what does each actually measure?
10. An ordinal feature (S/M/L/XL): one-hot or integer-encode? Argue both sides, pick one for a linear model.

## 🔴 Tricky (5)
1. MNAR salary data: prove that no imputation using observed data alone can be unbiased. What outside info would fix it?
2. You one-hot encode after splitting; the test set has an unseen category. Trace exactly what breaks in the pipeline and the two correct fixes.
3. StandardScaler on a feature that is 99% zeros (sparse) — what happens and why is it usually wrong?
4. Two perfectly collinear features in OLS: what happens to the normal equations? (Hint: X'X invertibility.)
5. Feature selection inside vs outside CV: explain the selection-bias experiment (Ambroise & McLachlan) in your own words.

## 🧪 Coding Challenges (5) — implement in `qb-week4_challenges.py`
1. Build a ColumnTransformer pipeline (impute→scale numeric, impute→one-hot categorical) on Titanic and CV it leakage-free.
2. Implement IQR-based outlier capping (winsorizing) as a custom sklearn transformer with fit/transform.
3. Compute VIF for all Titanic numeric features by hand (loop of linear regressions) and rank them.
4. Demonstrate target-encoding leakage: naive vs out-of-fold target encoding, compare CV scores honestly.
5. Show that tree models are scale-invariant: same RandomForest accuracy with and without StandardScaler.
