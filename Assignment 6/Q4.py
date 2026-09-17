import numpy as np
y = np.array([40, 65, 30, 85])
X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
], dtype=float)

print("Shape of X:", X.shape)
print("Dimensions of X:", X.ndim)

print("\nTranspose of X (X.T):")
print(X.T)

print("\nExplanation:")
print("The transpose changes rows into columns and columns into rows.")
print("X has shape (4, 3), while X.T has shape (3, 4).")
XT_X = X.T @ X
print("\nX.T @ X:")
print(XT_X)
inverse = np.linalg.inv(XT_X)
print("\nInverse of X.T @ X:")
print(inverse)
beta = inverse @ X.T @ y
print("\nOLS Coefficients (Beta):")
print(beta)
print("\nInterpretation of coefficients:")
print("Beta[0] represents the effect of Sleep Hours.")
print("Beta[1] represents the effect of Activity Level.")
print("Beta[2] represents the effect of Stress Level.")
print("\nBeta values:")
print("Sleep coefficient   :", beta[0])
print("Activity coefficient:", beta[1])
print("Stress coefficient  :", beta[2])
new_user = np.array([5, 40, 7])
prediction = new_user @ beta
print("\nNew User:")
print(new_user)
print("\nPredicted Assistance Score:")
print(prediction)