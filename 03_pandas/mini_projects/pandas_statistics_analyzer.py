import pandas as pd


# ============================================================
# Pandas Student Statistics Analyzer
# ============================================================

students = pd.DataFrame({
    "Student": [
        "Student 1", "Student 2", "Student 3", "Student 4",
        "Student 5", "Student 6", "Student 7", "Student 8",
        "Student 9", "Student 10"
    ],
    "Python": [78, 85, 72, 90, 88, 76, 95, 81, 69, 92],
    "NumPy": [85, 91, 81, 76, 94, 89, 90, 84, 73, 88],
    "Math": [92, 87, 89, 84, 91, 93, 96, 86, 75, 95]
})


scores = students[["Python", "NumPy", "Math"]]


print("PANDAS STUDENT STATISTICS ANALYZER")
print("===================================")


# ============================================================
# 1. Dataset
# ============================================================

print("\nStudent Dataset")
print("----------------------------")
print(students)


# ============================================================
# 2. Descriptive Statistics
# ============================================================

print("\nDescriptive Statistics")
print("----------------------------")
print(scores.describe())


# ============================================================
# 3. Mean
# ============================================================

means = scores.mean()

print("\nSubject Means")
print("----------------------------")
print(means)


# ============================================================
# 4. Median
# ============================================================

print("\nSubject Medians")
print("----------------------------")
print(scores.median())


# ============================================================
# 5. Mode
# ============================================================

print("\nSubject Modes")
print("----------------------------")
print(scores.mode())


# ============================================================
# 6. Standard Deviation
# ============================================================

print("\nStandard Deviation")
print("----------------------------")
print(scores.std())


# ============================================================
# 7. Variance
# ============================================================

print("\nVariance")
print("----------------------------")
print(scores.var())


# ============================================================
# 8. Quantiles
# ============================================================

print("\nQuantiles")
print("----------------------------")
print(
    scores.quantile([0.25, 0.50, 0.75])
)


# ============================================================
# 9. Correlation
# ============================================================

print("\nCorrelation")
print("----------------------------")
print(scores.corr())


# ============================================================
# 10. Highest and Lowest Subject Average
# ============================================================

print("\nSubject Comparison")
print("----------------------------")

highest_subject = means.idxmax()
lowest_subject = means.idxmin()

print("Highest Average:", highest_subject, means.max())
print("Lowest Average:", lowest_subject, means.min())


# ============================================================
# 11. Create Student Average
# ============================================================

students["Average"] = scores.mean(axis=1)

print("\nStudent Averages")
print("----------------------------")
print(
    students[["Student", "Average"]]
)


# ============================================================
# 12. Best and Lowest Student
# ============================================================

best_index = students["Average"].idxmax()
lowest_index = students["Average"].idxmin()

print("\nBest Student")
print("----------------------------")
print(
    students.loc[
        best_index,
        ["Student", "Average"]
    ]
)

print("\nLowest Student")
print("----------------------------")
print(
    students.loc[
        lowest_index,
        ["Student", "Average"]
    ]
)


# ============================================================
# 13. Above Class Average
# ============================================================

class_average = students["Average"].mean()

print("\nClass Average")
print("----------------------------")
print(class_average)

print("\nStudents Above Class Average")
print("----------------------------")

above_average = students[
    students["Average"] > class_average
]

print(
    above_average[
        ["Student", "Average"]
    ]
)


# ============================================================
# 14. Performance Spread
# ============================================================

print("\nPerformance Range")
print("----------------------------")

for subject in scores.columns:
    value_range = scores[subject].max() - scores[subject].min()
    print(subject, "Range:", value_range)


# ============================================================
# 15. Final Summary
# ============================================================

print("\nFinal Summary")
print("============================")
print("Students:", len(students))
print("Class Average:", class_average)
print("Best Subject:", highest_subject)
print("Lowest Subject:", lowest_subject)
print("Best Student:", students.loc[best_index, "Student"])
print("Best Student Average:", students.loc[best_index, "Average"])