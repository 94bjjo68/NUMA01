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
		if(isinstance(other, (int, float))):
			other = Interval(other)
		return Interval(self.a - other.b, self.b - other.a)

	def __mul__(self, other):	
		if(isinstance(other, (int, float))):
			other = Interval(other)
		variations = [self.a*other.a, self.a*other.b, self.b*other.b]
		return Interval(min(variations), max(variations))
	
	def __rmul__(self, other):	
		if(isinstance(other, (int, float))):
			other = Interval(other)
		variations = [self.a*other.a, self.a*other.b, self.b*other.b]
		return Interval(min(variations), max(variations))

	def __truediv__(self, other):
		if 0 in Interval(other.a, other.b) or  np.inf:
			raise ValueError('Please make sure values is of sort int and x !=0')
		else:
			variations = [self.a/othe.a , self.a/other.b , self.b/other.a, self.b/other.b]
			return Interval(min(variations), max(variations))
	def __pow__(self, other):
		variations = [self.a**other, self.b**other]
		return Interval(min(variations), max(variations))
	def __contains__(self, other):
		if other>= self.a and other<=self.b:
			return True
		else:
			return False
	def Return(self):
		return [self.a, self.b]

		
def func(X):
	return (3*X**3)-(2*X**2)+(5*X)-1
a=1000

xl = np.linspace(0.,1,1000)
xu = np.linspace(0.,1,1000) + 0.5

y_list = []
for n in range(a):
	lst = func(Interval(xl[n], xu[n])) 
	y_list.append(lst.Return()) 


plt.plot(xl, y_list, c='r')


plt.show()




