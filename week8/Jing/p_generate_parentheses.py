"""
From: http://oj.leetcode.com/problems/generate-parentheses/
Author: Jing Zhou
Date: May 4, 2014
Thought: This one is quite good...
It only appends ) when the number of left bracets is larger than the right
"""
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        ls = []
        self.generate(ls, "", 0, 0, n)
        return ls
    def generate(self, ls, one, l, r, n):
        if l == n:
            ls.append(one+(n-r)*")")
            return
        self.generate(ls, one+"(", l+1, r, n)
        if l>r:
            self.generate(ls, one+")", l, r+1, n)
