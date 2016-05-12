#! /Bin/env python
import numpy as np
from scipy import *
from scipy.integrate import quad as Q
from scipy import linalg
import matplotlib.pyplot as plt

##-------------------- CONFIG Task 1-3 --------------------------

f = lambda x: np.exp(x) #Finction to integrate
start =0 # start value
stop =10 # stop value
bars =20 #amount of bars
tollerence = 30 # when approximation should break
# End of Config 

## ------------------- TASK 1 -----------------------------------

# Return the the approximation integral
# Can this be done without the np.array ? it is needed for the while loop
def ctrapezoidal(f, a, b, n):
    i = linspace(1, n-1, n-1) # A list i from 1 to n-1
    x_i = a +((np.array(i)/n)*(b-a))
    h = (b-a)/n
    return np.asarray([((h/2)*(f(a)+f(b)))+(h*sum(f(x_i)))]), np.asarray([h])


## ------------------- TASK 2 -----------------------------------

I = Q(f, start, stop)[0] # .integrate.quad funtion

I_h = ctrapezoidal(f, start, stop, 1)[0] #Would like to know how this could be written i a nicer way!?
H = ctrapezoidal(f, start, stop, 1)[1]
i=1
while (abs(I_h[-1]-I) > tollerence): # breaks when approximation is good enough (defined in CONFIG)
    I_h = np.append(I_h, ctrapezoidal(f, start, stop, 2**i)[0])
    H = np.append(H, ctrapezoidal(f, start, stop, 2**i)[1])
    i+=1

##--------------------- TASK 3 ---------------------------------
#plt.loglog(H ,abs(I_h-I), basex=10, basey=10) #just plotting whaever
#plt.grid(which='both')
#plt.show()

## --------------- TASK 4-7 CONFIG -----------------------------
x = np.asarray([0.0, 0.5, 1.0, 1.5, 2.0, 2.5])
y = np.asarray([-2.0,0.5, -2.0, 1.0, -0.5, 1.0])
xs = np.asarray(linspace(0, 3, 100))

##--------------------- TASK 4 ---------------------------------
def MatrixConstruct(V):
    N = len(V)
    Z = np.asarray(V**(N-1))
    for i in range(1, N):
        A = (V**(N-i-1))
        Z = np.column_stack((Z,A )) # Kind of append command for arrays
    return Z

##--------------------- TASK 5 ----------------------------------
def interpoly(X, Y):
    V = MatrixConstruct(X)
    return linalg.solve(V, Y)[::-1]

##--------------------- TASK 6 ----------------------------------
def polyval(c, z):
    summ = 0
    for i in range(len(c)):
        summ =summ + c[i]*z**(i)
    return summ
print (polyval([1, 2, 3], 2))
##-------------------- TASK 7 ----------------------------------
plt.plot(xs, polyval(interpoly(x, y), xs), '--k')
plt.plot(x, y, '*' )
plt.show()
