#!/usr/bin/env python
# encoding: utf-8

def getSum(*argv):
    res = 0
    for arg in argv:
        if isinstance(arg, int):
            res += arg
    return res



print(getSum(1, 3, 4.0, 'hi'))
