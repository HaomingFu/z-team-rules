"""
From: http://oj.leetcode.com/problems/search-insert-position/
Author: Jing Zhou
Date: May 7, 2014
Hardness: super easy...
"""


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer

    def searchInsert(self, A, target):
        for i, val in enumerate(A):
            if val >= target:
                return i
        return len(A)
