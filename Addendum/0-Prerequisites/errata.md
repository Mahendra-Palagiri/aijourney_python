# 🗒 Errata — known issues in the frozen main repo

The main repo is intentionally frozen (no renames, no edits). This file records known issues so
they are *documented* rather than *fixed*, and so the Addendum avoids repeating them.

## Naming / typos (cosmetic — do not propagate to Addendum)
| Location | Issue |
|---|---|
| `1-PythonFundations/` | "Fundations" → Foundations (also in `docs/curriculum/1-PythonFundations/`) |
| `3-MLFoundations/week6/3.StatsmodelsOLS_InerpretingCoefficients.py` | "Inerpreting" → Interpreting |
| `3-MLFoundations/week7/3.CrossValdiationMechanics_CVMathIntuition.py` | "Valdiation" → Validation |
| `2-DataAnalysis_Visualization/week3/7.challange.py` | "challange" → challenge |
| `4-DeepLearningFoundations/week9/1.WhyNueralNetworksExist.md` | "Nueral" → Neural |

## Structural notes
- Main `README.md` (Week 8 section) references `projects/week8_capstone/`; actual content lives in
  `3-MLFoundations/week8/`.
- `docs/curriculum/5-AppliedAI/` and `docs/curriculum/6-Deployment_FinalCapstone/` are empty folders —
  superseded by Addendum Modules 4 and 5.
- `docs/questionbanks/3.qb-week3.md` is an empty stub (only nav links) — superseded by
  `Addendum/1-ConsolidationPack/questionbanks/qb-week3.md`.
- `3-MLFoundations/week8/notebooks/` is empty (planned for exploration, never used).
- Answer sheets (`docs/answersheet/`) cover weeks 1–2 only — Addendum question banks include their own
  answer-workspace placeholders instead.

## Convention upgrades adopted by the Addendum (not retrofitted to main repo)
- Paired `N.0.theory.md / N.1.practice.py` everywhere (main repo only does this in weeks 10–12)
- Folder names without typos; lowercase-hyphenated week folders
- Every week ends with a written artifact (defense/retrospective/comparison)
