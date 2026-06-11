"""
Week E — Day 6: Vanishing Gradients & LSTMs — Why Memory Needs Gates
====================================================================

Practice placeholder — pairs with `6.0.lstm-vanishing-gradients.md` in this folder.

HOW TO USE (when you reach this lesson):
  1. Read the paired markdown FIRST (topics, learning goals, core mechanics).
  2. Work through the "Build in the paired .py" exercises below, in order.
  3. Keep this header docstring; append a short "what I learned / what surprised me"
     note at the bottom when done (the main repo's best habit).

EXERCISES (from the paired markdown):
  1. THE measurement: train vanilla RNN on a synthetic long-dependency task (recall token seen k steps ago) for
  2. Instrument gradients: hook `.grad` norms per time step; log-scale plot of gradient norm vs distance-from-loss 
  3. Same task, nn.LSTM: accuracy vs k again — the rescue, quantified on one overlay plot.
  4. Exploding case: remove clipping on a high learning rate; show loss → NaN; add clip_grad_norm_; stable. Both ru
  5. Upgrade Day-5's name classifier to LSTM; compare accuracy + training curves.

Status: NOT STARTED
"""

# =====================================================================
# Exercise 1
# =====================================================================
# TODO


if __name__ == "__main__":
    print("Lesson placeholder — see paired markdown: 6.0.lstm-vanishing-gradients.md")
