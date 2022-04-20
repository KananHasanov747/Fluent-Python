"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> from unicodedata import name
>>> {chr (i) for i in range (32, 256) if 'SIGN' in name (chr (i), '')}
{'§', '%', '=', '©', '#', '¥', '¢', '¤', '>', '¶', '<', '°', '±', '£', 'µ', '¬', '®', '$', '+', '÷', '×'}
"""