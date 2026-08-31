import pandas as pd


# ============================================================
# Pandas Student Performance Pivot Analyzer
# ============================================================

students = pd.DataFrame({
    "Student": [
        "Student 1", "Student 2", "Student 3", "Student 4",
        "Student 5", "Student 6", "Student 7", "Student 8",
        "Student 9", "Student 10", "Student 11", "Student 12"
    ],
    "Department": [
        "Science", "Science", "Arts", "Arts",
        "Commerce", "Commerce", "Science", "Arts",
        "Commerce", "Science", "Commerce", "Arts"
    ],
    "Gender": [
        "Male", "Female", "Female", "Male",
        "Male", "Female", "Male", "Female",
        "Male", "Female", "Female", "Male"
    ],
    "Python": [78, 85, 72, 90, 88, 76, 95, 81, 69, 92, 84, 87],
    "NumPy": [85, 91, 81, 76, 94, 89, 90, 84, 73, 88, 86, 92],
    "Math": [92, 87, 89, 84, 91, 93, 96, 86, 75, 95, 90, 88]
})


print("PANDAS STUDENT PERFORMANCE PIVOT ANALYZER")
print("==========================================")


# ============================================================
# 1. Basic Dataset
# ============================================================

print("\nDataset")
print("----------------------------")
print(students)


# ============================================================
# 2. Department Distribution
# ============================================================

print("\nStudents By Department")
print("----------------------------")

print(
    students["Department"].value_counts()
)


# ============================================================
# 3. Gender Distribution
# ============================================================

print("\nStudents By Gender")
print("----------------------------")

print(
    students["Gender"].value_counts()
)


# ============================================================
# 4. Average Marks By Department
# ============================================================

department_average = pd.pivot_table(
    students,
    values=["Python", "NumPy", "Math"],
    index="Department",
    aggfunc="mean"
)

print("\nAverage Marks By Department")
print("----------------------------")
print(department_average)


# ============================================================
# 5. Department + Gender Analysis
# ============================================================

gender_analysis = pd.pivot_table(
    students,
    values=["Python", "NumPy", "Math"],
    index="Department",
    columns="Gender",
    aggfunc="mean"
)

print("\nAverage Marks By Department And Gender")
print("----------------------------")
print(gender_analysis)


# ============================================================
# 6. Multiple Statistics
# ============================================================

statistics = pd.pivot_table(
    students,
    values=["Python", "Math"],
    index="Department",
    aggfunc=["mean", "max", "min"]
)

print("\nDepartment Statistics")
print("----------------------------")
print(statistics)


# ============================================================
# 7. Department vs Gender
# ============================================================

cross_table = pd.crosstab(
    students["Department"],
    students["Gender"]
)

print("\nDepartment vs Gender")
print("----------------------------")
print(cross_table)


# ============================================================
# 8. Department Gender Percentages
# ============================================================

cross_percentage = pd.crosstab(
    students["Department"],
    students["Gender"],
    normalize="index"
)

print("\nDepartment Gender Percentages")
print("----------------------------")
print(cross_percentage)


# ============================================================
# 9. Wide → Long
# ============================================================

long_data = pd.melt(
    students,
    id_vars=["Student", "Department", "Gender"],
    value_vars=["Python", "NumPy", "Math"],
    var_name="Subject",
    value_name="Score"
)

print("\nLong Format")
print("----------------------------")
print(long_data)


# ============================================================
# 10. Subject Performance
# ============================================================

subject_average = long_data.groupby(
    "Subject"
)["Score"].mean()

print("\nAverage Score By Subject")
print("----------------------------")
print(subject_average)


# ============================================================
# 11. Best Subject
# ============================================================

best_subject = subject_average.idxmax()

print("\nBest Subject")
print("----------------------------")
print(best_subject)
print("Average:", subject_average[best_subject])


# ============================================================
# 12. Long → Wide
# ============================================================

wide_data = long_data.pivot(
    index=["Student", "Department", "Gender"],
    columns="Subject",
    values="Score"
).reset_index()

print("\nBack To Wide Format")
print("----------------------------")
print(wide_data)


# ============================================================
# 13. Overall Student Average
# ============================================================

students["Average"] = students[
    ["Python", "NumPy", "Math"]
].mean(axis=1)


# ============================================================
# 14. Best Student Per Department
# ============================================================

best_students = students.loc[
    students.groupby("Department")["Average"].idxmax()
]

print("\nBest Student Per Department")
print("----------------------------")

print(
    best_students[
        ["Department", "Student", "Average"]
    ].sort_values("Department")
)


# ============================================================
# 15. Final Summary
# ============================================================

print("\nFinal Summary")
print("============================")
print("Total Students:", len(students))
print("Departments:", students["Department"].nunique())
print("Class Average:", students["Average"].mean())
print("Best Subject:", best_subject)