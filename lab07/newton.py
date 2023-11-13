import argparse
import sympy as sp

def newton_raphson(expr, start, max_iterations, tolerance, step):
    x = sp.symbols('x')
    
    f = sp.lambdify(x, expr)
    df = sp.lambdify(x, sp.diff(expr, x))

    current_guess = start

    for n in range(max_iterations):
        current_value = f(current_guess)
        current_derivative = df(current_guess)
        
        if abs(current_derivative) < step:
            raise ValueError("Derivative too small.")
        
        next_guess = current_guess - current_value / current_derivative
        
        if abs(next_guess - current_guess) < tolerance:
            return next_guess, n + 1 

        current_guess = next_guess

    

    return current_guess, max_iterations

parser = argparse.ArgumentParser(description='Find a zero of a function using the Newton-Raphson method.', add_help=False)
parser.add_argument('--help', action='help', help='Show this help message and exit.')
parser.add_argument('expression', type=str, help='The mathematical expression as a string. Example: "x**2+x+1"')
parser.add_argument('-s', '--start', type=float, default=0, help='Starting point for the iteration.', required=False)
parser.add_argument('-m', '--max_iterations', type=int, default=1000, help='Maximum number of iterations.')
parser.add_argument('-t', '--tolerance', type=float, default=0.0001, help='Tolerance for convergence.')
parser.add_argument('-h', '--step', type=float, default=1e-7, help='The step size for the derivative.')


args = parser.parse_args()

expr = sp.sympify(args.expression)

root, iterations = newton_raphson(expr, args.start, args.max_iterations, args.tolerance, args.step)

print(f"Root: {root}, Iterations: {iterations}")


# python newton.py "x**2+x+1" -h 0.00001

