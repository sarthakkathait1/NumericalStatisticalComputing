import numpy as np

def jacobi(A, b, x0, tol=1e-10, max_iter=100):
    n = len(b)
    x = x0.copy()

    for _ in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s) / A[i, i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        x = x_new
    return x

A = np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]])
b = np.array([-1, 2, 3])
x0 = np.zeros(len(b))
x = jacobi(A, b, x0)
print(x)