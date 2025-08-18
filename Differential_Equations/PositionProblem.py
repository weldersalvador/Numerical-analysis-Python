from sympy import symbols,diff,lambdify
import sympy as sp
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

print("Zero da função: {}".format(zero(3)))


