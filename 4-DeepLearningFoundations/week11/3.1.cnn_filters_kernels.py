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
print(f"{'~'*20} OUTPUT {'~'*20} ")
print(f"Grayscale Image Shape : {images.shape}")

color_images = torch.rand(8,3,64,64)
print(f"Color Image Shape : {color_images.shape}")

'''~~~~~~~~~~~~~~~~~~~~ OUTPUT ~~~~~~~~~~~~~~~~~~~~ 
Grayscale Image Shape : torch.Size([4, 1, 28, 28])
Color Image Shape : torch.Size([8, 3, 64, 64])
'''

# =============================================================================
# 2. convolution layer
# =============================================================================
# A convolution layer looks for "local patterns" in an image
cnn_grayscale = nn.Conv2d(
    in_channels=1,
    out_channels=8,
    kernel_size=3
)

cnn_colorimage = nn.Conv2d(
    in_channels=3,
    out_channels=16,
    kernel_size=3
)

# =============================================================================
# 3. Applying convolution layer on top of image
# =============================================================================
grayscale_ouput = cnn_grayscale(images)
color_output = cnn_colorimage(color_images)

# =============================================================================
# 4. Observing and understanding the output
# =============================================================================
print(f"\n{'~'*20} OUTPUT {'~'*20} ")
print(f"Grayscale Image Input Shape : {images.shape}")
print(f"Grayscale Image Output Shape : {grayscale_ouput.shape}")

print(f"\nColor Image Input Shape : {color_images.shape}")
print(f"Color Image Output Shape : {color_output.shape}")

'''~~~~~~~~~~~~~~~~~~~~ OUTPUT ~~~~~~~~~~~~~~~~~~~~ 
Grayscale Image Input Shape : torch.Size([4, 1, 28, 28])
Grayscale Image Output Shape : torch.Size([4, 8, 26, 26])

CNN for Gray Scale. --> in_channels=1, out_channels=8, kernel_size=3
* Takes one input channel
* Applies 8 Filters (out_channel) /Kernels (Each Kernal application produces a feature map which helps in understanding image  (Horizontal edge, vertical edge, corner, curve..))
* Given the Kernel size is 3 (With 0 padding applied (implicit)), the out put shape becomes (inputshape-kernelshape+1) i.e. (28-3+1) --> 26 x 26
* A filter aka kernel is a small grid of learnable weights. (lets say 3 x 3)

Color Image Input Shape : torch.Size([8, 3, 64, 64])
Color Image Output Shape : torch.Size([8, 16, 62, 62])

CNN for Gray Scale. --> in_channels=3, out_channels=16, kernel_size=3
* Takes one input channel
* Applies 16 Filters(out_channel)/Kernels (Each Kernal application produces a feature which helps in understanding image  (Horizontal edge, vertical edge, corner, curve..))
* Given the Kernel size is 3 (With 0 padding applied (implicit)), the out put shape becomes (inputshape-kernelshape+1) i.e. (64-3+1) --> 62 x 62
* A filter aka kernel is a small grid of learnable weights. (lets say 3 x 3)

'''

print("")


