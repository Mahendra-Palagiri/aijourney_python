import torch
from torch.utils.data import Subset, DataLoader
from torchvision import datasets, transforms
from torch import nn
from SmallCNN import SmallCNN
from Utils import Utils


# =============================================================================
# Define the pipleines
# =============================================================================
train_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
])

validation_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
])

# =============================================================================
# Dataset Load (We are reusing exisisting data downloads)
# =============================================================================
train_data = datasets.CIFAR10(
    root="5-AppliedAI/week14/Data",
    download=False,
    train=True,
    transform=train_transform
)

val_data = datasets.CIFAR10(
    root="5-AppliedAI/week14/Data",
    download=False,
    train=True,
    transform=validation_transform
)

#Iteraion 1 ::
'''
#Shuffle indices once
indices = torch.randperm(len(train_data)) #RandPerm will shuffle the order of indices of images (the physical images are not reordered its just their indices are considered in random order)

#Select subset of images
train_subset= Subset(train_data,indices[:45000])
val_subset = Subset(val_data,indices[45000:])
'''

#Iteraion 2 ::
#without fixed random seed we might get differnt split wehen the script is run (we will make script repetable)

generator = torch.Generator().manual_seed(42)
indices = torch.randperm(len(train_data),generator=generator)

train_subset= Subset(train_data,indices[:45000])
val_subset = Subset(val_data,indices[45000:])

print(f"train_subset_elements :: {len(train_subset)} \nval_subset_elements :: {len(val_subset)}")
print(f"Overlapping Indices : { len(set(train_subset.indices.tolist()) & set(val_subset.indices.tolist())) }")

''' --- OUTPUT --
train_subset_elements :: 45000 
val_subset_elements :: 5000
Overlapping Indices : 0
'''


# =============================================================================
# Small CCN Baseline
# =============================================================================
train_dataloader = DataLoader(dataset=train_subset,batch_size=64,shuffle=True,num_workers=0)
val_dataloader = DataLoader(dataset=val_subset,batch_size=64,shuffle=False,num_workers=0)

images,labels = next(iter(train_dataloader))
print(f"Images Shape : {images.shape}\nLabels Shape: {labels.shape}")

''' -- OUTPUT ---
Images Shape : torch.Size([64, 3, 32, 32])
Labels Shape: torch.Size([64])
'''

model = SmallCNN()
outputs = model(images)
print(f"Output Shape : {outputs.shape}")

''' --- OUTPUT ---
Intial Shape: torch.Size([64, 3, 32, 32])
Shape After First Convolution: torch.Size([64, 16, 32, 32])
Shape After First Relu: torch.Size([64, 16, 32, 32])
Shape After First Maxpool: torch.Size([64, 16, 16, 16])
Shape After Second Convolution: torch.Size([64, 32, 16, 16])
Shape After Second Relu: torch.Size([64, 32, 16, 16])
Shape After Second Maxpool: torch.Size([64, 32, 8, 8])
Shape After Flattening: torch.Size([64, 2048])
Shape After classifier: torch.Size([64, 10])
Output Shape : torch.Size([64, 10])
'''

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(),lr=0.001, weight_decay=0.0)

train_avg_loss, train_accuracy = Utils.run_one_epoch(model=model,dataloader=train_dataloader,criterion=criterion,optimizer=optimizer,is_training=True)
val_avg_loss, val_accuracy = Utils.run_one_epoch(model=model,dataloader=val_dataloader,criterion=criterion,optimizer=optimizer,is_training=False)

print(f"Training Loss : {train_avg_loss}\nTraining Accuracy : {train_accuracy}\nValidation Loss : {val_avg_loss}\nValidation Accuracy : {val_accuracy}")

''' --- OUTPUT --
Training Loss : 1.5016452167510987
Training Accuracy : 0.46626666666666666
Validation Loss : 1.2917528882980347
Validation Accuracy : 0.544
'''
