#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def grayCode(self, n):
        if n < 1:
            return [0]
        res = [0,1]
        for i in range(1, n):
            temp = []
            for each in res:
                temp.append(self.power(2,i) + each)
            temp.reverse()
            res += temp
        return res
    def power(self, x, y):
        res = 1
        for i in range(0, y):
            res *= x
        return res
