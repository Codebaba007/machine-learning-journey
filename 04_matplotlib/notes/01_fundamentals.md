# 📝 Notes: Data Visualization Fundamentals

## 1. Matplotlib Architecture
Matplotlib has two main interfaces:
- **Pyplot (MATLAB-style)**: `plt.plot()`. Good for quick, simple plots.
- **Object-Oriented API**: `fig, ax = plt.subplots()`. Best practice for complex, customized plots. You modify the `Axes` object directly.

## 2. Choosing the Right Plot
- **Line Plot**: Trends over time.
- **Scatter Plot**: Relationships/correlation between two continuous variables.
- **Bar Chart**: Comparing categorical data.
- **Histogram**: Distribution of a single continuous variable.
- **Box Plot / Violin Plot**: Distribution across categories, showing outliers.

## 3. Seaborn: Statistical Data Visualization
Seaborn is built on top of Matplotlib and integrates closely with Pandas DataFrames.
- It provides beautiful default styles.
- Functions like `sns.pairplot()` and `sns.heatmap()` perform complex visualizations and aggregations in a single line of code.

## 4. ML Visualizations
Visualizing model performance is key:
- **Confusion Matrix**: Visualizes True/False Positives/Negatives.
- **ROC Curve**: Trade-off between TPR and FPR.
- **Feature Importance**: Bar charts showing which variables matter most.
