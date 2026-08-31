# 📓 Computer Vision Notes

## 1. Image Processing Basics
- Images are represented as multi-dimensional arrays (Height x Width x Channels).
- Color spaces: RGB, Grayscale, HSV.
- Basic operations: Resizing, cropping, filtering (blurring, edge detection).

## 2. Convolutional Neural Networks (CNNs) Deep Dive
- **Convolutions**: Extract features using sliding filters (kernels).
- **Padding and Stride**: Control the spatial dimensions of the output volume.
- **Pooling**: Downsample spatial dimensions (Max Pooling, Average Pooling) to reduce parameters and gain translation invariance.
- **Receptive Field**: The area of the original input image that affects a particular feature map unit.

## 3. Data Augmentation
Crucial for preventing overfitting in CV tasks where data is limited.
- Techniques: Rotations, flips, scaling, color jittering, random cropping.
- `torchvision.transforms` provides tools for easy augmentation during data loading.

## 4. Popular CNN Architectures
- **VGG**: Simple, deep networks using small 3x3 filters. Computationally heavy.
- **ResNet (Residual Networks)**: Introduced skip connections to solve the vanishing gradient problem in very deep networks.
- **Inception/GoogLeNet**: Uses multiple filter sizes in parallel within the same layer.
- **EfficientNet**: Systematically scales network depth, width, and resolution.

## 5. Object Detection
Identifying objects and their locations via bounding boxes.
- **Two-Stage Detectors**: Propose regions, then classify (e.g., R-CNN, Faster R-CNN). Highly accurate but slower.
- **One-Stage Detectors**: Predict bounding boxes and classes simultaneously directly from the image (e.g., YOLO, SSD). Faster, suitable for real-time.
- **Metrics**: Intersection over Union (IoU), mean Average Precision (mAP).

## 6. Image Segmentation
Assigning a class to every pixel in an image.
- **Semantic Segmentation**: Treats multiple objects of the same class as a single entity. (e.g., U-Net, FCN).
- **Instance Segmentation**: Identifies individual objects of the same class distinctly. (e.g., Mask R-CNN).

## 7. Transfer Learning in CV
Fine-tuning models pre-trained on massive datasets (like ImageNet) is the standard practice for almost all CV tasks, vastly reducing training time and required data.
