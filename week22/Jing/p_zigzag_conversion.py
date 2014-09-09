"""
From: https://oj.leetcode.com/problems/zigzag-conversion/
Author: Jing Zhou
Date: Aug 27, 2014
Thought: Simple looping
Tags: Quite easy
"""



class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        res = ""
        s_l = len(s)
        for i in range(min(nRows, s_l)):
            res = res + s[i]
            index = i
            if i == 0 or i == nRows - 1:
                while index + (nRows-1)*2 < s_l:
                    res = res + s[index+(nRows-1)*2]
                    index = index +(nRows-1)*2
            else:
                while index + 2*(nRows-i-1) < s_l:
                    res = res + s[index + 2*(nRows-i-1)]
                    if i != 0 and i != nRows - 1 and index + (nRows-1)*2 < s_l:
                        res = res + s[index+(nRows-1)*2]
                    index = index + (nRows-1)*2
        return res
