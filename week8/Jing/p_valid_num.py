"""
From: http://oj.leetcode.com/problems/valid-number/
Author: Jing Zhou
Date: May 01, 2014
Thought: super easy...
"""
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        try:
            num = float(s)
        except:
            return False
        return True
