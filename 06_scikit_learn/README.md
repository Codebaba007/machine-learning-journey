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
## Current Progress

Scikit-learn — Day 5 completed — Covered regression evaluation metrics, residuals, MAE, MSE, RMSE, R², baseline comparison, and held-out test evaluation.

Completed:
- Day 1 — Scikit-learn Foundations and Train/Test Split
- Day 2 — Data Preprocessing and Feature Scaling
- Day 3 — Linear Regression
- Day 4 — Multiple Linear Regression
- Day 5 — Regression Evaluation Metrics

Next Step: Continue with Scikit-learn Day 6.

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
---
## Day 2 — Data Preprocessing and Feature Scaling

### Topics Covered

- Why feature scales matter
- Feature scaling
- Standardization
- Z-score scaling
- `StandardScaler`
- `fit()`
- `transform()`
- `fit_transform()`
- Training data vs testing data during preprocessing
- Data leakage in feature scaling

### Functions and Classes

- `StandardScaler()`
- `train_test_split()`
- `fit_transform()`
- `transform()`
- `DataFrame.mean()`
- `DataFrame.std()`

### What I Learned

- Why different feature scales can affect certain ML algorithms
- How standardization transforms numerical features
- How to interpret standardized values
- The difference between `fit()`, `transform()`, and `fit_transform()`
- How to fit a scaler on training data and apply it to testing data
- Why preprocessing must avoid test-data leakage
- How to compare original and standardized feature values

### Formula

Standardization:

z = (x - μ) / σ

Where:

- `x` is the original feature value
- `μ` is the feature mean
- `σ` is the feature standard deviation
- `z` is the standardized value

### Mini Project

Built a Housing Feature Scaling Analysis.

The project:

- Created an illustrative housing dataset
- Selected house area and bedroom count as input features
- Split data into training and testing subsets
- Applied `StandardScaler` to the features
- Compared original and standardized values
- Checked feature means and standard deviations
- Visualized feature distributions before and after scaling

### Key Concept

Fit preprocessing transformations on the training data only, then apply the learned transformation to the test data. This helps prevent data leakage during model evaluation.
---
## Day 3 — Linear Regression

### Topics Covered

- Introduction to regression
- Linear regression
- Simple linear regression
- Input features and numerical targets
- The linear regression equation
- Slope and coefficient
- Intercept
- Actual values vs predicted values
- Residuals
- Training and testing workflow
- Mean Absolute Error (MAE)
- Inspecting learned model parameters
- Visualizing regression lines and predictions

### Scikit-learn Classes and Functions

- `LinearRegression()`
- `train_test_split()`
- `mean_absolute_error()`
- `fit()`
- `predict()`
- `coef_`
- `intercept_`

### What I Learned

- How regression predicts numerical values
- How linear regression models a relationship using a linear equation
- What the input feature `
---
## Day 4 — Multiple Linear Regression

### Topics Covered

- Simple vs. multiple linear regression
- Multiple input features
- Numerical targets
- The multiple linear regression equation
- Feature coefficients
- Intercept
- Interpreting coefficients while holding other features constant
- Actual vs. predicted values
- Residuals
- Training and testing data
- Mean Absolute Error (MAE)
- Making predictions for new observations
- Visualizing actual vs. predicted values

### Scikit-learn Classes and Functions

- `LinearRegression()`
- `train_test_split()`
- `mean_absolute_error()`
- `fit()`
- `predict()`
- `coef_`
- `intercept_`

### What I Learned

- The difference between simple and multiple linear regression
- How multiple features contribute to a numerical prediction
- How to interpret the multiple linear regression equation
- What each feature coefficient represents
- How to interpret the intercept
- How to inspect learned coefficients using `model.coef_`
- How to inspect the intercept using `model.intercept_`
- How to train a model using multiple input features
- How to predict targets for held-out data and new observations
- How to calculate and interpret residuals
- How Mean Absolute Error measures prediction errors
- Why coefficients describe model relationships but do not automatically establish causation

### Key Formula

Multiple linear regression:

ŷ = b₀ + b₁x₁ + b₂x₂

Where:

- `ŷ` is the predicted target
- `b₀` is the intercept
- `b₁` is the coefficient for the first feature
- `x₁` is the first feature value
- `b₂` is the coefficient for the second feature
- `x₂` is the second feature value

Residual:

e = y − ŷ

Where:

- `e` is the residual
- `y` is the actual target
- `ŷ` is the predicted target

### Mini Project

Built a House Price Prediction Analysis Using Multiple Linear Regression.

The project:

- Created an illustrative housing dataset
- Used house area and bedroom count as input features
- Used house price as the target
- Split the data into training and testing subsets
- Trained a multiple linear regression model
- Inspected the learned coefficients and intercept
- Predicted prices for held-out houses
- Predicted the price of a new example house
- Calculated residuals and Mean Absolute Error
- Visualized actual vs. predicted prices

### Key Concept

Multiple linear regression uses several input features to predict a numerical target. Each feature has a learned coefficient, and the model combines the feature contributions with the intercept to generate a prediction.

A coefficient describes the change in the model's prediction associated with a one-unit increase in that feature when the other features remain constant.
---
## Day 5 — Regression Evaluation Metrics

### Topics Covered

- Why regression models need evaluation metrics
- Actual vs. predicted values
- Residuals and absolute errors
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² score (coefficient of determination)
- Interpreting regression evaluation results
- Comparing a model with a baseline
- Evaluating predictions on held-out test data

### Scikit-learn Functions and Classes

- `mean_absolute_error()`
- `mean_squared_error()`
- `r2_score()`
- `LinearRegression()`
- `DummyRegressor()`
- `train_test_split()`

### What I Learned

- Why a trained regression model must be evaluated
- How residuals measure the difference between actual and predicted values
- How MAE measures the average absolute prediction error
- How MSE squares errors and gives larger errors more weight
- How RMSE returns the error measurement to the target's original units
- How R² compares model predictions against a mean-prediction baseline
- Why lower MAE, MSE, and RMSE values are generally better when comparing models on the same evaluation data
- Why R² is not the same as prediction accuracy
- How to compare a linear regression model against a simple baseline
- Why evaluation should use held-out test data

### Key Formulas

Residual:

e = y − ŷ

Mean Absolute Error:

MAE = (1/n) × Σ|yᵢ − ŷᵢ|

Mean Squared Error:

MSE = (1/n) × Σ(yᵢ − ŷᵢ)²

Root Mean Squared Error:

RMSE = √MSE

R² score:

R² = 1 − SS_res / SS_tot

### Mini Project

Built a House Price Regression Evaluation Analysis.

The project:

- Created an illustrative housing dataset
- Used house area and bedroom count as features
- Used house price as the target
- Split the dataset into training and testing subsets
- Trained a linear regression model
- Created a mean-prediction baseline using `DummyRegressor`
- Evaluated both approaches using MAE, MSE, RMSE, and R²
- Compared actual and predicted test prices
- Predicted the price of a new example house
- Visualized actual vs. predicted prices

### Key Concept

Regression evaluation metrics measure different aspects of prediction performance. MAE summarizes absolute errors, MSE and RMSE penalize larger errors more strongly, and R² measures performance relative to a mean-prediction baseline.

Calculating evaluation metrics does not automatically retrain or improve a model. Model improvement requires additional decisions, such as revising features or choosing a different model, followed by appropriate validation.

The housing dataset is illustrative and should not be treated as real-world market data.
