def regula_falsi(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("The Regula Falsi method fails.")
        return None
    
    iteration = 0
    while abs(b - a) > tol and iteration < max_iter:
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1
    return c
# Example usage
def func(x):
    return x**3 - 4*x - 9
    
# Example usage
root = regula_falsi(func, 0, 3)
print(f"Root found by Regula Falsi: {root}")