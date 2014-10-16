#!/usr/bin/env python
# encoding: utf-8
def countAndSay(n):
    last = '1'
    ix = 1
    while ix < n:
        s = say(last)
        last = s
        ix += 1
    return last

def say(s):
    if len(s)==1:
        return '1'+s
    num = 1
    ix=1
    res = ''
    while ix < len(s):
        if s[ix]==s[ix-1]:
            num += 1
        else:
            res += str(num)+ s[ix-1]
            num=1
        ix += 1
    res += str(num) + s[-1]
    return res

s = int(input())
print(countAndSay(s))
