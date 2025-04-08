import numpy as np

def gauss_seidel(A, b, x0, tol=1e-10, max_iter=100):
    n = len(b)
    x = x0.copy()

    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        x = x_new
    return x

A = np.array([[4, 1, 2], [3, 5, 1], [1, 1, 3]])
b = np.array([4, 7, 3])
x0 = np.zeros(len(b))
x = gauss_seidel(A, b, x0)
print(x)
