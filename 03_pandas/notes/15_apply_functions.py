import pandas as pd


students = pd.DataFrame({
    "Student": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Frank"
    ],
    "Python": [85, 72, 90, 65, 95, 78],
    "NumPy": [88, 70, 92, 60, 90, 80],
    "Status": [
        "Active",
        "Inactive",
        "Active",
        "Inactive",
        "Active",
        "Active"
    ]
})


print("ORIGINAL DATA")
print(students)
students["Python_Double"] = students["Python"].apply(lambda x: x * 2)
print("\nDATA WITH DOUBLED PYTHON SCORES")
print(students)

def add_bonus(score):
    return score + 5
students["Python_Bonus"] = students["Python"].apply(add_bonus)
print("\nDATA WITH BONUS ADDED TO PYTHON SCORES")
print(students)

students["Python_Bonus_Lambda"] = students["Python"].apply(
    lambda score: score + 5
)
print("\nDATA WITH BONUS ADDED TO PYTHON SCORES USING LAMBDA")
print(students)

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

students["Grade"] = students["Python"].apply(get_grade)
print("\nDATA WITH GRADES BASED ON PYTHON SCORES")
print(students) 
def pass_status(score):
    if score >= 70:
        return "Pass"
    return "Fail"


students["Result"] = students["Python"].apply(
    pass_status
)

print("\nResult")
print(students[["Student", "Python", "Result"]])

def calculate_average(row):
    return (row["Python"] + row["NumPy"]) / 2


students["Average"] = students.apply(
    calculate_average,
    axis=1
)

print("\nAverage")
print(
    students[
        ["Student", "Python", "NumPy", "Average"]
    ]
)
def performance(row):
    if row["Average"] >= 85:
        return "Excellent"
    elif row["Average"] >= 70:
        return "Good"
    else:
        return "Needs Improvement"


students["Performance"] = students.apply(
    performance,
    axis=1
)

print("\nPerformance")
print(
    students[
        ["Student", "Average", "Performance"]
    ]
)
students["Total"] = students.apply(
    lambda row: row["Python"] + row["NumPy"],
    axis=1
)

print("\nTotal Score")
print(
    students[
        ["Student", "Python", "NumPy", "Total"]
    ]
)
students["Summary"] = students.apply(
    lambda row:
        row["Student"]
        + " - "
        + row["Performance"],
    axis=1
)

print("\nStudent Summary")
print(
    students[
        ["Student", "Performance", "Summary"]
    ]
)
status_map = {
    "Active": 1,
    "Inactive": 0
}

students["Status_Code"] = students["Status"].map(
    status_map
)

print("\nStatus Codes")
print(
    students[
        ["Student", "Status", "Status_Code"]
    ]
)

