import pandas as pd


students = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Python": [78, 85, 72, 90, 88, 76, 95, 81],
    "NumPy": [85, 91, 81, 76, 94, 89, 90, 84],
    "Math": [92, 87, 89, 84, 91, 93, 96, 86]
})


scores = students[["Python", "NumPy", "Math"]]


# 1. Descriptive Statistics

print("Descriptive Statistics")
print("====================")
print(scores.describe())


# 2. Mean

print("\nMean")
print("====================")
print(scores.mean())


# 3. Median

print("\nMedian")
print("====================")
print(scores.median())


# 4. Mode

print("\nMode")
print("====================")
print(scores.mode())


# 5. Standard Deviation

print("\nStandard Deviation")
print("====================")
print(scores.std())


# 6. Variance

print("\nVariance")
print("====================")
print(scores.var())


# 7. Minimum

print("\nMinimum")
print("====================")
print(scores.min())


# 8. Maximum

print("\nMaximum")
print("====================")
print(scores.max())


# 9. Quantiles

print("\nQuantiles")
print("====================")
print(
    scores.quantile([0.25, 0.50, 0.75])
)


# 10. Correlation

print("\nCorrelation")
print("====================")
print(scores.corr())


# 11. Subject Totals

print("\nSubject Totals")
print("====================")
print(scores.sum())


# 12. Subject With Highest Average

subject_means = scores.mean()

print("\nHighest Average Subject")
print("====================")
print("Subject:", subject_means.idxmax())
print("Average:", subject_means.max()) 