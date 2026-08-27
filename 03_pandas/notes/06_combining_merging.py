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

combined_rows = pd.concat([df1, df2], ignore_index=True)

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
# 3. merge() — Inner Join
# ============================================================

students = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Student": ["A", "B", "C", "D"]
})

marks = pd.DataFrame({
    "Student_ID": [1, 2, 3, 5],
    "Math": [92, 85, 89, 95]
})

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
# 4. Left Join
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
# 5. Right Join
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
# 6. Outer Join
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
# 7. merge() Using Different Column Names
# ============================================================

student_info = pd.DataFrame({
    "ID": [1, 2, 3],
    "Student": ["A", "B", "C"]
})

student_marks = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Math": [92, 85, 89]
})

merged = pd.merge(
    student_info,
    student_marks,
    left_on="ID",
    right_on="Student_ID"
)

print("\nDifferent Key Names")
print("====================")
print(merged)


# ============================================================
# 8. join()
# ============================================================

students = pd.DataFrame({
    "Student": ["A", "B", "C"]
}, index=[1, 2, 3])

marks = pd.DataFrame({
    "Python": [78, 85, 72],
    "Math": [92, 87, 89]
}, index=[1, 2, 3])

joined = students.join(marks)

print("\nUsing join()")
print("====================")
print(joined)