'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> octets = b'Monst\xe9al'
>>> octets.decode ('cp1252')
'Montréal'
>>> octets.decode ('iso8859_7')
'Montrιal'
>>> octets.decode (koi8_r)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'koi8_r' is not defined
>>> octets.decode ('koi8_r')
'MontrИal'
>>> octets.decode ('utf_8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in
position 5: invalid continuation byte
>>> octets.decode ('utf_8', errors = 'replace')
'Montr�al'
'''