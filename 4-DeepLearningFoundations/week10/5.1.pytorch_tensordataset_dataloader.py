import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader

# =============================================================================
# 1. Sample Input
# =============================================================================
X = torch.tensor([
    [8.0, 2.0],
    [4.0, 7.0],
    [6.0, 1.0],
    [3.0, 9.0]
])

y = torch.tensor([
    [20.0],
    [30.0],
    [15.0],
    [40.0]
])

print(f"\n---- OUTPUT -----")
print(f"\nX Shape. --> {X.shape} \nY Shape --> {y.shape}")

'''---- OUTPUT -----

X Shape. --> torch.Size([4, 2]) 
Y Shape --> torch.Size([4, 1])
'''

# =============================================================================
# 2. Create a tensor dataset
# =============================================================================
tndataset = TensorDataset(X,y)

print(f"\n---- OUTPUT -----")
print(f"\n Lenght of dataset --> {len(tndataset)}")

first_features,first_target= tndataset[0]

print(f"\tFirst Sample Features --> {first_features} \n\tFirst Sample Target --> {first_target}")

'''---- OUTPUT -----

 Lenght of dataset --> 4
        First Sample Features --> tensor([8., 2.]) 
        First Sample Target --> tensor([20.])
'''

# =============================================================================
# 3. Create DataLoader
# =============================================================================
tnloader = DataLoader(tndataset,batch_size=2,shuffle=True) #Split the whole data into two batches and shuffle the data

print(f"\n---- OUTPUT -----\n\tBatches from data loader")

for batch_index,(batch_x,batch_y) in enumerate(tnloader):
    print(f"\n\tBatch--> {batch_index}\n\tBatch_x --> {batch_x}\n\tBatch_y --> {batch_y}\n\tBatch_x_shape --> {batch_x.shape}\n\tBatch_y_shape --> {batch_y.shape}")

'''---- OUTPUT -----
        Batches from data loader

        Batch--> 0
        Batch_x --> tensor([[4., 7.],
        [6., 1.]])
        Batch_y --> tensor([[30.],
        [15.]])
        Batch_x_shape --> torch.Size([2, 2])
        Batch_y_shape --> torch.Size([2, 1])

        Batch--> 1
        Batch_x --> tensor([[8., 2.],
        [3., 9.]])
        Batch_y --> tensor([[20.],
        [40.]])
        Batch_x_shape --> torch.Size([2, 2])
        Batch_y_shape --> torch.Size([2, 1])
'''

# =============================================================================
# 4. Define Simple model. (In normal scenarios we might not use this rather use something like nn.Linear(2,1))
# =============================================================================
class SimpleRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2,1)

    def forward(self,x):
        return self.linear(x)
    
model = SimpleRegressionModel()
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)


# =============================================================================
# 5. Evaluating the dataset using Loader 
# =============================================================================
num_epochs = 5 #Run through the optimziation process for the whole dataset 5 times

print(f"\n---- OUTPUT -----\nEvaluating the model using tensor loader with 5 epochs")
for epoch in range(num_epochs):
    total_loss =0.0

    print(f"\n\nEpoch {epoch+1}/{num_epochs}")
    for batch_index,(batch_x,batch_y) in enumerate(tnloader):
        optimizer.zero_grad() #clear gradients at each batch run

        predictions = model(batch_x)
        loss = loss_fn(predictions,batch_y)
        
        loss.backward()
        optimizer.step()

        print(f"\nEpoch-Batch:'{epoch+1}-{batch_index}'\n\tbatch_x: {batch_x}\n\tbatch_y:{batch_y}")

        total_loss+=loss.item()
    
    avg_loss = total_loss/len(tnloader)
    print(f"\naverage_loss {avg_loss}")

'''---- OUTPUT -----

Evaluating the model using tensor loader with 5 epochs


Epoch 1/5

Epoch-Batch:'1-0'
        batch_x: tensor([[8., 2.],
        [4., 7.]])
        batch_y:tensor([[20.],
        [30.]])

Epoch-Batch:'1-1'
        batch_x: tensor([[3., 9.],
        [6., 1.]])
        batch_y:tensor([[40.],
        [15.]])

average_loss 316.4540824890137


Epoch 2/5

Epoch-Batch:'2-0'
        batch_x: tensor([[3., 9.],
        [8., 2.]])
        batch_y:tensor([[40.],
        [20.]])

Epoch-Batch:'2-1'
        batch_x: tensor([[6., 1.],
        [4., 7.]])
        batch_y:tensor([[15.],
        [30.]])

average_loss 17.11622941493988


Epoch 3/5

Epoch-Batch:'3-0'
        batch_x: tensor([[4., 7.],
        [6., 1.]])
        batch_y:tensor([[30.],
        [15.]])

Epoch-Batch:'3-1'
        batch_x: tensor([[3., 9.],
        [8., 2.]])
        batch_y:tensor([[40.],
        [20.]])

average_loss 8.040742807090282


Epoch 4/5

Epoch-Batch:'4-0'
        batch_x: tensor([[6., 1.],
        [3., 9.]])
        batch_y:tensor([[15.],
        [40.]])

Epoch-Batch:'4-1'
        batch_x: tensor([[8., 2.],
        [4., 7.]])
        batch_y:tensor([[20.],
        [30.]])

average_loss 7.461418867111206


Epoch 5/5

Epoch-Batch:'5-0'
        batch_x: tensor([[6., 1.],
        [3., 9.]])
        batch_y:tensor([[15.],
        [40.]])

Epoch-Batch:'5-1'
        batch_x: tensor([[8., 2.],
        [4., 7.]])
        batch_y:tensor([[20.],
        [30.]])

average_loss 13.25368356704712
'''

# =============================================================================
# 5. Inspect final predictions (We did the training in batches and apply final prediction on whole dataset)
# =============================================================================
with torch.no_grad():
    final_predictions = model(X)
    final_loss = loss_fn(final_predictions,y)

print(f"\n ---- OUTPUT ----- ")
print(f"\n\tActual Values : {y}")
print(f"\n\t Final Prediction: {final_predictions} \n\t Final Loss: {final_loss}")

''' ---- OUTPUT ----- 

    Actual Values : tensor([[20.],
    [30.],
    [15.],
    [40.]])

    Final Prediction: tensor([[18.5649],
    [30.5584],
    [12.1977],
    [36.2062]]) 
    
    Final Loss: 6.154275894165039
'''