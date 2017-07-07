# -*- coding: utf-8 -*-
registry = []


def register(func):
    print('run register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


if __name__ == '__main__':
    print(registry)

