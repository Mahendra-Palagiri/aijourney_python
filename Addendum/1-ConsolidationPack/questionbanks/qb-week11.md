# 📑 Week 11 Question Bank — CNNs
> Covers: why CNNs, [N,C,H,W], filters/kernels/feature maps, stride/padding output math, pooling, building & training CNNs, shape debugging
> Answers: work in `qb-week11_challenges.py`.

## 🟢 Easy (10)
1. Two reasons fully connected nets are wasteful/wrong for raw images.
2. Name each letter of [N, C, H, W] and give the tensor shape for a batch of 32 RGB 64×64 images.
3. What is a kernel/filter, and what does one filter produce when slid over an image?
4. What does `out_channels=16` mean for Conv2d — how many filters, what output shape contribution?
5. Output-size formula for one spatial dim: write it (with kernel k, stride s, padding p, input n).
6. What does padding=1 with kernel 3 achieve, and why is that pairing so common?
7. MaxPool vs AvgPool — what does each keep?
8. Why do we Flatten before the final Linear layer? What shape goes in?
9. Which loss for multi-class image classification, and what shape are logits/targets?
10. A grayscale dataset gives images shaped [H,W] — which two dimensions must you add back, and with what calls?

## 🟡 Medium (10)
1. Weight sharing: count parameters of a 3×3 conv (1→16 channels) vs a Linear from 28×28 to 16 units. What's the ratio?
2. Translation equivariance: explain why convolution detects a feature anywhere in the image while a Linear layer cannot.
3. Compute the output shape of: input [1,1,28,28] → Conv(k=5,s=1,p=0) → MaxPool(2) → Conv(k=3,s=1,p=1) → MaxPool(2). Show each step.
4. Stride-2 convolution vs MaxPool for downsampling — compare mechanics and trade-offs.
5. Why does each successive conv layer "see" a larger region of the original image (receptive field)? Compute it for two stacked 3×3 convs.
6. Channels mismatch errors: Conv2d(3,16) receiving [N,1,H,W] — what exact error, and the two legitimate fixes?
7. The flatten-size bug: where does the magic number in the first Linear layer come from, and the two ways to never hard-code it wrong?
8. Why is `CrossEntropyLoss(logits, labels)` correct but `CrossEntropyLoss(softmax(logits), labels)` subtly terrible?
9. What spatial information does pooling destroy, and why might that be fine for classification but fatal for localization?
10. Feature-map visualization: what do early-layer filters tend to learn vs deeper ones, and why does that hierarchy emerge?

## 🔴 Tricky (5)
1. Prove the parameter count of Conv2d is (k·k·C_in + 1)·C_out and verify against PyTorch's `numel()` for one layer.
2. Derive why SAME padding p=(k−1)/2 only works cleanly for odd k. What do frameworks do for even k?
3. A 1×1 convolution has no spatial extent — so what is it for? Give the channel-mixing/bottleneck argument.
4. Show that convolution is a linear operation (it could be written as a giant sparse matrix multiply). Where does the nonlinearity come from?
5. Global average pooling can replace Flatten+Linear — explain how, and what invariance it buys.

## 🧪 Coding Challenges (5) — implement in `qb-week11_challenges.py`
1. Implement 2-D convolution from scratch in NumPy (single channel, arbitrary k/s/p); match `nn.Conv2d` output with the same kernel weights.
2. Write `shape_tracer(model, input_shape)` that prints the tensor shape after every layer (use forward hooks).
3. Hand-design kernels (edge detect, blur, sharpen); apply via Conv2d with frozen weights; visualize feature maps on one image.
4. Rebuild the Week-11 small CNN from memory; verify parameter count by hand vs `sum(p.numel())`.
5. Break it on purpose: introduce each of the five "common CNN mistakes" from Day 7; record each exact error message in comments.
