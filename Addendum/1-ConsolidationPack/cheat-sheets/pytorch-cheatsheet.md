# 🔥 PyTorch Cheat Sheet (fill from your own code)
> Harvest from: weeks 9–12, especially `4-DeepLearningFoundations/week10/*.py`, `week11/*.py`

## Sections to fill
1. **Tensors** — creation, dtype/device, shape vocabulary ([]=scalar, [3]=vector, [2,3]=2 samples × 3 features)
2. **Shape surgery** — reshape, view, squeeze/unsqueeze, flatten, permute; the [N,C,H,W] table with worked examples
3. **Autograd** — requires_grad, backward(), .grad, zero_grad ⚠️accumulation, no_grad, detach
4. **nn.Module template** — the canonical class skeleton (init + forward), pasted from Week 10 and annotated
5. **Layers used so far** — Linear, ReLU, Conv2d(in,out,k,s,p), MaxPool2d, Flatten (+param-count formulas: Linear=(in+1)·out, Conv=(k·k·Cin+1)·Cout)
6. **Conv output-size formula** — out = (n + 2p − k)/s + 1, with your Week-11 worked examples
7. **Losses & optimizers** — CrossEntropyLoss (logits+class indices!), MSELoss; SGD vs Adam and when
8. **Data** — Dataset/TensorDataset/DataLoader(batch_size, shuffle train only)
9. **The canonical training loop** — train(): forward→loss→zero_grad→backward→step; eval(): eval()+no_grad
10. **Persistence** — state_dict save/load round-trip
11. **Gotchas log** — the five Week-11 common mistakes + every shape error you hit, with exact error text
