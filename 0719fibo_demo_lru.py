import functools

from clockdecorator import clock

@functools.lru_cache ()
@clock
def fibonacci (n):
	return n if n < 2 else fibonacci (n - 2) + fibonacci (n - 1)

if __name__ == '__main__':
	print (fibonacci (100))