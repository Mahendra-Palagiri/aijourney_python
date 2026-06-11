# 📑 Week 10 Question Bank — PyTorch
> Covers: tensors, ops/broadcasting, autograd, nn.Module, losses/optimizers, Dataset/DataLoader, train/eval modes, full workflow
> Answers: work in `qb-week10_challenges.py`.

## 🟢 Easy (10)
1. Tensor with shape [] vs [3] vs [2,3] — name each and give a data example (Week-10 Day-1 drill).
2. What does `requires_grad=True` switch on?
3. What do `.backward()` and `.grad` do/contain?
4. Why call `optimizer.zero_grad()` every step? What accumulates otherwise?
5. `reshape` vs `unsqueeze` vs `squeeze` — what does each do to shape [3]?
6. What two methods must every `nn.Module` subclass define/override?
7. What does `nn.Linear(4, 2)` create, parameter-count included?
8. Dataset vs DataLoader — separate responsibilities in one sentence each.
9. `model.train()` vs `model.eval()` — what layers behave differently?
10. What does `torch.no_grad()` save, and where in the workflow does it belong?

## 🟡 Medium (10)
1. Broadcasting: predict the result shape of [3,1] + [1,4], and of [2,3] + [3]. State the two broadcasting rules.
2. Why must the input feature count match a Linear layer's first dimension? What error do you get otherwise (recall Week-10 Day-1)?
3. Draw the computation graph for z = (x·w).sum(); what is dz/dw and why does autograd agree?
4. Gradient accumulation: when is it a FEATURE (large effective batch), and how is it implemented deliberately?
5. Why do we train on logits + `CrossEntropyLoss` instead of softmax + NLL manually? Numerical-stability argument.
6. SGD vs Adam: what extra state does Adam keep per parameter, and what problem does it solve?
7. `TensorDataset` + `DataLoader(shuffle=True)`: why shuffle train but never validation/test?
8. What goes wrong if you forget `model.eval()` before validation when the model has dropout?
9. In-place ops (`x += 1`) can break autograd — why, mechanically?
10. Map every line of the canonical training loop to its Week-9 concept (forward, loss, backward, step, zero).

## 🔴 Tricky (5)
1. `loss.backward()` is called twice without `zero_grad` — write the exact contents of `.grad` after each call.
2. A tensor view shares memory with its base; show how modifying a view corrupts the original and when autograd will scream.
3. Why does `.detach()` exist? Give a real use (e.g., logging loss, target networks) and what graph edge it cuts.
4. Explain why DataLoader's last batch can be smaller, and find a line of model code that silently breaks because of it (hard-coded batch dims).
5. Reproduce a wrong-loss-shape bug: CrossEntropyLoss with targets shaped [N,1] instead of [N] — what happens and why?

## 🧪 Coding Challenges (5) — implement in `qb-week10_challenges.py`
1. Rebuild the Week-10 end-to-end workflow from a BLANK file, from memory, in <60 lines. Compare with the original.
2. Implement a manual SGD step (p -= lr*p.grad inside no_grad) and match `torch.optim.SGD` losses for 10 steps.
3. Write a custom Dataset class for the Titanic CSV (numeric features) and train the Week-10 model on it.
4. Demonstrate broadcasting mastery: implement standardization (x-mean)/std over a [N,F] batch without loops.
5. Save/load: `state_dict` round-trip; prove the reloaded model gives bit-identical predictions.
