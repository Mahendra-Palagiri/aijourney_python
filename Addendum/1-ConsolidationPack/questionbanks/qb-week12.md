# 📑 Week 12 Question Bank — DL Mini-Capstone (fill AFTER closing Week 12)
> Covers: end-to-end DL workflow, baseline vs CNN comparison, evaluation discipline, model defense
> Answers: work in `qb-week12_challenges.py`. Questions reference YOUR actual capstone results — keep them open while answering.

## 🟢 Easy (10)
1. What dataset did you choose and why is it appropriate for a first DL capstone?
2. State your train/val/test sizes and how you guaranteed no overlap.
3. What batch shape enters the baseline model vs the CNN? Why are they different?
4. Why must the baseline be trained with the SAME splits/seeds/epochs as the CNN?
5. How many parameters in your baseline vs your CNN? Which is bigger — and is that what you expected?
6. Which loss and optimizer did you use, and what was the learning rate?
7. What was your single-use test accuracy for the selected model?
8. Where does `model.eval()` + `torch.no_grad()` appear in your capstone, and why there?
9. What is your capstone's equivalent of Week 8's "leakage prevention" section?
10. Name one thing the retrospective says you'd do differently.

## 🟡 Medium (10)
1. Quantify the baseline→CNN improvement. Is the gap big enough to justify CNN complexity? Argue with numbers.
2. Your val curve vs train curve: diagnose bias vs variance for EACH model, with the curve shapes as evidence.
3. Why is comparing best-epoch validation scores between models subtly unfair? What's the honest protocol?
4. If the CNN had scored WORSE than the baseline, list (in order) the three first things to check.
5. How would adding dropout/batch-norm change your training curves? Predict before Module 4-G teaches it.
6. What augmentations would suit your dataset, and which would be label-destroying (e.g., vertical flip on digits)?
7. Estimate the compute cost ratio per epoch (baseline vs CNN) from parameter counts and feature-map sizes. Did wall-clock agree?
8. Where could class imbalance hide in your dataset, and how would you detect it from the confusion matrix?
9. Your test set is used once — so how do you report uncertainty on that single number? (Bootstrap the test predictions.)
10. Translate your capstone's defense into Week-8 language: metric choice, protocol, comparison, risks. What sections were hardest and why?

## 🔴 Tricky (5)
1. Both models see flattened data eventually (CNN flattens late). Express precisely WHERE the CNN's advantage is created.
2. If you re-ran everything with a different seed, which results would move most: baseline acc, CNN acc, or the gap? Why?
3. Early stopping on validation loss is itself a form of hyperparameter tuning — explain what it "spends" and what stays honest.
4. Suppose 5% of test images were near-duplicates of training images. Estimate the inflation effect and how to detect it (hashing — your `.venv` has ImageHash).
5. Defend (or attack) this claim: "the baseline-vs-CNN comparison is the single most informative experiment in the whole curriculum."

## 🧪 Coding Challenges (5) — implement in `qb-week12_challenges.py`
1. Bootstrap your test predictions (1,000 resamples) → 95% CI on test accuracy for both models.
2. Build and plot both confusion matrices; identify the top-3 confused class pairs and SHOW examples of each.
3. Run the seed-stability experiment: 5 seeds × both models; box-plot the accuracy distributions.
4. Mine the errors: visualize the 16 highest-confidence WRONG predictions of the CNN. Hypothesize patterns.
5. Write `predict.py`: load saved state_dict, take one image path, output class + probabilities — your first inference script (bridge to Module 5-K).
