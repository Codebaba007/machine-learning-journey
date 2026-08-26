import pandas as pd


students = pd.DataFrame({
    "Student": [
        "Student 1", "Student 2", "Student 3",
        "Student 4", "Student 5", "Student 6",
        "Student 7", "Student 8", "Student 9",
        "Student 10"
    ],
    "Department": [
        "Science", "Science", "Arts", "Arts", "Science",
        "Commerce", "Commerce", "Science", "Arts", "Commerce"
    ],
    "Python": [78, 67, 72, 90, 85, 92, 74, 88, 81, 95],
    "NumPy": [85, 88, 81, 76, 91, 89, 79, 94, 84, 90],
    "Math": [92, 95, 89, 84, 87, 93, 82, 91, 86, 96]
})


print("STUDENT DATA")
print("====================")
print(students)


# 1. Group By Department

print("\nGroup By Department")
print("====================")

grouped = students.groupby("Department")

print(grouped["Python"].mean())


# 2. Average of All Subjects by Department

print("\nSubject Averages By Department")
print("====================")

print(
    grouped[["Python", "NumPy", "Math"]].mean()
)


# 3. Total Marks by Department

print("\nTotal Marks By Department")
print("====================")

print(
    grouped[["Python", "NumPy", "Math"]].sum()
)


# 4. Highest Marks by Department

print("\nHighest Marks By Department")
print("====================")

print(
    grouped[["Python", "NumPy", "Math"]].max()
)


# 5. Lowest Marks by Department

print("\nLowest Marks By Department")
print("====================")

print(
    grouped[["Python", "NumPy", "Math"]].min()
)


# 6. Number of Students in Each Department

print("\nStudent Count By Department")
print("====================")

print(
    students.groupby("Department")["Student"].count()
)


# 7. Multiple Aggregations

print("\nMultiple Aggregations")
print("====================")

print(
    grouped["Python"].agg(["mean", "max", "min", "count"])
)


# 8. Overall Average

students["Average"] = students[
    ["Python", "NumPy", "Math"]
].mean(axis=1)

print("\nStudent Averages")
print("====================")
print(students[["Student", "Department", "Average"]])


# 9. Average By Department

print("\nAverage Score By Department")
print("====================")

print(
    students.groupby("Department")["Average"].mean()
)


# 10. Best Department

department_average = (
    students.groupby("Department")["Average"].mean()
)

best_department = department_average.idxmax()

print("\nBest Department")
print("====================")
print(best_department)
print("Average:", department_average[best_department])