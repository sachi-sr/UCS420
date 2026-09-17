import numpy as np

temp = np.array([25, 28, 31, 35, 38, 27, 33, 40])

correcttemp = temp + 2
print("Corrected temperature:", correcttemp)

f = (9/5) * correcttemp + 32
print("Temperature in Fahrenheit:", f)

greater = correcttemp[correcttemp > 32]
print("Readings greater than 32°C:", greater)

count = np.sum(correcttemp > 32)
print("Number of readings exceeding 32°C:", count)