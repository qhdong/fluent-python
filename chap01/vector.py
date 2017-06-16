#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import hypot


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == '__main__':
    a = Vector(1, 2)
    b = Vector(3, 4)
    print(a + b)
    print(a * 3)
    print(abs(a))
    if a:
        print('True')

    # Test for repr(%r), prefer %r in `__repr__`
    print(Vector('1', '2'))
