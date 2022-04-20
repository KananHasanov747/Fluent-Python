'''

>>> avg = make_averager ()
>>> avg (10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".../7.13Incorrect_higher_order_function.py", line 6, in averager
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment

'''

def make_averager ():
	count = 0
	total = 0

	def averager (new_value):
		count += 1
		total += new_value
		return total / count

	return averager