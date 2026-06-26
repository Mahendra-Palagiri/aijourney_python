import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from basedata import train_loader,val_loader,test_loader,printdatalengths
from imporvedimagemodel import ImprovedImageModel

LEARNING_RATE = 0.001

print("")
print(f"{40*'='} OUTPUT {40*'='}")

#=============================== Dataset Checks ===============================================
printdatalengths() #Check the orignal data lengths

images,labels = next(iter(train_loader))
print(f"\nInput batch Shape :: {images.shape}")
print(f"Input Labels Shape :: {labels.shape}")

#=============================== Improved model check =========================================
improved_model = ImprovedImageModel()
print(f"\nImproved Image Model :: {improved_model}")

logits = improved_model(images)
print(f"\nOuput Logits Shape :: {logits.shape}")

#Inspecting intermediate shapes
features = improved_model.features(images)
flattened = improved_model.flatten(features)
logits_from_parts = improved_model.classifier(flattened)

print("\nIntermediate shape check:")
print("Input shape:     ", images.shape)
print("Feature shape:   ", features.shape)
print("Flattened shape: ", flattened.shape)
print("Logits shape:    ", logits_from_parts.shape)

#=============================== Prediction====================================================
predictions = torch.argmax(logits,dim=1)

print("\nPredictions shape:", predictions.shape)
print("First 10 predictions:", predictions[:10])
print("First 10 labels:", labels[:10])

#=============================== Loss function ================================================
loss_fn = nn.CrossEntropyLoss()
loss = loss_fn(logits,labels)
print("\nLoss before training:", loss.item())

#=============================== Optimizer ====================================================
optimizer = torch.optim.Adam(improved_model.parameters(),lr=LEARNING_RATE)
print(f"\n Optimizer :: {optimizer}")


print("")

'''======================================== OUTPUT ========================================
length of Training data set :: 48000
length of Validation data set :: 12000
length of Test data set :: 10000

Input batch Shape :: torch.Size([64, 1, 28, 28])
Input Labels Shape :: torch.Size([64])

Improved Image Model :: ImprovedImageModel(
  (features): Sequential(
    (0): Conv2d(1, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): ReLU()
    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (3): Conv2d(16, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (4): ReLU()
    (5): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (classifier): Linear(in_features=1568, out_features=10, bias=True)
)

Ouput Logits Shape :: torch.Size([64, 10])

Intermediate shape check:
Input shape:      torch.Size([64, 1, 28, 28])
Feature shape:    torch.Size([64, 32, 7, 7])
Flattened shape:  torch.Size([64, 1568])
Logits shape:     torch.Size([64, 10])

Predictions shape: torch.Size([64])
First 10 predictions: tensor([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
First 10 labels: tensor([9, 8, 2, 6, 9, 0, 3, 5, 2, 1])

Loss before training: 2.309687376022339

 Optimizer :: Adam (
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