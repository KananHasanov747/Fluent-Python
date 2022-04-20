'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> import bisect
>>> def grade (score, breakpoints = [60, 70, 80, 90], graades = 'FDCBA'):
...		i = bisect.bisect (breakpoints, score)
...		return grades [i]
...
>>> [grade (score) for score in [33, 99, 77, 70, 89, 90, 100]]


'''