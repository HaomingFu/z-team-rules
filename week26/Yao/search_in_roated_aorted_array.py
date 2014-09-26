#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/search-in-rotated-sorted-array/
# Status: AC
# Date: Sep. 25, 2014

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        try:
            res = A.index(target)
        except:
            res = -1
        return res
