import numpy as np

sachi = np.linspace(10, 100, 25)

print("Array:")
print(sachi)

print("\nDimensions:", sachi.ndim)
print("Shape:", sachi.shape)
print("Total elements:", sachi.size)
print("Data type:", sachi.dtype)
print("Total bytes consumed:", sachi.nbytes)


transpose_array = sachi.reshape(1, 25)

print("\nTranspose using reshape():")
print(transpose_array)


print("\nTranspose using T:")
print(sachi.T)