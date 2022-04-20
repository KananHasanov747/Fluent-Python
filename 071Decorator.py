"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> target ()
running inner ()
>>> target
<function deco.<locals>.inner at ...>

"""

def deco (func):
	def inner ():
		print ('running inner ()')
	return inner

@deco
def target ():
	print ('running target ()')