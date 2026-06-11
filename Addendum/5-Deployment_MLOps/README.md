> # ⚠️ DRAFT — DO NOT STUDY AS WRITTEN
> Written June 2026, BEFORE the main course Phase 6 (Weeks 17–20: deployment, MLOps, final capstone) was built.
> **After the main course is finished:** compare each week below against what the main course actually covered,
> delete duplicates, keep only the delta (expected keeper: Week J pytest/SQL/code-structure — verify, don't assume).
> Track the revision in ../CHECKLIST.md.

# 🏗 Module 5 — Deployment & MLOps (the upgraded Phase 6)

The planned Phase 6, made concrete — plus the software-engineering and SQL foundations the analysis found
missing entirely. Ends with the final capstone: a complete ML **system**, defended.

| Week | Theme | Days | Capstone artifact |
|---|---|---|---|
| J | Software engineering for ML: pytest, structure/typing/logging, SQL ×2, git/CI | 5 | tested+typed package, CI green |
| K | Deployment: artifact → FastAPI → Docker → patterns → monitoring/drift → integration | 6 | `weekK_serving_defense.md` |
| L | MLOps: MLflow tracking → registry → data versioning → pipelines → integration | 5 | `weekL_defense.md` + lifecycle diagram |
| M | Final capstone: charter → data layer → modeling → serving → automation → monitoring → defense | 7 | `FINAL_DEFENSE.md` + tag `addendum-v1.0` |

## Standing rules
- Week J's tests + Week K's containers + Week L's tracking are LAWS once learned (no experiment without a
  run ID; no service without tests; no artifact without lineage).
- Reuse over rebuild: Week M assembles J–L components; building anew is a failure mode, not thoroughness.
- New packages: `pytest mypy ruff pre-commit pydantic fastapi uvicorn mlflow dvc pandera prefect` — pin in
  addendum-requirements.txt as encountered (Week J-5 owns the file).

## Status
- [ ] Week J · - [ ] Week K · - [ ] Week L · - [ ] Week M → flip ✅ in Addendum README → 🎓
