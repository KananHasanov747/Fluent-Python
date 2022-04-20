'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> s = 'cafe'
>>> len (s)
4
>>> b = s.encode ('utf8')
>>> b
b'caf\xc3\xa9'
>>> len (b)
5
>>> b.decode ('utf8')
'cafe'
'''