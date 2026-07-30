# 🔥 PyTorch Cheatsheet

```python
import torch
import torch.nn as nn
import torch.optim as optim
```

## Tensors
```python
x = torch.tensor([[1., 2.], [3., 4.]])
x = torch.zeros(2, 2)
x = torch.rand(2, 2)
x = x.to('cuda') # Move to GPU
```

## Autograd
```python
x = torch.ones(2, 2, requires_grad=True)
y = x + 2
z = y * y * 3
out = z.mean()
out.backward()
print(x.grad)
```

## nn.Module
```python
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(10, 20)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(20, 2)
        
    def forward(self, x):
        x = self.relu(self.linear1(x))
        return self.linear2(x)
```

## Common Layers
```python
nn.Linear(in_features, out_features)
nn.Conv2d(in_channels, out_channels, kernel_size)
nn.LSTM(input_size, hidden_size)
nn.BatchNorm2d(num_features)
nn.Dropout(p=0.5)
```

## Loss & Optimizers
```python
criterion = nn.CrossEntropyLoss() # or MSELoss(), BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001) # or SGD, AdamW
```

## Training Loop
```python
for epoch in range(epochs):
    for inputs, labels in dataloader:
        inputs, labels = inputs.to(device), labels.to(device)
        
        optimizer.zero_grad() # Clear gradients
        
        outputs = model(inputs) # Forward pass
        loss = criterion(outputs, labels) # Calculate loss
        
        loss.backward() # Backward pass
        optimizer.step() # Update weights
```

## DataLoader & Dataset
```python
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    def __len__(self): return len(self.data)
    def __getitem__(self, idx): return self.data[idx], self.labels[idx]

dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
```

## Transforms
```python
from torchvision import transforms
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
```

## Saving & Loading
```python
torch.save(model.state_dict(), 'model.pth')
model.load_state_dict(torch.load('model.pth'))
```

## Transfer Learning
```python
import torchvision.models as models
model = models.resnet18(pretrained=True)
for param in model.parameters():
    param.requires_grad = False
model.fc = nn.Linear(model.fc.in_features, num_classes)
```

## Device Management
```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
```
