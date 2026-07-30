# 🚀 Mini Projects: NumPy

## 1. Image as Array Manipulator
**Description:** Load an image as a NumPy array (using `matplotlib.pyplot.imread`), apply transformations (grayscale conversion, cropping, applying a color filter, rotating), and save the result.
**Skills:** Array slicing, multi-dimensional array arithmetic, broadcasting.
**Starter Instructions:** Convert an RGB image (HxWx3) to grayscale by averaging the color channels, or using the standard luminance formula: `Y = 0.2989*R + 0.5870*G + 0.1140*B`.

## 2. Matrix Calculator
**Description:** Build a command-line tool that performs matrix operations (addition, multiplication, determinant, inverse, transpose) on matrices provided by the user.
**Skills:** `np.linalg`, matrix operations, user input parsing.
**Starter Instructions:** Allow the user to define matrix dimensions and values. Implement a menu system to select the operation.

## 3. Statistical Analyzer
**Description:** Generate a large mock dataset of student grades (e.g., 1000 students, 5 subjects) using `np.random`. Compute the top student, hardest subject, overall average, and standard deviation per subject.
**Skills:** Random generation, axis-based aggregation, `argmax`/`argmin`.
**Starter Instructions:** Create a (1000, 5) array. Use `np.mean(axis=0)` for subject averages. Use `np.sum(axis=1)` to find total grades per student.
