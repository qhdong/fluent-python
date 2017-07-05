# -*- coding: utf-8 -*-
class C:
    pass

def func():
    pass

c = C()
print('listing attributes of functions that dosen\'t exist in plain instances')
print(sorted(set(dir(func)) - set(dir(c))))
