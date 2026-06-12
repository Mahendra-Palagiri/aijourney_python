import torch
import torch.nn as nn
from torch.utils.data import DataLoader,random_split
from torchvision import transforms
from torchvision.datasets import FashionMNIST
from baselineModel import BaselineNN
from util import UtilHelper

#==========================================================================
#Basic Settings
#==========================================================================
BATCH_SIZE = 64
RANDOM_SEED = 42

INPUT_SIZE = 1 * 28 * 28
HIDDEN_SIZE = 128
NUM_CLASSES = 10
LEARNING_RATE = 0.001
EPOCHS = 5

torch.manual_seed(RANDOM_SEED) #makes PyTorch’s random choices more repeatable.

# =============================================================================
# Data Setup
# =============================================================================
transform = transforms.ToTensor()

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

#loss function
loss_fn = nn.CrossEntropyLoss()

#Optimizer
optimizer = torch.optim.Adam(params=baseline_model.parameters(), lr=LEARNING_RATE)


# =============================================================================
# Train baseline model
# =============================================================================

baseline_history =[]
print(f"\nTraining baseline model....")
util_helper = UtilHelper()

for epoch in range(EPOCHS):

    train_loss, train_acc = util_helper.train_one_epoch(baseline_model,train_loader,loss_fn,optimizer)
    
    val_loss, val_acc = util_helper.evaluate(baseline_model,val_loader,loss_fn)

    epoch_result = {
        "epoch": epoch + 1,
        "train_loss": train_loss,
        "train_acc": train_acc,
        "val_loss": val_loss,
        "val_acc": val_acc
    }

    baseline_history.append(epoch_result)

    print(
        f"Epoch {epoch + 1}/{EPOCHS} | "
        f"Train Loss: {train_loss:.4f} | "
        f"Train Acc: {train_acc:.4f} | "
        f"Val Loss: {val_loss:.4f} | "
        f"Val Acc: {val_acc:.4f}"
    )

# -----------------------------
# Final baseline result
# -----------------------------
final_baseline_result = baseline_history[-1]

print("\nFinal baseline result:")
print(final_baseline_result)

# ----------------------------
# Phase 3 completion message
# -----------------------------
print("\nPhase 3 complete: baseline model has been trained and evaluated.")
print("Next phase: build the improved image-aware model.")

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

Training baseline model....
Epoch 1/5 | Train Loss: 2.2682 | Train Acc: 0.1875 | Val Loss: 2.2072 | Val Acc: 0.1020
Epoch 2/5 | Train Loss: 2.2738 | Train Acc: 0.0625 | Val Loss: 2.1298 | Val Acc: 0.1588
Epoch 3/5 | Train Loss: 2.0944 | Train Acc: 0.1875 | Val Loss: 2.0677 | Val Acc: 0.2581
Epoch 4/5 | Train Loss: 2.0839 | Train Acc: 0.1875 | Val Loss: 2.0026 | Val Acc: 0.3287
Epoch 5/5 | Train Loss: 1.9257 | Train Acc: 0.4531 | Val Loss: 1.9351 | Val Acc: 0.3569

Final baseline result:
{'epoch': 5, 'train_loss': 1.9257044792175293, 'train_acc': 0.453125, 'val_loss': 1.935075447400411, 'val_acc': 0.35691666666666666}

Phase 3 complete: baseline model has been trained and evaluated.
Next phase: build the improved image-aware model.
'''



