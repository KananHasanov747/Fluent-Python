"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> from types import MappingProxyType
>>> d = {1: 'A'}
>>> d_proxy = MappingProxyType (d)
>>> d_proxy
mappingproxy ({1: 'A'})
>>> d_proxy [1]						#1
'A'
>>> d_proxy [2] = 'x'				#2
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'mappingproxy' object odes not support item assignment
>>> d [2] = 'B'
>>> d_proxy							#3
mappingproxy ({1: 'A', 2: 'B'})
>>> d_proxy [2]
'B'
>>>
"""