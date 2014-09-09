#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/pascals-triangle-ii/
# Status: Accepted
# Date: Setemper 1

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex < 0:
            return []
        elif rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        a = [1,1]
        for numr in range(2, rowIndex + 1):
            temp = [0]*(numr+1)
            temp[0] = temp[numr] = 1
            for i in range(1, numr):
                temp[i] = a[i-1] + a[i]
            a = temp
        return temp
