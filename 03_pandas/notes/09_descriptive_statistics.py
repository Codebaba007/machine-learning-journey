import pandas as pd


students = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Python": [78, 85, 72, 90, 88, 76, 95, 81],
    "NumPy": [85, 91, 81, 76, 94, 89, 90, 84],
    "Math": [92, 87, 89, 84, 91, 93, 96, 86]
})


print("STUDENT DATA")
print("====================")
print(students)


# 1. Descriptive Statistics

print("\nDescriptive Statistics")
print("====================")
print(students[["Python", "NumPy", "Math"]].describe())


# 2. Mean

print("\nMean")
print("====================")
print(students[["Python", "NumPy", "Math"]].mean())


# 3. Median

print("\nMedian")
print("====================")
print(students[["Python", "NumPy", "Math"]].median())


# 4. Mode

print("\nMode")
print("====================")
print(students[["Python", "NumPy", "Math"]].mode())


# 5. Standard Deviation

print("\nStandard Deviation")
print("====================")
print(students[["Python", "NumPy", "Math"]].std())


# 6. Variance

print("\nVariance")
print("====================")
print(students[["Python", "NumPy", "Math"]].var())


# 7. Minimum and Maximum

print("\nMinimum")
print("====================")
print(students[["Python", "NumPy", "Math"]].min())

print("\nMaximum")
print("====================")
print(students[["Python", "NumPy", "Math"]].max())


# 8. Sum

print("\nTotal Marks")
print("====================")
print(students[["Python", "NumPy", "Math"]].sum())


# 9. Count

print("\nCount")
print("====================")
print(students[["Python", "NumPy", "Math"]].count())


# 10. Quantiles

print("\nQuantiles")
print("====================")
print(
    students[["Python", "NumPy", "Math"]].quantile(
        [0.25, 0.50, 0.75]
    )
)


# 11. Correlation

print("\nCorrelation")
print("====================")
print(
    students[["Python", "NumPy", "Math"]].corr()
)