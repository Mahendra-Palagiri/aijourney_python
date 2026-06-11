import torch
import torch.nn as nn

class BaselineNN(nn.Module):
    def __init__(self,input_size: int, hidden_size:int,num_classes:int):
        super().__init__()

        self.INPUT_SIZE = input_size
        self.HIDDEN_SIZE = hidden_size
        self.NUM_CLASSES = num_classes

        self.flatten = nn.Flatten()

        self.network = nn.Sequential(
            nn.Linear(in_features=self.INPUT_SIZE, out_features=self.HIDDEN_SIZE),
            nn.ReLU(),
            nn.Linear(in_features=self.HIDDEN_SIZE,out_features=self.NUM_CLASSES)
        )
    
    def forward(self,x):
        x = self.flatten(x)
        logits = self.network(x)
        return logits