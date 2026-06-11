# 🧮 NumPy Cheat Sheet (fill from your own code — sources noted)
> Harvest from: `1-PythonFundations/week2/numpy_basics.py`, `numpy_advanced.py`, `3-MLFoundations/week6/1.Regression_fromScratch.py`

## Sections to fill (keep examples runnable, 1–3 lines each)
1. **Creation** — array, zeros/ones, arange, linspace, random (with seed!)
2. **Shape & dtype** — .shape/.ndim/.dtype, reshape, ravel, transpose; the [rows, cols] mental model
3. **Indexing & slicing** — basic, boolean masks, fancy indexing; view vs copy ⚠️
4. **Broadcasting rules** — the 2 rules, worked examples [3,1]+[1,4], [2,3]+[3]; common failure shapes
5. **Math & reductions** — elementwise ops, sum/mean/std with `axis=` (the axis mental model — draw it)
6. **Linear algebra** — @, dot, norm, (later: eig, svd from Module 3-D)
7. **Vectorization patterns** — replacing loops; standardize a [N,F] matrix in one line
8. **Gotchas log** — integer division dtype, NaN propagation, in-place vs copy, == vs np.isclose
