"""
From: https://oj.leetcode.com/problems/gray-code/
Author: Jing Zhou
Date: Jun 19, 2014
Thought: As long as you know how to generate gray code...
Tags: graycode, math, formula
"""


class Solution:
    # @return a list of integers
    def grayCode(self, n):
        res = [0]
        for i in range(1, n+1):
            newRes = ([2**(i-1)+j for j in reversed(res)])
            res.extend(newRes)
        return res
