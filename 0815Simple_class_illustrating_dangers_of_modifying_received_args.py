class TwilightBus:
	""" Автобус, из которого бесследно исчезают пассажиры """

	def __init__ (self, passengers = None):
		if passengers is None:
			self.passengers = []
		else:
			self.passengers = list (passengers)

	def pick (self, name):
		self.passengers.append (name)

	def drop (self, name):
		self.passengers.remove (name)