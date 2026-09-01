import pandas as pd


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


print("STUDENT DATA")
print("====================")
print(students)


# ============================================================
# 1. Convert Strings to Datetime
# ============================================================

students["Join_Date"] = pd.to_datetime(
    students["Join_Date"]
)

students["Exam_Date"] = pd.to_datetime(
    students["Exam_Date"]
)

print("\nDatetime Columns")
print("====================")
print(students.dtypes)


# ============================================================
# 2. Extract Year
# ============================================================

students["Join_Year"] = students["Join_Date"].dt.year

print("\nYear")
print("====================")
print(students[["Student", "Join_Date", "Join_Year"]])


# ============================================================
# 3. Extract Month
# ============================================================

students["Join_Month"] = students["Join_Date"].dt.month

print("\nMonth")
print("====================")
print(students[["Student", "Join_Date", "Join_Month"]])


# ============================================================
# 4. Extract Month Name
# ============================================================

students["Join_Month_Name"] = (
    students["Join_Date"].dt.month_name()
)

print("\nMonth Name")
print("====================")
print(
    students[
        ["Student", "Join_Date", "Join_Month_Name"]
    ]
)


# ============================================================
# 5. Extract Day
# ============================================================

students["Join_Day"] = students["Join_Date"].dt.day

print("\nDay")
print("====================")
print(
    students[
        ["Student", "Join_Date", "Join_Day"]
    ]
)


# ============================================================
# 6. Find Day of Week
# ============================================================

students["Join_Day_Name"] = (
    students["Join_Date"].dt.day_name()
)

print("\nDay Name")
print("====================")
print(
    students[
        ["Student", "Join_Date", "Join_Day_Name"]
    ]
)


# ============================================================
# 7. Calculate Date Difference
# ============================================================

students["Days_To_Exam"] = (
    students["Exam_Date"] -
    students["Join_Date"]
).dt.days

print("\nDays Until Exam")
print("====================")
print(
    students[
        ["Student", "Join_Date", "Exam_Date", "Days_To_Exam"]
    ]
)


# ============================================================
# 8. Filter By Date
# ============================================================

filtered = students[
    students["Join_Date"] >= "2025-03-01"
]

print("\nStudents Who Joined After March 1")
print("====================")
print(
    filtered[
        ["Student", "Join_Date"]
    ]
)


# ============================================================
# 9. Sort By Date
# ============================================================

sorted_students = students.sort_values(
    by="Exam_Date"
)

print("\nSorted By Exam Date")
print("====================")
print(
    sorted_students[
        ["Student", "Exam_Date"]
    ]
)


# ============================================================
# 10. Date Range
# ============================================================

date_range = pd.date_range(
    start="2025-01-01",
    end="2025-01-07"
)

print("\nDate Range")
print("====================")
print(date_range)