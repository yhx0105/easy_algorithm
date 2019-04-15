# -*- coding: utf-8 -*-
a_string = 'this is a global variable'


def outer(some_func):
    def inner():
        print('before some_func')
        ret = some_func()
        print(ret + 1)

    return inner


def foo():
    return 1


decoration = outer(foo)
decoration()
