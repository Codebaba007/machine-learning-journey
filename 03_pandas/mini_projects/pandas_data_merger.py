import pandas as pd


# ============================================================
# Pandas Student Data Merger
# ============================================================

students = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 5],
    "Student": [
        "Student 1",
        "Student 2",
        "Student 3",
        "Student 4",
        "Student 5"
    ],
    "Department": [
        "Science",
        "Science",
        "Arts",
        "Commerce",
        "Arts"
    ]
})


marks = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 6],
    "Python": [78, 85, 72, 90, 88],
    "NumPy": [85, 91, 81, 76, 94],
    "Math": [92, 87, 89, 84, 91]
})


attendance = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 5],
    "Attendance": [95, 88, 92, 78, 96]
})


print("PANDAS STUDENT DATA MERGER")
print("============================")


# ============================================================
# 1. Display Original DataFrames
# ============================================================

print("\nStudent Information")
print("----------------------------")
print(students)

print("\nMarks")
print("----------------------------")
print(marks)

print("\nAttendance")
print("----------------------------")
print(attendance)


# ============================================================
# 2. Inner Merge
# ============================================================

inner = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="inner"
)

print("\nInner Merge")
print("----------------------------")
print(inner)


# ============================================================
# 3. Left Merge
# ============================================================

merged = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="left"
)

print("\nLeft Merge")
print("----------------------------")
print(merged)


# ============================================================
# 4. Merge Attendance
# ============================================================

merged = pd.merge(
    merged,
    attendance,
    on="Student_ID",
    how="left"
)

print("\nAfter Adding Attendance")
print("----------------------------")
print(merged)


# ============================================================
# 5. Calculate Average
# ============================================================

merged["Average"] = merged[
    ["Python", "NumPy", "Math"]
].mean(axis=1)

print("\nWith Average")
print("----------------------------")
print(merged)


# ============================================================
# 6. Handle Missing Marks
# ============================================================

for column in ["Python", "NumPy", "Math"]:
    merged[column] = merged[column].fillna(
        merged[column].mean()
    )


# ============================================================
# 7. Recalculate Average
# ============================================================

merged["Average"] = merged[
    ["Python", "NumPy", "Math"]
].mean(axis=1)


# ============================================================
# 8. Performance Status
# ============================================================

merged["Status"] = merged["Average"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)


# ============================================================
# 9. High Performers
# ============================================================

print("\nHigh Performers")
print("----------------------------")

high_performers = merged[
    merged["Average"] >= 80
]

print(
    high_performers[
        ["Student", "Department", "Average"]
    ]
)


# ============================================================
# 10. Attendance Filter
# ============================================================

print("\nStudents With Attendance >= 90%")
print("----------------------------")

high_attendance = merged[
    merged["Attendance"] >= 90
]

print(
    high_attendance[
        ["Student", "Attendance"]
    ]
)


# ============================================================
# 11. Department Analysis
# ============================================================

print("\nDepartment Performance")
print("----------------------------")

department_average = merged.groupby(
    "Department"
)["Average"].mean()

print(department_average)


# ============================================================
# 12. Best Student
# ============================================================

best_index = merged["Average"].idxmax()

print("\nBest Student")
print("----------------------------")
print("Student:", merged.loc[best_index, "Student"])
print("Average:", merged.loc[best_index, "Average"])


# ============================================================
# 13. Final Dataset
# ============================================================

print("\nFinal Merged Dataset")
print("============================")

print(merged)