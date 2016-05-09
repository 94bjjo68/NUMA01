
import matplotlib.pyplot as plt 
import math as m
import numpy as np
#import pylab as py
#import scipy as sc 
from scipy.linalg import solve,lstsq 
import sympy as sym
from scipy.integrate import quad as q
import pprint as pp
"""
TASK 1 
Approximation (I_h) of a definate intergral through the composite trapezoidal rule.

Inputs:
f is the function to integrate, this can be altered in cell 33
a is the lower bound
b is the highest bound
n is the number of intervals 

Outputs:
Actual integrand (I) from the scipy.integrate.squad function
Approximated integrand (I_h) from the composite trapezoidal rule.

"""
a = 0
b = 6
n = [100]
def f(x):
        return m.e**x 
def Ih(f,a,b,n):
    s = 0
    h =((b-a)/n[-1])
    for i in range (1,n[-1]):
           x = a + ((i/n[-1])*(b-a))
           s = s + f(x)
    I = ((h*0.5)*(f(a)+f(b)))+(h*s)
    return I
I = q(lambda x:m.e**x,a,b)
I = I[0] 
error =abs(Ih(f,a,b,n) - I)
print ("TASK 1")
print("Approximation Ih:",Ih(f,a,b,n))
print("Actual integrand I:",I)
print ("Error:",error)
print()

"""
TASK 2
Function to increase n until the approximation is inside a given error tolerance. 

Inputs:
ep is the error tolerance

Outputs:
error, difference between the approximation and actual value
n,number of intervals required for a given error tolerance (ep)
Actual integrand (I), from the scipy.integrate.squad function
Approximated integrand (I_h), from the composite trapezoidal rule.

"""
ep = 0.5 #choose a sigma value as given error tolerace for  approximation
while (error>ep):
    n.append(n[-1]+1)
    error = abs(Ih(f,a,b,n) - I)
print ("TASK 2")
print ("Given tolerance:",ep)
print("New approximation:",Ih(f,a,b,n))
print ("Error:",error)
print ("Required number of intervalls:",n[-1])
print()
"""
Task 3
Function to create a log10 plot of the step size (h) and resulting error. 

x-axis is the value of h as a list
y-axis is the value of the error as a list

"""
X = [] #Empty list to fill in values for the x axis (h)
Y = [] #Empty list to fill in values for the y axis (error)
for k in range (1,n[-1]):
    H = (b-a)/k
    s = 0
    for i in range(1,n[-1]): 
        x = a + ((i/n[-1])*(b-a))
        s = s + f(x)
    approx =((H/2)*(f(a)+f(b)))+(H*s)
    X.append(H)
    Y.append(approx)
print ("TASK 3")
plt.loglog(X,Y,"g-",linewidth = 2)
plt.title ("Growth of error with respect to ''step size'' ")
plt.grid(which='major', color='k', linestyle='-',linewidth=1.5, alpha = 0.8)
plt.grid(which='minor', color='k', linestyle='-',alpha = 0.5)
plt.xlabel("Log(10)h")
plt.ylabel("Log(10)error")
plt.show()
print()

"""
TASK 4
Function to create a matrix with N+1  rows and columns from a given vector x
In this function 
Inputs:
Vector X

Outputs: 
Matrix with horisontal row x^n - x^0 and vertical row x^n to x^0
""" 
x = 2 #example
#x = sym.Symbol("x") # alternative to give a general matrix
X = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5]) #vector to provide or serves as a source for N+1 values
def matrixbuilder(X):
    L =[]
    for i in range (len(X)): # provides values to add into matrix
        L.append(x**i) 
    H = np.fliplr(np.tile(L,(len(X),1)))
    return np.matrix(H) 
print ("TASK 4")
pp.pprint(matrixbuilder(X)) 
print ()
"""
TASK 5
Function to find the coefficient vector (c) between to vectors 
X is here ''translated'' into a matrix using the matrixbuilder function 

Input:
X vector
Y vector

Output:
coefficient vector (array) c to solve the given system
"""
Y = np.array([-2.0, 0.5, -2.0, 1.0, -0.5, 1.0]) 
def interpoly(X,Y):
    return lstsq(matrixbuilder(X),Y)#builds matrix from vector X (with a defined x-variable) and solves system
print ("Task 5")
print ("Coefficient vector c:")
pp.pprint(interpoly(X,Y))
print()


"""
TASK 6
Function to ''create"" the polynomial (as an vector) for the given formula 

Input:
value of c variable
value of z variable
N value 

Output:
The polynomial as a vector 

"""
N = 3 #example 
a = np.linspace(0,N,len(X))
def polyval(c,z):
    s = 0
    for c in range (1,N+1):
        for i in range(1,N+1):#nestling or ''double looping'', for-looping 2 variables
            s = s + (c*z**i)
    return s
print ("TASK 6")
print ("Polynomial:",polyval(interpoly(X,Y),a)) #using c as c and a as z(not really sure about z)
print()



"""
TASK 7
Plotting (x_i,y_i) and the polynomial from polyval, ''controll of polynomial function"

Input:
Functions from task 4,5,6

Output:
Plot
"""

print ("TASK 7")
plt.plot(a,(polyval(interpoly(X,Y),a)),"b-") #plots the polynomial 
plt.plot(X,(polyval(interpoly(X,Y),X)),"k.") #plots (x_i,y_i) 
plt.grid(True)  
plt.show()#polynomial seems to pass through the points,in the given intervall 
