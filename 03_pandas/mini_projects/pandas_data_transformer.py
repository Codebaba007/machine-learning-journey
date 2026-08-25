import pandas as pd


students = pd.DataFrame({
    "Student": [
        "Student 1",
        "Student 2",
        "Student 3",
        "Student 4",
        "Student 5",
        "Student 6",
        "Student 7",
        "Student 8",
        "Student 9",
        "Student 10"
    ],
    "Python": [78, 67, 72, 90, 85, 92, 74, 88, 81, 95],
    "NumPy": [85, 88, 81, 76, 91, 89, 79, 94, 84, 90],
    "Math": [92, 95, 89, 84, 87, 93, 82, 91, 86, 96]
})


print("PANDAS STUDENT DATA TRANSFORMER")
print("============================")


# 1. Create Total

students["Total"] = students[
    ["Python", "NumPy", "Math"]
].sum(axis=1)


# 2. Create Average

students["Average"] = students[
    ["Python", "NumPy", "Math"]
].mean(axis=1)


# 3. Create Status

students["Status"] = students["Average"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)


# 4. Create Grade

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


students["Grade"] = students["Average"].apply(get_grade)


# 5. Rename Subject Columns

students = students.rename(columns={
    "Python": "Python_Marks",
    "NumPy": "NumPy_Marks",
    "Math": "Math_Marks"
})


# 6. Display Transformed Dataset

print("\nTransformed Dataset")
print("----------------------------")
print(students)


# 7. Sort By Average

print("\nStudents Ranked By Average")
print("----------------------------")

ranked_students = students.sort_values(
    by="Average",
    ascending=False
)

print(
    ranked_students[
        ["Student", "Average", "Grade"]
    ]
)


# 8. Best Student

best_student = students.loc[
    students["Average"].idxmax()
]

print("\nBest Student")
print("----------------------------")
print("Student:", best_student["Student"])
print("Average:", best_student["Average"])
print("Grade:", best_student["Grade"])


# 9. Students With Average >= 80

print("\nHigh Performers")
print("----------------------------")

high_performers = students[
    students["Average"] >= 80
]

print(
    high_performers[
        ["Student", "Average", "Grade"]
    ]
)


# 10. Subject Rankings

print("\nSubject Averages")
print("----------------------------")

print(
    students[
        ["Python_Marks", "NumPy_Marks", "Math_Marks"]
    ].mean()
)


# 11. Lowest Performing Students

print("\nLowest Performers")
print("----------------------------")

lowest = students.sort_values(
    by="Average",
    ascending=True
)

print(
    lowest[
        ["Student", "Average", "Grade"]
    ].head(3)
)


# 12. Final Summary

print("\nFinal Summary")
print("============================")
print("Number of Students:", len(students))
print("Class Average:", students["Average"].mean())
print("Highest Average:", students["Average"].max())
print("Lowest Average:", students["Average"].min())
print("Number of Students Passing:", (students["Status"] == "Pass").sum())