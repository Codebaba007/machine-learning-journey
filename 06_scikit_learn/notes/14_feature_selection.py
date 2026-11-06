
import numpy as np

from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# -----------------------------------
# 1. Create dataset
# -----------------------------------

X = np.array([
    [1000, 2, 10, 500],
    [1200, 2, 8, 600],
    [1500, 3, 5, 700],
    [1800, 3, 4, 800],
    [2000, 4, 3, 900],
    [2200, 4, 2, 950],
    [900,  2, 15, 400],
    [1600, 3, 6, 750],
    [1400, 3, 7, 650],
    [2500, 5, 1, 1000]
])

y = np.array([
    120, 140, 180, 220, 250,
    280, 100, 195, 165, 320
])

feature_names = [
    "Area",
    "Bedrooms",
    "Age",
    "Income"
]

# -----------------------------------
# 2. SelectKBest
# -----------------------------------

selector = SelectKBest(
    score_func=f_regression,
    k=2
)

X_selected = selector.fit_transform(X, y)

print("SelectKBest scores:")
print(selector.scores_)

print("\nSelected features:")
print(selector.get_support())

print("\nSelected feature names:")
print(np.array(feature_names)[selector.get_support()])

# -----------------------------------
# 3. Random Forest feature importance
# -----------------------------------

forest = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

forest.fit(X, y)

importance = forest.feature_importances_

print("\nRandom Forest feature importance:")

for name, score in zip(feature_names, importance):
    print(f"{name}: {score:.4f}")

# -----------------------------------
# 4. Recursive Feature Elimination
# -----------------------------------

rfe = RFE(
    estimator=LinearRegression(),
    n_features_to_select=2
)

X_rfe = rfe.fit_transform(X, y)

print("\nRFE selected features:")
print(np.array(feature_names)[rfe.support_])

print("\nRFE rankings:")
print(rfe.ranking_)

# -----------------------------------
# 5. Train/test split
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining shape:", X_train.shape)
print("Testing shape:", X_test.shape)
