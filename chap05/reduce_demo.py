# -*- coding: utf-8 -*-
import timeit
from functools import reduce
from operator import add


# 比较 reduce 和 sum 的速度
print(timeit.timeit(stmt='reduce(add, range(100))', globals=globals()))
print(timeit.timeit(stmt='b = sum(range(100))', globals=globals()))

# 判断是否是可调用对象
print([callable(o) for o in [len, 3, 'hello', timeit.Timer]])
