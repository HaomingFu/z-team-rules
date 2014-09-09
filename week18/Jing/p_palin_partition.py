"""
From: https://oj.leetcode.com/problems/palindrome-partitioning/
Author: Jing Zhou
Date: Jul 15, 2014
Thought: recursion. note how to copy a list in Python and also the index in Python
Tags: recursion, palindrome, string
"""



class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s:
            return []
        result = []
        tmp = []
        self.partitionPan(s, 0, tmp, result)
        return result

    def partitionPan(self, s, start, tmp, result):
        if start == len(s):
            result.append(tmp[::])
            return
        i = start+1
        while i <= len(s):
            if self.isPalin(s, start, i-1):
                tmp.append(s[start:i])
                self.partitionPan(s, i, tmp, result)
                tmp.pop()
            i += 1

    def isPalin(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
