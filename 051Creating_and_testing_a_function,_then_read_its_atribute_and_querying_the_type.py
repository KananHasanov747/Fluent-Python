"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> def factorial (n):
...		'''returns n!'''
...		return 1 if n < 2 else n * factorial (n - 1)
>>> factorial (42)
1405006117752879898543142606244511569936384000000000
>>> factorial.__doc__
'returns n!'
>>> type (factorial)
<class 'function'>

"""