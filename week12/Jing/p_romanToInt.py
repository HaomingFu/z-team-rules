"""
From: https://oj.leetcode.com/problems/roman-to-integer/
Author: Jing Zhou
Date: May 26, 2014
Thought: This one is easy as long as you know the rule to convert...
"""



class Solution:
    # @return an integer
    def romanToInt(self, s):
        result = 0
        for i, v in enumerate(s):
            if i > 0 and self.convert(v) > self.convert(s[i-1]):
                result += self.convert(v) - 2*self.convert(s[i-1])
            else:
                result += self.convert(s[i])
        return result

    def convert(self, c):
        if c == 'I':
            return 1
        elif c == 'V':
            return 5
        elif c == 'X':
            return 10
        elif c == 'L':
            return 50
        elif c == 'C':
            return 100
        elif c == 'D':
            return 500
        elif c == 'M':
            return 1000
        else:
            return 0
