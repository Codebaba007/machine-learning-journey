# 📝 Fundamentals of Machine Learning

## 1. Supervised vs. Unsupervised Learning
- **Supervised Learning**: The algorithm learns from labeled training data. It tries to map input features to a known target variable. Examples: Regression, Classification.
- **Unsupervised Learning**: The algorithm learns from unlabeled data. It tries to find hidden structure or patterns. Examples: Clustering, Dimensionality Reduction.

## 2. The Bias-Variance Tradeoff
This is a central problem in supervised learning.
- **Bias**: Error from erroneous assumptions in the learning algorithm. High bias can cause an algorithm to miss relevant relations (underfitting).
- **Variance**: Error from sensitivity to small fluctuations in the training set. High variance can cause an algorithm to model the random noise in the training data (overfitting).
- **Goal**: Find the sweet spot where both bias and variance are low enough to generalize well to unseen data.

## 3. Overfitting and Underfitting
- **Overfitting**: Model performs exceptionally well on training data but poorly on test data. Solutions: Regularization, more data, simpler model, dropout (in NNs).
- **Underfitting**: Model is too simple to capture the underlying trend. Performs poorly on both training and test data. Solutions: More complex model, better feature engineering.

## 4. Feature Engineering
The process of using domain knowledge to extract features from raw data.
- **Imputation**: Handling missing values.
- **Encoding**: Converting categorical variables to numerical (One-Hot, Label Encoding).
- **Scaling/Normalization**: Standardizing the range of independent variables.

## 5. Model Evaluation
- **Classification Metrics**: Accuracy, Precision, Recall, F1-Score, ROC-AUC.
- **Regression Metrics**: MSE, RMSE, MAE, R-squared.

## 6. Cross-Validation
A resampling procedure used to evaluate machine learning models on a limited data sample.
- **k-Fold CV**: The dataset is divided into *k* sets. The model is trained on *k-1* sets and evaluated on the remaining set. Repeated *k* times.

## 7. Ensemble Methods
Combining multiple learning algorithms to obtain better predictive performance.
- **Bagging** (e.g., Random Forest): Trains multiple models independently and averages their predictions. Reduces variance.
- **Boosting** (e.g., XGBoost, AdaBoost): Trains models sequentially, each trying to correct the errors of its predecessor. Reduces bias.

## 8. Regularization
A technique used to prevent overfitting by adding a penalty term to the loss function.
- **L1 Regularization (Lasso)**: Adds absolute value of magnitude of coefficient as penalty. Can lead to sparse models.
- **L2 Regularization (Ridge)**: Adds squared magnitude of coefficient as penalty.
