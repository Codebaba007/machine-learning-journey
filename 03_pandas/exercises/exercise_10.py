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


# ============================================================
# 1. Count Students By Department
# ============================================================

print("Students By Department")
print("====================")

print(
    students["Department"].value_counts()
)


# ============================================================
# 2. Count Students By Gender
# ============================================================

print("\nStudents By Gender")
print("====================")

print(
    students["Gender"].value_counts()
)


# ============================================================
# 3. Average Python Marks By Department
# ============================================================

print("\nAverage Python By Department")
print("====================")

python_pivot = pd.pivot_table(
    students,
    values="Python",
    index="Department",
    aggfunc="mean"
)

print(python_pivot)


# ============================================================
# 4. Average All Subjects By Department
# ============================================================

print("\nAverage Subjects By Department")
print("====================")

subject_pivot = pd.pivot_table(
    students,
    values=["Python", "NumPy", "Math"],
    index="Department",
    aggfunc="mean"
)

print(subject_pivot)


# ============================================================
# 5. Department + Gender Pivot Table
# ============================================================

print("\nAverage Marks By Department And Gender")
print("====================")

gender_pivot = pd.pivot_table(
    students,
    values=["Python", "NumPy", "Math"],
    index="Department",
    columns="Gender",
    aggfunc="mean"
)

print(gender_pivot)


# ============================================================
# 6. Crosstab — Department vs Gender
# ============================================================

print("\nDepartment vs Gender")
print("====================")

cross_table = pd.crosstab(
    students["Department"],
    students["Gender"]
)

print(cross_table)


# ============================================================
# 7. Crosstab Percentages
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
# 8. Wide → Long Using melt()
# ============================================================

long_data = pd.melt(
    students,
    id_vars=["Student", "Department", "Gender"],
    value_vars=["Python", "NumPy", "Math"],
    var_name="Subject",
    value_name="Score"
)

print("\nLong Format")
print("====================")

print(long_data)


# ============================================================
# 9. Average Score By Subject
# ============================================================

print("\nAverage Score By Subject")
print("====================")

subject_average = long_data.groupby(
    "Subject"
)["Score"].mean()

print(subject_average)


# ============================================================
# 10. Long → Wide Using pivot()
# ============================================================

wide_data = long_data.pivot(
    index=["Student", "Department", "Gender"],
    columns="Subject",
    values="Score"
).reset_index()

print("\nBack To Wide Format")
print("====================")

print(wide_data)