"""
From: https://oj.leetcode.com/problems/minimum-path-sum/
Author: Jing Zhou
Date: Jul 17, 2014
Thought: A very easy DP problem, passed at first try
Tags: DP
"""



class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not grid:
            return 0
        w, h = len(grid[0]), len(grid)
        DP = [[0]*w for _ in range(h)]
        DP[0][0] = grid[0][0]
        for i in range(1, w):
            DP[0][i] = DP[0][i-1] + grid[0][i]
        for j in range(1, h):
            DP[j][0] = DP[j-1][0] + grid[j][0]
        for i in range(1, h):
            for j in range(1, w):
                DP[i][j] = DP[i-1][j] + grid[i][j] if DP[i-1][j] < DP[i][j-1] else DP[i][j-1] + grid[i][j]
        return DP[h-1][w-1]
