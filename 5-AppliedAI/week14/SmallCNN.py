import torch
from torch import nn

class SmallCNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.features = nn.Sequential(
            nn.Conv2d(in_channels=3,out_channels=16,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(in_channels=16,out_channels=32,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.flatten = nn.Flatten(start_dim=1)
        self.classifier = nn.Linear(32*8*8,10)

    def forward(self,x):
        # print(f"Intial Shape: {x.shape}")
        x =self.features[0](x)
        # print(f"Shape After First Convolution: {x.shape}")
        x =self.features[1](x)
        # print(f"Shape After First Relu: {x.shape}")
        x =self.features[2](x)
        # print(f"Shape After First Maxpool: {x.shape}")
        x =self.features[3](x)
        # print(f"Shape After Second Convolution: {x.shape}")
        x =self.features[4](x)
        # print(f"Shape After Second Relu: {x.shape}")
        x =self.features[5](x)
        # print(f"Shape After Second Maxpool: {x.shape}")
        x = self.flatten(x)
        # print(f"Shape After Flattening: {x.shape}")
        x = self.classifier(x)
        # print(f"Shape After classifier: {x.shape}")
        return x
        