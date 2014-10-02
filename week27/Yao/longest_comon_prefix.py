#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/longest-common-prefix/
# Date: Oct. 2, 2014
# Status: AC

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 2:
            return self.commonPrefix(strs[0], strs[1])
        n = len(strs)
        mid = n // 2
        str1 = self.longestCommonPrefix(strs[:mid+1])
        str2 = self.longestCommonPrefix(strs[mid+1:n])
        return self.commonPrefix(str1, str2)

    def commonPrefix(self, str1, str2):
        if not str1 or not str2:
            return ""
        str1, str2 = min([str1, str2]), max([str1, str2])
        for i, c in enumerate(str1):
            if c!= str2[i]:
                return str1[:i]
        return str1
