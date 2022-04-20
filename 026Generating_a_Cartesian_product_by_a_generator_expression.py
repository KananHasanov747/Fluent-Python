'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
... 	print (tshirt)
...

'''