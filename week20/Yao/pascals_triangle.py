#!/usr/bin/env python
# encoding: utf-8
# From: https://oj.leetcode.com/problems/pascals-triangle/
# Date: August 31
# Status: Accepted

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows < 1:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1, 1]]
        res = [[1], [1,1]]
        for numr in range(3, numRows + 1):
            temp = [0]*numr
            temp[0] = temp[numr-1] = 1
            for i in range(1, numr - 1):
                temp[i] = res[numr-2][i-1] + res[numr-2][i]
            res.append(temp)
        return res

