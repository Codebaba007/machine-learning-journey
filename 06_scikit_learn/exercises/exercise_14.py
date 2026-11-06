
import numpy as np

from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([
    [1000, 2, 10, 500],
    [1200, 2, 8, 600],
    [1500, 3, 5, 700],
    [1800, 3, 4, 800],
    [2000, 4, 3, 900],
    [2200, 4, 2, 950],
    [900, 2, 15, 400],
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
# 1. SelectKBest
# -----------------------------------

selector = SelectKBest(
    score_func=f_regression,
    k=2
)

X_selected = selector.fit_transform(X, y)

print("SelectKBest selected features:")
print(np.array(feature_names)[selector.get_support()])

print("\nSelectKBest feature scores:")
for name, score in zip(feature_names, selector.scores_):
    print(f"{name}: {score:.4f}")

print("\nSelected feature data:")
print(X_selected)

# -----------------------------------
# 2. Random Forest feature importance
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
# 3. Recursive Feature Elimination
# -----------------------------------

rfe = RFE(
    estimator=LinearRegression(),
    n_features_to_select=2
)

X_rfe = rfe.fit_transform(X, y)

print("\nRFE selected features:")
print(np.array(feature_names)[rfe.support_])

print("\nRFE feature rankings:")
for name, rank in zip(feature_names, rfe.ranking_):
    print(f"{name}: Rank {rank}")

print("\nRFE selected feature data:")
print(X_rfe)
