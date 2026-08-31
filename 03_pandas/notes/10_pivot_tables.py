import pandas as pd


students = pd.DataFrame({
    "Student": [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J"
    ],
    "Department": [
        "Science", "Science", "Arts", "Arts", "Commerce",
        "Commerce", "Science", "Arts", "Commerce", "Science"
    ],
    "Gender": [
        "Male", "Female", "Female", "Male", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],
    "Python": [78, 85, 72, 90, 88, 76, 95, 81, 69, 92],
    "NumPy": [85, 91, 81, 76, 94, 89, 90, 84, 73, 88],
    "Math": [92, 87, 89, 84, 91, 93, 96, 86, 75, 95]
})


print("STUDENT DATA")
print("====================")
print(students)


# ============================================================
# 1. value_counts()
# ============================================================

print("\nDepartment Counts")
print("====================")
print(students["Department"].value_counts())


print("\nGender Counts")
print("====================")
print(students["Gender"].value_counts())


# ============================================================
# 2. pivot_table() — Average Marks By Department
# ============================================================

print("\nAverage Marks By Department")
print("====================")

department_pivot = pd.pivot_table(
    students,
    values=["Python", "NumPy", "Math"],
    index="Department",
    aggfunc="mean"
)

print(department_pivot)


# ============================================================
# 3. pivot_table() — Department + Gender
# ============================================================

print("\nAverage Marks By Department And Gender")
print("====================")

department_gender = pd.pivot_table(
    students,
    values=["Python", "NumPy", "Math"],
    index="Department",
    columns="Gender",
    aggfunc="mean"
)

print(department_gender)


# ============================================================
# 4. Multiple Aggregations
# ============================================================

print("\nMultiple Statistics By Department")
print("====================")

statistics = pd.pivot_table(
    students,
    values=["Python", "Math"],
    index="Department",
    aggfunc=["mean", "max", "min"]
)

print(statistics)


# ============================================================
# 5. crosstab()
# ============================================================

print("\nDepartment vs Gender")
print("====================")

cross_table = pd.crosstab(
    students["Department"],
    students["Gender"]
)

print(cross_table)


# ============================================================
# 6. crosstab() With Percentages
# ============================================================

print("\nDepartment vs Gender Percentage")
print("====================")

cross_percentage = pd.crosstab(
    students["Department"],
    students["Gender"],
    normalize="index"
)

print(cross_percentage)


# ============================================================
# 7. Create Average Column
# ============================================================

students["Average"] = students[
    ["Python", "NumPy", "Math"]
].mean(axis=1)

print("\nStudent Averages")
print("====================")
print(
    students[
        ["Student", "Department", "Average"]
    ]
)


# ============================================================
# 8. Melt — Wide To Long Format
# ============================================================

long_format = pd.melt(
    students,
    id_vars=["Student", "Department", "Gender"],
    value_vars=["Python", "NumPy", "Math"],
    var_name="Subject",
    value_name="Score"
)

print("\nLong Format Using melt()")
print("====================")
print(long_format)


# ============================================================
# 9. Analyze Long Format
# ============================================================

print("\nAverage Score By Subject")
print("====================")

print(
    long_format.groupby("Subject")["Score"].mean()
)


# ============================================================
# 10. Pivot Long Data Back
# ============================================================

wide_format = long_format.pivot(
    index=["Student", "Department", "Gender"],
    columns="Subject",
    values="Score"
).reset_index()

print("\nBack To Wide Format")
print("====================")
print(wide_format)