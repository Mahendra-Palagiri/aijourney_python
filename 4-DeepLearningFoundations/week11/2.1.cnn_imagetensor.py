import torch
import torch.nn as nn


# =============================================================================
# 1. Images tensor
# (N,C,H,W)
# N  - Number of images
# C  - Channel. (Grayscale is 1 and color is 3. (Red , Green, Blue))
# H  - Height of image (in pixels)
# W  - Width of image (in pixels)
# =============================================================================
print("")

images = torch.rand(4,1,28,28)  # 4 GrayScale images
print(f"----- OUTPUT ----- ")
print(f"Grayscale Image Shape : {images.shape}")

color_images = torch.rand(8,3,64,64)
print(f"Color Image Shape : {color_images.shape}")

'''----- OUTPUT ----- 
Grayscale Image Shape : torch.Size([4, 1, 28, 28])
Color Image Shape : torch.Size([8, 3, 64, 64])
'''

# =============================================================================
# 2. Flattening grayscale image
# =============================================================================
flattened_grayscaleimages = images.reshape(4,-1)
print(f"\n----- OUTPUT ----- ")
print(f"Flattened grayscale images: {flattened_grayscaleimages.shape}")

'''----- OUTPUT ----- 
Flattened grayscale images: torch.Size([4, 784])  --> 28 pixels x 28 pixels. = 784
'''


# =============================================================================
# 3. Adding missing batch dimension
# =============================================================================
#Sometimes we might have one grayscale image defined like this torch.rand(1,28,28) (i.e. this is missing the number of images (batch))
base_image = torch.rand(1,28,28)
print(f"\n----- OUTPUT ----- ")
print(f"base Image Shape : {base_image.shape}")

#For neural network Conv2d we need the batch dimension [N,C,H,W]
image_wbatchdimension = base_image.unsqueeze(0)
print(f"Image Shape with batch size: {image_wbatchdimension.shape}")

'''----- OUTPUT ----- 
base Image Shape : torch.Size([1, 28, 28])
Image Shape with batch size: torch.Size([1, 1, 28, 28])
'''


# =============================================================================
# 4. Adding missing channel dimensions
# =============================================================================
#Sometimes we might have one grayscale image defined like this torch.rand(28,28) (i.e. this is missing the number of images (batch) and the channels both)

base_image = torch.rand(28,28)
print(f"\n----- OUTPUT ----- ")
print(f"base Image Shape : {base_image.shape}")

image_wbatchandchannel = base_image.unsqueeze(0).unsqueeze(0)
print(f"Image Shape with batch size and channel: {image_wbatchandchannel.shape}")

'''----- OUTPUT ----- 
base Image Shape : torch.Size([28, 28])
Image Shape with batch size and channel: torch.Size([1, 1, 28, 28])
'''

# =============================================================================
# 5. nn.Conv2d shape check
# =============================================================================
image = torch.rand(4,1,28,28)
conv = nn.Conv2d(in_channels=1,out_channels=8,kernel_size=3)
output = conv(image)

print(f"\n----- OUTPUT ----- ")
print(f"base Image Shape : {image.shape}")
print(f"Modified Shape : {output.shape}")

'''---- OUTPUT ----- 
base Image Shape : torch.Size([4, 1, 28, 28])
Modified Shape : torch.Size([4, 8, 26, 26])

Input length = 28
Kernel size  = 3

Number of valid positions = 28 - 3 + 1 = 26

'''

print("")
