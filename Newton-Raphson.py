def newton_raphson(f, f_prime, x0, tol=1e-5, max_iter=100):
    x = x0
    iteration = 0
    
    while abs(f(x)) > tol and iteration < max_iter:
        if f_prime(x) == 0:
            print("Derivative is zero, no solution found.")
            return None
        x = x - f(x) / f_prime(x)
        iteration += 1
    
    return x

# Example usage:
def func(x):
    return x**3 - x - 2  # Function: f(x) = x^3 - x - 2

def func_prime(x):
    return 3*x**2 - 1  # Derivative: f'(x) = 3x^2 - 1

initial_guess = float(input("Enter initial guess: "))
root = newton_raphson(func, func_prime, initial_guess)
print(f"Root found using Newton-Raphson: {root}")
