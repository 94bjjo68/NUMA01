# -*- coding: utf-8 -*-
"""
Created on Mon May 16 10:36:05 2016

@author: Ägare
"""

from numpy import *
from scipy import *
from pylab import *
from matplotlib.pyplot import *
from xml.dom import minidom

"""
Functionality trough class to create a mesh from a finite amount of elements 
Where each element is a triangle composed of 3 connected nodes. 

A node can be described from it's coordinates(x,y):
na = [xa,ya]
nb = [xb,yb]
nc = [xc,yc]

A element can then be described as a matrix of 3 sets of nodes (number)
TA = [na,nb,nc]

The mesh can be described as a tuple of all the elements and the nodes in the region:
M = |na,nb,nc||xa,ya|
    |nb,na,nc||xb,yb|
    |nc,na,nb||xc,yc|
""" 

class Mesh(object):
    
    def __init__(self, C, N):
        
        self.C = C
        self.N = N
    
    def __repr__(self):
        return '(%s, %s)' % (self.C, self.N)
        
    
    def __Jacobian__(self):
        J = []
        C = self.C
        N = self.N
        s = size(self.N[:, 0])     # s = Antal trianglar
        
        #creating empty arrays of length s 
        
        xa = zeros(s) 
        xb = zeros(s)
        xc = zeros(s)
        ya = zeros(s)
        yb = zeros(s)
        yc = zeros(s)
        
        for i in range(s): 
        #for-loop to calculate the coordinates of each vector for every triangle  
            xa[i] = C[int(N[i, 0]) - 1, 0]
            xb[i] = C[int(N[i, 1]) - 1, 0]
            xc[i] = C[int(N[i, 2]) - 1, 0]
            ya[i] = C[int(N[i, 0]) - 1, 1]
            yb[i] = C[int(N[i, 1]) - 1, 1]
            yc[i] = C[int(N[i, 2]) - 1, 1]
            a = array([xc[i] - xb[i], yc[i] - yb[i]])
            b = array([xc[i] - xa[i], yc[i] - ya[i]])
            c = array([xb[i] - xa[i], yb[i] - ya[i]])
            
            #calculating angles in each triangle 
            alpha = arccos((abs(dot(b, c)))/(sqrt(dot(b, b))*sqrt(dot(c,c))))
            beta = arccos((abs(dot(a, c)))/(sqrt(dot(a, a))*sqrt(dot(c,c))))
            gamma = arccos((abs(dot(b, a)))/(sqrt(dot(a, a))*sqrt(dot(b,b)))) 
            minangle = min(alpha, beta, gamma)
            
            if minangle >= pi/2000000: #def minimum allowed angle 
                J.append(abs((xb[i]-xa[i])*(yc[i]-ya[i])-(yb[i]-ya[i])*(xc[i]-xa[i])))
                #calculating the jacobian 
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
        
        #creating empty arrays of length s 
        
        xa = zeros(s)
        xb = zeros(s)
        xc = zeros(s)
        ya = zeros(s)
        yb = zeros(s)
        yc = zeros(s)
        
        A = [] #list of the area for every triangle 
        
        for i in range(s):
            xa[i] = C[int(N[i, 0]) - 1, 0]
            xb[i] = C[int(N[i, 1]) - 1, 0]
            xc[i] = C[int(N[i, 2]) - 1, 0]
            ya[i] = C[int(N[i, 0]) - 1, 1]
            yb[i] = C[int(N[i, 1]) - 1, 1]
            yc[i] = C[int(N[i, 2]) - 1, 1]
            a = array([xc[i] - xb[i], yc[i] - yb[i]])
            b = array([xc[i] - xa[i], yc[i] - ya[i]])
            #c = array([xb[i] - xa[i], yb[i] - ya[i]])
            
            #alpha = arccos((abs(dot(b, c)))/(sqrt(dot(b, b))*sqrt(dot(c,c))))
            #beta  = arccos((abs(dot(a, c)))/(sqrt(dot(a, a))*sqrt(dot(c,c))))
            gamma = arccos((abs(dot(b, a)))/(sqrt(dot(b, b))*sqrt(dot(a,a))))
        
            A.append(sqrt(dot(a,a))*sqrt(dot(b,b))*abs(sin(gamma))/2)
            
        Area = sum(A) # sum of  the area of all the triangles
        
        return Area
        
    def __plotting__(self):
        
        C = self.C
        N = self.N
        
        s = size(self.N[:, 0])
        x = C[:, 0]
        y = C[:, 1]
        L = []
        for i in range(s):
            L.append(i)
        CV = array(L) # for facecolor 
        return plt.tripcolor(x, y, N-1, facecolors = CV, edgecolors = 'k')
        
#------------------------------ DATA INPUT -----------------------------------#
c = genfromtxt ('coord1_1.txt')
n = genfromtxt ('elementnode1_1.txt')  
coords = c.T
nodes = n.T    
m = Mesh(coords, nodes)
#------------------------------ DATA OUTPUT ----------------------------------#
f = lambda x,y: 1
J = m.__Jacobian__()
I = m.__Integral__(f)
A = m.__Area__()
#------------------------------ PRINT SECTION --------------------------------#
print(m)
print()
print('J =', J)
print()
print('The integral of the function over the given area is', I) 
print('The total area of the domain is', A)
print("The difference between the integral of the constant function 1 and the area is:",abs(m.__Integral__(f)-m.__Area__()))

#---------------------------- Plotting of surface ----------------------------#
plt.figure()
plt.gca().set_aspect('equal')  
m.__plotting__()
plt.title('Triplot of our surface')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
"""
xmlconv 
Function to unpack data recived from dolphin.xml and append to plotable lists.

"""
def xmlconv(name): 
    
    xmldoc = minidom.parse(name) #restructuring data 
    itemlist = xmldoc.getElementsByTagName('vertex')#def how to get data 
    
    X = [] #unpacking X coords 
    for s in itemlist:
        X.append(s.attributes['x'].value)
            
    Y = []#unpacking Y coords 
    for s in itemlist:
        Y.append(s.attributes['y'].value)
         
    itemlist = xmldoc.getElementsByTagName('triangle')
    
    V0 = [] #nodes a
    for s in itemlist:
        V0.append(s.attributes['v0'].value)
        
    V1 = []#nodes b
    for s in itemlist:
        V1.append(s.attributes['v1'].value)
        
    V2 = []#nodes c
    for s in itemlist:
        V2.append(s.attributes['v2'].value)
        
    coords = zeros([len(X), 2])
    coords[:, 0] = X
    coords[:, 1] = Y
    
    nodes = zeros([len(V0), 3])
    nodes[:, 0] = V0
    nodes[:, 1] = V1
    nodes[:, 2] = V2
    
    nodes += 1

    return coords, nodes
#----------------------------DATA INPUT -------------------------------------#
xml = xmlconv('dolfin_fine.xml')
m = Mesh(xml[0], xml[1])
#----------------------------DATA OUTPUT ------------------------------------#
Y = xml[0][:,1]
X = xml[1][:,1]  
f = lambda x,y: 1
J = m.__Jacobian__()
I = m.__Integral__(f)  
A = m.__Area__()
squarearea = (int(max(X)) - int(min(X)))*(int(max(Y)) - int(min(Y)))
#--------------------------Print Section ------------------------------------#
print('The integral of the function over the given area is', I) 
print('The total area of the domain is', A)
print('The area of the the shape is', squarearea - A)
print("The difference between the integral of the constant function 1 and the area is:",abs(m.__Integral__(f)-m.__Area__()))

#------------------------ Plotting of surface -------------------------------#
plt.figure()
plt.gca().set_aspect('equal')  
m.__plotting__()
plt.title('Triplot of our surface')
plt.xlabel('x')
plt.ylabel('y')
plt.show()