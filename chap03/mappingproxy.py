#!/usr/bin/env python
# -*- coding: utf-8 -*-
from types import MappingProxyType


d = dict(one=1, two=2)
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy['one'])
d_proxy['trhee'] = 2

