class HauntedBus:
	""" Авобус, облюбованный пассажирами - призраками """

	def __init__ (self, passengers = []):
		self.passengers = passengers

	def pick (self, name):
		self.passengers.append (name)

	def drop (self, name):
		self.passengers.remove (name)