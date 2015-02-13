#!/usr/bin/env python
# encoding: utf-8

def trailingZeros(n):
    res = 0
    a = 5
    while a < n:
        res += (n // a)
        a *= 5
    return res


if __name__ == "__main__":
    print(trailingZeros(29))
