'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> from collections import namedtuple
>>> City = namedtuple ('City', 'name country population coordinates')
>>> City._fields
>>> LatLong = namedtuple ('LatLong', 'lat long')
>>> delhi_data = ('Delphi NCR', 'IN' ,21.935, LatLong (28.613889, 77.208889))
>>> delhi = City._make (delhi_data)
>>> delhi._asdict ()

>>> for key, value in delhi._asdict ().items ():
... 	print (key + ':', value)
...

'''