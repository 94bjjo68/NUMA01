"""
Author: Erik
Created on: Mon Apr 25 11:56:08 2016
Last modified on: 17/05/2016 by Erik

Python version 3.5
"""
import matplotlib.pyplot as plt 
import numpy as np  

"""
TASK 1 to 9 
------------------------------------------------------------------------------

(1)Class "interval" which is initialized with two real numbers representing
the left  lower (a) and right upper(b) endpoints respectively.
------------------------------------------------------------------------------

(2)With functionality to display the four basic arithmetic operations using ufuncs.
------------------------------------------------------------------------------

(3)with functionality to print a given interval. 
------------------------------------------------------------------------------

(4)with functionality to use  the basic "+,-,*, /" operations on 2 given intervals
using ufuncs (__add__,__sub__,__mul__,__div__)
------------------------------------------------------------------------------

5)with functionality to raise ValueErrors for division by zero and a infinitely 
large products from__truediv__.
------------------------------------------------------------------------------

(6)with functionalitiy to handle degenerate intervall {a,b} where a=b 
eg. I3=(a) gives (a,a)
------------------------------------------------------------------------------

******(7)with functionality to handle addition of real number to the interval
eg. I1+1  gives [a+1,b+1]
------------------------------------------------------------------------------

(8)with functionality to use the __contains__ ufunc to check wheter a value 
is in the given interval. eg. is b in [a,c] gives true 
------------------------------------------------------------------------------

(9)with functionality  to raise a given interval with the power on n with
 the __pow__ ufunc.

""" 
##############################################################################
class interval:#creating class 
    def __init__(self, a,b=None): #defining the attributes in the class 
       self.a = a
       if b == None:
           self.b = a
       else:
           self.b = b
    def __repr__(self):#def a display function
        return '[{},{}]'.format(self.a,self.b) #defining the format and filling it in 
    def __add__(self,other): #defining the addition operation
        return interval(self.a+other.a,self.b+other.b)
    def __sub__(self,other):#defining the subtraction operation
        return interval(self.a-other.b,self.b-other.a)
    def __mul__(self,other):#defining the mulitiplication operation 
        lm = [self.a*other.a,self.a*other.b,self.b*other.a,self.b*other.b]#skapar lista utifrån teori
        return interval(min(lm),max(lm))
    def __truediv__(self,other):#defining the division operation 
        if (other.a*other.b) == 0 : #rasing valueError to handle division by zero
            raise ValueError ("Divison by zero is not defined, denominator is:",other.a*other.b)
        ld = [self.a/other.b,self.a/other.b,self.b/other.a,self.b/other.b]#create list
        if max(ld) == np.inf:#positive infinite product
                raise ValueError("Divison product is +infinite")
        if min(ld) == -np.inf:#negative infinite product 
                raise ValueError("Division product is -infinite")
        return interval(min(ld),max(ld)) 
    def __contains__(self,value):#defining a function to see if a value lies in given interval
        if value<=self.b and value>=self.a:#parameters of if-function 
            return True
        else:
            return False
    def __pow__(self,value): #defining a power function 
        if value%2 > 0 or value%2 <0: #odd values, "rest" after divison by 2
            return interval(self.a**value,self.b**value)
        if value%2==0: # even values, "rest" after divison by 2
            if self.a>=0:
                return interval(self.a**value,self.b**value)
            if self.b<0:
               return interval(self.b**value,self.a**value)
            else:
                lp = [self.a**value,self.b**value]
                return interval(0,max(lp))
##############################################################################               
print("Task 3")
I1 = interval(1,2)
I2 = interval(3,4) 
print(I1)
print()

print("Tasks 4")
print(I1+I2) #[4,6]
print(I1-I2) #[-3,-1]
print(I1*I2) #[3,8]
print(I1/I2) #[0,25,0,666..]
print()

#I3 = interval(-1.e10000,2) 
#print(I1/I2)#negative infinity 

print("Tasks 6")
I3 = interval(1) #interval from 1 to 1 
print(I3) #[1,1]
print()

print("Tasks 7")
I4 = interval(2,3)
#print(I4+1)
#print(1+I4)
#print(1.0+I4)
print()

print("Task 8")
print("is 2 in interval I1:",2 in I1) #true
print("is 5 in interval I2:",5 in I2 )#false 
print()

print("Task 9")
I5 = interval(-2,2) 
print(I5**2) # [0, 4]
print(I5**3) # [-8, 8]
print()

"""
TASK 10
Evaluation and plotting of the given polynomial p(x) 
using a lower bound (xl) and a upper bound (xu)
""" 
xl=np.linspace(0.,1,1000)#lower bound 
xu=np.linspace(0.,1,1000)+0.5 # upper bound 
def p(x): # def polynomial 
    return ((3*x**3) -(2*x**2) + (5*x) -1)
print("Task 10")
plt.plot(xl,p(xu),"b-",label = "upper bound")
plt.plot(xl,p(xl),"g-",label = "lower bound")
plt.plot(xl,(p(xu)-p(xl)),"--",color = "orange",label="diff")
plt.xlabel("x interval")
plt.ylabel("p(x)")
plt.legend(bbox_to_anchor=(1.4, 1.025))
plt.show()
##############################################################################