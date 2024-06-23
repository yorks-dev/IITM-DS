import numpy as np

a = np.array([[2, 3, 5], [1, 2, 3], [1, 1, 2]])
b = np.array([1, 1, 88])
x = np.linalg.solve(a, b)

print(x)
