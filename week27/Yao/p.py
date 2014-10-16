#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def __init__(self):
        self.res= []

    def permute(self, num):
        self.helper(num, 0, len(num)-1)
        return self.res

    def helper(self, num, k, n):
        if k == n:
            newLi = list(num)
            self.res.append(newLi)
        else:
            for i in range(k, n+1):
                num[k], num[i] = num[i], num[k]
                self.helper(num, k+1, n)
                num[k], num[i] = num[i], num[k]

s = Solution()
num = [0,1]
print(s.permute(num))
