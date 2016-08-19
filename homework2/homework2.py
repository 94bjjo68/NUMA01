import numpy as np
import matplotlib.pyplot as plt

class Interval:
	def __init__(self, *args):
		self.a = args[0]		
		if(len(args)==2):
			self.b = args[1]
		else:
			self.b = args[0]		


	def __repr__(self):
		return repr([self.a, self.b])

	def __add__(self, other ): 
		if(isinstance(self,Interval) and isinstance(other, Interval)):
			return Interval( self.a + other.a, self.b + other.b)
		if(isinstance(other,( int, float))):
			other = Interval(other)
			return Interval(self.a + other.a, self.b + other.b)


	def __radd__(self, other):
		return Interval(self.a + other, self.b + other)
	def __sub__(self, other):
		return Interval(self.a - other.b, self.b - other.a)

	def __mul__(self, other):
		return Interval(self.a * other.a, self.b * other.b)

	def __truediv__(self, other):
		if (other.a or other.b) == 0 or np.inf:
			return 'Please make sure values is of sort int and x !=0'
		else:
			return nterval(self.a / other.b, self.b / other.a)
	def __pow__(self, other):
		return Interval(self.a**other, self.b**other)



def func(X):
	return (3*X**3)-(2*X**2)+(5*X)-1

xl = np.linspace(0.,1,1000)
xu = np.linspace(0.,1,1000) + 0.5

plt.plot(xl, func(xl), c='r')
plt.plot(xl, func(xu), c='b')
plt.plot(xl, func(xu)-func(xl), c='black')
plt.show()




