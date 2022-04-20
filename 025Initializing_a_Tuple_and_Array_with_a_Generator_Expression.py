'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> symbols = 'ß˙¥®ßˆå¬æ'
>>> tuple (ord (symbol) for symbol in symbols)

>>> import array
>>> array.array ('I', (ord (symbol) for symbol in symbols))

'''