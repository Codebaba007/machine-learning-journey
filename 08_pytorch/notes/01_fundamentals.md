# 📓 PyTorch Framework Notes

## 1. Tensors
- Tensors are the fundamental data structure in PyTorch, similar to NumPy arrays but with GPU support.
- Creation: `torch.tensor()`, `torch.zeros()`, `torch.randn()`.
- Operations: Matrix multiplication (`@`, `torch.matmul`), reshaping (`view`, `reshape`), indexing.

## 2. Autograd (Automatic Differentiation)
- PyTorch's autograd engine automatically computes gradients for tensor operations.
- Setting `requires_grad=True` on a tensor tracks all operations on it.
- Calling `.backward()` on a scalar loss tensor computes the gradients and stores them in the `.grad` attribute of the respective tensors.

## 3. nn.Module
- The base class for all neural network modules.
- Custom models subclass `nn.Module`.
- Must define `__init__` (where layers are defined) and `forward` (where the forward pass is defined).
- Parameters of layers defined in `__init__` are automatically registered and tracked.

## 4. Datasets and DataLoaders
- `torch.utils.data.Dataset`: An abstract class representing a dataset. You must implement `__len__` and `__getitem__`.
- `torch.utils.data.DataLoader`: Wraps a Dataset and provides an iterable over the dataset, handling batching, shuffling, and multiprocess data loading.

## 5. The Training Loop
A standard PyTorch training loop involves:
1. Zero the gradients (`optimizer.zero_grad()`).
2. Forward pass to get outputs (`model(inputs)`).
3. Calculate the loss (`loss_fn(outputs, targets)`).
4. Backward pass to compute gradients (`loss.backward()`).
5. Update weights (`optimizer.step()`).

## 6. GPU Acceleration
- Moving tensors and models to GPU: `.to('cuda')` or `.cuda()`.
- Ensure inputs and the model are on the same device.

## 7. Model Saving and Loading
- Saving state dict: `torch.save(model.state_dict(), 'model.pth')`
- Loading state dict: `model.load_state_dict(torch.load('model.pth'))`
- Checkpointing is crucial for long training jobs to resume interrupted training.

## 8. Transfer Learning
- Using pre-trained models (e.g., from `torchvision.models`).
- Freeze earlier layers (`requires_grad = False`) and replace/retrain the final classification head for the new task.
