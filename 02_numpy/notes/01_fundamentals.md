# 📝 Notes: NumPy Fundamentals

## 1. Arrays vs Lists
NumPy arrays (`ndarray`) differ from Python lists in crucial ways:
- **Homogeneous**: All elements must be of the same type (dtype), allowing for contiguous memory allocation.
- **Vectorized Operations**: Operations apply to the whole array at once, implemented in optimized C code.

## 2. Vectorization
Vectorization is the process of replacing explicit loops with array expressions.
Instead of:
```python
for i in range(len(a)):
    c[i] = a[i] + b[i]
```
NumPy does:
```python
c = a + b
```
This results in massively faster execution.

## 3. Broadcasting
Broadcasting is a powerful mechanism that allows NumPy to work with arrays of different shapes when performing arithmetic operations.
- NumPy compares dimensions starting from the trailing edge.
- Two dimensions are compatible if they are equal, or if one of them is 1.

## 4. Linear Algebra in NumPy
ML models rely heavily on linear algebra. NumPy provides `np.dot`, `@` operator for matrix multiplication, and the `np.linalg` module for eigenvalues, decompositions, and inversions.

## 5. Shape Manipulation
Reshaping data is a constant requirement (e.g., flattening an image array to feed into a dense neural network layer). Use `.reshape()`, `.ravel()`, and `.flatten()`. Note that `.reshape()` and `.ravel()` often return views, saving memory.
