import torch
import torch.nn as nn
from torch.utils.data import DataLoader,random_split
from torchvision.datasets import FashionMNIST
from torchvision import transforms


#==========================================================================
#Basic Settings
#==========================================================================
BATCH_SIZE = 64
RANDOM_SEED = 42

torch.manual_seed(RANDOM_SEED) #makes PyTorch’s random choices more repeatable.

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


def printdatalengths():
    print(f"length of Training data set :: {len(train_data)}")
    print(f"length of Validation data set :: {len(val_data)}")
    print(f"length of Test data set :: {len(test_data)}")