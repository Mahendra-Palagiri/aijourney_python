import torch
import torch.nn as nn


# =============================================================================
# CNN class
# =============================================================================

class SmallCNN(nn.Module):
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

        self.classifier = nn.Linear(16*7*7,10) #Convert the output features of image (16 Channels with 7 X 7 output after last maxpool in features into 10 output class scores)

    def forward(self, x):
        print("Input:", x.shape)
        x = self.features[0](x)
        print("After conv1:", x.shape)
        x = self.features[1](x)
        print("After relu1:", x.shape)
        x = self.features[2](x)
        print("After pool1:", x.shape)
        x = self.features[3](x)
        print("After conv2:", x.shape)
        x = self.features[4](x)
        print("After relu2:", x.shape)
        x = self.features[5](x)
        print("After pool2:", x.shape)
        x = x.reshape(x.shape[0], -1)
        print("After flatten:", x.shape)
        x = self.classifier(x)
        print("After classifier:", x.shape)
        return x


# =============================================================================
# Evaluating the model
# =============================================================================
model = SmallCNN()

images = torch.rand(4,1,28,28)

print(f"\n{'~'*20} OUTPUT {'~'*20} ")
output = model(images)

print(f"\n\nmodel :: {model}")
print(f"\n\nfinal output {output}")


'''~~~~~~~~~~~~~~~~~~~~ OUTPUT ~~~~~~~~~~~~~~~~~~~~ 
Input: torch.Size([4, 1, 28, 28])
After conv1: torch.Size([4, 8, 28, 28])
After relu1: torch.Size([4, 8, 28, 28])
After pool1: torch.Size([4, 8, 14, 14])
After conv2: torch.Size([4, 16, 14, 14])
After relu2: torch.Size([4, 16, 14, 14])
After pool2: torch.Size([4, 16, 7, 7])
After flatten: torch.Size([4, 784])
After classifier: torch.Size([4, 10])


model :: SmallCNN(
  (features): Sequential(
    (0): Conv2d(1, 8, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): ReLU()
    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (3): Conv2d(8, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (4): ReLU()
    (5): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (classifier): Linear(in_features=784, out_features=10, bias=True)
)


final output tensor(
    [
        [ 0.1474, -0.0322,  0.0381, -0.2796, -0.1058,  0.2738, -0.0954,  0.0149,0.0095,  0.1986],
        [ 0.1323, -0.0019,  0.0433, -0.2500, -0.0966,  0.2530, -0.1217,  0.0444,0.0385,  0.2283],
        [ 0.1199,  0.0063,  0.0050, -0.2330, -0.0616,  0.2726, -0.1333,  0.0479,0.0238,  0.2353],
        [ 0.1106, -0.0100,  0.0813, -0.2250, -0.0849,  0.2913, -0.1327,  0.0095,0.0156,  0.2023]
    ]
'''