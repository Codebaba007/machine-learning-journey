import numpy as np


# ============================================================
# NumPy Day 6 — Random Numbers & Data Generation
# ============================================================


# ------------------------------------------------------------
# 1. Random Numbers Between 0 and 1
# ------------------------------------------------------------

numbers = np.random.rand(5)

print("Random Numbers:")
print(numbers)


# ------------------------------------------------------------
# 2. Random 2D Array
# ------------------------------------------------------------

matrix = np.random.rand(3, 4)

print("\nRandom 2D Array:")
print(matrix)


# ------------------------------------------------------------
# 3. Random Integers
# ------------------------------------------------------------

numbers = np.random.randint(1, 101, size=10)

print("\nRandom Integers:")
print(numbers)


# ------------------------------------------------------------
# 4. Random Integer Matrix
# ------------------------------------------------------------

matrix = np.random.randint(1, 101, size=(3, 4))

print("\nRandom Integer Matrix:")
print(matrix)


# ------------------------------------------------------------
# 5. Random Uniform Distribution
# ------------------------------------------------------------

numbers = np.random.uniform(10, 20, size=5)

print("\nUniform Random Numbers:")
print(numbers)


# ------------------------------------------------------------
# 6. Random Normal Distribution
# ------------------------------------------------------------

numbers = np.random.normal(50, 10, size=10)

print("\nNormal Distribution:")
print(numbers)


# ------------------------------------------------------------
# 7. Random Choice
# ------------------------------------------------------------

subjects = ["Python", "NumPy", "Math", "Statistics"]

chosen = np.random.choice(subjects, size=5)

print("\nRandom Choices:")
print(chosen)


# ------------------------------------------------------------
# 8. Random Choice From Numbers
# ------------------------------------------------------------

marks = np.array([60, 70, 80, 90, 100])

chosen_marks = np.random.choice(marks, size=5)

print("\nRandom Marks:")
print(chosen_marks)


# ------------------------------------------------------------
# 9. Random Seed
# ------------------------------------------------------------

np.random.seed(42)

numbers_1 = np.random.randint(1, 101, size=5)

print("\nSeeded Random Numbers:")
print(numbers_1)


# Reset the same seed

np.random.seed(42)

numbers_2 = np.random.randint(1, 101, size=5)

print("\nSame Seed Again:")
print(numbers_2)


# ------------------------------------------------------------
# 10. Synthetic Student Dataset
# ------------------------------------------------------------

np.random.seed(42)

student_marks = np.random.randint(
    40,
    101,
    size=(10, 3)
)

print("\nSynthetic Student Dataset:")
print(student_marks)


# ------------------------------------------------------------
# 11. Dataset Statistics
# ------------------------------------------------------------

print("\nDataset Statistics")
print("============================")

print("Average:", np.mean(student_marks))
print("Highest:", np.max(student_marks))
print("Lowest:", np.min(student_marks))
print("Standard Deviation:", np.std(student_marks))


# ------------------------------------------------------------
# 12. Random Dataset With Normal Distribution
# ------------------------------------------------------------

np.random.seed(42)

heights = np.random.normal(
    loc=170,
    scale=8,
    size=20
)

print("\nSynthetic Heights:")
print(heights)

print("Average Height:", np.mean(heights))
print("Standard Deviation:", np.std(heights))