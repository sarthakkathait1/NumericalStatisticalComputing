def bisection(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("The bisection method fails.")
        return None
    
    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1
    return (a + b) / 2

# Example usage
def func(x):
    return x**3 - 4*x - 9

root = bisection(func, 0, 3)
print(f"Root found by Bisection: {root}")
