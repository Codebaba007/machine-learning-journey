# ✍️ Deep Learning Exercises

Test your understanding of neural network mechanics.

## Conceptual Questions
1. ⭐ Why do we need activation functions in a neural network?
2. ⭐ Explain the vanishing gradient problem. Which activation function helps solve it?
3. ⭐⭐ Walk through the steps of one iteration of training a neural network (Forward pass -> Loss calculation -> Backpropagation -> Weight update).
4. ⭐⭐ How does Dropout prevent overfitting?
5. ⭐⭐⭐ Compare and contrast Adam optimizer with basic SGD. Why is Adam often preferred?

## Mathematical/Analytical Exercises
6. ⭐ Given an input `x = [0.5, -0.2]` and weights `w = [1.0, 2.0]` with bias `b = 0.1`, calculate the output of a single neuron using a ReLU activation function.
7. ⭐⭐ Calculate the derivative of the Sigmoid function `f(x) = 1 / (1 + e^-x)` with respect to `x`.
8. ⭐⭐ Calculate the number of trainable parameters in a dense layer with 128 inputs and 64 outputs.
9. ⭐⭐⭐ Describe the mathematical operation happening inside a 2D Convolutional layer.

## Architecture Design Exercises
10. ⭐ Design a simple Multi-Layer Perceptron (specify layers and sizes) to classify a 28x28 grayscale image into 10 categories.
11. ⭐⭐ Design an architecture that takes in a sequence of 50 words (represented as vectors of size 100) and outputs a binary sentiment classification.
12. ⭐⭐⭐ Propose an evaluation strategy and hyperparameter tuning plan (which parameters to tune and in what ranges) for training a deep neural network on a limited dataset.
