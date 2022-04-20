'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

1 часть:
>>> import numpy
>>> a = numpy.arange (12)
>>> a

>>> type (a)

>>> a.shape

>>> a.shape = 3, 4
>>> a

>>> a [2]

>>> a [2, 1]

>>> a [:, 1]

>>> a.transpose ()


2 часть:
>>> import numpy
>>> floats = numpy.loadtxt ('floats-10M-lines.txt')
>>> floats [-3:]

>>> floats *= .5
>>> floats [-3:]

>>> from time import perf_counter as pc
>>> t0 = pc (); floats /= 3; pc () - t0

>>> numpy.save ('floats-10M', floats)
>>> floats2 = numpy.load ('floats-10M.npy', 'r+')
>>> floats2 *= 6
floats2 [-3:]


'''