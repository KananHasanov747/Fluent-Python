"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> from operator import methodcaller
>>> s = 'The time has come'
>>> upcase = methodcaller ('upper')
>>> upcase (s)
'THE TIME HAS COME'
>>> hiphenate = methodcaller ('replace', ' ', '-')
>>> hiphenate (s)
'The-time-has-come'

"""