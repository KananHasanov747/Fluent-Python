'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> import array
>>> numbers = array.array ('h', [-2, -1, 0, 1, 2])
>>> memv = memoryview (numbers)
>>> len (memv)

>>> memv [0]

>>> memv_oct = memv.cast ('B')
>>> memv_oct.tolist ()

>>> memv_oct [5] = 4
>>> numbers


'''