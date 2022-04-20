'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> os.listdir ('.')
['abc.txt', 'digits-of-ϖ.txt']
>>> os.listdir (b'.')
[b'abc.txt', b'digits-of-\xcf\x80.txt']
>>> pi_name_bytes = os.listdir (b'.')[1]
>>> pi_name_str = pi_name_bytes.decode ('ascii', 'surrogateescape')
>>> pi_name_str
'digits-of-\udccf\udc80.txt'
>>> pi_name_str_encode ('ascii', 'surrogateescape')
b'digits-of-\xcf\x80.txt'

'''