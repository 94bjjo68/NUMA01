import numpy as np


class Interval:
	def __init__(self, a, b):
		self.a = a 
		self.b = b 

	def __repr__(self):
		return repr([self.a, self.b])

	def __add__(self, other):
		return Interval( self.a + other.a, self.b + other.b) 

	def __sub__(self, other):
		return Interval(self.a - other.b, self.b - other.a)
		 
	def __mul__(self, other):
		return Interval(self.a * other.a, self.b * other.b)

	def __truediv__(self, other):
		if (other.a, other.b) == 0 or np.inf:
			return 'Please make sure values is of sort int and x !=0' 
		else:
			return nterval(self.a / other.b, self.b / other.a)


I1 = Interval(1, 2)
I2 = Interval(1, 4)
print(I1)
print(I2 + I1)
print (I1-I2)
print (I1*I2)
print (I1/I2)
		

