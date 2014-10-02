#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/3sum-closest/
# Date: Oct. 2
# Status: AC

def threeSumClosest( num, target):
    minimum = 10000000
    res = 0
    n = len(num)
    num.sort()
    for ix in range(0, n):
        jx = ix + 1
        kx = n-1
        while jx < kx:
            s = num[ix] + num[jx] + num[kx]
            diff = abs(s - target)
            if diff < minimum:
                minimum = diff
                res = s
            if s < target:
                jx += 1
            else:
                kx -= 1
    return res

if __name__ == "__main__":
    num = [1, 1, -1, -1, 3]
    target = -1
    print(threeSumClosest(num, target))

