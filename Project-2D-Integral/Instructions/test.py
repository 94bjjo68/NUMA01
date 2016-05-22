import numpy as np
from pylab import *
from random import randint


dataMatrix1 = genfromtxt('coord1_1.txt')
c1 = dataMatrix1[:1]
c2 = dataMatrix1[1:2,]

dataMatrix2 = genfromtxt('elementnode1_1.txt')
e1= dataMatrix2[:1].astype(int)
e2 = dataMatrix2[1:2,].astype(int)
e3= dataMatrix2[2:3,].astype(int)

print (len(c1[0]))
x = []
y = []
#for i in range(0, len(e1[0])):
#	x.append([ [ c1[0][e1[0][i]], c1[0][e2[0][i]], c1[0][e3[0][i]] ] ])
#	y.append([ [ c2[0][e1[0][i]], c2[0][e2[0][i]], c2[0][e3[0][i]] ] ])
print ( [ c2[0][e1[0][20]], c2[0][e2[0][20]], c2[0][e3[0][20]] ] )
print (e1[0]) 
print (e2[0])
print (e3[0])
col=['green', 'red', 'blue']
for i in range(0, len(e1[0])-1):
	plt.plot([ c1[0][e1[0][i]-1], c1[0][e2[0][i]], c1[0][e3[0][i]-1] ] , [ c2[0][e1[0][i]-1], c2[0][e2[0][i]-1], c2[0][e3[0][i]-1] ],'--k', c=col[randint(0,2)] )
plt.show()

