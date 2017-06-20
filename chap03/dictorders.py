#!/usr/bin/env python
# -*- coding: utf-8 -*-

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

a = dict(DIAL_CODES)
b = dict(sorted(DIAL_CODES))
c = dict(sorted(DIAL_CODES, key=lambda x: x[1]))
assert a == b and b == c
print(a.keys())
print(b.keys())
print(c.keys())

