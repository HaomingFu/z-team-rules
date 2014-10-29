#!/usr/bin/env python
# encoding: utf-8

def power(x, n):
    res = 1
    if n ==0:
        return float(1)
    sign = n
    if sign < 0:
        n = -n

    while n >= 1:
        if n % 2 == 1:
            res = res * x
        x = x*x
        n = int(n/2)

    return res if sign > 0 else 1/res

print(power(2, 10))
