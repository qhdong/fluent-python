# -*- coding: utf-8 -*-
from collections import UserDict


class DoubleDict(UserDict):

    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


if __name__ == '__main__':
    d = DoubleDict(a=2)
    d['foo'] = 'bar'
    d.update(game=3)
    print(d)
