#!/usr/bin/env python
# encoding: utf-8

# from: https://oj.leetcode.com/problems/3sum/
# Date: Oct.2, 2014
# Status: Ac
def threeSum( num):
    res = []
    if not num:
        return []
    if len(num) < 3:
        return []
    num.sort()
    n = len(num)
    for ix in range(0, n):
        jx = ix + 1
        kx = n -1
        if ix == 0 or num[ix]>num[ix-1]:
            while jx < kx:
                if num[ix] + num[jx] + num[kx] == 0:
                    res.append([num[ix], num[jx], num[kx]])
                    jx += 1
                    kx -= 1
                    while jx < kx and num[jx] == num[jx - 1]:
                        jx += 1
                    while jx < kx and num[kx] == num[kx +1]:
                        kx -= 1
                elif num[ix] + num[jx] + num[kx] < 0:
                    jx += 1
                else:
                    kx -= 1
    return res

num = [-1,0,1,2,-1,-4]
print(threeSum(num))

