#!/usr/bin/env python
# encoding: utf-8

# From:https://oj.leetcode.com/problems/search-insert-position/
# Date: sep. 30, 2014
# Status: AC

def searchInsert(self, A, target):
    ix = 0
    n = len(A)
    while ix < n:
        if A[ix] == target:
            return ix
        if A[ix] < target:
            ix += 1
        else:
            return ix
    return ix
