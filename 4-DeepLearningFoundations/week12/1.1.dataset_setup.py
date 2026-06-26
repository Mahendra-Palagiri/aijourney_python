import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from torchvision import datasets,transforms
from torchvision.datasets import FashionMNIST

# =============================================================================
# Basic settings
# =============================================================================
BATCH_SIZE=64
RANDOM_SEED = 42
torch.manual_seed(RANDOM_SEED)

# =============================================================================
# Transform
# =============================================================================
transform = transforms.ToTensor()

# =============================================================================
# Load FashionMNIST dataset
# =============================================================================
# Torchvision combines:
# mirror + filename
#
# So we override the mirror only.
# Do not replace FashionMNIST.resources with full URLs.
FashionMNIST.mirrors = [
    "https://github.com/zalandoresearch/fashion-mnist/raw/master/data/fashion/"
]

train_full= datasets.FashionMNIST(
    root="4-DeepLearningFoundations/week12/data", #Root directory of data set
    train=True, #True for training and False for testing
    download=True, #Downloads from internet if data doesnt exists in local root folder
    transform=transform #Transforms the data to tensor
)

test_data = datasets.FashionMNIST(
    root="4-DeepLearningFoundations/week12/data",
    train=False,
    download=True,
    transform=transform
)

# =============================================================================
# training and validation data split
# =============================================================================
train_size = int(0.8 * len(train_full)) #80% data for training
val_size = int(0.2 * len(train_full)) # 20% data for validation

train_data, val_data = random_split(
    train_full,
    [train_size,val_size],
    generator=torch.Generator().manual_seed(RANDOM_SEED)
    )

# =============================================================================
# DataLoaders
# =============================================================================
train_loader = DataLoader(
    train_data,
    batch_size=BATCH_SIZE,
    shuffle=True
)

val_loader = DataLoader(
    val_data,
    batch_size=BATCH_SIZE,
    shuffle=False
)

test_loader = DataLoader(
    test_data,
    batch_size=BATCH_SIZE,
    shuffle=False
)

print("")
print(f"{'='*30} OUTPUT {'='*30}" )
# =============================================================================
# Dataset Size Checks
# =============================================================================
print("Train size:", len(train_data))
print("Validation size:", len(val_data))
print("Test size:", len(test_data))
print("Train size type:", type(train_size))
print("Validation size type:", type(val_size))

# =============================================================================
# Inspect one batch
# =============================================================================
images, labels = next(iter(train_loader))

print("\nImages shape:", images.shape)
print("Labels shape:", labels.shape)
print("Image dtype:", images.dtype)
print("Label dtype:", labels.dtype)

# =============================================================================
# Inspect one image and label
# =============================================================================
single_image = images[0]
single_label = labels[0]

print("\nSingle image shape:", single_image.shape)
print("Single label:", single_label.item())

# ============================================================================
# Class names
# =============================================================================
class_names = train_full.classes

print("\nClass names:")
print(class_names)
print("\nSample label mapping:")
print("Label index:", single_label.item())
print("Class name:", class_names[single_label.item()])

# =============================================================================
# Shape summary
# =============================================================================
print("\nShape summary:")
print("One image:        [1, 28, 28]")
print("One batch:        [64, 1, 28, 28]")
print("One label:        integer from 0 to 9")
print("One label batch:  [64]")
print("Baseline input:   [64, 1, 28, 28] -> [64, 784]")
print("Improved input:   [64, 1, 28, 28] stays image-shaped longer")

print("")

'''============================== OUTPUT ==============================
Train size: 48000
Validation size: 12000
Test size: 10000
Train size type: <class 'int'>
Validation size type: <class 'int'>

Images shape: torch.Size([64, 1, 28, 28])
Labels shape: torch.Size([64])
Image dtype: torch.float32
Label dtype: torch.int64

Single image shape: torch.Size([1, 28, 28])
Single label: 9

Class names:
['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

Sample label mapping:
Label index: 9
Class name: Ankle boot

Shape summary:
One image:        [1, 28, 28]
One batch:        [64, 1, 28, 28]
One label:        integer from 0 to 9
One label batch:  [64]
Baseline input:   [64, 1, 28, 28] -> [64, 784]
Improved input:   [64, 1, 28, 28] stays image-shaped longer
'''