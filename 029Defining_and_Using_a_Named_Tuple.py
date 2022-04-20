'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> from collections import namedtuple
>>> City = namedtuple ('City', 'name country population coordinates')
>>> tokyo = City ('Tokyo', 'JP', 36.933, (35.689722, 139691667))
>>> tokyo

>>> tokyo.population

>>> tokyo.coordinates

>>> tokyo [1]

'''