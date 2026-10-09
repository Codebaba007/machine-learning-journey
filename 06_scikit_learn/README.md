# Scikit-learn

This section covers Scikit-learn, the main Python library used to learn and practice classical Machine Learning.

## Topics

- Machine Learning foundations
- Features, targets, and datasets
- Training and testing data
- Train/test splitting
- Regression
- Classification
- Data preprocessing
- Feature scaling
- Model evaluation
- Cross-validation
- Hyperparameter tuning
- Pipelines
- Clustering

## Structure

- `notes/` — Learning notes and code examples
- `exercises/` — Practice problems
- `mini_projects/` — Practical Machine Learning projects

---
### Current Progress

Scikit-learn — Day 1 — Covered Scikit-learn foundations, features and targets, dataset shapes, supervised learning, train/test splitting, model fitting, prediction, evaluation, and the first regression mini-project.

Next Step: Continue with Scikit-learn Day 2.
---

## Day 1 — Scikit-learn Foundations and Train/Test Split

### Topics Covered

- Introduction to Scikit-learn
- Machine Learning models
- Observations, features, and targets
- Feature matrix `X` and target vector `y`
- Dataset shapes
- Supervised learning
- Regression vs classification
- Training data vs testing data
- Generalization
- `train_test_split()`
- `test_size`
- `random_state`
- `shuffle`
- `fit()` and `predict()`
- Mean Absolute Error
- Basic prediction visualization
- Data leakage fundamentals

### Functions and Classes

- `train_test_split()`
- `LinearRegression()`
- `mean_absolute_error()`
- `fit()`
- `predict()`
- `DataFrame.shape`
- `DataFrame.head()`
- `plt.scatter()`
- `plt.plot()`

### What I Learned

- What Scikit-learn provides for Machine Learning
- The difference between features and targets
- How to represent input features using `X` and targets using `y`
- How dataset shapes represent observations and features
- Why supervised learning requires input examples and known targets
- The difference between regression and classification
- Why data is split into training and testing subsets
- How `test_size` controls the test-set proportion
- How `random_state` helps reproduce a data split
- Why training performance does not necessarily represent performance on unseen data
- How to train a model using `fit()`
- How to generate predictions using `predict()`
- How Mean Absolute Error measures prediction errors
- Why data leakage can produce misleading evaluation results

### Mini Project

Built a House Price Prediction workflow using Scikit-learn.

The project:

- Creates an illustrative housing dataset
- Uses house area and bedroom count as features
- Uses house price as the target
- Splits data into training and testing subsets
- Trains a linear regression model
- Predicts prices for held-out observations
- Calculates Mean Absolute Error
- Compares actual and predicted prices
- Visualizes predictions using Matplotlib

### Key Concept

The standard supervised Machine Learning workflow is:

Prepare features and targets → split the data → fit the model → predict on held-out features → evaluate predictions against the known targets.

The test set should remain separate from model fitting so that it can provide a more meaningful estimate of performance on unseen data.

### Important Note

The housing dataset is illustrative and is intended for learning the Machine Learning workflow. Its results should not be treated as a reliable estimate of real-world housing prices.

