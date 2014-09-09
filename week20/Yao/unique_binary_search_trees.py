#!/usr/bin/env python
# encoding: utf-8

#Status: Accepted
#Date: August 31
#From: https://oj.leetcode.com/problems/unique-binary-search-trees/
class Solution:
    # @return an integer
    def numTrees(self, n):
        if n <= 1:
            return 1
        res = [0]*(n + 1)
        res[0]=1
        res[1] = 1
        for ix in range(2, n+1):
            for i range(1, ix+1):
                res[ix] = res[ix] + res[i-1]*res[ix-i]
        return res[n]
