#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/plus-one/
# Status: AC
# Date: Sep. 25, 2014

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        n = len(digits) - 1
        tmp = 1
        while n > -1:
            val = digits[n] + tmp
            tmp = val // 10
            digits[n] = val % 10
            n -= 1
        res = digits
        if tmp == 1:
            res = [1] + digits
        return res
