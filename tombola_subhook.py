# 11.17

class Sized (ABCMeta):

	__slots__ = ()

	@abstractmethod
	def __len__ (self):
		return 0

	@classmethod
	def __subclasshook__ (cls, C):
		if cls is Sized:
			if any ("__len__" in B.__dict__ for B in C.__mro__):
				return True
		return NotImplemented