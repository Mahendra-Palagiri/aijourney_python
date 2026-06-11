# 📑 Week 9 Question Bank — Neural Network Foundations
> Covers: why NNs, anatomy, forward prop, activations, loss & gradient descent, backprop/chain rule, training dynamics
> Answers: work in `qb-week9_challenges.py`.

## 🟢 Easy (10)
1. Why can't stacked linear layers (no activation) represent anything more than one linear layer? 
2. Name the parts: layer, neuron, weight, bias. What is "learned" and what is "architecture"?
3. Write the computation of a single neuron with inputs x, weights w, bias b, activation f.
4. ReLU, sigmoid, tanh — formulas, output ranges, and one typical use of each.
5. What is forward propagation, in one sentence?
6. What does the loss function measure, and why must it be differentiable?
7. Gradient descent update rule — write it and name every symbol.
8. What is an epoch? A batch? A learning rate?
9. What question does backpropagation answer for each individual weight?
10. What are the symptoms of overfitting during NN training (curve shapes)?

## 🟡 Medium (10)
1. Explain why non-linearity gives a network its expressive power, using XOR as the canonical counterexample.
2. Chain rule in a 2-layer net: write dLoss/dw1 as a product of local derivatives and name each factor.
3. Why does sigmoid cause vanishing gradients in deep nets? Use its derivative's max value (0.25).
4. Why is ReLU's "dead neuron" problem a thing? What in the gradient causes it?
5. Mini-batch vs full-batch vs single-sample SGD: what does batch size trade off (noise vs speed vs generalization)?
6. Learning-rate too high vs too low: describe the loss curve AND the weight-space picture.
7. Why initialize weights randomly instead of zeros? What symmetry breaks?
8. MSE for regression, cross-entropy for classification — why does pairing cross-entropy with sigmoid/softmax give cleaner gradients?
9. "Backprop is just bookkeeping of the chain rule" — defend this statement with the local-gradient picture from Day 5.
10. Where do gradients get COMPUTED vs APPLIED in the training loop? Map each to a future PyTorch call (backward/step/zero_grad).

## 🔴 Tricky (5)
1. Derive the full gradient for a 1-hidden-neuron network y = w2·ReLU(w1·x + b1) + b2 with MSE loss, by hand.
2. Two networks with identical loss but very different weight magnitudes — which generalizes better and why (margin/regularization intuition)?
3. Why does the SAME learning rate work badly for layers with very different input scales? Connect to Week-6's feature-scaling finding.
4. A 10-layer sigmoid network trains 100× slower in early layers — estimate the gradient attenuation factor and show the math.
5. Universal approximation says one hidden layer suffices — so why go deep? Give the composition/efficiency argument.

## 🧪 Coding Challenges (5) — implement in `qb-week9_challenges.py`
1. Implement forward + backward pass for a 2-layer network in pure NumPy (no autograd); train it on XOR.
2. Verify your NumPy gradients against PyTorch autograd on identical weights (max abs diff < 1e-6).
3. Plot activation functions AND their derivatives on one grid; mark the vanishing-gradient zones.
4. Train the Week-9 tiny PyTorch NN with lr ∈ {1e-4, 1e-2, 1.0}; overlay the three loss curves and explain.
5. Show symmetry breaking: train with zero-init vs random-init on the same data; plot both loss curves.
