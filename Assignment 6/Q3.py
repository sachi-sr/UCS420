import numpy as np


original = np.array([1, 2, 3, 4, 5, 6])
subset = original[1:5]
print("Original:", original)
print("Subset:", subset)
subset[0] = 999
print("\nAfter modifying subset:")
print("Original:", original)
print("Subset:", subset)
copied_subset = original[1:5].copy()
copied_subset[0] = 500
print("\nAfter modifying copied subset:")
print("Original:", original)
print("Copied subset:", copied_subset)

matrix = np.arange(1, 13).reshape(3, 4)
print("3 × 4 Matrix:")
print(matrix)
print("First row:")
print(matrix[0])
flat = matrix.flatten()
raveled = matrix.ravel()
print("Using flatten():")
print(flat)
print("\nUsing ravel():")
print(raveled)
raveled = matrix.ravel()
raveled[0] = 100
print("Raveled array:")
print(raveled)
print("\nOriginal matrix:")
print(matrix)
matrix = np.arange(1, 13).reshape(3, 4)

flat = matrix.flatten()
flat[0] = 500
print("Flattened array:")
print(flat)
print("\nOriginal matrix:")
print(matrix)
matrix = np.arange(1, 13).reshape(3, 4)
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)
print("Data type:", matrix.dtype)