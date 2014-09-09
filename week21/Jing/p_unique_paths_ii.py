"""
From: https://oj.leetcode.com/problems/unique-paths-ii/
Author: Jing Zhou
Date: Aug 31, 2014
Thought: 2 D dynamic programming, can be done in 1 D dynamic...
Tags: DP numbers math
"""



class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            paths[0][0] = 1
        for i in range(1, m):
            if paths[i-1][0] == 0 or obstacleGrid[i][0] == 1:
                paths[i][0] = 0
            else:
                paths[i][0] = 1
        for j in range(1, n):
            if paths[0][j-1] == 0 or obstacleGrid[0][j] == 1:
                paths[0][j] = 0
            else:
                paths[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m-1][n-1]
