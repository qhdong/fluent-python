# -*- coding: utf-8 -*-
import weakref


a = {1, 2}
b = a

def bye():
    print('bye')

ender = weakref.finalize(b, bye)

print(ender.alive)
del a

print(ender.alive)
b = 'c'

print(ender.alive)

