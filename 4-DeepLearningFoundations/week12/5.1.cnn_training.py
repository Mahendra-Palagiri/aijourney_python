import torch
import torch.nn as nn
from util import UtilHelper
from basedata import train_loader,val_loader,test_loader
from imporvedimagemodel import ImprovedImageModel
from torch.utils.data import DataLoader


LEARNING_RATE = 0.001
EPOCHS = 50


improved_model = ImprovedImageModel()
improved_loss_fn = nn.CrossEntropyLoss()
improved_optimizer = torch.optim.Adam(improved_model.parameters(), lr=LEARNING_RATE)

improved_history = []

print("")
print(f"{40*'='} OUTPUT {40*'='}")
print("\nTraining improved image-aware model...\n")

for epoch in range(EPOCHS):

    util = UtilHelper()
    train_loss, train_acc = util.train_one_epoch(
        improved_model,
        train_loader,
        improved_loss_fn,
        improved_optimizer
    )

    val_loss, val_acc = util.evaluate(
        improved_model,
        val_loader,
        improved_loss_fn
    )

    epoch_result = {
        "epoch": epoch + 1,
        "train_loss": train_loss,
        "train_acc": train_acc,
        "val_loss": val_loss,
        "val_acc": val_acc
    }

    improved_history.append(epoch_result)

    print(
        f"Epoch {epoch + 1}/{EPOCHS} | "
        f"Train Loss: {train_loss:.4f} | "
        f"Train Acc: {train_acc:.4f} | "
        f"Val Loss: {val_loss:.4f} | "
        f"Val Acc: {val_acc:.4f}"
    )

# -----------------------------

# Final improved result

# -----------------------------

final_improved_result = improved_history[-1]

print("\nFinal improved model result:")
print(final_improved_result)

# -----------------------------
# Improved history table
# -----------------------------

print("\nImproved model history:")
print("Epoch | Train Loss | Train Acc | Val Loss | Val Acc")

for row in improved_history:
    print(
        f"{row['epoch']:>5} | "
        f"{row['train_loss']:.4f}     | "
        f"{row['train_acc']:.4f}    | "
        f"{row['val_loss']:.4f}   | "
        f"{row['val_acc']:.4f}"
    )


print("")

'''======================================== OUTPUT ========================================

Training improved image-aware model...

Epoch 1/5 | Train Loss: 2.3298 | Train Acc: 0.0625 | Val Loss: 2.2996 | Val Acc: 0.1490
Epoch 2/5 | Train Loss: 2.2928 | Train Acc: 0.2656 | Val Loss: 2.2883 | Val Acc: 0.1872
Epoch 3/5 | Train Loss: 2.2836 | Train Acc: 0.2656 | Val Loss: 2.2747 | Val Acc: 0.2168
Epoch 4/5 | Train Loss: 2.2653 | Train Acc: 0.2500 | Val Loss: 2.2593 | Val Acc: 0.2473
Epoch 5/5 | Train Loss: 2.2689 | Train Acc: 0.2031 | Val Loss: 2.2386 | Val Acc: 0.2682

Final improved model result:
{'epoch': 5, 'train_loss': 2.268934488296509, 'train_acc': 0.203125, 'val_loss': 2.238579797744751, 'val_acc': 0.26816666666666666}

Improved model history:
Epoch | Train Loss | Train Acc | Val Loss | Val Acc
    1 | 2.3298     | 0.0625    | 2.2996   | 0.1490
    2 | 2.2928     | 0.2656    | 2.2883   | 0.1872
    3 | 2.2836     | 0.2656    | 2.2747   | 0.2168
    4 | 2.2653     | 0.2500    | 2.2593   | 0.2473
    5 | 2.2689     | 0.2031    | 2.2386   | 0.2682

'''