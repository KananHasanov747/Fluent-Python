'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> import locale
>>> locale.setlocale (locale.LC_COLLATE, 'pt.BR.UTF-8')
'pt_BR.UTF-8'
>>> fruits = ['caju', 'atemoia', 'cajá', 'açai', 'acerola']
>>> sorted_fruits = sorted (fruits, key = locale.strxfrm)
>>> sorted_fruits
['açai', 'acerola', 'atemoia', 'cajá', 'caju']

'''