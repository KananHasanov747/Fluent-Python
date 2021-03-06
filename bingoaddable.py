# 13.18

import itertools

from tombola import Tombola
from bingo import BingoCarge

class AddableBingocage (BingoCarge):

	def __add__ (self, other):
		if isinstance (other, Tombola):
			return AddableBingocage (self.inspect () + other.inspect ())
		else:
			return NotImplemented

	def __iadd__ (self, other):
		if isinstance (other, Tombola):
			other_iterable = other.inspect ()
		else:
			try:
				other_iterable = iter (other)
			except TypeError:
				self_cls = type (self).__name__
				msg = "right operand in += must be {!r} or an iterable"
				raise TypeError (msg.format (self_cls))
			self.load (other_iterable)
			return self