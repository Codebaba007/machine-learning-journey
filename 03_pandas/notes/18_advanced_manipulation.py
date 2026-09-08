import pandas as pd


students = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Department": ["CSE", "EEE", "CSE", "BBA", "EEE"],
    "Age": [21, 22, 20, 23, 21],
    "Score": [85, 72, 91, 65, 78]
})


print("Original Data")
print(students)


# Create new columns
print("\nUsing assign()")

students = students.assign(
    Bonus=5,
    Final_Score=students["Score"] + 5
)

print(students)


# Rename columns
print("\nUsing rename()")

students = students.rename(
    columns={
        "Final_Score": "FinalScore"
    }
)

print(students)


# Remove columns
print("\nUsing drop()")

students = students.drop(columns=["Bonus"])

print(students)


# Sort using multiple columns
print("\nSorting by Department and Score")

students = students.sort_values(
    ["Department", "Score"],
    ascending=[True, False]
)

print(students)


# Filter using query()
print("\nUsing query()")

high_scores = students.query("Score >= 80")

print(high_scores)


# Get largest values
print("\nUsing nlargest()")

top_students = students.nlargest(
    3,
    "Score"
)

print(top_students)


# Get smallest values
print("\nUsing nsmallest()")

lowest_students = students.nsmallest(
    2,
    "Score"
)

print(lowest_students)


# Limit values within a range
print("\nUsing clip()")

students["Score"] = students["Score"].clip(
    lower=70,
    upper=90
)

print(students)


# Practical workflow
print("\nFinal Data Transformation")

students = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Department": ["CSE", "EEE", "CSE", "BBA", "EEE"],
    "Score": [85, 72, 91, 65, 78],
    "Attendance": [95, 82, 98, 70, 88]
})

students = students.assign(
    FinalScore=students["Score"] + 5
)

students = students.rename(
    columns={
        "FinalScore": "Final_Score"
    }
)

students = students.query(
    "Attendance >= 80"
)

students = students.sort_values(
    "Final_Score",
    ascending=False
)

students["Final_Score"] = students["Final_Score"].clip(
    upper=100
)

print(students)