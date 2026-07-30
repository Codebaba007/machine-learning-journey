# 🧠 Scikit-Learn Cheatsheet

## The API Pattern
```python
model = Model(hyperparams)
model.fit(X_train, y_train)
preds = model.predict(X_test)
transformed_data = model.transform(X) # For transformers
```

## Preprocessing
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

## Train/Test Split & CV
```python
from sklearn.model_selection import train_test_split, cross_val_score
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scores = cross_val_score(model, X, y, cv=5)
```

## Classification Models
```python
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
```

## Regression Models
```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
```

## Clustering
```python
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
```

## Dimensionality Reduction
```python
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
```

## Model Evaluation
```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score, mean_squared_error, r2_score
```

## Pipelines
```python
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier())
])
pipeline.fit(X_train, y_train)
```

## Hyperparameter Tuning
```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
param_grid = {'n_estimators': [100, 200], 'max_depth': [None, 10]}
grid = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid.fit(X_train, y_train)
```

## Feature Selection
```python
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(f_classif, k=10)
X_new = selector.fit_transform(X, y)
```
