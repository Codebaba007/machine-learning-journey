import numpy as np


# ============================================================
# NumPy Data Cleaner
# ============================================================

subjects = ["Python", "NumPy", "Mathematics"]

data = np.array([
    [78, 85, 92],
    [67, np.nan, 95],
    [72, 81, 89],
    [np.nan, 76, 84],
    [85, 91, 87],
    [90, 88, 94]
])


print("NUMPY DATA CLEANER")
print("============================")


# ------------------------------------------------------------
# Raw Dataset
# ------------------------------------------------------------

print("\nRaw Dataset")
print("----------------------------")
print(data)


# ------------------------------------------------------------
# Dataset Information
# ------------------------------------------------------------

print("\nDataset Information")
print("----------------------------")
print("Students:", data.shape[0])
print("Subjects:", data.shape[1])
print("Shape:", data.shape)


# ------------------------------------------------------------
# Missing Value Analysis
# ------------------------------------------------------------

missing_mask = np.isnan(data)
missing_count = np.sum(missing_mask)

print("\nMissing Value Analysis")
print("----------------------------")
print("Total Missing Values:", missing_count)
print("Missing By Subject:", np.sum(missing_mask, axis=0))


# ------------------------------------------------------------
# Calculate Subject Means
# ------------------------------------------------------------

subject_means = np.nanmean(data, axis=0)

print("\nSubject Means")
print("----------------------------")

for i in range(len(subjects)):
    print(subjects[i], ":", subject_means[i])


# ------------------------------------------------------------
# Clean Dataset
# ------------------------------------------------------------

for column in range(data.shape[1]):
    missing = np.isnan(data[:, column])
    data[missing, column] = subject_means[column]


print("\nCleaned Dataset")
print("----------------------------")
print(data)


# ------------------------------------------------------------
# Student Statistics
# ------------------------------------------------------------

student_totals = np.sum(data, axis=1)
student_averages = np.mean(data, axis=1)

print("\nStudent Performance")
print("----------------------------")

for i in range(len(data)):
    print(f"\nStudent {i + 1}")
    print("Total:", student_totals[i])
    print("Average:", student_averages[i])


# ------------------------------------------------------------
# Pass / Fail
# ------------------------------------------------------------

print("\nPass / Fail Analysis")
print("----------------------------")

status = np.where(student_averages >= 50, "Pass", "Fail")

for i in range(len(status)):
    print(f"Student {i + 1}: {status[i]}")


# ------------------------------------------------------------
# Best Student
# ------------------------------------------------------------

best_student_index = np.argmax(student_averages)

print("\nBest Student")
print("----------------------------")
print("Student:", best_student_index + 1)
print("Average:", student_averages[best_student_index])


# ------------------------------------------------------------
# Subject Analysis
# ------------------------------------------------------------

subject_averages = np.mean(data, axis=0)

best_subject_index = np.argmax(subject_averages)
weakest_subject_index = np.argmin(subject_averages)

print("\nSubject Analysis")
print("----------------------------")
print(
    "Best Subject:",
    subjects[best_subject_index]
)
print(
    "Best Subject Average:",
    subject_averages[best_subject_index]
)

print(
    "Weakest Subject:",
    subjects[weakest_subject_index]
)
print(
    "Weakest Subject Average:",
    subject_averages[weakest_subject_index]
)


# ------------------------------------------------------------
# Performance Thresholds
# ------------------------------------------------------------

print("\nPerformance Thresholds")
print("----------------------------")

print("Marks >= 80:", np.sum(data >= 80))
print("Marks >= 90:", np.sum(data >= 90))
print("Marks < 70:", np.sum(data < 70))


# ------------------------------------------------------------
# Final Sorted Dataset
# ------------------------------------------------------------

print("\nSorted Student Marks")
print("----------------------------")
print(np.sort(data, axis=1))


# ------------------------------------------------------------
# Final Summary
# ------------------------------------------------------------

print("\nFinal Summary")
print("============================")
print("Students:", len(data))
print("Subjects:", len(subjects))
print("Missing Values Fixed:", missing_count)
print("Overall Average:", np.mean(data))
print("Highest Mark:", np.max(data))
print("Lowest Mark:", np.min(data))
print("Best Student:", best_student_index + 1)