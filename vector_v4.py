# 10.12
from array import array
import reprlib
import math
import numbers
import functools
import operator

class Vector:
	typecode = 'd'

	def __init__ (self, components):
		self._components = array (self.typecode, components)

	def __iter__ (self):
		return iter (self._components)

	def __repr__ (self):
		components = reprlib.repr (self._components)
		components = components [components.find ('['):-1]
		return 'Vector ({})'.format (components)

	def __str__ (self):
		return str (tuple (self))

	def __bytes__ (self):
		return (bytes ([ord (self.typecode)]) +
				bytes (self._components))

	def __eq__ (self, other):
		# return tuple (self) == tuple (other)

		# 10.13
		# if len (self) != len (other):
		# 	return False
		# for a, b in zip (self, other):
		# 	if a != b:
		# 		return False
		# return True

		# 10.14
		return len (self) == len (other) and all (a == b for a, b in zip (self, other))

	def __hash__ (self):
		# hashes = (hash (x) for x in self._components)
		# return functools.reduce (operator.xor, hashes, 0)

		hashes = map (hash, self._components)
		return functools.reduce (operator.xor, hashes)

	def __abs__ (self):
		return math.sqrt (sum (x * x for x in self))

	def __bool__ (self):
		return bool (abs (self))

	@classmethod
	def frombytes (cls, octets):
		typecode = chr (octets [0])
		memv = memoryview (octets [1:]).cast (typecode)
		return cls (memv)

	def __len__ (self):
		return len (self._components)

	def __getitem__ (self, index):
		cls = type (self)
		
		if isinstance (index, slice):
			return cls (self._components [index])

		elif isinstance (index, numbers.Integral):
			return self._components [index]

		else:
			msg = '{cls.__name__} indices must be integers'
			raise TypeError (msg.format (cls = cls))

	shortcut_names = 'xyzt'
	def __setattr__ (self, name, value):
		cls = type (self)
		if len (name) == 1:
			if name in cls.shortcut_names:
				error = 'readonly attribute {attr_name!r}'
			elif name.islower ():
				error = "can't set attributes 'a' to 'z' in {cls_name!r}"
			else:
				error = ''
			if error:
				msg = error.format (cls_name = cls.__name__, attr_name = name)
				raise AttributeError (msg)
		super ().__setattr__ (name, value)
