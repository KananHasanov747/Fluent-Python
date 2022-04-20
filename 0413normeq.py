"""
Служебные функции для сравнения нормализованных Unicode - строк.

Использование нормальной формы С, с учетом регистра:

>>> s1 = 'café'
>>> s2 = 'cafe\u0301'
>>> s1 == s2
False
>>> nfc_equal (s1, s2)
True
>>> nfc_equal ('A', 'a')
False

Использование нормальной формы С, со сворачиванием регистра:

>>> s3 = 'Straße'
>>> s4 = 'strasse'
>>> s3 == s4
False
>>> nfc_equal (s3, s4)
False
>>> fold_equal (s3, s4)
True
>>> fold_equal (s1, s2)
True
>>> fold_equal ('A', 'a')
True

"""

from unicodedata import normalize

def nfc_equal (str1, str2):
	return normalize ('NFC', str1) == normalize ('NFC', str2)

def fold_equal (str1, str2):
	return (normalize ('NFC', str1).casefold () == normalize ('NFC', str2).casefold ())