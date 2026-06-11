# 🔬 scikit-learn Cheat Sheet (fill from your own code)
> Harvest from: weeks 3–8, especially `3-MLFoundations/week8/src/pipeline.py` (your best sklearn code)

## Sections to fill
1. **The API contract** — fit / predict / transform / fit_transform; estimator vs transformer; get_params
2. **Splitting** — train_test_split(stratify=, random_state=), KFold, StratifiedKFold, TimeSeriesSplit, GroupKFold
3. **Pipeline & ColumnTransformer** — the Week-8 leakage-safe template, pasted verbatim, annotated
4. **Preprocessing** — SimpleImputer strategies, StandardScaler/MinMaxScaler, OneHotEncoder(handle_unknown=)
5. **Models used so far** — LogisticRegression(C=, penalty=, max_iter=), LinearRegression, Ridge/Lasso/ElasticNet, KNN, RandomForest, GradientBoosting (+ key hyperparameters of each, one line per param)
6. **Metrics** — classification (accuracy, precision, recall, f1, roc_auc, log_loss, confusion_matrix), regression (MAE, MSE, RMSE, R²); scoring= strings for CV
7. **CV & tuning** — cross_val_score, cross_validate, GridSearchCV / RandomizedSearchCV (param grid syntax with pipeline prefixes: `model__C`)
8. **Inspection** — coef_/intercept_, feature_importances_, permutation_importance, get_feature_names_out
9. **Gotchas log** — fitting on test, forgetting stratify, pipeline step naming, refit behavior of SearchCV
