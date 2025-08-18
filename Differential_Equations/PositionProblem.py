from sympy import symbols,diff,lambdify
import numpy as np

x = symbols('x')
f = x - x**(1/3) - 2
f_function = lambdify(x,f)
f_prime = diff(f,x)
f_prime_function =  lambdify(x,f_prime)


def zero(x0,x1,precision = 0.001,max = 100):
    prime = f_prime_function
    solutions = []
    k = 1
    solutions.append(f_function(x0))
    solutions.append(f_function(x1))
    while(f_function(solutions[k]) > precision or k == max):
        solutions.append(solutions[k] - (f_function(solutions[k - 1])/prime(solutions[k-1])))
        k += 1
    return solutions[k]

print("Zero da função: {}".format(zero(3,5)))


