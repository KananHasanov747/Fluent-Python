"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> from collections import namedtuple
>>> metro_data = [
... 	('Tokyo', 'JP', 36.933, (35.687922, 139.691667)),
... 	('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
... 	('Mexico City', 'MX', 20.142, (19.43333, -99.133333)),
... 	('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
... 	('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
... ]
>>> LatLong = namedtuple ('LatLong', 'lat long')
>>> Metropolis = namedtuple ('Metropolis', 'name cc pop coord')
>>> metro_areas = [Metropolis (name, cc, pop, LatLong (lat, long))
... 	for name, cc, pop, (lat, long) in metro_data]
>>> metro_areas [0]
Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.687922, long=139.691667))
>>> metro_areas [0].coord.lat
35.687922
>>> from operator import attrgetter
>>> name_lat = attrgetter ('name', 'coord.lat')
>>> for city in sorted (metro_areas, key = attrgetter ('coord.lat')):
... 	print (name_lat (city))
... 
('Sao Paulo', -23.547778)
('Mexico City', 19.43333)
('Delhi NCR', 28.613889)
('Tokyo', 35.687922)
('New York-Newark', 40.808611)

"""