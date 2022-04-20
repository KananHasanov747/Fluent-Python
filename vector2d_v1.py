# 9.3

from vector2d_v0 import Vector2d

@classmethod
def frombytes (cls, octets):
	typecode = chr (octets [0])
	memv = memoryview (octets [1:]).cast (typecode)
	return cls (*memv)