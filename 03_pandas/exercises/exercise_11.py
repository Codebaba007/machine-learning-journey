import pandas as pd


# 1. Create DataFrame

students = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E", "F"],
    "Join_Date": [
        "2025-01-15",
        "2025-02-20",
        "2025-03-10",
        "2025-04-05",
        "2025-05-25",
        "2025-06-12"
    ],
    "Exam_Date": [
        "2025-06-15",
        "2025-06-20",
        "2025-06-25",
        "2025-07-01",
        "2025-07-05",
        "2025-07-10"
    ],
    "Python": [78, 85, 72, 90, 88, 76]
})


# 2. Convert Dates

students["Join_Date"] = pd.to_datetime(
    students["Join_Date"]
)

students["Exam_Date"] = pd.to_datetime(
    students["Exam_Date"]
)


# 3. Extract Year

students["Join_Year"] = students[
    "Join_Date"
].dt.year


# 4. Extract Month Number

students["Join_Month"] = students[
    "Join_Date"
].dt.month


# 5. Extract Day Number

students["Join_Day"] = students[
    "Join_Date"
].dt.day


# 6. Extract Month Name

students["Join_Month_Name"] = students[
    "Join_Date"
].dt.month_name()


# 7. Extract Weekday Name

students["Join_Day_Name"] = students[
    "Join_Date"
].dt.day_name()


# 8. Calculate Days Between Join and Exam

students["Days_To_Exam"] = (
    students["Exam_Date"] -
    students["Join_Date"]
).dt.days


# 9. Filter Students Who Joined After March 1

after_march = students[
    students["Join_Date"] > "2025-03-01"
]

print("Students Who Joined After March 1")
print("==============================")
print(
    after_march[
        ["Student", "Join_Date"]
    ]
)


# 10. Sort By Exam Date

sorted_students = students.sort_values(
    by="Exam_Date"
)

print("\nStudents Sorted By Exam Date")
print("==============================")
print(
    sorted_students[
        ["Student", "Exam_Date"]
    ]
)


# 11. Create One-Week Date Range

week = pd.date_range(
    start="2025-01-01",
    periods=7,
    freq="D"
)

print("\nOne Week Date Range")
print("==============================")
print(week)


# 12. Final DataFrame

print("\nFinal DataFrame")
print("==============================")
print(students)