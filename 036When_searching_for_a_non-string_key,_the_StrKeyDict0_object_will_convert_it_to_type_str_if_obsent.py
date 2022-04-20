'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

Tests for item retrieval using `d [key]` notation::

>>> d = StrKeyDict0 ([('2', 'two'), ('4', 'four')])
>>> d ['2']

>>> d [4]

>>> d [1]


Tests for item retrieval using `d.get(key)` notation::

>>> d.get ('2')

>>> d.get (4)

>>> d.get (1, 'N/A')


Tests for the `in` operator::

>>> 2 in d

>>> 1 in d

'''

class StrKeyDict0 (dict):

	def __missing__ (self, key):
		if isinstance (key, str):
			raise KeyError (key)
		return self [str (key)]

	def get (self, key, default = None):
		try:
			return self [key]
		except KeyError:
			return default

	def __contains__ (self, key):
		return key in self.keys () or str (key) in self.keys ()