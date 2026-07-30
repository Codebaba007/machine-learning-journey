# 📓 Deep Learning Fundamentals Notes

## 1. Neural Networks (Multilayer Perceptrons)
- Inspired by biological brains, consists of layers of interconnected "neurons".
- **Input Layer**: Receives raw data.
- **Hidden Layers**: Perform non-linear transformations.
- **Output Layer**: Produces the final prediction.

## 2. Forward Pass and Backpropagation
- **Forward Pass**: Data flows from input to output, calculating predictions and the final loss.
- **Backpropagation**: The algorithm for calculating the gradient of the loss function with respect to each weight. It uses the **Chain Rule** of calculus to propagate the error backwards from the output layer to the input layer.

## 3. Activation Functions
Introduce non-linearity, allowing networks to learn complex patterns.
- **Sigmoid**: Outputs between 0 and 1. Prone to vanishing gradients.
- **Tanh**: Outputs between -1 and 1. Also prone to vanishing gradients but zero-centered.
- **ReLU (Rectified Linear Unit)**: `max(0, x)`. Fast and helps mitigate vanishing gradients, but can suffer from "dying ReLU".
- **Softmax**: Used in output layer for multi-class classification to output probabilities.

## 4. Optimization Algorithms
Methods to update network weights to minimize loss.
- **SGD (Stochastic Gradient Descent)**: Updates weights based on a single training example or small batch.
- **Momentum**: Accelerates SGD in relevant directions and dampens oscillations.
- **Adam**: Adaptive Moment Estimation. Computes individual adaptive learning rates for different parameters.

## 5. Regularization in Deep Learning
- **Dropout**: Randomly dropping out (setting to zero) a proportion of neurons during training to prevent co-adaptation and overfitting.
- **Batch Normalization**: Normalizes the inputs of a layer to stabilize and accelerate training.

## 6. Intro to Specialized Architectures
- **CNNs (Convolutional Neural Networks)**: Designed for grid-like data (images). Uses convolutional layers to automatically learn spatial hierarchies of features.
- **RNNs (Recurrent Neural Networks)**: Designed for sequential data (text, time series). Possess a "memory" of previous inputs.
- **Transformers**: State-of-the-art architecture for sequences, relying entirely on self-attention mechanisms, dispensing with recurrence and convolutions.
