#!/usr/bin/env python
# -*- coding: utf-8 -*-
import timeit


TIMES = 10000

SETUP = """
symbols = '人生苦短，我用Python'
def non_ascii(c):
    return c > 127
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *("{:.3f}".format(x) for x in res))


symbols = '$¢£¥€¤'


if __name__ == '__main__':
    clock('listcomp:', '[ord(x) for x in symbols if ord(x) > 127]')
    clock('listcomp + func:', '[ord(x) for x in symbols if non_ascii(ord(x))]')
    clock('lambda', 'list(filter(non_ascii, map(ord, symbols)))')
    x = tuple(ord(x) for x in symbols)
    import array
    v = array.array('I', (ord(x) for x in symbols))
    print(v)