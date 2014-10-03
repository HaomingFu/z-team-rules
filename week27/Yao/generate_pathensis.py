#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/generate-parentheses/
# Date: Oct. 3, 2014
# Status: AC

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n < 1:
            return ['']
        res = []
        self.rec(n, n, '', res)

    def rec(self, left, right, s, res):
        if left > 0:
            self.rec(left-1, right, s + '(', res)
        if right > 0 and left < right:
            self.rec(left, right-1, s + ')', res)
        if left == 0 and right == 0:
            res.append(s)
