import pandas as pd


# ============================================================
# 1. concat() — Combine Rows
# ============================================================

df1 = pd.DataFrame({
    "Student": ["A", "B"],
    "Python": [78, 85]
})

df2 = pd.DataFrame({
    "Student": ["C", "D"],
    "Python": [72, 90]
})

combined_rows = pd.concat(
    [df1, df2],
    ignore_index=True
)

print("Combined Rows")
print("====================")
print(combined_rows)


# ============================================================
# 2. concat() — Combine Columns
# ============================================================

python = pd.DataFrame({
    "Student": ["A", "B", "C"],
    "Python": [78, 85, 72]
})

math = pd.DataFrame({
    "Math": [92, 87, 89]
})

combined_columns = pd.concat(
    [python, math],
    axis=1
)

print("\nCombined Columns")
print("====================")
print(combined_columns)


# ============================================================
# 3. Create DataFrames With Common Student_ID
# ============================================================

students = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Student": ["A", "B", "C", "D"]
})

marks = pd.DataFrame({
    "Student_ID": [1, 2, 3, 5],
    "Math": [92, 85, 89, 95]
})


# ============================================================
# 4. Inner Merge
# ============================================================

inner = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="inner"
)

print("\nInner Merge")
print("====================")
print(inner)


# ============================================================
# 5. Left Merge
# ============================================================

left = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="left"
)

print("\nLeft Merge")
print("====================")
print(left)


# ============================================================
# 6. Right Merge
# ============================================================

right = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="right"
)

print("\nRight Merge")
print("====================")
print(right)


# ============================================================
# 7. Outer Merge
# ============================================================

outer = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="outer"
)

print("\nOuter Merge")
print("====================")
print(outer)


# ============================================================
# 8. Different Key Names
# ============================================================

student_info = pd.DataFrame({
    "ID": [1, 2, 3],
    "Student": ["A", "B", "C"]
})

student_marks = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Math": [92, 85, 89]
})

different_keys = pd.merge(
    student_info,
    student_marks,
    left_on="ID",
    right_on="Student_ID"
)

print("\nDifferent Key Names")
print("====================")
print(different_keys)


# ============================================================
# 9. join()
# ============================================================

student_info = pd.DataFrame({
    "Student": ["A", "B", "C"]
}, index=[1, 2, 3])

student_marks = pd.DataFrame({
    "Python": [78, 85, 72],
    "Math": [92, 87, 89]
}, index=[1, 2, 3])

joined = student_info.join(student_marks)

print("\nUsing join()")
print("====================")
print(joined)


# ============================================================
# 10. concat vs merge
# ============================================================

# concat() → combines DataFrames by rows or columns.
# merge()  → combines related DataFrames using matching keys.