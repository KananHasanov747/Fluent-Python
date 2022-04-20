"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> a = 3
>>> b = 6
>>> def f2 (a):
...   print (a)
...   print (b)
...   b = 9
... 
>>> f2 (3)
3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f2
UnboundLocalError: local variable 'b' referenced before assignment
>>> def f3 (a):
...   global b
...   print (a)
...   print (b)
...   b = 9
...
>>> f3 (3)
3
6
>>> b
9
>>> f3 (3)
3
9
>>> b
9

"""
a = 3; b = 6

def f1 (a):
  print (a)
  print (b)

def f2 (a):
  print (a)
  print (b)
  b = 9

from dis import dis
print ('f1:', '\n')
print (dis (f1), '\n\n')
print ('f2:', '\n')
print (dis (f2))