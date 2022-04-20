"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> import unicodedata, functools
>>> nfc = functools.partial (unicodedata.normalize, 'NFC')
>>> s1 = 'café'
>>> s2 = 'cafe\u0301'
>>> s1, s2
('café', 'café')
>>> s1 == s2
False
>>> nfc (s1) == nfc (s2)
True

"""