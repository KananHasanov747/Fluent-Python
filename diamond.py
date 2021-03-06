# 12.4

class A:
	def ping (self):
		print ('ping:', self)

class B (A):
	def pong (self):
		print ('pong:', self)

class C (A):
	def pong (self):
		print ('PONG:', self)

class D (B, C):

	def ping (self):
		A.ping (self) # super ().ping ()
		print ('post-ping:', self)

	def pingpong (self):
		self.ping ()
		super ().ping ()
		self.pong ()
		super ().pong ()
		C.pong (self)

# class E (C, B):

# 	def ping (self):
# 		A.ping (self) # super ().ping ()
# 		print ('post-ping:', self)

# 	def pingpong (self):
# 		self.ping ()
# 		super ().ping ()
# 		self.pong ()
# 		super ().pong ()
# 		B.pong (self)