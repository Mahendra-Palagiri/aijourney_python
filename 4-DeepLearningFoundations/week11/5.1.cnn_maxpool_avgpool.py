import torch
import torch.nn as nn

# =============================================================================
# Images (Input)
# =============================================================================
images = torch.rand(4,1,28,28)

print("")
print(f"\n{'~'*20} OUTPUT {'~'*20} ")
print(f"Input size {images.shape}")

# =============================================================================
# Max Pool
# =============================================================================
max_pool = nn.MaxPool2d(kernel_size=2, stride=2)
max_out = max_pool(images)
print(f"\n After MaxPool 2d{max_out.shape}")


# =============================================================================
# Avg Pool
# =============================================================================
avg_pool = nn.AvgPool2d(kernel_size=2, stride=2)
avg_out = avg_pool(images)
print(f"\n After AveragePool 2d{avg_out.shape}")


# =============================================================================
# Executing a proper CNN block (Conv + ReLU  + Pooling)
# =============================================================================
block = nn.Sequential(
    nn.Conv2d(in_channels=1,out_channels=8,kernel_size=3,padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2,stride=2)
)
block_out = block(images)
print(f"\n After CNN block {block_out.shape}")


'''~~~~~~~~~~~~~~~~~~~~ OUTPUT ~~~~~~~~~~~~~~~~~~~~ 
Input size torch.Size([4, 1, 28, 28])



The way pool works lets assume we have a grid of 4 x 4 (and  pool set is defined as kernel=2 (cover 2 x 2 grid) and stride=2 (move two pixels at a time))

INPUT::
1 3 2 4
5 6 1 2
7 2 8 1
3 4 2 9

so the set becomes                    Max Pool               Avg Pool
                                        
-------   -------                  -----    -----        -------    -------
- 1 3 -   - 2 4 -                  - 6 -    - 4 -        - 3.75 -   - 2.25 -
- 5 6 -   - 1 2 -                  -----    -----        -------    -------
-------   -------

-------   -------                  -----    -----        -------    -------
- 7 2 -   - 8 1 -                  - 7 -    - 9 -        - 4.00 -   - 5.00 -
- 3 4 -   - 2 9 -                  -----    -----        -------    -------
-------   -------

Output formula for pool (follows similar to conv2d ) i.e. floor((inputsize+2 * padding-kernelsize)/stride)+1

After MaxPool 2dtorch.Size([4, 1, 14, 14]). --> floor((28+0-2)/2)+1 = 14

After AveragePool 2dtorch.Size([4, 1, 14, 14])--> floor((28+0-2)/2)+1 = 14

Even though the oputshape of max and avg pool looks same the way the data is considered is difrent (as explained above)

After CNN block torch.Size([4, 8, 14, 14])

INPUT : [4,1,28,28]
After Conv : [4,8,28,28]. (With padding=1 the output size remains the same, out_channels=8 so the channel size has changed from 1-->8 )
After ReLu : [4,8,28,28]. (No change in size)
After MaxPool : [4,8,14,14].

Point to be noted
Pool never effects the number of images. (4) or the channel count (8 in this case). It might have impact on Height and width. (based on stride and kernel)


CNNs use pooling to reduce spatial size, lower computation, keep strong signals, and make the model less sensitive to small shifts.
'''

print("")
