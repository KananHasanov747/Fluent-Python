'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> for codec in ['latin_1', 'utf_8', 'utf_16']:
... 	print (codec, 'El Niño'.encode (codec), sep='\t')
...
latin_1 b'El Ni\xf1o'
utf_8 b'El Ni\xc3\xb1o'
utf_16 b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'
'''