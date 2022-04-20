"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> from operator import mul
>>> from functools import partial
>>> triple = partial (mul, 3)
>>> triple (7)
21
>>> list (map (triple, range (1, 10)))
[3, 6, 9, 12, 15, 18, 21, 24, 27]

"""