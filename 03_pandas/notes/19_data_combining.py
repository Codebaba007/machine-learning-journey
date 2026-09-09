import pandas as pd


# First dataset
students_1 = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Department": ["CSE", "EEE", "CSE"]
})


# Second dataset
students_2 = pd.DataFrame({
    "Student_ID": [4, 5, 6],
    "Name": ["David", "Emma", "Frank"],
    "Department": ["BBA", "EEE", "CSE"]
})


print("First Dataset")
print(students_1)

print("\nSecond Dataset")
print(students_2)


# Combine rows
print("\nUsing concat()")

all_students = pd.concat(
    [students_1, students_2],
    ignore_index=True
)

print(all_students)


# Dataset with additional columns
scores = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 5, 6],
    "Math": [85, 72, 91, 65, 78, 88],
    "Python": [90, 68, 95, 70, 82, 92]
})


print("\nScores Dataset")
print(scores)


# Combine using a common column
print("\nUsing merge()")

student_scores = pd.merge(
    all_students,
    scores,
    on="Student_ID",
    how="inner"
)

print(student_scores)


# Inner merge
print("\nInner Merge")

inner_merge = pd.merge(
    all_students,
    scores,
    on="Student_ID",
    how="inner"
)

print(inner_merge)


# Left merge
print("\nLeft Merge")

left_merge = pd.merge(
    all_students,
    scores,
    on="Student_ID",
    how="left"
)

print(left_merge)


# Right merge
print("\nRight Merge")

right_merge = pd.merge(
    all_students,
    scores,
    on="Student_ID",
    how="right"
)

print(right_merge)


# Outer merge
print("\nOuter Merge")

outer_merge = pd.merge(
    all_students,
    scores,
    on="Student_ID",
    how="outer"
)

print(outer_merge)


# Fill missing values
print("\nHandling Missing Values")

outer_merge["Math"] = outer_merge["Math"].fillna(0)
outer_merge["Python"] = outer_merge["Python"].fillna(0)

print(outer_merge)


# Another dataset with missing information
updated_departments = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Department": ["CSE", "EEE", "CSE"]
})

original_departments = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Department": ["Computer Science", "Electrical", "Computer Science"]
})


# Fill missing values from another DataFrame
print("\nUsing combine_first()")

combined_departments = (
    updated_departments
    .set_index("Student_ID")
    .combine_first(
        original_departments.set_index("Student_ID")
    )
    .reset_index()
)

print(combined_departments)


# Combine datasets vertically
print("\nCombining More Data")

january = pd.DataFrame({
    "Student_ID": [1, 2],
    "Month": ["January", "January"],
    "Score": [85, 78]
})

february = pd.DataFrame({
    "Student_ID": [3, 4],
    "Month": ["February", "February"],
    "Score": [91, 88]
})

monthly_data = pd.concat(
    [january, february],
    ignore_index=True
)

print(monthly_data)


# Combine datasets horizontally
print("\nCombining Columns")

names = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"]
})

ages = pd.DataFrame({
    "Age": [21, 22, 20]
})

combined_columns = pd.concat(
    [names, ages],
    axis=1
)

print(combined_columns)


# Final dataset
print("\nFinal Student Dataset")

students = pd.merge(
    all_students,
    scores,
    on="Student_ID",
    how="left"
)

students["Math"] = students["Math"].fillna(0)
students["Python"] = students["Python"].fillna(0)

students["Average"] = (
    students["Math"] + students["Python"]
) / 2

print(students)