#!/usr/bin/env python
# encoding: utf-8

def atoi(str):
    str = str.strip()
    if not str:
        return None

    if str[0]=='+' or str[0]=='-':
        sign = str[0]
        if len(str) > 1:
            str = str[1:]
        else:
            return None

    res = 0
    for c in str:
        if c.isdigit():
            res = 10*res + int(c)
        else:
            break

    if sign == '-':
        return -res
    if res > 2147483647:
        return 2147483647
    if res <= -2147483648:
        return -2147483648

    return res

s = input()
print(atoi(s))
