import pandas as pd


students = pd.DataFrame({
    "Student": [
        "Alice",
        "Bob",
        "Charlie",
        "Alice",
        "David",
        "Bob",
        "Eve",
        "Frank",
        "Charlie",
        "Alice"
    ],
    "Department": [
        "CSE",
        "EEE",
        "CSE",
        "CSE",
        "BBA",
        "EEE",
        "CSE",
        "EEE",
        "CSE",
        "CSE"
    ],
    "Score": [
        85,
        72,
        90,
        92,
        78,
        80,
        95,
        88,
        94,
        87
    ]
})


duplicate_rows = students[
    students.duplicated()
]

duplicate_names = students[
    students.duplicated(
        subset=["Student"],
        keep=False
    )
]

duplicate_count = students.duplicated().sum()

unique_students = students.drop_duplicates(
    subset=["Student"],
    keep="first"
)

best_students = (
    students
    .sort_values(
        by="Score",
        ascending=False
    )
    .drop_duplicates(
        subset=["Student"],
        keep="first"
    )
)

students_without_duplicates = (
    students
    .sort_values(
        by="Score",
        ascending=False
    )
    .drop_duplicates(
        subset=["Student"],
        keep="first"
    )
    .sort_values(
        by="Student"
    )
)

department_counts = (
    students_without_duplicates["Department"]
    .value_counts()
)

average_scores = (
    students_without_duplicates
    .groupby("Department")["Score"]
    .mean()
)

students_without_duplicates.to_csv(
    "students_cleaned.csv",
    index=False
)

print(students)
print(duplicate_rows)
print(duplicate_names)
print(duplicate_count)
print(unique_students)
print(best_students)
print(department_counts)
print(average_scores)
print(students_without_duplicates)