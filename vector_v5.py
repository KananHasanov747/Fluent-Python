# 10.16

'''
A ``Vector`` is built from an iterable of numbers::

	>>> Vector ([3.1, 4.2])
	Vector ([3.1, 4.2])
	>>> Vector ((3, 4, 5))
	Vector ([3.0, 4.0, 5.0])
	>>> Vector ([3.0, 4.0, 5.0])
	Vector ([3.0, 4.0, 5.0])
	>>> Vector (range (10))
	Vector ([0.0, 1.0, 2.0, 3.0, 4.0, ...])


Tests with two dimensions (same results as ``vector2d_v1.py``)::

	>>> v1 = Vector ([3, 4])
	>>> x, y = v1
	>>> x, y
	(3.0, 4.0)
	>>> v1
	Vector ([3.0, 4.0])
	>>> v1_clone = eval (repr (v1))
	>>> v1 == v1_clone
	True
	>>> print (v1)
	(3.0, 4.0)
	>>> octets = bytes (v1)
	>>> octets
	b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
	>>> abs (v1)
	5.0
	>>> bool (v1), bool (Vector ([0, 0]))
	(True, False)


Test of ``.frombytes ()`` class method:

	>>> v1_clone = Vector.frombytes (bytes (v1))
	>>> v1_clone
	Vector ([3.0, 4.0])
	>>> v1 == v1_clone
	True


Test with three dimensions::

	>>> v1 = Vector ([3, 4, 5])
	>>> x, y, z = v1
	>>> x, y, z
	(3.0, 4.0, 5.0)
	>>> v1
	Vector ([3.0, 4.0, 5.0])
	>>> v1_clone = eval (repr (v1))
	>>> v1 == v1_clone
	True
	>>> print (v1)
	(3.0, 4.0, 5.0)
	>>> abs (v1) # doctest:+ELLIPSIS
	7.0710678118654755
	>>> bool (v1), bool (Vector ([0, 0, 0]))
	(True, False)


Test with many dimensions::

	>>> v7 = Vector (range (7))
	>>> v7
	Vector ([0.0, 1.0, 2.0, 3.0, 4.0, ...])
	>>> abs (v7) # doctest:+ELLIPSIS
	9.539392014169456


Test of ``.__bytes__`` and ``.frombytes ()`` methods::

	>>> v1 = Vector ([3, 4, 5])
	>>> v1_clone = Vector.frombytes (bytes (v1))
	>>> v1_clone
	Vector ([3.0, 4.0, 5.0])
	>>> v1 == v1_clone
	True


Tests of sequence behavior::

	>>> v1 = Vector ([3, 4, 5])
	>>> v1_clone = Vector.frombytes (bytes (v1))
	>>> v1_clone
	Vector ([3.0, 4.0, 5.0])
	>>> v1 == v1_clone
	True
	>>> v1 = Vector ([3, 4, 5])
	>>> len (v1)
	3
	>>> v1 [0], v1 [len (v1) - 1], v1 [-1]
	(3.0, 5.0, 5.0)


Test of slicing::

	>>> v7 = Vector (range (7))
	>>> v7 [-1]
	6.0
	>>> v1 [1:4]
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'v1' is not defined. Did you mean: 'v7'?
	>>> v7 [1:4]
	Vector ([1.0, 2.0, 3.0])
	>>> v7 [-1:]
	Vector ([6.0])
	>>> v7 [1,2]
	Traceback (most recent call last):
	 ...
	TypeError: Vector indices must be integers


Test of dynamic attribute access::

	>>> v7 = Vector (range (10))
	>>> v7.x
	0.0
	>>> v7.y, v7.z, v7.t
	(1.0, 2.0, 3.0)


Dynamic attribute lookup failures::

	>>> v7.k
	Traceback (most recent call last):
	 ...
	AttributeError: 'Vector' object has no attribute 'k'
	>>> v3 = Vector (range (3))
	>>> v3.t
	Traceback (most recent call last):
	 ...
	AttributeError: 'Vector' object has no attribute 't'
	>>> v3.spam
	Traceback (most recent call last):
	 ...
	AttributeError: 'Vector' object has no attribute 'spam'


Test of hashing::

	>>> v1 = Vector ([3, 4])
	>>> v2 = Vector ([3.1, 4.2])
	>>> v3 = Vector ([3, 4, 5])
	>>> v6 = Vector (range (6))
	>>> hash (v1), hash (v3), hash (v6)
	(7, 2, 1)


Most hash values of non-integers vary from a 32-bit to 64-bit CPython build::

	>>> import sys
	>>> hash (v2) == (384307168202284039 if sys.maxsize > 2 ** 32 else  357915986)
	True
	>>> v1 = Vector ([3, 4])
	>>> format (v1)
	'(3.0, 4.0)'
	>>> format (v1, '.2f')
	'(3.00, 4.00)'
	>>> format (v1, '.3e')
	'(3.000e+00, 4.000e+00)'


Test of ``format ()`` with Cartesian coordinates in 3D and 7D::

	>>> v3 = Vector ([3, 4, 5])
	>>> format (v3)
	'(3.0, 4.0, 5.0)'
	>>> format (Vector (range (7)))
	'(0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)'


Test of ``format ()`` with speial coordinates in 2D, 3D and 4d::

	>>> format (Vector ([1, 1]), 'h') # doctest:+ELLIPSIS
	'<1.4142135623730951, 0.7853981633974483>'
	>>> format (Vector ([1, 1]), '.3eh')
	'<1.414e+00, 7.854e-01>'
	>>> format (Vector ([1, 1]), '0.5fh')
	'<1.41421, 0.78540>'
	>>> format (Vector ([1, 1, 1]), 'h') # doctest:+ELLIPSIS
	'<1.7320508075688772, 0.9553166181245093, 0.7853981633974483>'
	>>> format (Vector ([2, 2, 2]), '.3eh')
	'<3.464e+00, 9.553e-01, 7.854e-01>'
	>>> format (Vector ([0, 0, 0]), '0.5fh')
	'<0.00000, 0.00000, 0.00000>'
	>>> format (Vector ([-1, -1, -1, -1]), 'h') # doctest:+ELLIPSIS
	'<2.0, 2.0943951023931957, 2.186276035465284, 3.9269908169872414>'
	>>> format (Vector ([2, 2, 2, 2]), '.3eh')
	'<4.000e+00, 1.047e+00, 9.553e-01, 7.854e-01>'
	>>> format (Vector ([0, 1, 0, 0]), '0.5fh')
	'<1.00000, 1.57080, 0.00000, 0.00000>'

'''

from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools

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
		return len (self) == len (other) and all (a == b for a, b in zip (self, other))

	def __hash__ (self):
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
	def __getattr__ (self, name):
		cls = type (self)
		if len (name) == 1:
			pos = cls.shortcut_names.find (name)
			if 0 <= pos < len (self._components):
				return self._components [pos]
		msg = '{.__name__!r} object has no attribute {!r}'
		raise AttributeError (msg.format (cls, name))

	def angle (self, n):
		r = math.sqrt (sum (x * x for x in self [n:]))
		a = math.atan2 (r, self [n - 1])
		if (n == len (self) - 1) and (self [-1] < 0):
			return math.pi * 2 - a
		else:
			return a

	def angles (self):
		return (self.angle (n) for n in range (1, len (self)))

	def __format__ (self, fmt_spec = ''):
		if fmt_spec.endswith ('h'): # hyperspherical coordinates
			fmt_spec = fmt_spec [:-1]
			coords = itertools.chain ([abs (self)],
									  self.angles ())
			outer_fmt = '<{}>'
		else:
			coords = self
			outer_fmt = '({})'
		components = (format (c, fmt_spec) for c in coords)
		return outer_fmt.format (', '.join (components))
