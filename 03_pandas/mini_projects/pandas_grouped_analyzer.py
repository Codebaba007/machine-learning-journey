import pandas as pd


students = pd.DataFrame({
    "Student": [
        "Student 1", "Student 2", "Student 3",
        "Student 4", "Student 5", "Student 6",
        "Student 7", "Student 8", "Student 9",
        "Student 10", "Student 11", "Student 12"
    ],
    "Department": [
        "Science", "Science", "Arts", "Arts",
        "Science", "Commerce", "Commerce", "Science",
        "Arts", "Commerce", "Science", "Arts"
    ],
    "Python": [78, 67, 72, 90, 85, 92, 74, 88, 81, 95, 79, 86],
    "NumPy": [85, 88, 81, 76, 91, 89, 79, 94, 84, 90, 83, 87],
    "Math": [92, 95, 89, 84, 87, 93, 82, 91, 86, 96, 88, 90]
})


print("PANDAS GROUPED STUDENT ANALYZER")
print("============================")


# 1. Create Average Column

students["Average"] = students[
    ["Python", "NumPy", "Math"]
].mean(axis=1)


print("\nStudent Dataset")
print("----------------------------")
print(students)


# 2. Group By Department

grouped = students.groupby("Department")


# 3. Number of Students

print("\nStudents By Department")
print("----------------------------")
print(grouped["Student"].count())


# 4. Average Performance

print("\nAverage Performance By Department")
print("----------------------------")

department_average = grouped["Average"].mean()

print(department_average)


# 5. Total Marks

print("\nTotal Marks By Department")
print("----------------------------")

print(
    grouped[
        ["Python", "NumPy", "Math"]
    ].sum()
)


# 6. Highest Performance

print("\nHighest Marks By Department")
print("----------------------------")

print(
    grouped[
        ["Python", "NumPy", "Math"]
    ].max()
)


# 7. Lowest Performance

print("\nLowest Marks By Department")
print("----------------------------")

print(
    grouped[
        ["Python", "NumPy", "Math"]
    ].min()
)


# 8. Multiple Aggregations

print("\nDepartment Statistics")
print("----------------------------")

print(
    grouped["Average"].agg([
        "mean",
        "max",
        "min",
        "count"
    ])
)


# 9. Best Department

best_department = department_average.idxmax()

print("\nBest Department")
print("----------------------------")
print("Department:", best_department)
print("Average:", department_average[best_department])


# 10. Best Student In Each Department

print("\nBest Student In Each Department")
print("----------------------------")

best_students = students.loc[
    students.groupby("Department")["Average"].idxmax()
]

print(
    best_students[
        ["Department", "Student", "Average"]
    ].sort_values("Department")
)


# 11. Students Above Class Average

class_average = students["Average"].mean()

print("\nClass Average")
print("----------------------------")
print(class_average)

print("\nStudents Above Class Average")
print("----------------------------")

above_average = students[
    students["Average"] > class_average
]

print(
    above_average[
        ["Student", "Department", "Average"]
    ]
)


# 12. Final Summary

print("\nFinal Summary")
print("============================")
print("Total Students:", len(students))
print("Number of Departments:", students["Department"].nunique())
print("Class Average:", class_average)
print("Best Department:", best_department)
print("Best Department Average:", department_average[best_department])