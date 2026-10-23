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
- Current Section: Scikit-learn
- Current Day: Day 10
- Current Topic: Scikit-learn Pipelines
- Completed Days: 10
- Next Topic: Handling Missing Data

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
---

## Day 6: Classification Fundamentals

### Topics Covered
- Regression vs classification
- Features (`X`) and class labels (`y`)
- Logistic Regression for binary classification
- Training and predicting with `fit()` and `predict()`
- Getting class probabilities with `predict_proba()`
- Understanding prediction thresholds
- Splitting classification data with `train_test_split()`
- Using `stratify=y` to preserve class proportions
- Applying `StandardScaler` to training, test, and new data
- Making predictions for a new customer

### Files
- `notes/06_classification.py`
- `exercises/exercise_06.py`
- `mini_projects/classification_analysis.py`

### Mini-Project
Built a customer-churn classification workflow using Logistic Regression. Prepared features and labels, split the data into training and testing sets, scaled numerical features, generated class predictions and probabilities, and predicted churn for a new customer.

### Key Learnings
- Regression predicts numerical values; classification predicts categories.
- `predict()` returns a predicted class.
- `predict_proba()` returns estimated probabilities for each class.
- `StandardScaler` standardizes numerical features.
- Fit the scaler on training data and reuse it to transform test and new data.
- `test_size` controls the test-set proportion.
- `random_state` makes the split reproducible.
- `stratify=y` approximately preserves class proportions.
- Predictions and probabilities alone do not establish model quality; classification evaluation comes next.
---

## Day 7: Classification Evaluation Metrics

### Topics Covered
- Evaluating classification models
- Accuracy and correct predictions
- Confusion matrix
- True Positive (TP) and True Negative (TN)
- False Positive (FP) and False Negative (FN)
- Precision and recall
- F1-score
- Scikit-learn evaluation functions
- `classification_report()`
- Evaluating predictions against test labels

### Files
- `notes/07_classification_metrics.py`
- `exercises/exercise_07.py`
- `mini_projects/classification_evaluation.py`

### Mini-Project
Built a customer-churn classification evaluation workflow using Logistic Regression. Prepared the dataset, split training and test data, scaled numerical features, trained the classifier, and evaluated predictions using accuracy, precision, recall, F1-score, and a confusion matrix.

### Key Learnings
- Accuracy measures the proportion of correct predictions.
- A confusion matrix summarizes correct predictions and classification errors.
- Precision measures how trustworthy positive predictions are.
- Recall measures how many actual positive cases the model identifies.
- F1-score balances precision and recall.
- `classification_report()` displays per-class evaluation metrics.
- Evaluation metrics should be calculated on held-out test data.
- Accuracy alone can be misleading when classes are imbalanced.
- Small synthetic datasets are useful for learning but cannot establish real-world model performance.
---

## Day 8: Underfitting, Overfitting, and Model Generalization

### Topics Covered
- Understanding model generalization
- Underfitting and overfitting
- Comparing training and test performance
- Decision tree regression
- Controlling model complexity with `max_depth`
- Mean Absolute Error (MAE)
- Comparing models with different depths
- Understanding the training-test error gap

### Files
- `notes/08_model_generalization.py`
- `exercises/exercise_08.py`
- `mini_projects/model_fit_analysis.py`

### Mini-Project
Built a model-fit analysis workflow using Decision Tree Regression. Trained models with different maximum depths, calculated training and test MAE, and compared their performance in a results table to investigate underfitting, overfitting, and generalization.

### Key Learnings
- Generalization means performing well on unseen data.
- Underfitting occurs when a model fails to learn important patterns.
- Overfitting occurs when a model fits training data too closely and performs worse on unseen data.
- Training performance alone cannot establish model quality.
- `max_depth` controls the maximum depth of a decision tree.
- Training MAE and test MAE help compare model performance.
- A large gap between training and test error can indicate overfitting.
- Synthetic datasets demonstrate concepts but do not establish real-world performance.
---

## Day 9: Hyperparameter Tuning and Cross-Validation

### Topics Covered
- Parameters vs. hyperparameters
- Decision tree hyperparameter `max_depth`
- Underfitting and overfitting in model selection
- Cross-validation with `cross_val_score()`
- Five-fold cross-validation
- Hyperparameter search with `GridSearchCV`
- Comparing candidate model settings
- Using negative MAE as a Scikit-learn scoring convention
- Selecting the best estimator with `best_estimator_`
- Evaluating the selected model on held-out test data

### Files
- `notes/09_hyperparameter_tuning.py`
- `exercises/exercise_09.py`
- `mini_projects/hyperparameter_tuning_analysis.py`

### Mini-Project
Built a hyperparameter-tuning analysis workflow using Decision Tree Regression and GridSearchCV. Compared different maximum tree depths using five-fold cross-validation, summarized training and validation MAE, selected the best candidate, and evaluated it on held-out test data.

### Key Learnings
- Parameters are learned from data; hyperparameters are selected before training.
- Cross-validation evaluates candidate settings across multiple data splits.
- `GridSearchCV` searches the specified hyperparameter combinations.
- Lower MAE indicates smaller average absolute prediction errors.
- Scikit-learn uses negative MAE for its model-selection scoring convention.
- `best_params_` returns the selected settings.
- `best_estimator_` returns the selected, refitted model.
- The test set should remain separate during hyperparameter selection and be used for final evaluation.
- The best candidate in a search is not guaranteed to be the best possible model.
---

## Day 10: Scikit-learn Pipelines

### Topics Covered
- Understanding machine-learning pipelines
- Combining preprocessing and modeling steps
- `Pipeline()` from Scikit-learn
- Integrating `StandardScaler` and `LogisticRegression`
- Training and predicting through a pipeline
- Preventing preprocessing data leakage
- Pipelines with `GridSearchCV`
- Tuning pipeline hyperparameters using `model__parameter` syntax
- Evaluating classification models

### Files
- `notes/10_ml_pipelines.py`
- `exercises/exercise_10.py`
- `mini_projects/pipeline_analysis.py`

### Mini-Project
Built a customer-churn classification workflow using a Scikit-learn Pipeline. Combined feature scaling and Logistic Regression, tuned regularization strength with GridSearchCV, compared cross-validation performance, and evaluated the selected pipeline using accuracy, precision, recall, F1-score, and a confusion matrix.

### Key Learnings
- A pipeline combines preprocessing and model training into one workflow.
- `pipeline.fit()` fits preprocessing steps and trains the estimator.
- `pipeline.predict()` applies the fitted preprocessing steps before making predictions.
- Preprocessing is fitted within each training fold during cross-validation.
- Pipeline hyperparameters use the `step_name__parameter_name` format.
- `model__C` tunes the regularization strength of Logistic Regression.
- GridSearchCV selects settings using cross-validation.
- The held-out test set should remain separate during model selection.
