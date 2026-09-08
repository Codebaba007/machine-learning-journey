import pandas as pd

students = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"],
    "Department": ["CSE", "EEE", "CSE", "BBA", "EEE", "CSE"],
    "Age": [21, 22, 20, 23, 21, 22],
    "Score": [88, 67, 95, 72, 81, 59],
    "Attendance": [92, 78, 96, 85, 89, 65]
})

students = students.assign(
    Bonus=5,
    Final_Score=students["Score"] + 5
)

students = students.rename(
    columns={"Final_Score": "FinalScore"}
)

students = students.drop(
    columns=["Bonus"]
)

sorted_students = students.sort_values(
    ["Department", "FinalScore"],
    ascending=[True, False]
)

high_scorers = students.query(
    "Score >= 80"
)

top_students = students.nlargest(
    3,
    "FinalScore"
)

lowest_students = students.nsmallest(
    2,
    "Score"
)

students["FinalScore"] = students["FinalScore"].clip(
    lower=0,
    upper=100
)

print("Original Data")
print(students)

print("\nSorted Data")
print(sorted_students)

print("\nHigh Scorers")
print(high_scorers)

print("\nTop 3 Students")
print(top_students)

print("\nLowest 2 Students")
print(lowest_students)

print("\nFinal Scores Limited to 0-100")
print(students)