#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def nextPermutation(self, num):
        if len(num) <=1:
            return num
        n = len(num)
        if n ==2:
            return [num[1], num[0]]
        for ix in range(n-2, -1, -1):
            if num[ix] < num[ix+1]:
                break
        if ix==0 and num[0]>=num[1]:
            num.reverse()
            return num
        if ix==0 and num[0]< num[1]:
            ix = 0
        for jx in range(n-1, ix, -1):
            if num[jx]>num[ix]:
                break
        num[ix], num[jx] = num[jx], num[ix]
        print(num)
        ix = ix +1
        jx = n-1
        while ix < jx:
            num[ix], num[jx] = num[jx], num[ix]
            ix += 1
            jx -= 1
        return num
s = Solution()
num = [1,2,3]
num = [5, 7,6, 0]
num = [1, 3, 2]
print(s.nextPermutation(num))

