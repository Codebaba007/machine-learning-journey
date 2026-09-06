import pandas as pd


students = pd.DataFrame({
    "Department": ["CSE", "CSE", "EEE", "EEE", "BBA", "BBA"],
    "Semester": [1, 2, 1, 2, 1, 2],
    "Student": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Score": [85, 90, 78, 88, 82, 91]
})


print("Original Data")
print(students)


print("\nCreating MultiIndex")
multi_students = students.set_index(
    ["Department", "Semester"]
)
print(multi_students)


print("\nViewing Index")
print(multi_students.index)


print("\nSelecting CSE Students")
print(multi_students.loc["CSE"])


print("\nSelecting CSE Semester 1")
print(multi_students.loc[("CSE", 1)])


print("\nSelecting Multiple Groups")
print(
    multi_students.loc[
        [
            ("CSE", 1),
            ("EEE", 2)
        ]
    ]
)


print("\nResetting Index")
normal_students = multi_students.reset_index()
print(normal_students)


print("\nSwapping Index Levels")
swapped = multi_students.swaplevel(
    "Department",
    "Semester"
)
print(swapped)


print("\nSorting Index")
sorted_students = multi_students.sort_index()
print(sorted_students)


print("\nSelecting CSE Using xs")
cse_students = multi_students.xs(
    "CSE",
    level="Department"
)
print(cse_students)


print("\nAverage Score by Department and Semester")
average_scores = (
    students
    .groupby(["Department", "Semester"])["Score"]
    .mean()
)
print(average_scores)


print("\nDepartment Statistics")
summary = students.groupby(
    "Department"
).agg({
    "Score": ["mean", "max", "min"]
})
print(summary)


print("\nFlattening Columns")
summary.columns = [
    "_".join(column)
    for column in summary.columns
]

summary = summary.reset_index()
print(summary)