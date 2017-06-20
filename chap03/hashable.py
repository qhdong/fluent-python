#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections.abc import Mapping


def foo(a):
    if isinstance(a, Mapping):
        print('You have a `items` method')


a = dict(one=1, two=2, three=3)
b = {"one": 1, "two": 2, "three": 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([("one", 1), ("two", 2), ("three", 3)])
e = dict({"one": 1, "two": 2, "three": 3})
print(a == b == c == d == e)

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
]

country_code = {country.upper(): code for code, country in DIAL_CODES}
print(country_code)

