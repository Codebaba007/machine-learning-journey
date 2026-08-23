# Pandas

A structured journey through Pandas with a focus on Machine Learning, Data Science, and AI.

---

## Overview

This repository documents my progress as I build a strong foundation in Pandas for Machine Learning.

The goal is to learn Pandas through practical exercises and projects before moving deeper into:

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

> **Day 2 — Data Selection and Filtering**  
> Next: **Pandas Data Cleaning and Missing Values**
---

## Day 1 — Pandas Fundamentals

### Topics Covered

- Introduction to Pandas
- Importing Pandas
- Pandas Series
- Pandas DataFrame
- Creating DataFrames
- DataFrame indexes
- Selecting columns
- Selecting multiple columns
- `shape`
- `columns`
- `dtypes`
- `head()`
- `tail()`
- `describe()`
- Calculating column statistics
- Creating calculated columns

### Files

- `notes/01_pandas_fundamentals.py`
- `exercises/exercise_01.py`
- `mini_projects/pandas_student_analyzer.py`

### Learning Outcomes

By the end of this day, I can:

- Understand the purpose of Pandas.
- Create Pandas Series.
- Create Pandas DataFrames.
- Understand rows, columns, and indexes.
- Select individual columns.
- Select multiple columns.
- Inspect the structure of a DataFrame.
- Use `head()` and `tail()` to inspect data.
- Use `describe()` for basic statistical analysis.
- Calculate statistics from DataFrame columns.
- Create new calculated columns.
- Perform basic analysis on structured datasets.

### Mini-Project — Pandas Student Performance Analyzer

Built a student performance analyzer using Pandas.

The project:

- Stores student marks using a Pandas DataFrame.
- Displays the student dataset.
- Displays the dataset shape.
- Displays DataFrame columns.
- Calculates student averages.
- Finds the highest Python mark.
- Finds the highest overall mark.
- Calculates subject averages.
- Identifies the best-performing student.
- Filters students with an average of 80 or higher.

The project introduced Pandas Series, DataFrames, column selection, DataFrame inspection, statistical calculations, and calculated columns.

---
---

## Day 2 — Data Selection and Filtering

### Topics Covered

- DataFrame row selection
- `loc[]`
- `iloc[]`
- Selecting individual rows
- Selecting multiple rows
- Selecting specific rows and columns
- Boolean filtering
- Conditional filtering
- Multiple conditions
- AND conditions with `&`
- OR conditions with `|`
- Range filtering
- Filtering based on column values
- Selecting columns from filtered data
- Creating calculated columns

### Files

- `notes/02_data_selection.py`
- `exercises/exercise_02.py`
- `mini_projects/pandas_data_filter.py`

### Learning Outcomes

By the end of this day, I can:

- Select rows using `loc[]`.
- Select rows using `iloc[]`.
- Select specific rows and columns.
- Filter DataFrames using Boolean conditions.
- Combine multiple filtering conditions.
- Use `&` for AND conditions.
- Use `|` for OR conditions.
- Filter values within a specific range.
- Select specific columns from filtered data.
- Create calculated columns for further filtering.
- Analyze structured datasets using conditional selection.

### Mini-Project — Pandas Student Data Filter

Built a student data filtering system using Pandas.

The project:

- Stores student marks in a DataFrame.
- Displays selected rows and columns.
- Filters students based on Python marks.
- Filters students based on Mathematics marks.
- Combines multiple conditions using AND.
- Combines multiple conditions using OR.
- Filters marks within a specified range.
- Calculates student averages.
- Identifies students with an average of 80 or higher.

The project combined DataFrame selection, `loc[]`, `iloc[]`, Boolean filtering, multiple conditions, and calculated columns.
---

## Repository Structure

```text
03_pandas/
│
├── README.md
│
├── notes/
│   └── 01_pandas_fundamentals.py
│
├── exercises/
│   └── exercise_01.py
│
└── mini_projects/
    └── pandas_student_analyzer.py