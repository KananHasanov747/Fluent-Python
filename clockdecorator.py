# Example 7.15
import time

def clock (func):
	def clocked (*args):
		t0 = time.perf_counter ()
		result = func (*args)
		elapsed = time.perf_counter () - t0
		name = func.__name__
		arg_str = ', '.join (repr (arg) for arg in args)
		# print ('[%.8fs] %s (%s) -> %r ' % (elapsed, name, arg_str, result))
		print (f'[{elapsed:.8f}s] {name} ({arg_str}) -> {result}')
		return result
	return clocked