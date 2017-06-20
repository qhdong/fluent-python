#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import ChainMap
import builtins


def open(path):
    f = builtins.open(path)
    return UpperCaser(f)


class UpperCaser:
    def __init__(self, f):
        self._f = f

    def read(self, count=-1):
        return self._f.read(count).upper()


pylookup = ChainMap(locals(), globals(), vars(builtins))
print(pylookup)




