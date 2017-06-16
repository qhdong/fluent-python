#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import random
from array import array


floats = array('d', (random() for _ in range(10 ** 7)))
print('last float is :', floats[-1])
with open('floats.bin', 'wb') as f:
    floats.tofile(f)
floats2 = array('d')
with open('floats.bin', 'rb') as f:
    floats2.fromfile(f, 10 ** 7)
print('last float from floats2 is:', floats2[-1])
print('are they equal?', floats == floats2)
