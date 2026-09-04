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
        "Frank"
    ],
    "Department": [
        "CSE",
        "EEE",
        "CSE",
        "CSE",
        "BBA",
        "EEE",
        "CSE",
        "EEE"
    ],
    "Score": [
        85,
        72,
        90,
        85,
        78,
        72,
        95,
        88
    ]
})


duplicates = students.duplicated()

print(duplicates)

duplicate_names = students.duplicated(
    subset=["Student"]
)

print(duplicate_names)

duplicate_records = students[
    students.duplicated(
        subset=["Student"],
        keep=False
    )
]

print(duplicate_records)

duplicate_count = students.duplicated().sum()

print(duplicate_count)

clean_students = students.drop_duplicates()

print(clean_students)

unique_students = students.drop_duplicates(
    subset=["Student"]
)

print(unique_students)

latest_students = students.drop_duplicates(
    subset=["Student"],
    keep="last"
)

print(latest_students)

sorted_students = students.sort_values(
    by="Score",
    ascending=False
)

best_students = sorted_students.drop_duplicates(
    subset=["Student"],
    keep="first"
)

print(best_students)