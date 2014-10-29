#!/usr/bin/env python
# encoding: utf-8

def getPermutaion(n, k):
    res = []
    temp = [str(i) for i in range(1, n+1)]
    permutate(n, 0, temp, res)
    t = ["".join(li) for li in res]
    t.sort()
    return t[k-1]


def permutate(n, ix,temp, res):
    if ix == n-1:
        res.append(list(temp))
        return
    for jx in range(ix, n):
        temp[jx], temp[ix] = temp[ix], temp[jx]
        permutate(n, ix+1, temp, res)
        temp[jx], temp[ix] = temp[ix], temp[jx]


n = 9
k = 100
print(getPermutaion(n, k))
