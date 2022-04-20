"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> factorial = lambda n: 1 if n < 2 else n * fact (n - 1)
>>> fact = factorial
>>> list (map (fact, range (6)))
[1, 1, 2, 6, 24, 120]
>>> [fact (n) for n in range (6)]
[1, 1, 2, 6, 24, 120]
>>> list (map (factorial, filter (lambda n: n % 2, range (6))))
[1, 6, 120]
>>> [factorial (n) for n in range (6) if n % 2]
[1, 6, 120]

"""