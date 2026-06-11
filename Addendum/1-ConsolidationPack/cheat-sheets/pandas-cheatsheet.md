# 🐼 Pandas Cheat Sheet (fill from your own code)
> Harvest from: `1-PythonFundations/week2/pandas_basics.py`, `Pandas_filtering.py`, `2-DataAnalysis_Visualization/week4/*.py`

## Sections to fill
1. **I/O** — read_csv (parse_dates, dtype, usecols), to_csv; caching pattern from Week 8 data_load.py
2. **Inspection** — head/info/describe/value_counts/isna().sum(); the first-5-minutes-with-any-dataset ritual
3. **Selection** — loc vs iloc (label vs position — the eternal confusion), boolean filtering, query
4. **Missing data** — isna, fillna, dropna; MCAR/MAR/MNAR decision notes from Week 4 Day 1
5. **Transformations** — assign, apply vs vectorized (when each), astype, pd.cut/qcut binning
6. **GroupBy** — split-apply-combine mental model; agg with dicts; transform vs agg ⚠️
7. **Merge/join/concat** — how='left/inner', validate=, indicator=; concat axis gotchas
8. **Categorical & encoding** — get_dummies vs sklearn OneHotEncoder (when each — pipeline answer!)
9. **Gotchas log** — SettingWithCopyWarning (and the .loc fix), chained indexing, index alignment surprises
