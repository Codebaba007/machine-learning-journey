# 📝 Notes: Python Fundamentals for ML

## 1. Data Structures
Machine learning heavily relies on data manipulation. Python offers versatile built-in structures:
- **Lists**: Ordered, mutable collections. Great for sequences of data points.
- **Dictionaries**: Key-value pairs. Ideal for storing hyperparameters or mappings.
- **Sets**: Unordered, unique items. Useful for finding unique categories in a dataset.
- **Tuples**: Ordered, immutable collections. Often used for data records or returning multiple values from a function.

## 2. Functions & Lambda
Functions are crucial for building reproducible ML pipelines (e.g., a function to clean data, a function to extract features).
- **def**: Standard function definition.
- **lambda**: Anonymous, inline functions often used with `apply()` or `map()` in Pandas.

## 3. Object-Oriented Programming (OOP)
In ML, models are often objects (e.g., `model = LinearRegression()`).
- **Classes**: Blueprints for objects.
- **Inheritance**: Creating custom model layers or data loaders by inheriting from base classes (like `nn.Module` in PyTorch).
- **Methods**: Functions bound to objects (like `.fit()`, `.predict()`).

## 4. File Handling
ML starts with loading data and ends with saving models.
- Context managers (`with open(...)`) ensure files are properly closed.
- Handling CSVs, JSON, and text files is a daily task.

## 5. Standard Libraries
- `os`, `sys`: System interactions, managing file paths.
- `json`, `csv`: Data serialization and parsing.
- `collections`, `itertools`: Advanced data manipulation and counting.
