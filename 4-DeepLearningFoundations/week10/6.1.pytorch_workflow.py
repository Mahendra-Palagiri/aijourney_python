import torch
from torch import nn
from torch.utils.data import TensorDataset,DataLoader

# =============================================================================
# 1. Sample Input
# =============================================================================
X = torch.tensor([
    [8.0, 2.0],
    [4.0, 7.0],
    [6.0, 1.0],
    [3.0, 9.0],
    [9.0, 4.0],
    [2.0, 6.0],
    [7.0, 3.0],
    [5.0, 8.0]
])

y = torch.tensor([
    [20.0],
    [30.0],
    [15.0],
    [40.0],
    [28.0],
    [26.0],
    [21.0],
    [35.0]
])


print(f"\n------ OUTPUT -------")
print(f"\nX.shape {X.shape}\ny.shape{y.shape}")

'''------ OUTPUT -------

X.shape torch.Size([8, 2])
y.shapetorch.Size([8, 1])
'''

# =============================================================================
# 2. Create Dataset and Dataloader
# =============================================================================
dataset = TensorDataset(X,y)
loader = DataLoader(dataset,batch_size=2,shuffle=True)

batch_x,batch_y = next(iter(loader)) #Sample verify

print(f"\n------ OUTPUT -------")
print(f"\nbatch_x:  {batch_x}\nbatch_x.shape{batch_x.shape}")
print(f"\nbatch_y:  {batch_y}\nbatch_y.shape{batch_y.shape}")

'''------ OUTPUT -------

batch_x:  tensor([[7., 3.],
        [9., 4.]])
batch_x.shapetorch.Size([2, 2])

batch_y:  tensor([[21.],
        [28.]])
batch_y.shapetorch.Size([2, 1])
'''

# =============================================================================
# 3. Define the model
# =============================================================================
class SimpleRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2,1)

    def forward(self,x):
        return self.linear(x)
    
# =============================================================================
# 4. Create instances 
# =============================================================================
model = SimpleRegressionModel()
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr=0.01)

print(f"\n------ OUTPUT -------")
print(f"\nmodel:  {model}")

'''------ OUTPUT -------

model:  SimpleRegressionModel(
  (linear): Linear(in_features=2, out_features=1, bias=True)
'''

# =============================================================================
# 5. Predictions before training
# =============================================================================
model.eval() #Puts the model in evaluation mode

with torch.no_grad():
    initial_predictions = model(X)
    initial_loss = loss_fn(initial_predictions,y)

print(f"\n------ OUTPUT -------")
print(f"\ninitial_predictions:  {initial_predictions}\n\ninitial_loss:{initial_loss}")

'''------ OUTPUT -------

initial_predictions:  tensor([[ 3.1815],
        [-0.3966],
        [ 2.4215],
        [-1.5117],
        [ 3.1204],
        [-1.1566],
        [ 2.3605],
        [-0.1637]])

initial_loss:753.5812377929688
'''

# =============================================================================
# 5. Predictions before training
# =============================================================================
model.train()

num_epochs =20

print(f"\n---- OUTPUT -----\nEvaluating the model using tensor loader with 20 epochs")
for epoch in range(num_epochs):
    total_loss =0.0

    print(f"\n\nEpoch {epoch+1}/{num_epochs}")
    for batch_index,(batch_x,batch_y) in enumerate(loader):
        optimizer.zero_grad() #clear gradients at each batch run

        predictions = model(batch_x)
        loss = loss_fn(predictions,batch_y)
        
        loss.backward()
        optimizer.step()

        # print(f"\nEpoch-Batch:'{epoch+1}-{batch_index}'\n\tbatch_x: {batch_x}\n\tbatch_y:{batch_y}\nprediction: {predictions}\nloss:{loss}")

        total_loss+=loss.item()
    
    avg_loss = total_loss/len(loader)
    print(f"\naverage_loss {avg_loss}")


# =============================================================================
# 6. Evaluate the model (Post training)
# =============================================================================
model.eval() 

with torch.no_grad():
    final_predictions = model(X)
    final_loss = loss_fn(final_predictions,y)

print(f"\n------ OUTPUT -------")
print(f"\nACTUAL EXPECTED OUTPUT")
print(f"\ny:  {y}")
print(f"\n~~~ Predictions before the model was evaluated ~~~")
print(f"initial_predictions:  {initial_predictions}\n\ninitial_loss:{initial_loss}")
print(f"\n~~~ Predictions after the model was evaluated ~~~")
print(f"final_predictions:  {final_predictions}\n\nfinal_loss:{final_loss}")

'''------ OUTPUT -------

ACTUAL EXPECTED OUTPUT

y:  tensor([[20.],
        [30.],
        [15.],
        [40.],
        [28.],
        [26.],
        [21.],
        [35.]])

~~~ Predictions before the model was evaluated ~~~
initial_predictions:  tensor([[ 0.4002],
        [-0.3565],
        [ 0.3857],
        [-0.6236],
        [ 0.2515],
        [-0.3710],
        [ 0.2370],
        [-0.4012]])

initial_loss:789.9099731445312

~~~ Predictions after the model was evaluated ~~~
final_predictions:  tensor([[20.8393],
        [32.9540],
        [13.9913],
        [38.7481],
        [29.7942],
        [26.1059],
        [22.9462],
        [38.2216]])

final_loss:3.6765213012695312
'''