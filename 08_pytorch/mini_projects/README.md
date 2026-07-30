# 🛠️ PyTorch Mini Projects

## 1. Custom Image Classifier
- **Description**: Build an end-to-end image classification pipeline using PyTorch for a custom dataset.
- **Skills Practiced**: Custom `Dataset` and `DataLoader`, `nn.Module` for CNN architectures, writing comprehensive training loops, evaluation.
- **Starter Instructions**: Choose a dataset like CIFAR-10 or a custom Kaggle dataset. Build a CNN from scratch. Implement training, validation, and test phases. Plot loss and accuracy curves.

## 2. Text Generator (Character-Level RNN)
- **Description**: Train an RNN to generate text character-by-character based on a specific style (e.g., Shakespeare, Wikipedia).
- **Skills Practiced**: Sequence data preparation, PyTorch `nn.RNN` or `nn.LSTM` modules, handling hidden states, sampling from output distributions.
- **Starter Instructions**: Preprocess text into sequences of characters. Build a model with an Embedding layer followed by an LSTM and a linear output layer. Write a script to generate new text after training.

## 3. Transfer Learning Fine-tuner
- **Description**: Take a state-of-the-art pre-trained model and fine-tune it for a specific niche task with limited data.
- **Skills Practiced**: `torchvision.models`, freezing layers, modifying model architecture, learning rate scheduling.
- **Starter Instructions**: Use a pre-trained ResNet18. Freeze all layers except the final fully connected layer. Train it on a dataset like Oxford-IIIT Pet Dataset or Flowers102. Compare the results against training from scratch.
