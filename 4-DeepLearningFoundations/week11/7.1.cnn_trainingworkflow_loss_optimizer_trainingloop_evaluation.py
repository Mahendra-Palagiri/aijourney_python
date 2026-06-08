import torch
import torch.nn as nn


# =============================================================================
# Build a small model
# =============================================================================
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
    
        self.features = nn.Sequential(
            nn.Conv2d(in_channels=1,out_channels=8,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(in_channels=8,out_channels=16,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.classifier = nn.Linear(16*7*7,10)

    def forward(self, x):
        x = self.features(x)
        x = x.reshape(x.shape[0], -1)
        x = self.classifier(x)
        return x
    


# =============================================================================
# Initialize Model, Optimizer and loss functions 
# =============================================================================
model = SimpleCNN()
loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# =========================================================================================
# Create the images initial object and lables (Labels can be considered as expected outputs) 
# ==========================================================================================
images = torch.rand(32,1,28,28)
labels = torch.randint(0,10,(32,)) #Creates 32 elments with each element between 0-9

print("")
print(f"\n{'~'*20} OUTPUT {'~'*20} ")
print(f"Images Shape : {images.shape}")
print(f"Labels Shape : {labels.shape}")

'''~~~~~~~~~~~~~~~~~~~~ OUTPUT ~~~~~~~~~~~~~~~~~~~~ 
Images Shape : torch.Size([32, 1, 28, 28])
Labels Shape : torch.Size([32])
'''

# =========================================================================================
# Train the model
# ==========================================================================================
model.train()

print(f"\n{'~'*20} OUTPUT {'~'*20} ")
for epoch in range(5):
    outputs = model(images)
    loss = loss_function(outputs,labels)

    optimizer.zero_grad() #reset gradients for each batch
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

'''~~~~~~~~~~~~~~~~~~~~ OUTPUT ~~~~~~~~~~~~~~~~~~~~ 
Epoch 1, Loss: 2.3253
Epoch 2, Loss: 2.3556
Epoch 3, Loss: 2.2437
Epoch 4, Loss: 2.2368
Epoch 5, Loss: 2.2241
'''

# =========================================================================================
# Evaluate the model
# ==========================================================================================
model.eval()

with torch.no_grad():
    outputs = model(images)
    predictions = torch.argmax(outputs, dim=1)
    accuracy = (predictions == labels).float().mean()

print(f"\n{'~'*20} OUTPUT {'~'*20} ")
print("Output shape:", outputs.shape)
print("Prediction shape:", predictions.shape)
print("Accuracy:", accuracy.item())

'''~~~~~~~~~~~~~~~~~~~~ OUTPUT ~~~~~~~~~~~~~~~~~~~~ 
Output shape: torch.Size([32, 10])
Prediction shape: torch.Size([32])
Accuracy: 0.15625
'''



print("")



''' ================ RETROSPECTION ========================

Q1. Why did we use a different loss function in Week 11 compared with earlier Week 9/10 examples?

Answer:
The loss function changed because the prediction task changed, not simply because we are using a CNN.

Earlier examples were mostly binary classification:
    - Output usually looked like [N, 1]
    - The model predicted one yes/no style score
    - A suitable loss was BCEWithLogitsLoss

Day 7 uses a 10-class classification setup:
    - Output looks like [N, 10]
    - The model gives 10 scores per image
    - Only one class is correct per image
    - A suitable loss is CrossEntropyLoss

Clean rule:
    - Binary classification       → BCEWithLogitsLoss
    - Multi-class classification  → CrossEntropyLoss
    - Regression                  → MSELoss or L1Loss

So:
    CNN + binary classification      → BCEWithLogitsLoss can still be used
    CNN + 10-class classification    → CrossEntropyLoss is the right fit


Q2. I thought cross entropy was mostly for boolean classification. Is CrossEntropyLoss the same as binary cross entropy?

Answer:
No. They are related ideas, but PyTorch gives us different loss functions for different classification setups.

Binary cross entropy is for two-outcome problems:
    - Example: yes/no, true/false, survived/not survived
    - Common PyTorch loss: BCEWithLogitsLoss
    - Typical output shape: [N, 1]

CrossEntropyLoss is for multi-class classification:
    - Example: digit class 0 through 9
    - Common PyTorch loss: CrossEntropyLoss
    - Typical output shape: [N, number_of_classes]
    - Label shape: [N]

In Day 7:
    outputs shape = [32, 10]
    labels shape  = [32]

That means we have 32 images, and each image has 10 class scores.
CrossEntropyLoss compares those 10 scores against the correct class index.

Important:
    We should not apply softmax before CrossEntropyLoss.
    CrossEntropyLoss expects raw logits and handles the softmax-style calculation internally.


Q3. Why did we use Adam here instead of the optimizer we used earlier?

Answer:
The optimizer changed because we chose a practical default for this CNN demo, not because CNNs require Adam.

Both of these are valid optimizers:
    - torch.optim.SGD(...)
    - torch.optim.Adam(...)

SGD is simpler and more manual:
    - Often needs more learning-rate tuning
    - Useful for understanding basic gradient descent behavior

Adam is more adaptive:
    - Often works well quickly in practice
    - Commonly used for small neural-network/CNN demos

The training loop stays the same either way:
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

Clean mental model:
    - Architecture decides the model structure: Linear model, neural network, CNN
    - Task decides the loss function: binary, multi-class, regression
    - Optimizer decides how weights are updated: SGD, Adam, etc.

For Day 7:
    Architecture = CNN
    Task         = 10-class classification
    Loss         = CrossEntropyLoss
    Optimizer    = Adam as a practical default

'''