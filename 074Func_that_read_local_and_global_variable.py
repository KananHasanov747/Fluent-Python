"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> def f1 (a):
... 	print (a)
... 	print (b)
... 
>>> f1 (3)
3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f1
NameError: name 'b' is not defined
>>> b = 6
>>> f1 (3)
3
6

"""