import numpy as np

steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

print("Total steps:", np.sum(steps))
print("Mean steps:", np.mean(steps))
print("Maximum steps:", np.max(steps))
print("Minimum steps:", np.min(steps))
print("Total steps for each day:", np.sum(steps, axis=0))
print("Total steps for each user:", np.sum(steps, axis=1))
max_position = np.unravel_index(np.argmax(steps), steps.shape)
print("Position of maximum value:", max_position)