import torch
import torch.nn as nn

# =============================================================================
# Running through several scenarios with padding and stride
# =============================================================================
images = torch.rand(4,1,7,7) #Taking a smaller picture for easier explanation


#Padding=0 and Stride=1 is the default behavior of the cnn
cnn_nopadding_1stride = nn.Conv2d(
    in_channels=1,
    out_channels=8,
    kernel_size=3,
    padding=0,
    stride=1
)

cnn_1padding_1stride = nn.Conv2d(
    in_channels=1,
    out_channels=8,
    kernel_size=3,
    padding=1,
    stride=1
)

cnn_nopadding_2stride = nn.Conv2d(
    in_channels=1,
    out_channels=8,
    kernel_size=3,
    padding=0,
    stride=2
)

print("")
out_nopadding_1stride = cnn_nopadding_1stride(images)
out_1padding_1stride = cnn_1padding_1stride(images)
out_nopadding_2stride = cnn_nopadding_2stride(images)
print(f"\n{'~'*20} OUTPUT {'~'*20} ")
print(f"Output size {out_nopadding_1stride.shape}")
print(f"\nOutput size {out_1padding_1stride.shape}")
print(f"\nOutput size {out_nopadding_2stride.shape}")

'''~~~~~~~~~~~~~~~~~~~~ OUTPUT ~~~~~~~~~~~~~~~~~~~~ 
*** Output size torch.Size([4, 8, 5, 5]) --> out_nopadding_1stride

    Padding 0  --> No pixels are added to original image so size remains same i.e. 7 x 7
    Stride 1. --> The filter/kernel moves one pixel at a time (and the kernel has to completely fit) so sliding window concept applied
        * 01-03, 02-04,03-05,04-06,05-07. (7th is the last pixel) --> For first row
        * 11-13, 12-14,13-15,14-16,15-17. (7th is the last pixel) --> For Second row
        * 21-23, 22-24,23-25,24-26,25-27. (7th is the last pixel) --> For Third row
        * 31-33, 32-34,33-35,34-36,35-37. (7th is the last pixel) --> For Fourth row
        * 41-43, 42-44,43-45,44-46,45-47. (7th is the last pixel) --> For Fith row (At this point 5,6 & 7 rows are completely covered by kernel)

        So the kernel can slide 5 time to the right and 5 times down one pixel at a time so the output shape is 5 x 5



*** Output size torch.Size([4, 8, 7, 7])-->out_1padding_1stride

    Padding 1  --> 1 Pixel added on each side (1 on left , 1 on right, 1 on top and and 1 on bottom i.e. height increased by 2 and width increased by 2) the image size becomes i.e. 9 x 9
    Stride 1. --> The filter/kernel moves one pixel at a time (and the kernel has to completely fit) so sliding window concept applied
    * 01-03, 02-04,03-05,04-06,05-07,06-08,07-09 (9th is the last pixel) --> For first row
    * .................
    * .................
    * .................
    * .................
    * .................
    * 71-73, 72-74,73-75,74-76,75-77,76-78,77-79 --For 7th row (At this point  7, 8 and 9 rows are completely covered by kernel)

    so the kernel can slide 7 times to the right and 7 times down so the image size of output becomes  7 X 7


*** Output size torch.Size([4, 8, 3, 3]) --> out_nopadding_2stride

    Padding 0  --> No pixels are added to original image so size remains same i.e. 7 x 7
    Stride 2. --> The filter/kernel moves one two pixes at a time
    * 01-03, 03-05,05-07. (7th is the last pixel) --> For first row. (Every slide is 2 pixels)
    * 31-33, 33-35,35-37. (7th is the last pixel) --> For first row. (Every slide is 2 pixels (2 vertically too))
    * 51-53, 53-55,55-57. (7th is the last pixel) --> 5th row at this point kernel compleletly occupied until 7th row (Every slide is 2 pixels(2 vertically too))

    so the kernel can slide 3 times to the right and 3 times down so the image size of output becomes  3 X 3

*** CONCLUSION :: Increasing the Stride length decreases the image size, Increasing the Padding size at the minimum keeps the same size or increases size
Formula for output size calculation:

output_size = floor((input_size + 2 × padding - kernel_size) / stride) + 1

in our case
out_nopadding_1stride = floor((7 + 2 × 0 - 3) / 1) + 1 i.e. ((7+0-3)/1)+1 = 5
out_1padding_1stride = floor((7 + 2 × 1 - 3) / 2) + 1 i.e. ((7+2-3)/1)+1 = 7
out_nopadding_2stride = floor((7 + 2 × 0 - 3) / 1) + 1 i.e. ((7+0-3)/2)+1 = 3


'''

print("")