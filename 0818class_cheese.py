class Cheese:
	def __init__ (self, kind):
		self.kind = kind

	def __repr__ (self):
		return f'Cheese ({self.kind})'