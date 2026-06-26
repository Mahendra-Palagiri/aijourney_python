import torch
import torch.nn as nn
from torch.utils.data import DataLoader,random_split
from torchvision import transforms
from torchvision.datasets import FashionMNIST
from baselineModel import BaselineNN

# =============================================================================
# Basic settings
# =============================================================================
BATCH_SIZE=64
RANDOM_SEED = 42

INPUT_SIZE = 1 * 28 * 28 #Size when we flatten the image
HIDDEN_SIZE = 128 #Hidden neural network layer
NUM_CLASSES = 10 #Final output classes from the model
LEARNING_RATE = 0.001

torch.manual_seed(RANDOM_SEED)

# =============================================================================
# Data Setup
# =============================================================================
transform = transforms.ToTensor()

FashionMNIST.mirrors = [
    "https://github.com/zalandoresearch/fashion-mnist/raw/master/data/fashion/"
]

train_full = FashionMNIST(
    root="4-DeepLearningFoundations/week12/data",
    train=True,
    download=True,
    transform=transform
)

test_data = FashionMNIST(
    root="4-DeepLearningFoundations/week12/data",
    train=False,
    download=True,
    transform=transform
)

train_size = int(0.8 * len(train_full))
val_size  = int(len(train_full)-train_size)

train_data, val_data = random_split(
    dataset=train_full,
    lengths=[train_size, val_size],
    generator=torch.Generator().manual_seed(RANDOM_SEED)
)

train_loader = DataLoader(
    dataset=train_data,
    batch_size=BATCH_SIZE,
    shuffle=True
)

val_loader = DataLoader(
    dataset=val_data,
    batch_size=BATCH_SIZE,
    shuffle=False
)

test_loader= DataLoader(
    dataset=test_data,
    batch_size=BATCH_SIZE,
    shuffle=False
)

# =============================================================================
# Applying the base model
# =============================================================================
print("")
print(f"{40*'='} OUTPUT {40*'='}")
baseline_model = BaselineNN(
    input_size=INPUT_SIZE,
    hidden_size=HIDDEN_SIZE,
    num_classes=NUM_CLASSES
)
print(f"\nBaseline_Model : {baseline_model}")

#retrieve set of images and labels
images , labels = next(iter(train_loader))
print(f"\nImages Shape: {images.shape}")
print(f"Labels Shape: {labels.shape}")

#run a foward pass
logits = baseline_model(images)
print(f"\nLogits Shape: {logits.shape}")

#predictions from logits
predictions = torch.argmax(logits,dim=1)
print("\nPredictions shape:", predictions.shape)
print("First 10 predictions:", predictions[:10])
print("First 10 labels:", labels[:10])

#loss function
loss_fun = nn.CrossEntropyLoss()
loss = loss_fun(logits,labels)
print("\nLoss before training:", loss.item())

#Optimizer
optimizer = torch.optim.Adam(params=baseline_model.parameters(), lr=LEARNING_RATE)
print("\nOptimizer:", optimizer)

print("")

'''======================================== OUTPUT ========================================

Baseline_Model : BaselineNN(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (network): Sequential(
    (0): Linear(in_features=784, out_features=128, bias=True)
    (1): ReLU()
    (2): Linear(in_features=128, out_features=10, bias=True)
  )
)

Images Shape: torch.Size([64, 1, 28, 28])
Labels Shape: torch.Size([64])

Logits Shape: torch.Size([64, 10])

Predictions shape: torch.Size([64])
First 10 predictions: tensor([8, 8, 8, 5, 8, 9, 8, 8, 5, 8])
First 10 labels: tensor([9, 8, 8, 5, 2, 8, 9, 4, 1, 5])

Loss before training: 2.2682154178619385

Optimizer: Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    capturable: False
    decoupled_weight_decay: False
    differentiable: False
    eps: 1e-08
    foreach: None
    fused: None
    lr: 0.001
    maximize: False
    weight_decay: 0
)
'''