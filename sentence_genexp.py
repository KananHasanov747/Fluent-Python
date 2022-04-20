# 14.9

import re
import reprlib

RE_WORD = re.compile ('\w+')

class Sentence:

	def __init__ (self, text):
		self.text = text

	def __repr__ (self):
		return (match.group () for match in RE_WORD.finditer (self.text))