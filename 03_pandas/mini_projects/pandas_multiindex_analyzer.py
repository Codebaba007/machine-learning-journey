import pandas as pd


students = pd.DataFrame({
    "Department": [
        "CSE", "CSE", "CSE",
        "EEE", "EEE", "EEE",
        "BBA", "BBA", "BBA"
    ],
    "Semester": [
        1, 1, 2,
        1, 2, 2,
        1, 1, 2
    ],
    "Student": [
        "Alice", "Alex", "Bob",
        "Charlie", "David", "Daniel",
        "Eve", "Emma", "Frank"
    ],
    "Score": [
        85, 92, 90,
        78, 88, 84,
        82, 95, 91
    ]
})


print("Original Student Data")
print(students)


print("\nCreating MultiIndex")
multi_students = students.set_index(
    ["Department", "Semester"]
)
print(multi_students)


print("\nCSE Students")
print(multi_students.loc["CSE"])


print("\nCSE Semester 1")
print(multi_students.loc[("CSE", 1)])


print("\nEEE Semester 2")
print(multi_students.loc[("EEE", 2)])


print("\nStudents Without MultiIndex")
normal_students = multi_students.reset_index()
print(normal_students)


print("\nIndex Levels Swapped")
swapped = multi_students.swaplevel(
    "Department",
    "Semester"
)
print(swapped)


print("\nSorted MultiIndex")
sorted_students = multi_students.sort_index()
print(sorted_students)


print("\nCSE Students Using xs")
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
department_stats = (
    students
    .groupby("Department")
    .agg(
        Average_Score=("Score", "mean"),
        Highest_Score=("Score", "max"),
        Lowest_Score=("Score", "min"),
        Student_Count=("Student", "count")
    )
)
print(department_stats)


print("\nDepartment and Semester Analysis")
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


print("\nFinal Analysis as Normal DataFrame")
final_analysis = final_analysis.reset_index()
print(final_analysis)


final_analysis.to_csv(
    "student_multiindex_analysis.csv",
    index=False
)

print("\nSaved student_multiindex_analysis.csv")