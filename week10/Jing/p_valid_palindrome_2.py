"""
From: http://oj.leetcode.com/problems/valid-palindrome/
Author: Jing Zhou
Date: May 18, 2014
Thought: one liner
"""


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        return [c for c in s.upper() if c.isalnum()] == [c for c in reversed(s.upper()) if c.isalnum()]
