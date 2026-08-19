import numpy as np


marks = np.array([
    [78, 85, 92],
    [67, 88, 95],
    [72, 81, 89],
    [90, 76, 84],
    [85, 91, 87]
])


subjects = ["Python", "NumPy", "Mathematics"]


print("STUDENT STATISTICS ANALYZER")
print("============================")


# Basic dataset information

print("\nDataset Shape:", marks.shape)
print("Number of Students:", marks.shape[0])
print("Number of Subjects:", marks.shape[1])


# Overall statistics

print("\nOverall Statistics")
print("----------------------------")
print("Total Marks:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))
print("Range:", np.ptp(marks))


# Subject statistics

print("\nSubject Statistics")
print("----------------------------")

subject_totals = np.sum(marks, axis=0)
subject_averages = np.mean(marks, axis=0)
subject_highest = np.max(marks, axis=0)
subject_lowest = np.min(marks, axis=0)
subject_std = np.std(marks, axis=0)

for i in range(len(subjects)):
    print(f"\n{subjects[i]}")
    print("Total:", subject_totals[i])
    print("Average:", subject_averages[i])
    print("Highest:", subject_highest[i])
    print("Lowest:", subject_lowest[i])
    print("Standard Deviation:", subject_std[i])


# Student statistics

print("\nStudent Statistics")
print("----------------------------")

student_totals = np.sum(marks, axis=1)
student_averages = np.mean(marks, axis=1)
student_highest = np.max(marks, axis=1)
student_lowest = np.min(marks, axis=1)

for i in range(len(marks)):
    print(f"\nStudent {i + 1}")
    print("Total:", student_totals[i])
    print("Average:", student_averages[i])
    print("Highest:", student_highest[i])
    print("Lowest:", student_lowest[i])


# Performance analysis

print("\nPerformance Analysis")
print("----------------------------")

print("Marks >= 80:", np.sum(marks >= 80))
print("Marks >= 90:", np.sum(marks >= 90))
print("Marks < 70:", np.sum(marks < 70))


# Subject-level performance

print("\nSubject Performance")
print("----------------------------")

students_above_80 = np.sum(marks >= 80, axis=0)

for i in range(len(subjects)):
    print(
        f"{subjects[i]} - "
        f"Students scoring >= 80: {students_above_80[i]}"
    )


# Best and weakest subject

best_subject_index = np.argmax(subject_averages)
weakest_subject_index = np.argmin(subject_averages)

print("\nBest Subject:", subjects[best_subject_index])
print("Best Subject Average:", subject_averages[best_subject_index])

print("\nWeakest Subject:", subjects[weakest_subject_index])
print("Weakest Subject Average:", subject_averages[weakest_subject_index])