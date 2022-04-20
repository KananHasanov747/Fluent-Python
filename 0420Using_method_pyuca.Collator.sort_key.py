'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> import pyuca
>>> coll = pyuca.Collator ()
>>> fruits = ['caju', 'atemoia', 'cajá', 'açai', 'acerola']
>>> sorted_fruits = sorted (fruits, key = coll.sort_key)
>>> sorted_fruits
['açai', 'acerola', 'atemoia', 'cajá', 'caju']

'''