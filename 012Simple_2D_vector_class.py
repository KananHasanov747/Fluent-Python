from math import hypot

class Vector:
	def __init__ (self, x = 0, y = 0):
		self.x = x;
		self.y = y;

	def __repr__ (self):
		return 'Vector (%r, %r)' % (self.x, self.y)


	''' функция abs нужно для вычисления длины вектора (гипотенузы)
	например, abs( Vector (3, 4)) означает
	sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5 '''
	def __abs__ (self):
		return hypot (self.x, self.y)

	def __bool__ (self):
		return bool (abs (self))

	def __add__ (self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector (x, y)

	def __mul__ (self, scalar):
		return Vector (self.x * scalar, self.y * scalar)