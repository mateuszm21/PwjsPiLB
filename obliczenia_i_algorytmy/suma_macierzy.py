import numpy as np

A = np.random.randint(50, size=(128, 128))
B = np.random.randint(50, size=(128, 128))
C = np.random.randint(1, size=(128, 128))
for x in range(128):
    for y in range(128):
       C[x][y] = A[x][y] + B[x][y]

print(A)
print(B)
print(C)
