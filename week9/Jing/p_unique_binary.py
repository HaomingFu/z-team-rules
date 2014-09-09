"""
From: http://oj.leetcode.com/problems/unique-binary-search-trees/
Author: Jing Zhou
Date: May 10, 2014
Thought: the idea is quite easy actually
"""
class Solution:
    # @return an integer
    def numTrees(self, n):
        c = 1
        for i in range(2, n+1):
            c = 2*(2*i-1)*c/(i+1)
        return c
