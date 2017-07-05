# -*- coding: utf-8 -*-
from functools import reduce
from operator import mul, itemgetter, attrgetter, methodcaller
from pprint import pprint
from collections import namedtuple


def fact(n):
    return reduce(mul, range(1, n+1))


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]
name_lat = attrgetter('name', 'coord.lat')


if __name__ == '__main__':
    print(fact(5))
    print(pprint(sorted(metro_data, key=itemgetter(1))))
    cc_name = itemgetter(1, 0)
    for metro in metro_data:
        city_name = cc_name(metro)
        print(city_name)
    for city in sorted(metro_areas, key=attrgetter('coord.lat')):
        print(name_lat(city))

    s = 'The time has come'
    upcase = methodcaller('upper')
    print(upcase(s))
    hiphenate = methodcaller('replace', ' ', '_')
    print(hiphenate(s))
