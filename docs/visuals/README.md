# Curated learning visuals

Updated **2026-10-23**. Open the **[status sheet and complete image list](STATUS.md)** for every delivered file, the weekly counts and completion record.

The active set contains **41 PNGs and one retained HTML visualizer**, covering Weeks 1–13 and the existing Week 14 Days 1–2 practice. All review recommendations and the weekly-summary coverage checks are implemented. The status sheet reports coverage by week/day rather than editing history.

Visuals are grouped by learning question. Week 2 now has three companions (array axes, broadcasting/masks, Pandas/plotting); Week 7 has ordinary CV, nested CV and learning curves; Week 10 has batching, autograd state and the training workflow; Week 11 separates spatial arithmetic from RGB/channel shapes. Other weeks use one or more images according to the content. There is no one-image-per-week or one-image-per-day quota.

## Open and maintain

- [Delivered images and completed review items](STATUS.md)
- [Machine-readable active inventory, source mapping and archive hashes](curated-visuals.json)
- [Current refinement drawings](render_refined_guides.py)
- [Original weekly drawings](render_weekly_guides.py)
- [Existing Week 14 drawings](render_week14_guides.py)

```sh
.venv/bin/python docs/visuals/render_refined_guides.py
.venv/bin/python docs/visuals/render_week14_guides.py
.venv/bin/python docs/visuals/verify_learning_flows.py
```

The refinement renderer writes only its 29 declared targets, checks canonical paths, and keeps pre-refinement backups of replaced images. `--only` can select named drawing functions after a focused repair. The weekly renderer uses the current drawing for a revised target, preventing accidental reversion to its earlier layout. The legacy daily text-card renderer remains retired.

## Scope and evidence

- Images complement the full lesson text; they do not replace theory, exercises or answer keys.
- Toy examples are labeled; Week 3's decision regions are schematic, not fitted Iris performance.
- Week 6 interpretation guides distinguish recorded influential rows from schematic residual geometry. The three original experiment plots are preserved.
- Week 8 uses the existing model-defense report. Fold standard deviation is not described as a confidence interval.
- Week 12 uses the approximate recorded validation accuracy and loss; there is no invented final-test score or training curve.
- Week 13 TF-IDF declares raw-count TF, smoothed natural-log IDF, and no normalization in its worked table. Cosine examples use exact geometry. Retrieval shows the stored index supplying search.
- Existing Week 14 practice images remain available. Future curriculum follows the [MasterPlan map](../../MasterPlan/1-PROGRAM-MAP.md); later Addendum visuals are outside this completed pass.

## Recoverable history

- [76 retired daily text cards](archive/text-card-batch/)
- [11 pre-refinement versions](archive/refinement-2026-10-23/)
- [Original Week 14 Day 1 image](archive/week14-originals/1.1.RealImageData_Normalization_Augmentation.png)

The [inventory](curated-visuals.json) records archive hashes. The older [batch progress file](../lesson-visual-progress.json) retains historical mappings; it points to this current inventory rather than treating archived cards as missing work.
