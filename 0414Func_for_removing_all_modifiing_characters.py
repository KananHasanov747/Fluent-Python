import unicodedata
import string

def shave_marks (txt):
	"""Удалить все диакритические знаки"""
	norm_txt = unicodedata.normalize ('NFD', txt)
	shaved = ''.join (c for c in norm_txt
					  if not unicodedata.combining (c))
	return unicodedata.normalize ('NFC', shaved)

# 4.16
def shave_marks_latin (txt):
	"""Удалить все диактритические знаки для базовых символов набора Latin"""
	norm_txt = unicodedata.normalize ('NFD', txt)
	latin_base = False
	keepers = []
	for c in norm_txt:
		if unicodedata.combining (c) and latin_base:
			continue # игнорировать диакритические знаки
					 # для базовых символов набора Latin
			keepers.append (c)
			# если это не модифицирующий символ, значит новый базовый
			if not unicodedata.combining (c):
				latin_base = c in string.ascii_letters
	shaved = ''.join (keepers)
	return unicodedata.normalize ('NFC', shaved)

# 4.17
single_map = str.maketrans (""",ƒ„†^‹''""•--`›""",
							"""'f"*^‹''""---~›""")

multi_map = str.maketrans ({
	'€': '<euro>',
	'…': '...',
	'Œ': 'OE',
	'™': '(TM)',
	'œ': 'oe',
	'‰': '<per mille>',
	'‡': '**',
	})

multi_map.update (single_map)
def dewinize (txt):
	"""Заменить символы Win1252 символами ASCII или их последовательностями"""
	return txt.translate (multi_map)

def asciize (txt):
	no_marks = shave_marks_latin (dewinize (txt))
	no_marks = no_marks.replace ('ß', 'ss')
	return unicodedata.normalize ('NFKC', no_marks)