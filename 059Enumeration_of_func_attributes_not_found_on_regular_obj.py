"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> class C: pass
>>> obj = C ()
>>> def func (): pass
>>> sorted (set (dir (func)) - set (dir (obj)))
['__annotations__', '__builtins__', '__call__',
	'__closure__', '__code__', '__defaults__',
	'__get__', '__globals__', '__kwdefaults__',
	'__name__', '__qualname__']

"""