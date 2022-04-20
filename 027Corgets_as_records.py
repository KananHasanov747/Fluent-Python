'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> lax_coordinates = (33.9425, -118.408056)
>>> city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
>>> traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
... 	('ESP', 'XDA205856')]
>>> for passport in sorted (traveler_ids):
... 	print ('%s / %s' % passport)
...

>>> for country, _ in traveler_ids:
... 	print (country)
...

>>> for _, passport_number in traveler_ids:
... 	print (passport_number)

'''