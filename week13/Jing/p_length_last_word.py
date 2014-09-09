"""
From: https://oj.leetcode.com/problems/length-of-last-word/
Author: Jing Zhou
Date: Jun 04, 2014
Thought: Just another oneliner with Python... will try other languages
"""



class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.rstrip().split(' ')[-1])
