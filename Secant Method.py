def secant(f, x0, x1, tol=1e-5, max_iter=100):
    iteration = 0
    while abs(x1 - x0) > tol and iteration < max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        iteration += 1
    return x1

def func(x):
    return x**3 - 5*x + 1
    
root = secant(func, 0, 3)
print(f"Root found by Secant: {root}")