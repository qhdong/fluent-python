# -*- coding: utf-8 -*-
import array
import math


class Vector2d:
    """A 2d-dimensional vector
    
    >>> v1 = Vector2d(3, 4)
    >>> print(v1)
    (3.0, 4.0)
    >>> v1
    >>> Vector2d(3.0, 4.0)
    >>> x, y = v1
    >>> x, y
    (3.0, 4.0)
    """
    __slots__ = ('__x', '__y')
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r}, {!r})'.format(classname, *self)

    def __str__(self):
        return str(tuple(self))

    def __bool__(self):
        return self.x or self.y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __bytes__(self):
        return (bytes(ord(self.typecode)) +
                bytes(array.array(self.typecode, *self)))

    @classmethod
    def from_bytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'

        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)
