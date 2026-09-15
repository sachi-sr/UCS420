import numpy as np
ucs420_sachi = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 15, 20, 35]
])
print("Original Array:")
print(ucs420_sachi)
print("\nMean:", np.mean(ucs420_sachi))
print("Median:", np.median(ucs420_sachi))
print("Maximum:", np.max(ucs420_sachi))
print("Minimum:", np.min(ucs420_sachi))
print("Unique elements:", np.unique(ucs420_sachi))
reshaped_ucs420_sachi = ucs420_sachi.reshape(4, 3)
print("\nReshaped Array (4 x 3):")
print(reshaped_ucs420_sachi)
resized_ucs420_sachi = np.resize(ucs420_sachi, (2, 3))
print("\nResized Array (2 x 3):")
print(resized_ucs420_sachi)