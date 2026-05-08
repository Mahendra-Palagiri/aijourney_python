import torch
from torch import nn


# =============================================================================
# 1. Define a simple model
# =============================================================================
class SimpleRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2,1)

    def forward(self,x):
        return self.linear(x)
    

# =============================================================================
# 2. Create input (train) and output (prediction validation) data 
# =============================================================================
X = torch.tensor([
    [8.0, 2.0],
    [4.0, 7.0],
    [6.0, 1.0],
    [3.0, 9.0]
])

#The actual value and the model output "dimension" should match (so our SimpleRegressionClass has Liner(2,1) i.e. take 2 input features and give out an output)
y = torch.tensor([
    [20.0],
    [30.0],
    [15.0],
    [40.0]
])

print(f"\n------OUTPUT-------")
print(f"\n INPUT : x.shape --> {X.shape}\n OUTPUT : y.shape --> {y.shape}")

'''------OUTPUT-------

 INPUT : x.shape --> torch.Size([4, 2])
 OUTPUT : y.shape --> torch.Size([4, 1]) 
'''


# =============================================================================
# 3. Create model, loss function, and optimizer
# =============================================================================
model = SimpleRegressionModel()
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01) #Stochastic Graident Descent (SGD)

print(f"\n------OUTPUT-------")
print(f"\n Model --> {model}")

'''------OUTPUT-------

 Model --> SimpleRegressionModel(
  (linear): Linear(in_features=2, out_features=1, bias=True)
)
'''

# =============================================================================
# 4. Inspect initial parameters
# =============================================================================
print(f"\n------OUTPUT-------\n Initial Parameters")
for name,param in model.named_parameters():
    print(f"\n ** Name --> {name} \n ** Value --> {param} \n ** Required_gradient_tracking --> {param.requires_grad} \n ** Shape --> {param.shape}")

'''
------OUTPUT-------
 Initial Parameters

 ** Name --> linear.weight 
 ** Value --> Parameter containing: tensor([[0.6278, 0.6801]], requires_grad=True) 
 ** Required_gradient_tracking --> True #We dont need to specifially mention that to be tracked as nn.Module by defaults tracks these hence true
 ** Shape --> torch.Size([1, 2])

 ** Name --> linear.bias 
 ** Value --> tensor([0.1608], requires_grad=True)  
 ** Required_gradient_tracking --> True 
 ** Shape --> torch.Size([1])
'''

# =============================================================================
# 5. Forward Pass
# =============================================================================
predictions = model(X) # We dont need to call model.forward(x) as nn.Module understands and calls the forward function accordingly when we say model(x)
print(f"\n------OUTPUT-------")
print(f"\n Predicted values (Before any optimzations) --> {predictions} \n Shape --> {predictions.shape}")

'''------OUTPUT-------
#At this point the predicted values seems to be way off to the original values (y tensor)

 Predicted values (Before any optimzations) --> tensor([[6.5433],
        [7.4324],
        [4.6076],
        [8.1647]], grad_fn=<AddmmBackward0>) 
 Shape --> torch.Size([4, 1])
'''


# =============================================================================
# 6. Compute the loss
# =============================================================================
loss = loss_fn(predictions,y)
print(f"\n------OUTPUT-------\n Loss before applying any step function (optimization) --> {loss}")

'''------OUTPUT-------
 Loss before applying any step function (optimization) --> 452.96649169921875
 '''

# =============================================================================
# 7. Run a backward pass
# =============================================================================
optimizer.zero_grad() #Ensure gradients are cleared after each batch run
loss.backward()
print(f"\n------OUTPUT-------\n\nGradients after backward pass:")
for name,param in model.named_parameters():
    print(f"\n ** Name --> {name} \n ** Value --> {param}\n ** Grad --> {param.grad}")

'''------OUTPUT-------

Initial  Params
Value --> Parameter containing: tensor([[0.6278, 0.6801]], requires_grad=True) 
Value --> Parameter containing: tensor([0.1608], requires_grad=True) 


Gradients and Parameters after backward pass:

 ** Name --> linear.weight 
 ** Value --> Parameter containing: tensor([[0.6278, 0.6801]], requires_grad=True)
 ** Grad --> tensor([[-177.8922, -240.8982]])

 ** Name --> linear.bias 
 ** Value --> Parameter containing: tensor([0.1608], requires_grad=True)
 ** Grad --> tensor([-39.1260])

'''

# =============================================================================
# 8. Perform Optimization
# =============================================================================
optimizer.step()
print(f"\n------OUTPUT-------\n\nParmeters after Optimization Step:")
for name,param in model.named_parameters():
    print(f"\n ** Name --> {name} \n ** Value --> {param}")

'''------OUTPUT-------

Initial  Params
Value --> Parameter containing: tensor([[0.6278, 0.6801]], requires_grad=True) 
Value --> Parameter containing: tensor([0.1608], requires_grad=True) 

Params after backward pass
Value --> Parameter containing: tensor([[0.6278, 0.6801]], requires_grad=True) 
Value --> Parameter containing: tensor([0.1608], requires_grad=True) 

Parmeters after Optimization Step:

 ** Name --> linear.weight 
 ** Value --> Parameter containing: tensor([[2.4067, 3.0890]], requires_grad=True)

 ** Name --> linear.bias 
 ** Value --> Parameter containing: tensor([0.5521], requires_grad=True)
'''

# =============================================================================
# 9. Running one more forward pass to check how the model has changed
# =============================================================================
new_predictions = model(X)
new_loss = loss_fn(new_predictions,y)
print(f"\n------OUTPUT-------")
print(f"\n Old Predictions --> {predictions} \n Old Loss --> {loss}")
print(f"\n\nNew Predictions after one optimzation step -->  {new_predictions}, \nnew loss --> {new_loss}")


'''------OUTPUT-------

# The model has significantly improved its performance after just one optimiztion 
# (Not perfectly close to original values but relatively improved performance)

y = torch.tensor([
    [20.0],
    [30.0],
    [15.0],
    [40.0]
])

 Old Predictions --> tensor([[6.5433],
        [7.4324],
        [4.6076],
        [8.1647]], grad_fn=<AddmmBackward0>) 
 Old Loss --> 452.96649169921875


New Predictions after one optimzation step -->  tensor([[25.9839],
        [31.8022],
        [18.0814],
        [35.5736]], grad_fn=<AddmmBackward0>), 
new loss --> 17.035686492919922
'''