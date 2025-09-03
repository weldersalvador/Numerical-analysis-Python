import numpy as np
import matplotlib.pyplot as plt

"""The motivation of this code is to plot a graph of a non-trivial function that results from a linear differential equation, 
specifically Example 5 in Chapter 2. The method used consists of calculating the integral over each partition width, multiplying, summing,
and then plotting the graph of the general function for each defined constant. An interesting note is that, as 𝑥→∞ all the functions tend to 0."""

def integrationFunction(x):
    return np.exp(x*x/4)

def function(x):
    return np.exp(-1*x*x/4)

#Intervals for the x-axis
b = 6
a = 0
t = np.linspace(a, b,100)

#Integration by Riemann sum
h = t[1] - t[0]
integral = np.cumsum(integrationFunction(t[:-1]))*h

#Multiple values for c
C = np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])

#the y-axis (A matrix that will save the values of each c)
y = np.zeros((len(C),len(t) - 1))

#Saving all the values of y for each c in a matrix 
i = 0
for c in C:
    y[i] = function(t[:-1])*integral + c*function(t[:-1])
    i += 1

for rows in y:
    plt.plot(t[:-1],rows)
plt.title('Graphics of the function based on different values of c (constant)')
plt.show()
