"""
From: https://oj.leetcode.com/problems/implement-strstr/
Author: Jing Zhou
Date: Jun 04, 2014
Thought: Using python sucked the fun of this problem... I think I'll go back to this problem and have another look in the future using something like C.
"""



ass Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        return haystack[haystack.find(needle):] if haystack.find(needle) != -1 else None
