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

> **Day 6 — Random Numbers and Data Generation**  
> Next: **NumPy Revision**

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

## Day 3 — Array Operations and Data Manipulation

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
- Broadcasting
- `np.zeros()`
- `np.ones()`
- `np.arange()`

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
- Understand vectorized operations.
- Apply broadcasting to compatible arrays.
- Create arrays using `zeros()` and `ones()`.
- Generate sequences using `arange()`.

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
- Applies a universal bonus using vectorized arithmetic.
- Applies subject-specific bonuses using broadcasting.
- Generates student numbers using `arange()`.
- Creates zero-filled and one-filled arrays using `zeros()` and `ones()`.

The project combined two-dimensional arrays, indexing, slicing, modification, vectorization, broadcasting, and NumPy array creation methods.
---
---

## Day 4 — Array Aggregation and Statistical Operations

### Topics Covered

- Array aggregation
- `axis`
- `np.sum()`
- `np.mean()`
- `np.max()`
- `np.min()`
- `np.std()`
- `np.median()`
- `np.argmax()`
- `np.argmin()`
- `np.ptp()`
- Boolean aggregation
- `np.any()`
- `np.all()`
- Counting Boolean conditions with `np.sum()`
- Combining Boolean conditions
- `axis=0`
- `axis=1`
- Statistical analysis of two-dimensional arrays

### Files

- `notes/03_array_aggregation.py`
- `exercises/exercise_03.py`
- `mini_projects/numpy_statistics_analyzer.py`

### Learning Outcomes

By the end of this day, I can:

- Perform aggregation operations on NumPy arrays.
- Calculate totals and averages.
- Find maximum and minimum values.
- Calculate standard deviation and median.
- Find the positions of maximum and minimum values.
- Calculate the range of an array.
- Use `axis=0` to analyze columns.
- Use `axis=1` to analyze rows.
- Use Boolean conditions to analyze array data.
- Determine whether any or all values satisfy a condition.
- Count values that satisfy a condition.
- Combine multiple Boolean conditions.
- Perform statistical analysis on two-dimensional datasets.

### Mini-Project — Student Statistics Analyzer

Built a **Student Statistics Analyzer** using NumPy.

The project:

- Stores student marks in a two-dimensional array.
- Displays dataset dimensions and structure.
- Calculates overall statistics.
- Calculates subject-level statistics.
- Calculates student-level statistics.
- Calculates averages, medians, ranges, and standard deviations.
- Identifies the best and weakest subject based on average performance.
- Counts marks meeting specific performance thresholds.
- Uses Boolean aggregation for performance analysis.
- Uses `argmax()` and `argmin()` to identify the best and weakest subjects.

The project combined NumPy aggregation, statistical operations, axis-based analysis, Boolean conditions, and two-dimensional dataset analysis.
---
---

## Day 5 — Array Manipulation and Data Cleaning

### Topics Covered

- Array concatenation
- `np.concatenate()`
- Vertical stacking
- `np.vstack()`
- Horizontal stacking
- `np.hstack()`
- Adding elements with `np.append()`
- Inserting elements with `np.insert()`
- Removing elements with `np.delete()`
- Conditional replacement
- `np.where()`
- Conditional labels
- Missing values
- `np.nan`
- Detecting missing values with `np.isnan()`
- Counting missing values
- `np.nanmean()`
- `np.nanmin()`
- `np.nanmax()`
- Replacing missing values
- Removing missing values
- Sorting arrays
- Column-based data cleaning
- Missing-value imputation
- Preparing datasets for machine learning

### Files

- `notes/04_array_manipulation.py`
- `exercises/exercise_04.py`
- `mini_projects/numpy_data_cleaner.py`

### Learning Outcomes

- Combine NumPy arrays.
- Stack arrays vertically and horizontally.
- Add, insert, and delete array elements.
- Replace values based on conditions.
- Use `np.where()` for vectorized conditional operations.
- Detect missing values using `np.isnan()`.
- Count missing values in a dataset.
- Calculate statistics while ignoring missing values.
- Replace missing values using column means.
- Remove missing values when appropriate.
- Sort array data.
- Perform basic data-cleaning operations on two-dimensional datasets.
- Prepare numerical data for later machine learning workflows.

### Mini-Project — NumPy Data Cleaner

Built a NumPy-based data cleaning and analysis system.

The project:

- Stores student performance data in a two-dimensional array.
- Detects missing values.
- Counts missing values by subject.
- Calculates subject averages while ignoring missing values.
- Replaces missing values with the corresponding subject average.
- Calculates student totals and averages.
- Classifies students as pass or fail.
- Identifies the best-performing student.
- Identifies the strongest and weakest subjects.
- Performs threshold-based performance analysis.
- Sorts each student's marks.
- Produces a cleaned dataset ready for further analysis.
---

---

## Day 6 — Random Numbers and Data Generation

### Topics Covered

- Random number generation
- `np.random.rand()`
- `np.random.randint()`
- `np.random.uniform()`
- `np.random.normal()`
- `np.random.choice()`
- Random seeds
- `np.random.seed()`
- Reproducible random data
- Synthetic dataset generation
- Random student datasets
- Statistical analysis of generated data

### Files

- `notes/05_random_numbers.py`
- `exercises/exercise_05.py`
- `mini_projects/numpy_random_data_generator.py`

### Learning Outcomes

- Generate random numerical data.
- Generate random integers within a specified range.
- Generate uniformly distributed values.
- Generate normally distributed values.
- Randomly select values from an array.
- Use random seeds for reproducibility.
- Generate synthetic datasets.
- Calculate statistics from generated data.
- Use generated datasets for experimentation and testing.

### Mini-Project — Random Student Dataset Generator

Built a synthetic student dataset generator using NumPy.

The project:

- Generates student marks randomly.
- Uses a fixed random seed for reproducibility.
- Calculates subject-level statistics.
- Calculates student averages.
- Identifies the best and lowest-performing students.
- Calculates overall dataset statistics.
- Determines pass/fail counts.
- Demonstrates how NumPy can generate synthetic data for experimentation.
---

## Repository Structure

```text
02_numpy/
│
├── README.md
├── notes/
├── exercises/
└── mini_projects/