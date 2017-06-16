#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from bisect import bisect
from bisect import insort


def grade(score, breakpoints=(60, 70, 80, 90), grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]


def inosrt_demo():
    SIZE = 7
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        insort(my_list, new_item)
        print('%2d ->' % new_item, my_list)


if __name__ == '__main__':
    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
    inosrt_demo()
