import pandas as pd


students = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Python": [85, 72, 90, 65, 95, 78],
    "NumPy": [88, 70, 92, 60, 90, 80]
})


def add_bonus(score):
    return score + 5


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"


def calculate_average(row):
    return (row["Python"] + row["NumPy"]) / 2


students["Python_Bonus"] = students["Python"].apply(add_bonus)

students["Grade"] = students["Python"].apply(get_grade)

students["Average"] = students.apply(
    calculate_average,
    axis=1
)

students["Total"] = students.apply(
    lambda row: row["Python"] + row["NumPy"],
    axis=1
)

students["Result"] = students["Average"].apply(
    lambda score: "Pass" if score >= 70 else "Fail"
)

print(students)