import torch
import torch.nn as nn

class ImprovedImageModel(nn.Module):
    IN_CHANNELS = 1
    PH1_OUT_CHANNELS = 16
    PH2_OUT_CHANNELS = 32
    KERNEL_SIZE=3
    POOL_KERNEL_SIZE=2
    PADDING =1 

    NUM_CLASSES = 10
    CNN_FLATTENED_SIZE = 32 * 7 * 7

    def __init__(self):
        super().__init__()

        self.features = nn.Sequential(
            nn.Conv2d(in_channels=self.IN_CHANNELS,out_channels=self.PH1_OUT_CHANNELS,kernel_size=self.KERNEL_SIZE,padding=self.PADDING),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=self.POOL_KERNEL_SIZE),
            nn.Conv2d(in_channels=self.PH1_OUT_CHANNELS,out_channels=self.PH2_OUT_CHANNELS,kernel_size=self.KERNEL_SIZE,padding=self.PADDING),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=self.POOL_KERNEL_SIZE)
        )

        self.flatten = nn.Flatten()

        self.classifier = nn.Linear(
            in_features=self.CNN_FLATTENED_SIZE,
            out_features=self.NUM_CLASSES
        )
    
    def forward(self,x):
        x = self.features(x)
        x = self.flatten(x)
        logits = self.classifier(x)
        return logits
