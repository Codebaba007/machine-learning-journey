import pandas as pd


# ============================================================
# Pandas Student Date Analyzer
# ============================================================

students = pd.DataFrame({
    "Student": [
        "Student 1",
        "Student 2",
        "Student 3",
        "Student 4",
        "Student 5",
        "Student 6",
        "Student 7",
        "Student 8"
    ],
    "Join_Date": [
        "2025-01-15",
        "2025-02-20",
        "2025-03-10",
        "2025-04-05",
        "2025-05-25",
        "2025-06-12",
        "2025-07-18",
        "2025-08-03"
    ],
    "Exam_Date": [
        "2025-06-15",
        "2025-06-20",
        "2025-06-25",
        "2025-07-01",
        "2025-07-05",
        "2025-07-10",
        "2025-08-15",
        "2025-09-01"
    ],
    "Python": [
        78, 85, 72, 90,
        88, 76, 95, 81
    ]
})


print("PANDAS STUDENT DATE ANALYZER")
print("============================")


# ============================================================
# 1. Original Dataset
# ============================================================

print("\nOriginal Dataset")
print("----------------------------")
print(students)


# ============================================================
# 2. Convert Date Columns
# ============================================================

students["Join_Date"] = pd.to_datetime(
    students["Join_Date"]
)

students["Exam_Date"] = pd.to_datetime(
    students["Exam_Date"]
)


# ============================================================
# 3. Extract Join Year
# ============================================================

students["Join_Year"] = (
    students["Join_Date"].dt.year
)


# ============================================================
# 4. Extract Join Month
# ============================================================

students["Join_Month"] = (
    students["Join_Date"].dt.month_name()
)


# ============================================================
# 5. Extract Join Day
# ============================================================

students["Join_Day"] = (
    students["Join_Date"].dt.day
)


# ============================================================
# 6. Find Join Weekday
# ============================================================

students["Join_Weekday"] = (
    students["Join_Date"].dt.day_name()
)


# ============================================================
# 7. Find Exam Weekday
# ============================================================

students["Exam_Weekday"] = (
    students["Exam_Date"].dt.day_name()
)


# ============================================================
# 8. Calculate Days Until Exam
# ============================================================

students["Days_To_Exam"] = (
    students["Exam_Date"] -
    students["Join_Date"]
).dt.days


# ============================================================
# 9. Sort Students By Join Date
# ============================================================

students = students.sort_values(
    by="Join_Date"
)

print("\nStudents Sorted By Join Date")
print("----------------------------")

print(
    students[
        ["Student", "Join_Date"]
    ]
)


# ============================================================
# 10. Filter Students By Join Date
# ============================================================

recent_students = students[
    students["Join_Date"] >= "2025-05-01"
]

print("\nStudents Who Joined From May")
print("----------------------------")

print(
    recent_students[
        ["Student", "Join_Date"]
    ]
)


# ============================================================
# 11. Students With Long Preparation Time
# ============================================================

long_preparation = students[
    students["Days_To_Exam"] >= 60
]

print("\nStudents With At Least 60 Days Preparation")
print("-------------------------------------------")

print(
    long_preparation[
        ["Student", "Days_To_Exam"]
    ]
)


# ============================================================
# 12. Count Students By Join Month
# ============================================================

print("\nStudents By Join Month")
print("----------------------------")

print(
    students["Join_Month"].value_counts()
)


# ============================================================
# 13. Best Student
# ============================================================

best_index = students["Python"].idxmax()

print("\nBest Python Student")
print("----------------------------")

print("Student:", students.loc[best_index, "Student"])
print("Score:", students.loc[best_index, "Python"])
print(
    "Exam Date:",
    students.loc[best_index, "Exam_Date"]
)


# ============================================================
# 14. Create Exam Schedule
# ============================================================

exam_schedule = students[
    [
        "Student",
        "Exam_Date",
        "Exam_Weekday"
    ]
].sort_values("Exam_Date")

print("\nExam Schedule")
print("----------------------------")
print(exam_schedule)


# ============================================================
# 15. Final Dataset
# ============================================================

print("\nFinal Analyzed Dataset")
print("============================")
print(students)


# ============================================================
# 16. Save Results
# ============================================================

students.to_csv(
    "student_date_analysis.csv",
    index=False
)

print("\nSaved: student_date_analysis.csv")