'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> import array
>>> numbers = array.array ('h', [-2, -1, 0, 1, 2])
>>> octets = bytes (numbers)
>>> octets
b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'
'''