import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)

    for i in range(n):
        max_row = np.argmax(abs(A[i:, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i][i+1:], x[i+1:])) / A[i][i]

    return x

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b = np.array([8, -11, -3])
x = gauss_elimination(A, b)
print(x)