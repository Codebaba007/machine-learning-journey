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


print("STUDENT PERFORMANCE ANALYZER")
print("============================")

print("\nStudent Dataset")
print("----------------------------")
print(students)


print("\nDataset Information")
print("----------------------------")
print("Shape:", students.shape)
print("Columns:", list(students.columns))


students["Average"] = students[["Python", "NumPy", "Math"]].mean(axis=1)

print("\nStudent Averages")
print("----------------------------")
print(students[["Student", "Average"]])


print("\nHighest Python Mark")
print("----------------------------")
print(students["Python"].max())


print("\nHighest Overall Mark")
print("----------------------------")
print(students[["Python", "NumPy", "Math"]].max().max())


print("\nSubject Averages")
print("----------------------------")
print("Python:", students["Python"].mean())
print("NumPy:", students["NumPy"].mean())
print("Math:", students["Math"].mean())


best_student_index = students["Average"].idxmax()

print("\nBest Student")
print("----------------------------")
print("Student:", students.loc[best_student_index, "Student"])
print("Average:", students.loc[best_student_index, "Average"])


print("\nStudents With Average 80+")
print("----------------------------")
high_performers = students[students["Average"] >= 80]

print(high_performers[["Student", "Average"]])