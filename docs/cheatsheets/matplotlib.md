# 📊 Matplotlib & Seaborn Cheatsheet

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

## Figure & Axes Anatomy
```python
fig, ax = plt.subplots(figsize=(8, 6))
# Figure is the whole window, Axes is the actual plot
```

## Basic Plots
```python
# Line
ax.plot(x, y)
# Scatter
ax.scatter(x, y)
# Bar
ax.bar(x, y)
# Histogram
ax.hist(data, bins=20)
```

## Customizing
```python
ax.set_title("Title")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()
ax.grid(True)
ax.plot(x, y, color='red', linestyle='--', marker='o')
```

## Subplots & Layouts
```python
fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0, 0].plot(x, y)
plt.tight_layout()
```

## Seaborn Statistical Plots
```python
sns.boxplot(x='cat', y='val', data=df)
sns.violinplot(x='cat', y='val', data=df)
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
sns.pairplot(df, hue='class')
```

## Saving Figures
```python
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
```

## Style Sheets
```python
plt.style.use('ggplot')
sns.set_theme(style="whitegrid")
```

## Common ML Visualizations
```python
# Confusion Matrix
from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test)

# ROC Curve
from sklearn.metrics import RocCurveDisplay
RocCurveDisplay.from_estimator(clf, X_test, y_test)
```
