import numpy as np

A = np.random.randint(50, size=(8, 8))

det = np.linalg.det(A)

print(A)
print(det)
