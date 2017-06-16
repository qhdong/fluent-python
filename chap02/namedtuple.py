#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'Japan', 36.933, (35.0934, 139.2344))
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
beijing_data = ('Beijing', 'China', 98.34, LatLong(33.22, 44.33))
beijing = City._make(beijing_data)
print(beijing)
for key, val in beijing._asdict().items():
    print(key, ':', val)

REVERSE = slice(None, None, -1)
a = list(range(10))
print(a[REVERSE])