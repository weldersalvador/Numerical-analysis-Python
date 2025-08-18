from sympy import symbols,diff,lambdify
import sympy as sp

"""Description: The function below returns a zero of a real function. The implementation has the physical
motivation of a free fall with air resistance, resulting in a differential equation with the form of
the variable "f"(Example 2 of the chapter one in the book "elementary differential equations and boundary
value problems. William E.Boyce/Richard C.DiPrima"). We want to know when (for wich t = x) the position of
the ball has value of 300, knowing that the inicial velocity is zero. It was used the Newthon Method
for reaching the zero value of the function"""

x = symbols('x')
f = 49*x + 245*sp.exp(-x/5) - 545
f_function = lambdify(x,f)
f_prime = diff(f,x)
f_prime_function =  lambdify(x,f_prime)


def zero(x0,max = 10):
    solutions = []
    k = 1
    solutions.append(x0)
    while(k < max):
        solutions.append(solutions[k - 1] - (f_function(solutions[k - 1])/f_prime_function(solutions[k-1])))
        k += 1
    return solutions[k - 1]

print("Root: {}".format(zero(3)))


