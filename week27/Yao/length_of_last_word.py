#!/usr/bin/env python
# encoding: utf-8


def lengthOfLastWord(s):
    li = s.split()
    n = len(li)
    if n == 0:
        return 0
    else:
        return len(li[-1])

s = "Hello  World "
print(lengthOfLastWord(s))
