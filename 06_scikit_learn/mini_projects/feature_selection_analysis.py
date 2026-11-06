
import numpy as np

from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# -----------------------------------
# 1. Create dataset
# -----------------------------------

X = np.array([
    [1000, 2, 10, 500, 101],
    [1200, 2, 8, 600, 205],
    [1500, 3, 5, 700, 309],
    [1800, 3, 4, 800, 410],
    [2000, 4, 3, 900, 515],
    [2200, 4, 2, 950, 612],
    [900, 2, 15, 400, 720],
    [1600, 3, 6, 750, 830],
    [1400, 3, 7, 650, 940],
    [2500, 5, 1, 1000, 105],
    [1100, 2, 12, 450, 215],
    [1900, 4, 3, 850, 325],
    [2300, 4, 2, 980, 435],
    [1700, 3, 5, 780, 545],
    [2100, 4, 2, 920, 655],
    [1300, 3, 9, 620, 765],
    [2400, 5, 1, 990, 875],
    [950, 2, 14, 420, 985],
    [1850, 3, 4, 820, 195],
    [1550, 3, 6, 730, 285]
])

y = np.array([
    120, 140, 180, 220, 250,
    280, 100, 195, 165, 320,
    130, 240, 290, 200, 270,
    150, 310, 105, 230, 185
])

feature_names = [
    "Area",
    "Bedrooms",
    "Age",
    "Income",
    "Random_ID"
]

# -----------------------------------
# 2. Split the data
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# -----------------------------------
# 3. Model using all features
# -----------------------------------

all_features_model = Pipeline([
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression())
])

all_features_model.fit(X_train, y_train)

all_predictions = all_features_model.predict(X_test)

all_mae = mean_absolute_error(
    y_test,
    all_predictions
)

print("Model using all features")
print("MAE:", round(all_mae, 2))

# -----------------------------------
# 4. Model using selected features
# -----------------------------------

selected_features_model = Pipeline([
    ("selection", SelectKBest(
        score_func=f_regression,
        k=3
    )),
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression())
])

selected_features_model.fit(X_train, y_train)

selected_predictions = selected_features_model.predict(X_test)

selected_mae = mean_absolute_error(
    y_test,
    selected_predictions
)

print("\nModel using selected features")
print("MAE:", round(selected_mae, 2))

# -----------------------------------
# 5. Display selected features
# -----------------------------------

selector = selected_features_model.named_steps["selection"]

selected_names = np.array(feature_names)[selector.get_support()]

print("\nSelected features:")
print(selected_names)

print("\nFeature scores:")
for name, score in zip(feature_names, selector.scores_):
    print(f"{name}: {score:.4f}")

# -----------------------------------
# 6. Compare performance
# -----------------------------------

print("\nModel comparison:")

print(f"All features MAE: {all_mae:.2f}")
print(f"Selected features MAE: {selected_mae:.2f}")

if selected_mae < all_mae:
    print("Feature selection improved test performance.")
elif selected_mae > all_mae:
    print("Using all features performed better.")
else:
    print("Both models performed equally.")
