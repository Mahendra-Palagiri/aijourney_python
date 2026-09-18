import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt 

# =============================================================================
# Dataset Load
# =============================================================================
imagedata = datasets.CIFAR10(
    download=True,
    root="5-AppliedAI/week14/data",
    train=True,
    transform=None
)

image, label = imagedata[0]

# =============================================================================
# Data Inspection
# =============================================================================
print(f"{30*'~'} INSPECT DATA  {30*'~'}")
print(f"Length of Dataset : {len(imagedata)}")
print(f"Image Classes : {imagedata.classes}")
print(f"Type of Image : {type(image)}")
print(f"Image Size : {image.size}")
print(f"Image Mode : {image.mode}")
print(f"Label : {label}")
print(f"Label Class : {imagedata.classes[label]}")

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INSPECT DATA  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Length of Dataset : 50000
Image Classes : ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
Type of Image : <class 'PIL.Image.Image'>
Image Size : (32, 32)
Image Mode : RGB
Label : 6
Label Class : frog
'''

# =============================================================================
# Display the Image
# =============================================================================
plt.imshow(image)
plt.title(imagedata.classes[label])
plt.axis("off")
# plt.show()

# =============================================================================
# Convert one Image to Tensor and Inspect
# =============================================================================
to_tensor= transforms.ToTensor()
tensor_image = to_tensor(image)
print(f"\n{30*'~'} INSPECT TENSOR IMAGE  {30*'~'}")
print(f"Type of Image : {type(tensor_image)}")
print(f"Image Shape : {tensor_image.shape}")
print(f"Image dtype : {tensor_image.dtype}")
print(f"Image Max : {tensor_image.max()}")
print(f"Image Min : {tensor_image.min()}")

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INSPECT TENSOR IMAGE  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Type of Image : <class 'torch.Tensor'>
Image Shape : torch.Size([3, 32, 32])
Image dtype : torch.float32
Image Max : 1.0
Image Min : 0.0
'''

# =============================================================================
# Apply basic transformation
# =============================================================================
basic_transform = transforms.Compose(
    [transforms.Resize((224,224)),
    transforms.ToTensor()]
)

basic_transformed_image = basic_transform(image)
print(f"\n{30*'~'} INSPECT BASIC TRANSFORMED IMAGE  {30*'~'}")
print(f"Type of Image : {type(basic_transformed_image)}")
print(f"Image Shape : {basic_transformed_image.shape}")
print(f"Image dtype : {basic_transformed_image.dtype}")
print(f"Image Max : {basic_transformed_image.max()}")
print(f"Image Min : {basic_transformed_image.min()}")

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INSPECT BASIC TRANSFORMED IMAGE  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Type of Image : <class 'torch.Tensor'>
Image Shape : torch.Size([3, 224, 224])
Image dtype : torch.float32
Image Max : 1.0
Image Min : 0.0
'''

# =============================================================================
# Apply Normalized transformation
# =============================================================================
normalized_transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
])

normalized_transformed_image = normalized_transform(image)
print(f"\n{30*'~'} INSPECT NORMALIZED TRANSFORMED IMAGE  {30*'~'}")
print(f"Type of Image : {type(normalized_transformed_image)}")
print(f"Image Shape : {normalized_transformed_image.shape}")
print(f"Image dtype : {normalized_transformed_image.dtype}")
print(f"Image Max : {normalized_transformed_image.max().item()}")
print(f"Image Min : {normalized_transformed_image.min().item()}")

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INSPECT NORMALIZED TRANSFORMED IMAGE  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Type of Image : <class 'torch.Tensor'>
Image Shape : torch.Size([3, 224, 224])
Image dtype : torch.float32
Image Max : 1.0
Image Min : -1.0
'''

# =============================================================================
# Label Safe Augumentation (To be completed)
# =============================================================================
labelsafe_transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.RandomHorizontalFlip(0.5),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
])

fig, axes = plt.subplots(2,2,figsize = (12,13))
fig.suptitle("2 x 2 transformations of frog")

for x in range(4):
    labelsafe_transformed_image = labelsafe_transform(image)
    print(f"\n{30*'~'} {x+1} INSPECT LABEL SAFE TRANSFORMED IMAGE   {30*'~'}")
    print(f"Type of Image : {type(labelsafe_transformed_image)}")
    print(f"Image Shape : {labelsafe_transformed_image.shape}")
    print(f"Image dtype : {labelsafe_transformed_image.dtype}")
    print(f"Image Max : {labelsafe_transformed_image.max().item()}")
    print(f"Image Min : {labelsafe_transformed_image.min().item()}")

    row = x//2 #Floor division
    col = x%2 
    display_tensor = labelsafe_transformed_image *0.5+0.5  #Converting from a normalized format to display format
    display_image = display_tensor.permute(1,2,0) #The shape of transfomred image is. [C,H,W] but pyplot requireds in [H,W,C]
    axes[row, col].set_title(f"Frog- Augmentation {x+1}")
    axes[row, col].axis("off")
    axes[row, col].imshow(display_image)


# plt.show()   

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 1 INSPECT LABEL SAFE TRANSFORMED IMAGE   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Type of Image : <class 'torch.Tensor'>
Image Shape : torch.Size([3, 224, 224])
Image dtype : torch.float32
Image Max : 1.0
Image Min : -1.0

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2 INSPECT LABEL SAFE TRANSFORMED IMAGE   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Type of Image : <class 'torch.Tensor'>
Image Shape : torch.Size([3, 224, 224])
Image dtype : torch.float32
Image Max : 1.0
Image Min : -1.0

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3 INSPECT LABEL SAFE TRANSFORMED IMAGE   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Type of Image : <class 'torch.Tensor'>
Image Shape : torch.Size([3, 224, 224])
Image dtype : torch.float32
Image Max : 1.0
Image Min : -1.0

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 4 INSPECT LABEL SAFE TRANSFORMED IMAGE   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Type of Image : <class 'torch.Tensor'>
Image Shape : torch.Size([3, 224, 224])
Image dtype : torch.float32
Image Max : 1.0
Image Min : -1.0
'''


# =============================================================================
# Training and evaluating pipelines
# =============================================================================
train_data = datasets.CIFAR10(
    download=False,
    root="5-AppliedAI/week14/data",
    train=True,
    transform=labelsafe_transform
)

test_data = datasets.CIFAR10(
    download=False,
    root="5-AppliedAI/week14/data",
    train=False,
    transform=normalized_transform
)

train_image, train_label = train_data[0]
test_image, test_label = test_data[0]

print(f"\n{30*'~'} TRAINING & TEST DATA INSPECTION {30*'~'}")
print(f"Datasets size  --> Training Data '{len(train_data)}'--- Test Data '{len(test_data)}'")
print(f"Images Shape   --> Training Image Shape '{train_image.shape}' --- Test Image Shape '{test_image.shape}' ")
print(f"Images dtype   --> Training Image datatype '{train_image.dtype}' --- Test Image datatype '{test_image.dtype}' ")


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TRAINING & TEST DATA INSPECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Datasets size  --> Training Data '50000'--- Test Data '10000'
Images Shape   --> Training Image Shape 'torch.Size([3, 224, 224])' --- Test Image Shape 'torch.Size([3, 224, 224])' 
Images dtype   --> Training Image datatype 'torch.float32' --- Test Image datatype 'torch.float32'
'''

# =============================================================================
# Using data loaders to retireves batches of data instad of doing it manually
# =============================================================================
train_dataloader = DataLoader(train_data,batch_size=8,shuffle=True,num_workers=0)
test_dataloader = DataLoader(test_data,batch_size=8,shuffle=False,num_workers=0)

train_images, train_labels = next(iter(train_dataloader))
test_images, test_labels = next(iter(test_dataloader))
print(f"\n{30*'~'} TRAINING & TEST DATA LOADER DATA {30*'~'}")
print(f"Images Shape   --> Training Images Shape '{train_images.shape}' --- Test Images Shape '{test_images.shape}' ")
print(f"Images dtype   --> Training Images datatype '{train_images.dtype}' --- Test Images datatype '{test_images.dtype}' ")
print(f"Images Max   --> Training Images Max '{train_images.max()}' --- Test Images Max '{test_images.max()}' ")
print(f"Images Min   --> Training Images Min '{train_images.min()}' --- Test Images Min '{test_images.min()}' ")

print(f"\nLabels Shape   --> Training Labels Shape '{train_labels.shape}' --- Test Labels Shape '{test_labels.shape}' ")
print(f"Labels dtype   --> Training Labels datatype '{train_labels.dtype}' --- Test Labels datatype '{test_labels.dtype}' ")
print(f"Labels Values   --> Training Labels Values '{train_labels}' --- Test Labels Values '{test_labels}' ")

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TRAINING & TEST DATA LOADER DATA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Images Shape   --> Training Images Shape 'torch.Size([8, 3, 224, 224])' --- Test Images Shape 'torch.Size([8, 3, 224, 224])' 
Images dtype   --> Training Images datatype 'torch.float32' --- Test Images datatype 'torch.float32' 
Images Max   --> Training Images Max '1.0' --- Test Images Max '1.0' 
Images Min   --> Training Images Min '-1.0' --- Test Images Min '-1.0' 

Labels Shape   --> Training Labels Shape 'torch.Size([8])' --- Test Labels Shape 'torch.Size([8])' 
Labels dtype   --> Training Labels datatype 'torch.int64' --- Test Labels datatype 'torch.int64' 
Labels Values   --> Training Labels Values 'tensor([0, 1, 3, 0, 6, 7, 8, 9])' --- Test Labels Values 'tensor([3, 8, 8, 0, 6, 6, 1, 6])' 
'''