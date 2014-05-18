"""
From: http://oj.leetcode.com/problems/valid-palindrome/
Author: Jing Zhou
Date: May 18, 2014
Thought: I often mess up termination condition.
For this one, it is when left is greater than right.
When that happens... It should be valid instead of invalid
"""


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        return self.isPalin(s, 0, len(s)-1)
    def isPalin(self, s, left, right):
        if not s:
            return True
        while(left <= right):
            while(not s[left].isalnum() and left < right):
                left += 1
            while(not s[right].isalnum() and right > left):
                right -= 1
            if s[left].upper() == s[right].upper():
                left += 1
                right -= 1
            else:
                return False
        return True
