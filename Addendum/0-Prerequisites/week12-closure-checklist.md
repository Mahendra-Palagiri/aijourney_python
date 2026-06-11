# ✅ Prerequisite Part 1 — Close Out Week 12 (main repo)

> **The full Addendum start-gate is the ENTIRE main course** (this checklist + Phases 5–6 / Weeks 13–20
> built and completed in the main repo, the usual way). Then revise Addendum Modules 4–5, then run
> `../CHECKLIST.md`. This file covers only the Week-12 portion.

The Week-12 deep-learning capstone in `4-DeepLearningFoundations/week12/` has an excellent
`0.0.framing.md` but all 13 implementation files are empty. **Nothing in this Addendum starts
until every box below is checked**, because Modules 4 & 5 reuse this capstone's model and workflow.

## Checklist (follows the existing file scaffold — fill those files, in order)

- [ ] `1.1.dataset_setup.py` — load image dataset (FashionMNIST or MNIST), build train/val/test splits,
      DataLoaders; print and verify batch shapes `[N, C, H, W]` before any modeling
- [ ] `1.0.dataset_setup.md` — record dataset choice rationale + shape inspection notes
- [ ] `2.x baseline model` — fully connected baseline: Flatten → Linear → ReLU → Linear → logits;
      justify layer sizes; count parameters
- [ ] `3.x baseline training` — CrossEntropyLoss + optimizer + training loop (Week-10 workflow);
      record train/val loss curves and accuracy
- [ ] `4.x CNN model` — Conv2d → ReLU → MaxPool2d (×2) → Flatten → Linear; verify shapes layer by layer
      (Week-11 Day 6 discipline)
- [ ] `5.x CNN training` — identical training/eval protocol as baseline (fair comparison; same seeds,
      same epochs, same splits)
- [ ] `6.x comparison` — table: params, train loss, val loss, val acc, test acc (test used ONCE);
      learning-curve plots side by side
- [ ] `7.0.retrospective.md` — model defense (architecture, loss, optimizer, shapes, results, risks)
      + retrospective connecting Weeks 9/10/11
- [ ] Update main `README.md` Week-12 row to ✅ with completion month
- [ ] Continue the main course: build and complete Phases 5–6 (Weeks 13–20) in the main repo as planned
- [ ] Then: revise Addendum Modules 4–5 against the finished main course, and start `../CHECKLIST.md`

## Definition of done
Same bar as Week 8: leakage-safe, reproducible (fixed seeds), honest single-use test set,
and a defense document a stranger could challenge you on.
