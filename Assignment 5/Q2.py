import numpy as np

arr = np.array([1, 2, 3, 6, 4, 5])

reverse_arr = arr[::-1]

print("Original Array:", arr)
print("Reversed Array:", reverse_arr)

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])

values, counts = np.unique(x, return_counts=True)

max_count = counts.max()
most_frequent = values[counts == max_count]

print("Most frequent value:", most_frequent)
print("Frequency:", max_count)

for value in most_frequent:
    print("Indices:", np.where(x == value)[0])