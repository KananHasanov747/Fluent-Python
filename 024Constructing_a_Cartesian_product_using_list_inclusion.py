'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> tshirts = [(color, size) for color in colors for size in sizes]
>>> tshirts

>>> for color in colors:
... 	for size in sizes:
... 		print ((color, size))
...

>>> tshirts = [(color, size) for size in sizes
... 						 for color in colors]
>>> tshirts

'''