#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import UserDict


class StrKeyDict(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value


if __name__ == '__main__':
    a = StrKeyDict()
    a['key'] = 2
    print(a[0])
