# 🔢 NumPy Cheatsheet

```python
import numpy as np
```

## Array Creation
```python
np.zeros((3, 3))
np.ones((2, 2))
np.arange(0, 10, 2) # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5) # 5 values from 0 to 1
np.random.rand(3, 3) # Uniform [0, 1)
np.random.randn(3, 3) # Normal distribution
```

## Array Attributes
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr.shape # (2, 3)
arr.dtype # int64
arr.ndim # 2
arr.size # 6
```

## Indexing & Slicing
```python
arr[0, 1] # Row 0, Col 1
arr[:, 1:] # All rows, columns from 1 to end
```

## Reshaping
```python
arr.reshape(3, 2)
arr.flatten() # 1D array copy
arr.ravel() # 1D array view
arr.transpose() # or arr.T
```

## Mathematical Operations
```python
arr + 5 # Broadcasting
arr * 2
arr1 + arr2 # Element-wise
```

## Aggregation
```python
arr.sum()
arr.mean(axis=0) # Mean across rows
arr.std()
arr.min(), arr.max()
arr.argmin(), arr.argmax() # Index of min/max
```

## Linear Algebra
```python
np.dot(A, B)
A @ B # Matrix multiplication
np.linalg.inv(A)
np.linalg.det(A)
np.linalg.eig(A)
U, S, V = np.linalg.svd(A)
```

## Boolean & Fancy Indexing
```python
arr[arr > 3] # Boolean indexing
arr[[0, 1], [1, 2]] # Elements at (0,1) and (1,2)
```

## Stacking & Splitting
```python
np.vstack((a, b)) # Vertical
np.hstack((a, b)) # Horizontal
np.split(arr, 3)
```

## Performance Tips
- Avoid loops; use vectorization.
- Use `in-place` operations when possible (`arr += 1`).
- Understand broadcasting to avoid unnecessary replication.
