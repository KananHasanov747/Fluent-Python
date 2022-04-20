'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> symbols = '˚∆˚∑øœ¨´'
>>> beyond_ascii = [ord (s) for s in symbols if ord (s) > 127]
>>> beyond_ascii

>>> beyond_ascii = list (filter (lambda c: c > 127, map (ord, symbols)))
>>> beyond_ascii

'''