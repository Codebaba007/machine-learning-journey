# NumPy

A structured journey through NumPy with a focus on Machine Learning, Data Science, and AI.

---

## Overview

This repository documents my progress as I build a strong foundation in NumPy for Machine Learning.

The goal is to learn NumPy through practical exercises and projects before moving deeper into:

- Pandas
- Matplotlib
- Statistics and Probability
- Scikit-learn
- Machine Learning
- PyTorch
- Deep Learning
- Computer Vision

Every day contains:

- Notes
- Exercises
- A Mini Project

---

# Current Progress

> **Day 2 — Array Operations and Data Manipulation**  
> Next: **Broadcasting and Advanced Array Operations**

---

## Day 1 — NumPy Fundamentals

### Topics Covered

- NumPy fundamentals
- Importing NumPy
- NumPy arrays
- `numpy.ndarray`
- Creating arrays
- Array indexing
- Negative indexing
- Array length
- Basic numerical operations
- `np.mean()`
- `np.max()`
- `np.min()`
- `np.sum()`
- `np.sort()`
- Boolean comparisons
- Array filtering
- Vectorized operations
- Arithmetic operations across arrays

### Files

- `notes/01_numpy_fundamentals.py`
- `exercises/exercise_01.py`
- `mini_projects/numpy_student_analyzer.py`

### Learning Outcomes

By the end of this day, I can:

- Create NumPy arrays.
- Access array elements using indexes.
- Use positive and negative indexing.
- Calculate basic statistics from arrays.
- Sort NumPy arrays.
- Perform arithmetic operations across entire arrays.
- Create Boolean conditions from arrays.
- Filter array values using Boolean conditions.
- Perform basic numerical data analysis using NumPy.

### Mini-Project — NumPy Student Performance Analyzer

Built a student performance analyzer using NumPy arrays.

The project:

- Stores student marks using a NumPy array.
- Calculates total marks.
- Calculates average marks.
- Finds the highest mark.
- Finds the lowest mark.
- Separates passing and failing marks.
- Sorts student marks.
- Applies a bonus to all marks using vectorized operations.

The project introduced NumPy arrays, numerical operations, Boolean filtering, and vectorized calculations.
---
---

## Day 2 — Array Operations and Data Manipulation

### Topics Covered

- Array shape
- Array dimensions
- One-dimensional arrays
- Two-dimensional arrays
- `shape`
- `ndim`
- 2D array indexing
- Row selection
- Column selection
- Array slicing
- 2D array slicing
- Reshaping arrays
- `reshape()`
- Changing array values
- Vectorized arithmetic
- Arithmetic operations between arrays

### Files

- `notes/02_array_operations.py`
- `exercises/exercise_02.py`
- `mini_projects/numpy_student_matrix_analyzer.py`

### Learning Outcomes

By the end of this day, I can:

- Understand the shape of a NumPy array.
- Determine the number of dimensions using `ndim`.
- Create and work with two-dimensional arrays.
- Access elements using row and column indexes.
- Select individual rows and columns.
- Slice NumPy arrays.
- Reshape arrays using `reshape()`.
- Modify values inside NumPy arrays.
- Perform arithmetic operations across entire arrays.
- Understand the basic idea of vectorization.

### Mini-Project — Student Marks Matrix Analyzer

Built a **Student Marks Matrix Analyzer** using a two-dimensional NumPy array.

The project:

- Stores student marks for multiple subjects.
- Displays the array shape.
- Displays the number of dimensions.
- Selects an individual student's marks.
- Selects marks from a specific subject.
- Selects the last two students using slicing.
- Updates an individual mark.
- Applies bonus marks using vectorized arithmetic.

The project combined two-dimensional arrays, indexing, slicing, modification, and vectorized operations.
---
## Repository Structure

```text
02_numpy/
│
├── README.md
├── notes/
├── exercises/
└── mini_projects/