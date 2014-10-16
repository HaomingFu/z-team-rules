#!/usr/bin/env python
# encoding: utf-8

def convert(s, nRows):
    store =['']*nRows
    curList = 0
    sign = 1
    if nRows==1:
        return s
    for c in s:
        store[curList] = store[curList] + c
        curList += sign
        if curList == nRows-1 or curList==0:
            sign*=-1

    return ''.join(store)


s = "PAYPALISHIRING"
print(convert(s,1))
