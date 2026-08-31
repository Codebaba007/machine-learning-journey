# 💻 PyTorch Exercises

Get hands-on with PyTorch syntax and concepts.

## Tensor Operations
1. ⭐ Create a 3x3 tensor of random numbers and another 3x3 tensor of ones. Add them together.
2. ⭐ Create a 1D tensor of size 10 and reshape it into a 2x5 tensor.
3. ⭐⭐ Perform matrix multiplication between a 2x3 tensor and a 3x4 tensor.

## Autograd
4. ⭐ Define a scalar tensor `x` with `requires_grad=True`. Compute `y = x^2 + 2x + 1`. Calculate the gradient of `y` with respect to `x` at `x=2`.
5. ⭐⭐ Show practically what happens if you forget to call `optimizer.zero_grad()` in a training loop.

## Custom Datasets
6. ⭐ Create a custom `Dataset` class that generates synthetic regression data (e.g., `y = 3x + 2 + noise`).
7. ⭐⭐ Implement a `Dataset` that reads images from a directory, resizes them, and converts them to tensors. Wrap it in a `DataLoader` with batch size 16.

## Model Building
8. ⭐ Subclass `nn.Module` to create a simple feed-forward network with one hidden layer.
9. ⭐⭐ Write a complete training loop to train the network from exercise 8 on the synthetic dataset from exercise 6. Include loss calculation, backpropagation, and weight updates.

## Advanced Tasks
10. ⭐⭐⭐ Modify your training loop from exercise 9 to calculate and print validation loss after every epoch.
11. ⭐⭐⭐ Implement model checkpointing: save the model with the best validation loss during training.
12. ⭐⭐⭐ Write a function to calculate the accuracy of your model on a test DataLoader.
