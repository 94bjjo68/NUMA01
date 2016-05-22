# -*- coding: utf-8 -*-
"""
Created on Mon May 16 10:36:05 2016

@author: Ägare
"""

from numpy import *
from scipy import *
from pylab import *
from matplotlib.pyplot import *

class Mesh(object):
    
    def __init__(self, C, N):
        
        self.C = C
        self.N = N
        #val =(A, B)
    
    def __repr__(self):
        return '(%s, %s)' % (self.C, self.N)
        
    #def __str__(self):
        #return '(%s, %s)' % (self.C, self.N)
        
    
    def __Jacobian__(self):
        J = []
        C = self.C
        N = self.N
        s = size(self.N[:, 0])     # s = Antal trianglar
        xa = zeros(s)
        xb = zeros(s)
        xc = zeros(s)
        ya = zeros(s)
        yb = zeros(s)
        yc = zeros(s)
        
        for i in range(s):
            xa[i] = C[int(N[i, 0]) - 1, 0]
            xb[i] = C[int(N[i, 1]) - 1, 0]
            xc[i] = C[int(N[i, 2]) - 1, 0]
            ya[i] = C[int(N[i, 0]) - 1, 1]
            yb[i] = C[int(N[i, 1]) - 1, 1]
            yc[i] = C[int(N[i, 2]) - 1, 1]
            a = array([xc[i] - xb[i], yc[i] - yb[i]])
            b = array([xc[i] - xa[i], yc[i] - ya[i]])
            c = array([xb[i] - xa[i], yb[i] - ya[i]])
            
            alpha = arccos((abs(dot(b, c)))/(sqrt(dot(b, b))*sqrt(dot(c,c))))
            beta = arccos((abs(dot(a, c)))/(sqrt(dot(a, a))*sqrt(dot(c,c))))
            gamma = arccos((abs(dot(b, a)))/(sqrt(dot(a, a))*sqrt(dot(b,b))))
            minangle = min(alpha, beta, gamma)
            
            if minangle >= pi/90:
                
                J.append(abs((xb[i]-xa[i])*(yc[i]-ya[i])-(yb[i]-ya[i])*(xc[i]-xa[i])))
            ####### Raise error: too thin triangles ###################################
            else:  
                raise Exception("Triangles are too thin, minangle is:",minangle)
                #J.append(0)
        return J
        
    def __Integral__(self, f):
        
        J = Mesh(self.C, self.N).__Jacobian__()
        S = sum(J)
        I = S*((1/6*f(0,0)) + (1/6*f(0,1)) + (1/6*f(1,0)))
        
        return I
        
    def __Area__(self):
        
        C = self.C
        N = self.N
        s = size(self.N[:, 0])     # s = Antal trianglar
        xa = zeros(s)
        xb = zeros(s)
        xc = zeros(s)
        ya = zeros(s)
        yb = zeros(s)
        yc = zeros(s)
        
        A = []
        
        for i in range(s):
            xa[i] = C[int(N[i, 0]) - 1, 0]
            xb[i] = C[int(N[i, 1]) - 1, 0]
            xc[i] = C[int(N[i, 2]) - 1, 0]
            ya[i] = C[int(N[i, 0]) - 1, 1]
            yb[i] = C[int(N[i, 1]) - 1, 1]
            yc[i] = C[int(N[i, 2]) - 1, 1]
            a = array([xc[i] - xb[i], yc[i] - yb[i]])
            b = array([xc[i] - xa[i], yc[i] - ya[i]])
            c = array([xb[i] - xa[i], yb[i] - ya[i]])
            
            alpha = arccos((abs(dot(b, c)))/(sqrt(dot(b, b))*sqrt(dot(c,c))))
            beta = arccos((abs(dot(a, c)))/(sqrt(dot(a, a))*sqrt(dot(c,c))))
            gamma = arccos((abs(dot(b, a)))/(sqrt(dot(a, a))*sqrt(dot(b,b))))
        
            A.append(b*c*sin(alpha)/2)
            
        Area = sum(A)
        
        return Area
            
        
        
from io import BytesIO
c = np.genfromtxt(io.BytesIO('Instructions/coord1_1.txt'),)
n = np.genfromtxt(io.BytesIO('Instructions/elementnode1_1.txt'),)  
                
print (c.T)
print (n.T)
coords = c.T
nodes = n.T

m = Mesh(coords, nodes)
#rint(m)

J = m.__Jacobian__()
#print('J =', J)

f = lambda x,y: 1

   
I = m.__Integral__(f)        
#print('The integral of the function over the given area is', I) 

A = m.__Area__()
#print('The total area of the domain is', A)

#print("The difference between the integral and the area is:",abs(m.__Integral__(f)-m.__Area__()))

  
