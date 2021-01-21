import numpy as np

A = np.random.randint(50, size=(8, 8))
B = np.random.randint(50, size=(8, 8))
C = np.random.randint(1, size=(8, 8))

for x in range(8):
    for y in range(8):
        for z in range(8):
            C[x][y] += A[x][z] * B[z][y]
print(A)
print(B)
print(C)
