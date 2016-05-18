import numpy as np
from pylab import *



dataMatrix1 = genfromtxt('coord1_1.txt')
c1 = dataMatrix1[:1].astype(int)
c2 = dataMatrix1[1:2,].astype(int)

dataMatrix2 = genfromtxt('elementnode1_1.txt')
e1= dataMatrix2[:1].astype(int)
e2 = dataMatrix2[1:2,].astype(int)
e3= dataMatrix2[2:3,].astype(int)
print (c1[e1[1]], c1[e1[1]])

#elements = []
#for i in range(0, len(dataMatrix2)):
#    elements = np.append([elements,  c1[e1[i]], c2[e1[i]], c1[e2[i]], c2[e2[i]], c2[e3[i]], c2[e3[i]] ] )
#    print (elements)
#print (elements)

plt.plot(x, y, '*')
plt.show()
