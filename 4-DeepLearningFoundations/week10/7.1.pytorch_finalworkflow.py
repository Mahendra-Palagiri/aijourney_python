import torch
from torch import nn
from torch.utils.data import TensorDataset,DataLoader

# =============================================================================
# 1. Sample Input
# =============================================================================
torch.manual_seed(42)

X = torch.rand(8,2)
y = torch.rand(8,1)


# =============================================================================
# 2. Dataset and Dataloader
# =============================================================================
dataset = TensorDataset(X,y)
loader = DataLoader(dataset,batch_size=2,shuffle=True)

# =============================================================================
# 3. Model Creation
# =============================================================================
class SimpleRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(2,4), # Converts two features into 4 outputs
            nn.ReLU(), #Applies non-linear activation function
            nn.Linear(4,1) #Converts 4 values to one ouput param
        )

    def forward(self,x):
        return self.net(x)
    

# =============================================================================
# 4. Initilization
# =============================================================================
model = SimpleRegressionModel()
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr=0.01)

# =============================================================================
# 5. Evaluation before the model training
# =============================================================================
model.eval()

with torch.no_grad():
    initial_prediction = model(X)
    initial_loss = loss_fn(initial_prediction,y)

# =============================================================================
# 6. Train the model
# =============================================================================
model.train()

num_epochs=40

print(f"\n------ OUTPUT -------")
for epoch in range(num_epochs):
    total_loss = 0.0

    for batch_x,batch_y in loader:
        optimizer.zero_grad()

        prediction = model(batch_x)
        loss = loss_fn(prediction,batch_y)

        loss.backward()
        optimizer.step()

        total_loss+=loss

    average_loss = total_loss/len(loader)
    if (epoch + 1) % 10 == 0 or epoch == 0:

        print(f"Epoch {epoch + 1}/{num_epochs} - Loss: {average_loss:.4f}")

'''------ OUTPUT -------
Epoch 1/40 - Loss: 0.2506
Epoch 10/40 - Loss: 0.0863
Epoch 20/40 - Loss: 0.0593
Epoch 30/40 - Loss: 0.0547
Epoch 40/40 - Loss: 0.0533
'''

# =============================================================================
# 7. Evaluation after the model training
# =============================================================================
model.eval()

with torch.no_grad():
    final_prediction = model(X)
    final_loss = loss_fn(final_prediction,y)

print(f"\n------ OUTPUT -------")
print(f"\nACTUAL EXPECTED OUTPUT")
print(f"\ny:  {y}")
print(f"\n~~~ Predictions before the model was evaluated ~~~")
print(f"initial_predictions:  {initial_prediction}\n\ninitial_loss:{initial_loss}")
print(f"\n~~~ Predictions after the model was evaluated ~~~")
print(f"final_predictions:  {final_prediction}\n\nfinal_loss:{final_loss}")

'''------ OUTPUT -------

ACTUAL EXPECTED OUTPUT

y:  tensor([[0.8854],
        [0.5739],
        [0.2666],
        [0.6274],
        [0.2696],
        [0.4414],
        [0.2969],
        [0.8317]])

~~~ Predictions before the model was evaluated ~~~
initial_predictions:  tensor([[ 0.0633],
        [ 0.1193],
        [ 0.0933],
        [ 0.1260],
        [-0.0167],
        [ 0.0275],
        [ 0.0317],
        [ 0.0315]])

initial_loss:0.26600560545921326

~~~ Predictions after the model was evaluated ~~~
final_predictions:  tensor([[0.5068],
        [0.5208],
        [0.5232],
        [0.5303],
        [0.4913],
        [0.4999],
        [0.5006],
        [0.5019]])

final_loss:0.05303540080785751

'''