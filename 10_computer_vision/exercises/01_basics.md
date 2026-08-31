# 🖼️ Computer Vision Exercises

## Image Preprocessing and Augmentation
1. ⭐ Load an image using PIL or OpenCV and display it.
2. ⭐ Apply a series of `torchvision.transforms` (resize, random horizontal flip, normalize) and display the resulting tensor as an image.
3. ⭐⭐ Create a DataLoader that applies different augmentations to the training set vs the validation set.

## CNN Architecture and Operations
4. ⭐ Calculate the output dimensions of a convolutional layer given an input size of 64x64, kernel size 3, stride 2, and padding 1.
5. ⭐⭐ Build a custom CNN block consisting of: Conv2d -> BatchNorm2d -> ReLU -> MaxPool2d.
6. ⭐⭐⭐ Implement a basic Residual Block (skip connection) in PyTorch.

## Advanced Implementations
7. ⭐⭐ Load a pre-trained ResNet18 model and inspect its architecture using `print(model)`.
8. ⭐⭐⭐ Write a function to calculate Intersection over Union (IoU) given two bounding boxes `[x1, y1, x2, y2]`.
9. ⭐⭐⭐ Extract features from an intermediate layer of a pre-trained model for a given image.
