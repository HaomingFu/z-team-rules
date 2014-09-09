"""
From: https://oj.leetcode.com/problems/unique-paths/
Author: Jing Zhou
Date: Jun 04, 2014
Thought: Just a combination problem... just one loop with the defination...
"""



class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        m -= 1
        n -= 1
        l, k = 1, 1
        if m==0 or n==0:
            return 1
        while(m>=1):
            l *= n+m
            k *= m
            m -= 1
        return l/k
