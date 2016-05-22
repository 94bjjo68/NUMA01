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
            
            if minangle >= pi/2000000:
                
                J.append(abs((xb[i]-xa[i])*(yc[i]-ya[i])-(yb[i]-ya[i])*(xc[i]-xa[i])))
            ####### Raise error: too thin triangles ###################################
            else:  
                raise Exception("Triangles are too thin, minangle is:",minangle)
                #J.append(0)
        return J
        
    def __Integral__(self, f):
        
        J = Mesh(self.C, self.N).__Jacobian__()
        S = sum(J)
        I = S*1/2*(1/3*f(0,0) + 1/3*f(0,1) + 1/3*f(1,0))
        
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
            beta  = arccos((abs(dot(a, c)))/(sqrt(dot(a, a))*sqrt(dot(c,c))))
            gamma = arccos((abs(dot(b, a)))/(sqrt(dot(b, b))*sqrt(dot(a,a))))
        
            A.append(sqrt(dot(a,a))*sqrt(dot(b,b))*abs(sin(gamma))/2)
            
        Area = sum(A)
        
        return Area
        
    def __plotting__(self):
        
        C = self.C
        N = self.N
        
        s = size(self.N[:, 0])
        O = ones([size(s), 3])
        x = C[:, 0]
        y = C[:, 1]
        Nprime = N - O
        L = []
        for i in range(s):
            L.append(i)
        CV = array(L)
        return plt.tripcolor(x, y, Nprime, facecolors = CV, edgecolors = 'k')
        

c = genfromtxt ('coord1_1.txt')
n = genfromtxt ('elementnode1_1.txt')  
                  
coords = c.T
nodes = n.T
    
m = Mesh(coords, nodes)

print(m)

J = m.__Jacobian__()
print('J =', J)

f = lambda x,y: 1

   
I = m.__Integral__(f)        
print('The integral of the function over the given area is', I) 

A = m.__Area__()
print('The total area of the domain is', A)

print("The difference between the integral and the area is:",abs(m.__Integral__(f)-m.__Area__()))

plt.figure()
plt.gca().set_aspect('equal')  
m.__plotting__()
plt.title('Triplot of our surface')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

from xml.dom import minidom

def xmlconv(name): 
    
    xmldoc = minidom.parse(name)
    itemlist = xmldoc.getElementsByTagName('vertex')
    
    X = []
    for s in itemlist:
        X.append(s.attributes['x'].value)
    print('X =', X)
        
    
    xmldoc = minidom.parse(name)
    itemlist = xmldoc.getElementsByTagName('vertex')
    
    Y = []
    for s in itemlist:
        Y.append(s.attributes['y'].value)
    print('Y =', Y)
        
    
    xmldoc = minidom.parse(name)
    itemlist = xmldoc.getElementsByTagName('triangle')
    
    V0 = []
    for s in itemlist:
        V0.append(s.attributes['v0'].value)
    
    xmldoc = minidom.parse(name)
    itemlist = xmldoc.getElementsByTagName('triangle')
    
    V1 = []
    for s in itemlist:
        V1.append(s.attributes['v1'].value)
        
    xmldoc = minidom.parse(name)
    itemlist = xmldoc.getElementsByTagName('triangle')
    
    V2 = []
    for s in itemlist:
        V2.append(s.attributes['v2'].value)
        
    l = len(X)
    coords = zeros([l, 2])
    coords[:, 0] = X
    coords[:, 1] = Y
    print(coords)
    
    n = len(V0)
    nodes = zeros([n, 3])
    nodes[:, 0] = V0
    nodes[:, 1] = V1
    nodes[:, 2] = V2
    
    nodes += 1

    return coords, nodes
    
xml = xmlconv('dolfin_coarse.xml')

m = Mesh(xml[0], xml[1])

print(m)

J = m.__Jacobian__()
print('J =', J)

f = lambda x,y: 1

   
I = m.__Integral__(f)        
print('The integral of the function over the given area is', I) 

A = m.__Area__()
print('The total area of the domain is', A)

print("The difference between the integral and the area is:",abs(m.__Integral__(f)-m.__Area__()))

plt.figure()
plt.gca().set_aspect('equal')  
m.__plotting__()
plt.title('Triplot of our surface')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
