"""
From: https://oj.leetcode.com/problems/climbing-stairs/
Author: Jing Zhou
Date: Jun 04, 2014
Thought: This one is super easy... Use an iterative way to calculate fabonacci numbers
"""



class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        result = [1, 2]
        for i in range(2, n):
            if result[0] > result[1]:
                result[1] = sum(result)
            else:
                result[0] = sum(result)
        return max(result)
