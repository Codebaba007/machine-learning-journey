import pandas as pd


students = pd.DataFrame({
    "Department": [
        "CSE",
        "CSE",
        "EEE",
        "EEE",
        "BBA",
        "BBA"
    ],
    "Semester": [
        1,
        2,
        1,
        2,
        1,
        2
    ],
    "Student": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Frank"
    ],
    "Score": [
        85,
        90,
        78,
        88,
        82,
        91
    ]
})


print("Original Data")
print(students)


print("\nCreating a MultiIndex")
multi_students = students.set_index(
    ["Department", "Semester"]
)
print(multi_students)


print("\nViewing the MultiIndex")
print(multi_students.index)


print("\nSelecting All CSE Students")
print(multi_students.loc["CSE"])


print("\nSelecting CSE Semester 1")
print(multi_students.loc[("CSE", 1)])


print("\nSelecting CSE Semester 1 and EEE Semester 2")
print(
    multi_students.loc[
        [
            ("CSE", 1),
            ("EEE", 2)
        ]
    ]
)


print("\nConverting Index Back to Columns")
normal_students = multi_students.reset_index()
print(normal_students)


print("\nSwapping Index Levels")
swapped = multi_students.swaplevel(
    "Department",
    "Semester"
)
print(swapped)


print("\nSorting by Index")
sorted_students = multi_students.sort_index()
print(sorted_students)


print("\nSelecting CSE Using the Department Level")
cse_students = multi_students.xs(
    "CSE",
    level="Department"
)
print(cse_students)


print("\nCalculating Average Score by Department and Semester")
department_semester_average = (
    students
    .groupby(["Department", "Semester"])["Score"]
    .mean()
)
print(department_semester_average)


print("\nCalculating Multiple Statistics by Department")
summary = students.groupby(
    "Department"
).agg({
    "Score": ["mean", "max", "min"]
})
print(summary)


print("\nFlattening MultiIndex Columns")
summary.columns = [
    "_".join(column)
    for column in summary.columns
]

summary = summary.reset_index()
print(summary)


print("\nFinal MultiIndex Analysis")
final_analysis = (
    students
    .groupby(["Department", "Semester"])
    .agg(
        Average_Score=("Score", "mean"),
        Highest_Score=("Score", "max"),
        Lowest_Score=("Score", "min"),
        Student_Count=("Student", "count")
    )
)
print(final_analysis)


print("\nResetting the Final Index")
final_analysis = final_analysis.reset_index()
print(final_analysis)